import os
import sys

from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
from langchain.vectorstores import Milvus
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain

def prompt(book):
    # if not book:
    #     print("Choose a book to read. If empty './books/00000_example.pdf' will be load")
    #     book = input("book: ")
    if not book:
        book = "./books/00000_example.pdf"

    collection_name = os.path.basename(book).split(".")[0]

    loader = PyPDFLoader(new_book)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    texts = [d.page_content for d in docs]
    metadatas = [d.metadata for d in docs]

    embeddings = OpenAIEmbeddings()
    vectorstore = Milvus.from_documents(
        docs,
        embeddings,
        connection_args={"host": "vectorstore", "port": "19530"},
        collection_name=f"_{collection_name}",
    )


    note_name = os.path.basename(book)
    # if notes/00000_example.pdf.txt exists, it will be used as chat history
    if not os.path.exists(f"notes/{note_name}"):
        with open(f"notes/{note_name}", "w") as f:
            f.write("")

    qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), vectorstore.as_retriever())

    chat_history = []

    while True:
        query = input("Enter your question: ")
        if query == "exit":
            break
        result = qa({"question": query, "chat_history": []})
        print(result["answer"])
        chat_history.append(query)
        chat_history.append(result["answer"])

def main(args):
    book = args[0]
    if not book:
        book = input("book: ")
    prompt(book)


# call main function
if __name__ == "__main__":
    # Get the command line arguments
    args = sys.argv[1:]
    main(args)
