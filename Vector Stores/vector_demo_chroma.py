from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# path setting
Parent_path = Path(__file__).parent

pdf_path = Parent_path / "python_guide.pdf"

# load documents

loader = PyPDFLoader(str(pdf_path))
docs = loader.load()

print(len(docs))
print(docs[0])