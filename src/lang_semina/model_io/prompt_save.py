from langchain import PromptTemplate

prompt = PromptTemplate(template="{group}의 멤버는 누가 있습니까 영어로 작성하세요", input_variables=["group"])
prompt_json = prompt.save("prompt.json")  