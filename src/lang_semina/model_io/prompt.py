from langchain import PromptTemplate 

prompt = PromptTemplate( 
		# group 메개 변수 
    template="{group}는 어디 소속사인가요？",
    input_variables=[
        "group"  
    ]
)

print(prompt.format(group="레드벨벳"))
print(prompt.format(group="에스파"))