from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Client 생성 
chat = ChatOpenAI(  
    model="gpt-3.5-turbo",
)

# Prompt 
prompt = PromptTemplate(
    template="{group}는 어디 소속사인가요？",
    input_variables=[
        "group" 
    ]
)

# 결합 
result = chat(
    [
        HumanMessage(content=prompt.format(group="에스파")),
        HumanMessage(content=prompt.format(group="레드벨벳")),
    ]
)
print(result.content)