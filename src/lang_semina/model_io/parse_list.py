from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser 
from langchain.schema import HumanMessage

# CommaSeparatedListOutputParser 초기화
output_parser = CommaSeparatedListOutputParser() 

chat = ChatOpenAI(model="gpt-3.5-turbo", )

result = chat(
    [
        HumanMessage(content="에스파의 대표적인 곡 3곡을 이야기 해주세요"),
        HumanMessage(content=output_parser.get_format_instructions()), 
    ]
)

output = output_parser.parse(result.content) 

for song in output:
    print("대표 곡 => " + song)