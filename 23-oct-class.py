import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

# Streamlit config
st.set_page_config(page_title="prajBot 💖", page_icon="🤖", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #2f2f2f;
        }
        h1 {
            text-align: center;
            font-size: 3em;
        }
        .title-pink {
            color: #ffb6c1;
        }
        .user-bubble {
            background-color: #d3d3d3;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            color: black;
        }
        .bot-bubble {
            background-color: #ffe4e1;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            color: #d63384;
        }
        .footer {
            text-align: center;
            font-size: 12px;
            color: #ff69b4;
        }
        .stSidebar {
            background-color: #ffb6c1 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar settings
st.sidebar.title("⚙️ Settings")
model_choice = st.sidebar.selectbox("Choose Model", ["mistralai/mistral-7b-instruct", "openai/gpt-3.5-turbo", "meta-llama/llama-2-13b-chat"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 64, 1024, 256)

# Initialize model
llm = ChatOpenAI(
    model=model_choice,
    temperature=temperature,
    max_tokens=max_tokens,
    api_key=api_key,
    base_url=base_url,
)

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Main UI
st.markdown("<h1><span class='title-pink'>prajBot</span> Clocked IN</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your personal AI assistant powered by LangChain & OpenRouter</p>", unsafe_allow_html=True)
st.markdown("---")

# Chat input
user_input = st.text_input("💬 What's cooking in that lil brain today?", placeholder="Ask me anything...")

if user_input:
    # Add user message to history
    st.session_state.chat_history.append(("user", user_input))

    # Prepare messages for model
    messages = [SystemMessage(content="You are a helpful and concise AI assistant.")]
    for role, msg in st.session_state.chat_history:
        if role == "user":
            messages.append(HumanMessage(content=f"<s>[INST] {msg} [/INST]"))

    # Get response
    with st.spinner("Thinking hard... "):
        try:
            response = llm.invoke(messages)
            st.session_state.chat_history.append(("bot", response.content.strip()))
        except Exception as e:
            st.session_state.chat_history.append(("bot", f" Error: {e}"))

# Display chat history
for role, msg in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"<div class='user-bubble'><strong>You:</strong> {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-bubble'><strong>prajBot:</strong> {msg}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p class='footer'>Made with 💖 by Praj using LangChain + OpenRouter + Streamlit</p>", unsafe_allow_html=True)

# NEW

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# 🔧 Function to initialize model dynamically
def get_llm(model_name="mistralai/mistral-7b-instruct", temperature=0.7, max_tokens=256):
    return ChatOpenAI(
        model=model_name,
        temperature=temperature,
        max_tokens=max_tokens,
        api_key=api_key,
        base_url=base_url,
    )

# 🧠 Function to get response from model
def get_response(prompt, model_name="mistralai/mistral-7b-instruct", temperature=0.7, max_tokens=256):
    llm = get_llm(model_name, temperature, max_tokens)
    messages = [
        SystemMessage(content="You are a helpful and concise AI assistant."),
        HumanMessage(content=f"<s>[INST] {prompt.strip()} [/INST]"),
    ]
    try:
        response = llm.invoke(messages)
        return response.content.strip() or "(no content returned)"
    except Exception as e:
        return f"❌ Error: {e}"

# 🧪 Example usage (can be removed in production)
if __name__ == "__main__":
    prompt = "Explain in simple terms how convolutional neural networks work."
    output = get_response(prompt, model_name="mistralai/mistral-7b-instruct", temperature=0.7, max_tokens=256)
    print("Assistant:", output)

#NEW


import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge import Rouge
from sentence_transformers import SentenceTransformer, util

# ---------------------------
# 1. Load environment vars
# ---------------------------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env")

# ---------------------------
# 2. Define two models
# ---------------------------
model_1 = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    temperature=0.7,
    max_tokens=256,
    api_key=api_key,
    base_url=base_url,
)

model_2 = ChatOpenAI(
    model="mistralai/mixtral-8x7b-instruct",
    temperature=0.7,
    max_tokens=256,
    api_key=api_key,
    base_url=base_url,
)

# ---------------------------
# 3. Define prompt
# ---------------------------
messages = [
    SystemMessage(content="You are a helpful and concise AI assistant."),
    HumanMessage(content="<s>[INST] Explain in simple terms what reinforcement learning is. [/INST]")
]

# ---------------------------
# 4. Get responses
# ---------------------------
response_1 = model_1.invoke(messages).content.strip()
response_2 = model_2.invoke(messages).content.strip()

print("\n--- MODEL 1: Mistral 7B ---")
print(response_1)
print("\n--- MODEL 2: Mixtral 8x7B ---")
print(response_2)

# ---------------------------
# 5. Evaluate responses
# ---------------------------

# BLEU
smooth_fn = SmoothingFunction().method1
bleu_score = sentence_bleu(
    [response_1.split()],
    response_2.split(),
    smoothing_function=smooth_fn
)

# ROUGE
rouge = Rouge()
rouge_scores = rouge.get_scores(response_1, response_2)[0]

# Cosine similarity using embeddings
embedder = SentenceTransformer("all-MiniLM-L6-v2")
emb1 = embedder.encode(response_1, convert_to_tensor=True)
emb2 = embedder.encode(response_2, convert_to_tensor=True)
cosine_sim = float(util.cos_sim(emb1, emb2))

# ---------------------------
# 6. Display results
# ---------------------------
print("\n--- Evaluation Metrics ---")
print(f"BLEU Score:  {bleu_score:.4f}")
print(f"ROUGE-1:     {rouge_scores['rouge-1']['f']:.4f}")
print(f"ROUGE-L:     {rouge_scores['rouge-l']['f']:.4f}")
print(f"Cosine Sim:  {cosine_sim:.4f}")