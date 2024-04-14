from langchain.llms import OpenAI

# 호출 모델
llm1 = OpenAI(model="gpt-3.5-turbo-instruct" 
             )

result1 = llm1(
    "아 배고파 맛있는 라면을 ",
    stop="." 
)
print(result1)
