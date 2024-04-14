import json
import openai 

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  
    messages=[
        {
            "role": "user",
            "content": "에스파의 신곡은 무엇인가요?"  
        },
    ],
    max_tokens=100,
    temperature=1,
    n=2
)

print(json.dumps(response, indent=2, ensure_ascii=False))