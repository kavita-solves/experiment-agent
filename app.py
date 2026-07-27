import streamlit as st
from langchain.messages import HumanMessage,AIMessage
from agent import agent

st.title("🧪 Experiment Designer")
st.caption("Design rigorous experiments in minutes")

# Memory - retain the memory after refresh

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "session_1"

# display the conversation history

for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    else:
        with st.chat_message("assistant"):
            if hasattr(message, 'content') and message.content:
                st.write(message.content)

# User input - input box

if prompt:= st.chat_input("Describe your experiment idea..."):
    # User message
    #user_msg = HumanMessage(content = prompt)
    #st.session_state.messages.append(user_msg)
    with st.chat_message("user"):
        st.write(prompt)

    # Agent response
    with st.chat_message("assistant"):
        with st.spinner("thinking..."):
            response = agent.invoke(
                {"messages": [HumanMessage(content = prompt)]},
                {"configurable": {"thread_id": st.session_state.thread_id}}
            )
            ai_response = response['messages'][-1].content
            st.write(ai_response)
    st.session_state.messages.append(HumanMessage(content = prompt))
    st.session_state.messages.append(AIMessage(content=ai_response))

    #I want to test a new hero image in our onboarding email
