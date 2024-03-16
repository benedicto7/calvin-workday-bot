from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
# from htmlTemplates import css, bot_template, user_template
from langchain_community.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
from langchain.vectorstores import FAISS
import textwrap
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

app = Flask(__name__)
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    # return get_Chat_response(input)

    loader = TextLoader('data/calvinworkday.txt', encoding='ISO-8859-1')
    text1 = loader.load()
    # testing huggning
    wrap_text_preserve_newlines(str(text1[0]))

    # Text Splitter
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    docs = text_splitter.split_documents(text1)

    # Embeddings
    embeddings = HuggingFaceEmbeddings()

    # Vectorstore: https://python.langchain.com/en/latest/modules/indexes/vectorstores.html

    db = FAISS.from_documents(docs, embeddings)

    # # query
    # query = "Suggested Links?"
    # docs = db.similarity_search(query)
    # wrap_text_preserve_newlines(str(docs[0].page_content))

    # create QA chain
    llm=HuggingFaceHub(repo_id="google/flan-ul2", model_kwargs={"temperature":0.01, "max_length":10000})

    chain = load_qa_chain(llm, chain_type="stuff")
    query = input
    docs = db.similarity_search(query)
    answer = chain.run(input_documents=docs, question=query)

    return answer

def wrap_text_preserve_newlines(text, width=110):
    # Split the input text into lines based on newline characters
    lines = text.split('\n')
    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)
    return wrapped_text

if __name__ == '__main__':
    app.run()