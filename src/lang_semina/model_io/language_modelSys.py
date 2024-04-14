from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage  # 사용자 메세지    
from langchain.schema import SystemMessage # 모델 성격 정의 


chat = ChatOpenAI(  
    # 모델 
    model="gpt-3.5-turbo",   
)

result = chat( 
    [
        SystemMessage(content='당신은 교수입니다 나쁜 교수죠 학생들에게 꼰대입니다. 최대한 사회적인 것을 연결해서 나쁘게 말하세요'),
        HumanMessage(content="교수님 해외 저널 쓰기 싫어요!"),
        
    ]
)
print(result.content)