# Thoth
**Thoth** is a cutting-edge _reading support tool_ inspired by the ancient Egyptian god of wisdom and knowledge. Our mission is to _enhance your reading experience_ by providing insightful summaries and fostering a deeper understanding of the content.

Thoth is designed to assist readers with thought-provoking questions and personalized recommendations, allowing you to engage with your favorite books on a whole new level. _Harness the wisdom of Thoth_ and unlock the full potential of your reading journey.

Embrace the power of knowledge with **Thoth** by your side.

## Setup
```
cp .env.sample .env
docker compose build
docker compose run --rm copilot
```

## sample
```
ebijun@Mac-mini-3 book-discussion-copilot % docker compose run --rm thoth
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