from langchain.chains import RetrievalQA   
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

chat = ChatOpenAI(model="gpt-3.5-turbo")

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

database = Chroma(
    persist_directory="./.data", 
    embedding_function=embeddings
)

# 데이터베이스를 Retriever로 변환
retriever = database.as_retriever() 

qa = RetrievalQA.from_llm(   
    llm=chat,   
    retriever=retriever,  
    return_source_documents=True  
)

result = qa("에스파 윈터의 매력을 알려주세요")

print(result["result"])  

print(result["source_documents"])  