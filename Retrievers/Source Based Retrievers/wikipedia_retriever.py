from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    top_k_results=1,
    lang="en"
)

query = "WHo is shivaji maharaj?"

results = retriever.invoke(query)

print(results)



