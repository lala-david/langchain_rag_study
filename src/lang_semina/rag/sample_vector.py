from langchain.embeddings import OpenAIEmbeddings 
from numpy import dot 
from numpy.linalg import norm 

# vector화 
embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

query_vector = embeddings.embed_query("에스파의 멤버중 윈터의 매력 포인트는?") 

print(f"벡터화된 질문: {query_vector[:5]}") 

document_1_vector = embeddings.embed_query("에스파의 윈터는 노래도 잘하고 매력적이며 웃는 얼굴이 이쁘다.")  
document_2_vector = embeddings.embed_query("진격의 거인 에렌 예거는 인류를 8할 남기고 대학살을 했다.")
document_3_vector = embeddings.embed_query("비트코인은 한화로 5억을 갈 것이다.")

cos_sim_1 = dot(query_vector, document_1_vector) / (norm(query_vector) * norm(document_1_vector)) 
print(f"문서 1과 질문의 유사도: {cos_sim_1}")
cos_sim_2 = dot(query_vector, document_2_vector) / (norm(query_vector) * norm(document_2_vector))  
print(f"문서 2와 질문의 유사도: {cos_sim_2}")
cos_sim_3 = dot(query_vector, document_3_vector) / (norm(query_vector) * norm(document_3_vector))  
print(f"문서 3와 질문의 유사도: {cos_sim_3}")