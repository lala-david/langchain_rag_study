from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings   
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import Chroma  

loader = PyMuPDFLoader("pdf/winter.pdf")  
documents = loader.load()

text_splitter = SpacyTextSplitter(   
    # 분할 크기 나누기  
    chunk_size=300,  
    # 한국어 설정 
    pipeline="ko_core_news_sm"  
)
splitted_documents = text_splitter.split_documents(documents) 

embeddings = OpenAIEmbeddings(  
    model="text-embedding-ada-002"  
)

database = Chroma(
    persist_directory="./.data",  # 벡터화 데이터 저장 위치 지정
    embedding_function=embeddings  # 벡터화할 모델을 지정
)

# 문서를 데이터베이스에 추가
database.add_documents(  
    splitted_documents,  
)

print("💎 데이터베이스 생성이 완료되었습니다!") 