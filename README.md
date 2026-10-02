# RAG LangChain Basics

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-text%20splitters-1C3C3C?logo=langchain&logoColor=white)

Small, runnable examples of the first two steps of a Retrieval Augmented Generation (RAG) pipeline: **loading documents** and **splitting them into chunks**. Each script does one thing, so you can run it, read the output, and change a parameter to see what happens.

```
Load documents  ->  Split into chunks  ->  Embed  ->  Store in vector DB  ->  Retrieve  ->  Generate
   (this repo)        (this repo)
```

## Project structure

```
RAG-LangChain-Basics/
├── Document Loader/
│   ├── sample.txt                          # Short article about RAG
│   └── textLoader.py                       # Load a .txt file with TextLoader
├── Text Splitters/
│   ├── CharacterTextSplitter.py            # Split on a single separator
│   ├── RecursiveCharacterTextSplitter.py   # Try separators from largest to smallest
│   ├── TokenTextSplitter.py                # Split by token count
│   ├── MarkdownTextSplitter.py             # Split along Markdown headings
│   ├── Document_code_splitter.py           # Load a PDF and split it as Python code
│   └── python_guide.pdf                    # Input for the code splitter
└── Vector Stores/
    ├── vector_demo_chroma.py               # Embed chunks, store in Chroma, search them  
    └── python_guide.pdf                    # Input for the vector store demo
```

## Setup

```bash
git clone https://github.com/Vikram739/RAG-LangChain-Basics.git
cd RAG-LangChain-Basics

pip install langchain-community langchain-text-splitters pypdf tiktoken langchain-huggingface langchain-chroma
```

| Package | Used for |
| --- | --- |
| `langchain-community` | `TextLoader` and `PyPDFLoader` |
| `langchain-text-splitters` | All the text splitters |
| `pypdf` | Reading PDF files |
| `tiktoken` | Counting tokens in `TokenTextSplitter` |
| `langchain-huggingface` | Local embedding models |
| `langchain-chroma` | Chroma vector store |

## Examples

### Document Loader

| Script | What it does |
| --- | --- |
| [`textLoader.py`](Document%20Loader/textLoader.py) | Loads `sample.txt` into a LangChain `Document` and prints its text |

### Text Splitters

| Script | Splitter | Settings | Best for |
| --- | --- | --- | --- |
| [`CharacterTextSplitter.py`](Text%20Splitters/CharacterTextSplitter.py) | `CharacterTextSplitter` | size 200, overlap 20, split on spaces | Plain text with a clear separator |
| [`RecursiveCharacterTextSplitter.py`](Text%20Splitters/RecursiveCharacterTextSplitter.py) | `RecursiveCharacterTextSplitter` | size 80, overlap 20 | General text; keeps paragraphs and sentences together when it can |
| [`TokenTextSplitter.py`](Text%20Splitters/TokenTextSplitter.py) | `TokenTextSplitter` | 10 tokens, overlap 2 | Staying under a model's token limit |
| [`MarkdownTextSplitter.py`](Text%20Splitters/MarkdownTextSplitter.py) | `MarkdownTextSplitter` | size 100, overlap 10 | Markdown docs, READMEs, notes |
| [`Document_code_splitter.py`](Text%20Splitters/Document_code_splitter.py) | `RecursiveCharacterTextSplitter.from_language` | Python, size 1000, overlap 50 | Source code and guides with code in them |

### Vector Stores

| Script | Embeddings | Vector store | What it does |
| --- | --- | --- | --- |
| [`vector_demo_chroma.py`](Vector%20Stores/vector_demo_chroma.py) | `sentence-transformers/all-MiniLM-L6-v2` | Chroma, saved to `./chroma_db` | Splits the PDF into 700 character chunks, embeds them, and returns the chunk closest to "What is list?" |

### Key terms

- **chunk_size**: the most characters (or tokens) one chunk can hold.
- **chunk_overlap**: how much of the end of one chunk is repeated at the start of the next, so a sentence cut in half still has context.
- **separators**: where the splitter prefers to cut. The recursive splitter tries `"\n\n"`, then `"\n"`, then `" "`, and only cuts mid-word as a last resort.

## Running the scripts

The text splitter examples can be run from anywhere:

```bash
python "Text Splitters/RecursiveCharacterTextSplitter.py"
```

`textLoader.py` opens `sample.txt` by name, so run it from inside its folder:

```bash
cd "Document Loader"
python textLoader.py
```

If you use the VS Code Code Runner extension, add this to `settings.json` so every script runs from its own folder:

```json
"code-runner.fileDirectoryAsCwd": true
```

## Notes

- `langchain-community` prints a `DeprecationWarning` on import. It does not stop the scripts from running.
- `PyPDFLoader` needs `pypdf`. If you see ``ImportError: `pypdf` package not found``, run `pip install pypdf`.

## Next steps

- [ ] Create embeddings for the chunks
- [ ] Store them in a vector database (FAISS or Chroma)
- [ ] Retrieve relevant chunks for a question
- [ ] Pass them to an LLM to generate an answer
