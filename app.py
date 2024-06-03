import streamlit as st
from llm import get_model
from global_settings import PAGE_TITLE_ICON, USER_ICON, ROBOT_ICON


def clear_chat_history():
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I assist you today?"}
    ]


st.set_page_config(page_title=f"{PAGE_TITLE_ICON} Llama Chatbot")

with st.sidebar:
    st.title(f"{PAGE_TITLE_ICON} Llama Chatbot")
    st.subheader("Models and parameters")
    selected_model = st.sidebar.selectbox(
        "Choose a Llama model",
        ["Llama3-8B-8192", "Llama3-70B-8192"],
        key="selected_model",
    )

    if selected_model == "Llama3-8B-8192":
        llm = get_model(model_name="llama3-8b-8192")
    elif selected_model == "Llama3-70B-8192":
        llm = get_model(model_name="llama3-70b-8192")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I assist you today?"}
    ]

## Write Message History
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"], avatar=USER_ICON).write(msg["content"])
    else:
        st.chat_message(msg["role"], avatar=ROBOT_ICON).write(msg["content"])


st.sidebar.button("Clear Chat History", on_click=clear_chat_history)


def generate_response():
    response = llm.stream_complete(prompt)
    for chunks in response:
        st.session_state["full_message"] += chunks.delta
        yield chunks.delta


if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar=USER_ICON).write(prompt)
    st.session_state["full_message"] = ""
    st.chat_message("assistant", avatar=ROBOT_ICON).write_stream(generate_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": st.session_state["full_message"]}
    )
