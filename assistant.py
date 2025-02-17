from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


class Assistant:
    def __init__(
        self,
        system_prompt,
        llm,
        message_history=[],
        vector_store=None,
        employee_information=None,
    ):
        self.system_prompt = system_prompt
        self.llm = llm
        self.message_history = message_history
        self.employee_information = employee_information 
        self.vector_store = vector_store
        self.chain = self.get_chain() 

    def get_response(self, user_input):
        return self.chain.stream(user_input)
    
    def get_chain(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            MessagesPlaceholder(variable_name="message_history"),
            ("human", "{user_input}"),
        ])
        llm = self.llm
        output_parser = StrOutputParser()
        chain = (
            {
                "retrieved_policy_information": self.vector_store.as_retriever(),
                "employee_information": lambda x: self.employee_information,
                "user_input": RunnablePassthrough(),
                "message_history": lambda x: self.message_history,
            } 
            | prompt 
            | llm 
            | output_parser
        )
        return chain
        