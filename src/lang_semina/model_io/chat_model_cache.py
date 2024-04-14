import time
import langchain
from langchain.cache import InMemoryCache  # InMemoryCache 
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# llm_cache에 InMemoryCache 설정
langchain.llm_cache = InMemoryCache() 

chat = ChatOpenAI()
# 실행 시간 
start = time.time() 

result = chat([
    HumanMessage(content="안녕하세요! 전 성준이에요")
])

# 시간 종료 
end = time.time() 
print(result.content)
print(f"실행 시간: {end - start}초")

start = time.time() 
#← 같은 내용으로 두 번째 실행을 함으로써 캐시가 활용되어 즉시 실행 완료됨
result = chat([ 
    HumanMessage(content="안녕하세요! 전 성준이에요")
])

# 시간 종료 
end = time.time() 
print(result.content)
print(f"실행 시간: {end - start}초")