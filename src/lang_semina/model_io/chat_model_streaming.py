from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    # streaming 모드 True 
    streaming=True, 
    callbacks=[
        # 콜백으로 설정  
        StreamingStdOutCallbackHandler()
    ]
)
resp = chat([ 
    HumanMessage(content="에스파의 멤버를 알려줘")
])