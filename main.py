import streamlit as st
from rag import generate_answer, process_urls

# Set page configuration
st.set_page_config(page_title="Smart URL Answer Bot", page_icon="🔍", layout="wide")

# Custom CSS for cleaner input and smaller links
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2rem;
            color: #aaa;
            margin-bottom: 2rem;
        }
        .stTextInput > div > input {
            background-color: #2a2a2a !important;
            color: white !important;
            border: none !important; /* ✅ Removes red border */
            border-radius: 6px !important;
        }
        .small-link {
            font-size: 0.85rem;
            color: #4da6ff;
        }
    </style>
""", unsafe_allow_html=True)

# App Title & Subtitle
st.markdown("<div class='title'>🔍 Your Smart URL Answer Bot</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ask natural language questions based on content from your favorite web pages.</div>", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 2])

# --- Left Column: URL Input and Processing ---
with col1:
    st.markdown("### 📥 Enter URLs to Process")
    url1 = st.text_input("🔗 URL 1")
    url2 = st.text_input("🔗 URL 2")
    url3 = st.text_input("🔗 URL 3")

    process_btn = st.button("🚀 Process URLs")
    status_placeholder = st.empty()

    if process_btn:
        urls = [url for url in (url1, url2, url3) if url.strip()]
        if not urls:
            status_placeholder.error("⚠️ Please enter at least one valid URL.")
        else:
            with st.spinner("Processing URLs..."):
                for status in process_urls(urls):
                    status_placeholder.info(status)

# --- Right Column: Question & Answer ---
with col2:
    st.markdown("### 💬 Ask a Question")
    query = st.text_input("Type your question here and press Enter:")

    if query:
        try:
            answer, sources = generate_answer(query)
            st.success("✅ Answer Generated!")

            st.markdown("#### 🧠 Answer")
            st.markdown(f"> {answer}")

            if sources:
                st.markdown("#### 📚 Sources")
                for source in sources.strip().split("\n"):
                    if source.strip():
                        short_url = source.replace("https://", "").replace("www.", "")
                        st.markdown(
                            f"<a href='{source}' target='_blank' class='small-link'>🔗 {short_url}</a>",
                            unsafe_allow_html=True
                        )
        except RuntimeError:
            st.error("⚠️ You must process the URLs first before asking a question.")
