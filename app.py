import streamlit as st
from sentence_transformers import SentenceTransformer
import fitz  # PyMuPDF
import faiss
import numpy as np
from transformers import pipeline
import tempfile
import re

# Set up the Streamlit app
st.set_page_config(page_title="RAG PDF Q&A")
st.title("📄 Ask Your PDF: Seattle Rent Chatbot")

# Load models
embedder = SentenceTransformer('all-MiniLM-L6-v2')
qa_model = pipeline("text2text-generation", model="google/flan-t5-base")

# Upload PDF
uploaded_file = st.file_uploader("📎 Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    # Extract text from PDF
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()

    # Clean and split text
    def clean_text(text):
        text = re.sub(r"\n+", " ", text)
        text = re.sub(r"\s{2,}", " ", text)
        return text.strip()

    def split_text(text, max_length=500):
        sentences = text.split(". ")
        chunks, current_chunk, current_

