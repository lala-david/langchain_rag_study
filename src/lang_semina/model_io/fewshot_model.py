from langchain.llms import OpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

# 프롬프트 예시 목록 
examples = [
    {
        "input": "에스파의 멤버는 지젤 윈터 카리나 닝닝으로 구성 되어있다.",  
        "output": "에스파의 멤버는 지젤, 윈터, 카리나, 닝닝으로 구성 되어있다!"   
    }
]


prompt = PromptTemplate(  
    # 전체 프롬프트가 기대하는 변수 이름 목록 
    input_variables=["input", "output"], 
    template="입력: {input}\n출력: {output}", 
)

few_shot_prompt = FewShotPromptTemplate(   
    examples=examples,   
    example_prompt=prompt, 
    # 지시어 추가하기
    prefix="아래 문장부호가 빠진 입력에 문장부호를 추가하세요. 추가할 수 있는 문장부호는 ',', '.','!'입니다. 다른 문장부호는 추가하지 마세요.", 
    suffix="입력: {input_string}\n출력:",  
    input_variables=["input_string"],  
)
llm = OpenAI()
formatted_prompt = few_shot_prompt.format( 
    input_string="오늘 에스파의 윈터 카리나를 만날 수 있어서 행복해 에스파 마이퍼스트 시사회를 보러가는데 너무 기대된다"
)

result = llm.predict(formatted_prompt)


print("formatted_prompt: ", formatted_prompt)
print("result: ", result)