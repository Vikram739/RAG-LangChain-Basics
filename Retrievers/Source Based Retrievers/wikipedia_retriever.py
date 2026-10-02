import sys

import wikipedia
from langchain_community.retrievers import WikipediaRetriever

sys.stdout.reconfigure(encoding="utf-8")                    # print non-English characters

# Wikipedia blocks requests without a proper User-Agent
wikipedia.set_user_agent("RAG-LangChain-Basics/1.0 (https://github.com/Vikram739/RAG-LangChain-Basics)")

retriever = WikipediaRetriever(
    top_k_results=3,
    lang="en"
)

query = "New York"

results = retriever.invoke(query)

print(results[0].page_content)



