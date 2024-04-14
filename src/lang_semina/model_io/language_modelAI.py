from langchain.chat_models import ChatOpenAI
# 사용자 메세지    
from langchain.schema import HumanMessage  
# AI 메세지 
from langchain.schema import AIMessage
chat = ChatOpenAI(  
    # 모델 
    model="gpt-3.5-turbo",   
)

result = chat( 
    [
        HumanMessage(content="블랙홀의 구조를 설명해줘"),
        AIMessage(content='{ChatModel의 답변인 블랙홀의 구조 설명}'),
        HumanMessage(content="그 구조 설명을 영어로 번역해줘"),
        
    ]
)
print(result.content)