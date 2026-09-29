import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

os.chdir(os.path.dirname(os.path.abspath(__file__)))          # run from this file's folder

loader = PyPDFLoader("python_guide.pdf")                        # loader
docs = loader.load()
print(docs[0])
