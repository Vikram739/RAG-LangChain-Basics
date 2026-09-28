from langchain_text_splitters import TokenTextSplitter

text = """LangChain simplifies working with LLMs by providing modular components like prompts, chains, memory, and tools."""

splitter = TokenTextSplitter(
    chunk_size=10,
    chunk_overlap=2
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)