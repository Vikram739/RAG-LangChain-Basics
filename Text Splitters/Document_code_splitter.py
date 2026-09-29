from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("python_guide.pdf")
docs = loader.load()
print(docs[0])
