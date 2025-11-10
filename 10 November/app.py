# frontend/app.py
import os
import requests
import streamlit as st

st.set_page_config(page_title="Streamlit + FastAPI Demo", page_icon="⚡", layout="centered")
st.title("⚡ Streamlit + FastAPI Demo")

# Allow override via env var for flexibility
BACKEND_URL = os.getenv("ST_BACKEND_URL", "http://127.0.0.1:8000")

with st.sidebar:
    st.subheader("Backend")
    st.write(f"Using: `{BACKEND_URL}`")
    st.caption("Tip: set ST_BACKEND_URL env var to change backend URL.")
    st.divider()
    if st.button("Health check"):
        try:
            r = requests.get(f"{BACKEND_URL}/health", timeout=5)
            st.success(r.json())
        except Exception as e:
            st.error(f"Health check failed: {e}")

def safe_get(url, **kwargs):
    try:
        with st.spinner("Calling API..."):
            r = requests.get(url, timeout=10, **kwargs)
            r.raise_for_status()
            return r.json(), None
    except Exception as e:
        return None, e

def safe_post(url, json=None, **kwargs):
    try:
        with st.spinner("Calling API..."):
            r = requests.post(url, json=json, timeout=10, **kwargs)
            r.raise_for_status()
            return r.json(), None
    except Exception as e:
        return None, e

# -----------------------------------------------------------------------------
# 1) Add Numbers (default values as per your spec: 45 and 35)
# -----------------------------------------------------------------------------
st.header("➕ Add Numbers")
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("First number", value=45, step=1)
with col2:
    b = st.number_input("Second number", value=35, step=1)

if st.button("Add"):
    data, err = safe_get(f"{BACKEND_URL}/add", params={"a": int(a), "b": int(b)})
    if err:
        st.error(f"Error: {err}")
    else:
        st.success(f"Result: **{data['result']}**")

st.divider()

# -----------------------------------------------------------------------------
# 2) Today's Date
# -----------------------------------------------------------------------------
st.header("📅 Today's Date")
if st.button("Get Date"):
    data, err = safe_get(f"{BACKEND_URL}/date")
    if err:
        st.error(f"Error: {err}")
    else:
        st.info(f"Today is **{data['date']}**")

st.divider()

# -----------------------------------------------------------------------------
# 3) Reverse a Word
# -----------------------------------------------------------------------------
st.header("🔁 Reverse a Word")
word = st.text_input("Enter a word", value="Abdullah")
if st.button("Reverse"):
    data, err = safe_post(f"{BACKEND_URL}/reverse", json={"text": word})
    if err:
        st.error(f"Error: {err}")
    else:
        st.success(f"Reversed: **{data['reversed']}**")

st.divider()

# -----------------------------------------------------------------------------
# 4) POST — Model in FastAPI (toy sentiment)
# -----------------------------------------------------------------------------
st.header("🧠 Text Sentiment (Toy Model)")
text = st.text_area("Enter text", value="I love this app, it is awesome but not bad at all!")
if st.button("Analyze"):
    data, err = safe_post(f"{BACKEND_URL}/model/predict", json={"text": text})
    if err:
        st.error(f"Error: {err}")
    else:
        label = data["label"].capitalize()
        score = data["score"]
        st.success(f"Prediction: **{label}** (score: {score})")

st.divider()

# -----------------------------------------------------------------------------
# 5) Simple Feedback Loop
# -----------------------------------------------------------------------------
st.header("📝 Feedback")
fb = st.text_input("Share quick feedback about the UI")
if st.button("Submit Feedback"):
    st.success("Thanks! (This demo just shows a toast; wire to a DB or API in real apps.)")