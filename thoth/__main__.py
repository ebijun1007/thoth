import thoth.cli

if __name__ == "__main__":
    thoth.cli.main()

# choose mode
# 1. archive
# 2. copilot

# archive mode
# load "shelf" collection from milvus
# start chat loop
## 1. ask question
## 2. get answer
## 3. save question and answer to "shelf" collection
## 4. export logs as "note"

# copilot mode
# load specific book's collection from milvus, etc "00000_bitcoin"
# start chat loop
## 1. choose chapter
## 2. ask question
## 3. get answer
## 4. save question and answer to book's collection
## 5. export logs as "note"

