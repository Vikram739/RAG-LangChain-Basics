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
└── Text Splitters/
    ├── CharacterTextSplitter.py            # Split on a single separator
    ├── RecursiveCharacterTextSplitter.py   # Try separators from largest to smallest
    ├── TokenTextSplitter.py                # Split by token count
    ├── MarkdownTextSplitter.py             # Split along Markdown headings
    ├── Document_code_splitter.py           # Load a PDF and split it as Python code
    └── python_guide.pdf                    # Input for the code splitter
```

## Setup

```bash
git clone https://github.com/Vikram739/RAG-LangChain-Basics.git
cd RAG-LangChain-Basics

pip install langchain-community langchain-text-splitters pypdf tiktoken
```

| Package | Used for |
| --- | --- |
| `langchain-community` | `TextLoader` and `PyPDFLoader` |
| `langchain-text-splitters` | All the text splitters |
| `pypdf` | Reading PDF files |
| `tiktoken` | Counting tokens in `TokenTextSplitter` |
