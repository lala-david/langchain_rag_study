from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever, RePhraseQueryRetriever 
from langchain import LLMChain
from langchain.prompts import PromptTemplate

retriever = WikipediaRetriever( 
    lang="ko", 
    doc_content_chars_max=500 
)

llm_chain = LLMChain( 
    llm = ChatOpenAI(  
        temperature = 0
    ), 
    prompt= PromptTemplate( 
        input_variables=["question"],
        template="""아래 질문에서 Wikipedia에서 검색할 키워드를 추출해 주세요.
질문: {question}
"""
))

re_phrase_query_retriever = RePhraseQueryRetriever( 
    llm_chain=llm_chain, 
    retriever=retriever,  
)

documents = re_phrase_query_retriever.get_relevant_documents("블랙홀 사건의 지평선이 뭐야?")

print(documents)