from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever

chat = ChatOpenAI()

retriever = WikipediaRetriever(  
    lang="ko",  
    doc_content_chars_max=500,   
    top_k_results=2,  
)

chain = RetrievalQA.from_llm( 
    llm=chat, 
    retriever=retriever, 
    return_source_documents=True,  
)

result = chain("가장 큰 블랙홀은?")  

source_documents = result["source_documents"]  

print(f"검색 결과: {len(source_documents)}건")  
for document in source_documents:
    print("---------------검색한 메타데이터---------------")
    print(document.metadata)
    print("---------------검색한 텍스트---------------")
    print(document.page_content[:100])
print("---------------응답---------------")
print(result["result"])  