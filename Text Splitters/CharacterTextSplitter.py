from langchain_text_splitters import CharacterTextSplitter

text = """LangChain is a powerful framework for developing applications powered by language models.
It enables developers to chain together components like LLMs, prompts, and memory to create advanced conversational AI systems.
Text splitters in LangChain help break large documents into smaller pieces for processing."""

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 20,  # to be common things between splits to save context
    separator = " "
)

chunks = splitter.split_text(text.replace("\n"," "))

print(len(chunks))
print(chunks)