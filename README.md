# book-discussion-copilot
Read e-book and discuss with LLM based copilot

Need OpenAI API key to call ChatGPT API.

## Setup
```
cp .env.sample .env
docker compose build
docker compose run --rm copilot
```

## sample
```
ebijun@Mac-mini-3 book-discussion-copilot % docker compose run --rm copilot
[+] Running 3/0
 ⠿ Container milvus-minio Running
 ⠿ Container milvus-etcd  Running
 ⠿ Container milvus-standalone Running

Choose a book to read. If empty './books/00000_example.pdf' will be load
book:
Enter your question: Who is the author?
 The author is Satoshi Nakamoto.
Enter your question: exit
ebijun@Mac-mini-3 book-discussion-copilot %
```