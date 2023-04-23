import os

from langchain.document_loaders import PyPDFLoader
from langchain.llms import OpenAI
from langchain.vectorstores import Milvus

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain

print("Choose a book to read. If empty './books/00000_example.pdf' will be load")
book = input("book: ")
if not book:
    book = "./books/00000_example.pdf"

collection_name = os.path.basename(book).split(".")[0]

loader = PyPDFLoader(book)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectorstore = Milvus.from_documents(
    docs,
    embeddings,
    connection_args={"host": "vectorstore", "port": "19530"},
    collection_name=f"_{collection_name}",
)

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