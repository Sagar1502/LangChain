with open("mbox-short.txt") as f:
    mbox_short=f.read()

from langchain_text_splitters import CharacterTextSplitter

text_splitter= CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000
)
texts=text_splitter.create_documents([mbox_short])
texts
print(texts[0].page_content)

