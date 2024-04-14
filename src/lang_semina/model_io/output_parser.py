from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import DatetimeOutputParser  #← Output Parser인 DatetimeOutputParser를 가져오기
from langchain.schema import HumanMessage

# DatetimeOutputParser를 초기화
output_parser = DatetimeOutputParser() 

chat = ChatOpenAI(model="gpt-3.5-turbo", )

prompt = PromptTemplate.from_template("{group}의 출시일을 알려주세요")

result = chat(
    [
        HumanMessage(content=prompt.format(group="iphone12 mini")),  
        # 언어모델에 지시사항 추가하기
        HumanMessage(content=output_parser.get_format_instructions()),  
    ]
)

# 출력 결과를 분석하여 날짜 및 시간 형식으로 변환
output = output_parser.parse(result.content) 

print(output)