from langchain.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(  
    lang="ko",   
)
# Wikipedia에서 관련 문서를 가져옴
documents = retriever.get_relevant_documents( 
    "블랙홀 퀘이사" 
)

print(f"검색 결과: {len(documents)}건")  

for document in documents:
    print("---------------검색한 메타데이터---------------")
    print(document.metadata) 
    print("---------------검색한 텍스트---------------")
     # 텍스트의 첫 100글자를 표시
    print(document.page_content[:100])