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
# print(docs[0])

# Splitting into chunks...

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=700,
    chunk_overlap = 50
)

chunks = splitter.split_documents(docs)
print(len(chunks))
print(chunks[0])

emd = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


db = Chroma.from_documents(
    documents=chunks,
    embedding=emd,
    persist_directory="./chroma_db"
)