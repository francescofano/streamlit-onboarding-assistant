import streamlit as st

class AssistantGUI:
    def __init__(self, assistant):
        self.assistant = assistant
        self.employee_information = assistant.employee_information
        self.message_history = assistant.message_history

    def handle_user_input(self):
        user_input = st.chat_input("Type here...", key="input")
        if user_input and user_input != "":
            st.chat_message("human").markdown(user_input)
            response_generator = self.get_response(user_input)
            with st.chat_message("ai"):
                response = st.write_stream(response_generator)
            self.message_history.append({"role": "user", "content": user_input})
            self.message_history.append({"role": "ai", "content": response})

            self.set_state("messages", self.message_history)

    def get_response(self, user_input):
        return self.assistant.get_response(user_input)
    
    def set_state(self, key, value):
        st.session_state[key] = value

    def display_messages(self):
        messages = self.message_history

        for message in messages:
            if message["role"] == "user":
                st.chat_message("human").markdown(message["content"])
            if message["role"] == "ai":
                st.chat_message("ai").markdown(message["content"])

    def render(self):
        with st.sidebar:
              st.write(self.employee_information)
        st.title("Assistant")
        self.display_messages()
        
        self.handle_user_input()
      
