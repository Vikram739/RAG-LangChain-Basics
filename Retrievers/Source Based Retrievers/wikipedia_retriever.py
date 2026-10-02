import sys

import wikipedia
from langchain_community.retrievers import WikipediaRetriever

sys.stdout.reconfigure(encoding="utf-8")                    # print non-English characters

# Wikipedia blocks requests without a proper User-Agent
wikipedia.set_user_agent("RAG-LangChain-Basics/1.0 (https://github.com/Vikram739/RAG-LangChain-Basics)")

retriever = WikipediaRetriever(
    top_k_results=1,
    lang="en"
)

query = "WHo is shivaji maharaj?"

results = retriever.invoke(query)

print(results)



