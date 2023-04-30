import os

import click
from colorama import Fore
from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
from langchain.vectorstores import Milvus
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ChatMessageHistory

from thoth.config import check_openai_api_key, create_config
from thoth.prompts.autocomplete import Mode, input_book, input_mode
from thoth.utils.logs import Logger
from thoth.utils.spinner import Spinner


@click.group(invoke_without_command=True)
@click.option("--speak", is_flag=True, help="Enable Speak Mode")

@click.pass_context
def main(ctx: click.Context,speak: bool) -> None:
    if ctx.invoked_subcommand is None:
        check_openai_api_key()

        logger = Logger()
        logger.typewriter_log(
            "Welcome to Thoth, the AI Assistant for the Reading book!", Fore.GREEN
        )

        mode = input_mode()
        if mode == Mode.FOCUS.value:
            book = input_book()
            collection_name = os.path.basename(book).split(".")[0]
        else:
            collection_name = "shelf"
        embeddings = OpenAIEmbeddings()
        loader = PyPDFLoader(f"./books/{book}")
        with Spinner("Parsing... "):
            documents = loader.load()
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            docs = text_splitter.split_documents(documents)
            vectorstore = Milvus.from_documents(
                docs,
                embeddings,
                connection_args={"host": "vectorstore", "port": "19530"},
                collection_name=f"_{collection_name}",
            )
        qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), vectorstore.as_retriever())
        history = ChatMessageHistory()
        while True:
            query = input("Ask: ")
            with Spinner("Reading... "):
                result = qa({"question": query, "chat_history": []})
            logger.typewriter_log(
                result["answer"], Fore.GREEN
            )
            history.add_user_message(query)
            history.add_ai_message(result["answer"])




if __name__ == "__main__":
    main()
