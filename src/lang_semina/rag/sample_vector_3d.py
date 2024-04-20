import plotly.express as px
from langchain.embeddings import OpenAIEmbeddings 
from numpy import dot 
from numpy.linalg import norm 

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

query_vector = embeddings.embed_query("에스파 윈터의 매력은?") 

document_1_vector = embeddings.embed_query("에스파 윈터는 이쁘다")  
document_2_vector = embeddings.embed_query("에스파 윈터는 너무 귀엽다.")
document_3_vector = embeddings.embed_query("비트코인은 한화로 5억을 갈 것이다.")


cos_sim_1 = dot(query_vector, document_1_vector) / (norm(query_vector) * norm(document_1_vector)) 
cos_sim_2 = dot(query_vector, document_2_vector) / (norm(query_vector) * norm(document_2_vector))  
cos_sim_3 = dot(query_vector, document_3_vector) / (norm(query_vector) * norm(document_3_vector))  


data = {
    "Type": ["Query", "☄ winter 1", "☄ winter 2", "👨🏻‍🚀 bitcoin"],
    "X": [query_vector[0], document_1_vector[0], document_2_vector[0], document_3_vector[0]],
    "Y": [query_vector[1], document_1_vector[1], document_2_vector[1], document_3_vector[1]],
    "Z": [query_vector[2], document_1_vector[2], document_2_vector[2], document_3_vector[2]],
    "Cosine Similarity": [1, cos_sim_1, cos_sim_2, cos_sim_3]
}


fig = px.scatter_3d(data, x="X", y="Y", z="Z", color="Type", text="Type", size_max=10, opacity=0.7, title="Vector Space Visualization")
fig.update_traces(marker=dict(size=5))
fig.show()
