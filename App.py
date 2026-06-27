import streamlit as st
from difflib import get_close_matches

st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖"
)

st.title("🤖 FAQ Chatbot")
st.write("Ask questions about AI and programming")

faq = {
    "what is ai":"Artificial Intelligence allows machines to think and learn.",
    
    "what is python":"Python is a popular programming language.",
    
    "what is machine learning":"Machine Learning helps systems learn from data.",
    
    "what is nlp":"Natural Language Processing helps computers understand language.",
    
    "what is deep learning":"Deep Learning uses neural networks.",
    
    "what is streamlit":"Streamlit is used to create web apps using Python.",
    
    "what is chatbot":"A chatbot is a program that responds to users automatically."
}

question = st.text_input("Ask your question:")

if st.button("Send"):

    question = question.lower()

    matches = get_close_matches(
        question,
        faq.keys(),
        n=1,
        cutoff=0.4
    )

    if matches:
        answer = faq[matches[0]]
        st.success("Bot Response:")
        st.write(answer)

    else:
        st.error("Sorry, I don't know the answer.")