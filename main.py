import streamlit as st
import requests

# Mood to Quotable tag mapping
mood_tags = {
    "Happy": "happiness",
    "Sad": "inspirational",
    "Motivated": "success",
    "Stressed": "wisdom",
    "Angry": "wisdom",
    "Love": "love",
    "Life": "life"
}

st.header("QUOTES for your MOOD!")
st.subheader("Generate mood-based quotes from the internet")

# Dropdown for mood selection
selected_mood = st.selectbox(
    "Select your mood",
    list(mood_tags.keys())
)

# Number of quotes
number = st.number_input(
    "Number of quotes",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

if st.button("Generate"):
    tag = mood_tags[selected_mood]

    url = f"https://api.quotable.io/quotes/random?tags={tag}&limit={number}"

    try:
        response = requests.get(url, timeout=10)
        st.write("Status Code:", response.status_code)
st.write("Response:", response.text)
response.raise_for_status()

        quotes = response.json()

        st.success(f"Here are {number} quote(s) for mood: {selected_mood}")

        for item in quotes:
            quote = item["content"]
            author = item["author"]

            st.write(f"**“{quote}”**")
            st.write(f"— {author}")
            st.divider()

    except requests.exceptions.RequestException as e:
    st.error(f"Request Error: {e}")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
    
