import uuid

import streamlit as st
from langchain.messages import HumanMessage, AIMessage

from agent import agent


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Experiment Designer",
    page_icon="🧪",
    layout="centered",
)


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Do not use the same thread_id for every user.
# A unique thread keeps conversations separate.
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "example_prompt" not in st.session_state:
    st.session_state.example_prompt = None


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

header_col, reset_col = st.columns([5, 1])

with header_col:
    st.title("🧪 AI Experiment Design Copilot")
    st.caption(
        "From idea to experiment design in minutes."
    )

with reset_col:
    if st.session_state.messages:
        if st.button("Start over", use_container_width=True):
            st.session_state.messages = []
            st.session_state.thread_id = str(uuid.uuid4())
            st.session_state.example_prompt = None
            st.rerun()


# ---------------------------------------------------------
# LANDING CONTENT
# Show only before the conversation begins
# ---------------------------------------------------------

if not st.session_state.messages:
    st.markdown(
        """
        Describe what you want to test. The agent will ask one question
        at a time and help you create a complete experiment design.
        """
    )

    st.markdown("#### What you will receive")

    feature_col_1, feature_col_2 = st.columns(2)

    with feature_col_1:
        st.markdown(
            """
            - Clear problem statement  
            - Null and alternative hypotheses  
            - Primary and guardrail metrics  
            """
        )

    with feature_col_2:
        st.markdown(
            """
            - Sample-size calculation  
            - Estimated duration  
            - Experiment setup and split  
            """
        )

    st.markdown("#### Try an example")

    example_col_1, example_col_2 = st.columns(2)

    with example_col_1:
        if st.button(
            "🛒 Test a redesigned checkout flow",
            use_container_width=True,
        ):
            st.session_state.example_prompt = (
                "I want to test whether a redesigned checkout flow "
                "increases purchases on our website."
            )
            st.rerun()

        if st.button(
            "📧 Test a new onboarding email",
            use_container_width=True,
        ):
            st.session_state.example_prompt = (
                "I want to test a new hero image in our onboarding email."
            )
            st.rerun()

    with example_col_2:
        if st.button(
            "📱 Test a push notification",
            use_container_width=True,
        ):
            st.session_state.example_prompt = (
                "I want to test a new push notification designed "
                "to increase app engagement."
            )
            st.rerun()

        if st.button(
            "💳 Improve subscription conversion",
            use_container_width=True,
        ):
            st.session_state.example_prompt = (
                "I want to test a new subscription offer "
                "to improve paid conversion."
            )
            st.rerun()

    st.info(
        "You do not need to know the sample size, experiment duration, "
        "or statistical terminology before you begin."
    )

    st.divider()


# ---------------------------------------------------------
# DISPLAY CONVERSATION HISTORY
# ---------------------------------------------------------

for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            if message.content:
                st.markdown(message.content)


# ---------------------------------------------------------
# COLLECT INPUT
# Accept either typed input or an example-button prompt
# ---------------------------------------------------------

typed_prompt = st.chat_input(
    "Describe your experiment idea...",
)

prompt = st.session_state.example_prompt or typed_prompt


# ---------------------------------------------------------
# RUN AGENT
# ---------------------------------------------------------

if prompt:
    # Clear button-generated prompt so it does not run again
    st.session_state.example_prompt = None

    user_message = HumanMessage(content=prompt)
    st.session_state.messages.append(user_message)

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Designing the next step..."):
            try:
                response = agent.invoke(
                    {"messages": [user_message]},
                    {
                        "configurable": {
                            "thread_id": st.session_state.thread_id
                        }
                    },
                )

                ai_response = response["messages"][-1].content
                st.markdown(ai_response)

                st.session_state.messages.append(
                    AIMessage(content=ai_response)
                )

            except Exception as error:
                st.error(
                    "I could not process that request. "
                    "Please try again."
                )
                st.exception(error)