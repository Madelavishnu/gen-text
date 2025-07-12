
'''
import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Streamlit UI
st.set_page_config(page_title="AI Text Summarizer", layout="centered")
st.title("📝 AI Text Summarizer")

# Text input
user_input = st.text_area("Paste your long text here 👇", height=200)

# Summarize button
if st.button("Summarize"):
    if user_input:
        with st.spinner("Generating summary..."):
            summary = summarizer(user_input, max_length=100, min_length=30, do_sample=False)
            st.subheader("📌 Summary:")
            st.success(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")

'''

import streamlit as st
from transformers import pipeline, TFAutoModelForSeq2SeqLM, AutoTokenizer

# Use a small TensorFlow-compatible model like T5
MODEL_NAME = "t5-small"  # or "google/pegasus-xsum" if needed

# Load tokenizer and model (TensorFlow backend)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = TFAutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Build a summarization pipeline using TensorFlow
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer, framework="tf")

# Streamlit UI
st.set_page_config(page_title="AI Text Summarizer", layout="centered")
st.title("📝 AI Text Summarizer")

user_input = st.text_area("Paste your long text here 👇", height=200)

if st.button("Summarize"):
    if user_input:
        with st.spinner("Generating summary..."):
            # Optional: prepend 'summarize:' for T5
            input_text = "summarize: " + user_input.strip()
            summary = summarizer(input_text, max_length=100, min_length=30, do_sample=False)
            st.subheader("📌 Summary:")
            st.success(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text.")
