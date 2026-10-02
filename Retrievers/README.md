# Retrievers

A retriever takes a question and returns the most relevant documents. A vector store can search, but a retriever wraps that search in a standard LangChain interface, so the same code works with any store and can be plugged straight into a chain.

```python
retriever = db.as_retriever(search_kwargs={"k": 3})
docs = retriever.invoke("What is a list?")
```

Here `db` is the Chroma store built in [`Vector Stores/vector_demo_chroma.py`](../Vector%20Stores/vector_demo_chroma.py).

## Source based retrievers

These fetch documents from an outside source instead of a local vector store.

| Script | What it does |
| --- | --- |
| [`wikipedia_retriever.py`](Source%20Based%20Retrievers/wikipedia_retriever.py) | Searches Wikipedia and returns each page as a LangChain `Document` |
