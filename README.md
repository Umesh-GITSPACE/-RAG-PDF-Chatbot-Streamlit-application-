# RAG PDF Chatbot – Ask Questions About Your PDF Using AI

This project is a Retrieval-Augmented Generation (RAG) chatbot built using Streamlit that allows users to upload a PDF file and ask natural language questions about its contents.

It combines PDF text extraction, semantic search, and answer generation using the following tools:
- PyMuPDF for extracting text from PDFs
- SentenceTransformers for converting text into embeddings
- FAISS for performing similarity search over embedded text chunks
- FLAN-T5 (via Hugging Face Transformers) for generating answers
- Streamlit for a lightweight, interactive web interface

The app can be run both locally and in Google Colab, with support for public access via ngrok.

## What This App Does

1. Accepts a PDF file upload
2. Extracts and cleans text from the file
3. Splits text into 500-character chunks
4. Embeds those chunks using all-MiniLM-L6-v2
5. Stores them in a FAISS index for fast similarity search
6. Accepts a user question, finds top matching chunks, and builds a prompt
7. Uses FLAN-T5 to generate a contextual answer
8. Displays the response in the Streamlit app

## Project Structure


## Dependencies

See `requirements.txt` for detailed versions and comments. It includes:

- streamlit
- sentence-transformers
- transformers
- faiss-cpu
- PyMuPDF
- numpy, scipy, scikit-learn
- torch
- pyngrok (for Colab support)

## How to Run the App Locally

1. Clone the repository:
   git clone https://github.com/yourusername/rag-pdf-chatbot.git

2. Navigate to the project folder:
   cd rag-pdf-chatbot

3. Install dependencies:
   pip install -r requirements.txt

4. Launch the app:
   streamlit run app.py

## How to Run in Google Colab

If you want to run the app in Google Colab:

1. Clone the repository:
   !git clone https://github.com/yourusername/rag-pdf-chatbot.git
   %cd rag-pdf-chatbot

2. Install requirements:
   !pip install -r requirements.txt

3. Run Streamlit in the background:
   !streamlit run app.py &> streamlit.log &

4. Open a public URL using ngrok:
   from pyngrok import ngrok  
   public_url = ngrok.connect(8501)  
   print("Streamlit app running at:", public_url)

## Example Use Case

You can upload a PDF like a Seattle Rent Market Report and ask:

"How have rent prices changed since 2020?"

The app retrieves the most relevant sections and generates an answer using FLAN-T5.

## To-Do

- Add multi-PDF support
- Let users switch between different models (e.g., GPT-3.5)
- Highlight source content for answers
- Add session memory or history

## Author

Umesh D.  
Connect on LinkedIn(https://www.linkedin.com/in/umesh-dhoddapaneni-355b57284/)

## License

MIT License
