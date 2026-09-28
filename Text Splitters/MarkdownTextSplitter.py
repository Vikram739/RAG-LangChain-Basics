from langchain_text_splitters import MarkdownTextSplitter

md_text = """
# LangChain Overview
LangChain helps developers build applications using LLMs.

## Components
- LLMs
- Chains
- Memory
- Agents
"""

splitter = MarkdownTextSplitter(
    chunk_size=100,
    chunk_overlap=10
)

chunks = splitter.split_text(md_text)

print(len(chunks))

for i , chunk in enumerate(chunks):
    print(f'\nChunk: {i+1} \n{chunk}')
