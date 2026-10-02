# Retrievers

A retriever takes a question and returns the most relevant documents. A vector store can search, but a retriever wraps that search in a standard LangChain interface, so the same code works with any store and can be plugged straight into a chain.

```python
retriever = db.as_retriever(search_kwargs={"k": 3})
docs = retriever.invoke("What is a list?")
```

Here `db` is the Chroma store built in [`Vector Stores/vector_demo_chroma.py`](../Vector%20Stores/vector_demo_chroma.py).

## Source based retrievers

Scripts in the `Source Based Retrievers` folder, grouped by where the documents come from.

| Script | What it does |
| --- | --- |
| [`wikipedia_retriever.py`](Source%20Based%20Retrievers/wikipedia_retriever.py) | Searches Wikipedia and returns each page as a LangChain `Document` |
| [`vectorestore_retriever.py`](Source%20Based%20Retrievers/vectorestore_retriever.py) | Builds an in-memory Chroma store from 4 documents and uses `as_retriever(search_kwargs={"k": 2})` to fetch the top 2 matches |
