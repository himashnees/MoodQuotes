import streamlit as st
import requests

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(
    page_title="MoodQuote",
    page_icon="💬",
    layout="centered"
)

# -----------------------------
# Mood Mapping
# -----------------------------
mood_keywords = {
    "😊 Happy": "happiness",
    "😔 Sad": "inspiration",
    "💪 Motivated": "success",
    "😌 Stressed": "wisdom",
    "😠 Angry": "calm",
    "❤️ Love": "love",
    "🌱 Life": "life"
}

# -----------------------------
# App Header
# -----------------------------
st.title("💬 MoodQuote")
st.subheader("Generate quotes from the internet based on your mood")

st.markdown("---")

# -----------------------------
# User Inputs
# -----------------------------
selected_mood = st.selectbox(
    "Select your mood",
    list(mood_keywords.keys())
)

number = st.slider(
    "Number of quotes",
    min_value=1,
    max_value=5,
    value=1
)

# -----------------------------
# Function to Fetch Quote
# -----------------------------
def fetch_quote(keyword=None):
    if keyword:
        url = f"https://zenquotes.io/api/random/{keyword}"
    else:
        url = "https://zenquotes.io/api/random"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    quote = data[0]["q"]
    author = data[0]["a"]

    return quote, author

# -----------------------------
# Display Quote Card
# -----------------------------
def display_quote_card(quote, author):
    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:12px;
            background-color:#f0f2f6;
            border-left:6px solid #4CAF50;
            margin-bottom:18px;">
            <h4 style="color:#222;">“{quote}”</h4>
            <p style="color:#555;"><i>— {author}</i></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.code(f'"{quote}" — {author}')

# -----------------------------
# Generate Mood-Based Quotes
# -----------------------------
if st.button("Generate Mood Quote"):
    keyword = mood_keywords[selected_mood]

    st.success(f"Here are quote(s) for your mood: {selected_mood}")

    for i in range(number):
        try:
            quote, author = fetch_quote(keyword)
            display_quote_card(quote, author)

        except requests.exceptions.RequestException as e:
            st.error("Could not fetch quote from the internet.")
            st.write("Technical error:", e)

        except Exception as e:
            st.error("Something went wrong.")
            st.write("Technical error:", e)

# -----------------------------
# Quote of the Day
# -----------------------------
st.markdown("---")

if st.button("🌞 Quote of the Day"):
    try:
        quote, author = fetch_quote()
        st.success("Here is your Quote of the Day")
        display_quote_card(quote, author)

    except requests.exceptions.RequestException as e:
        st.error("Could not fetch Quote of the Day.")
        st.write("Technical error:", e)

    except Exception as e:
        st.error("Something went wrong.")
        st.write("Technical error:", e)
