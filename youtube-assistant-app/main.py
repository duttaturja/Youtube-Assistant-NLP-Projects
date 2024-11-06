import streamlit as st
import LangChain_helper as lch
import textwrap

st.title("Youtube Assistant App")

with st.sidebar:
    with st.form(key='my_form'):
        yt_url = st.sidebar.text_area(label="Enter youtube url: ", max_chars=100)

        query = st.sidebar.text_area(label="Ask me anything: ", max_chars=100, key="query")

        submit = st.form_submit_button(label="Submit")

if yt_url and query and submit:
    db = lch.create_vector_db_from_youtube_url(yt_url)
    response, docs = lch.get_response_from_query(db, query)
    st.subheader("Answer: ")
    st.markdown(textwrap.fill(response, width=85))