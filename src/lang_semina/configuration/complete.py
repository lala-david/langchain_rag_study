import json
import openai

# Completion 사용 
response = openai.Completion.create(
		# 3.5-turbo-instruct를 지정
    engine="gpt-3.5-turbo-instruct", 
    # prompt를 지정
    prompt="에스파의 윈터가 엄청",
    # 문자가 나타나면 문장 종료  
    stop=".",
    max_tokens=100, 
    n=2, 
    temperature=0.5
)

print(json.dumps(response, indent=2, ensure_ascii=False))