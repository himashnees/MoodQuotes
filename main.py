import streamlit as st
import requests

# Mood to keyword mapping
mood_keywords = {
    "Happy": "happiness",
    "Sad": "inspiration",
    "Motivated": "success",
    "Stressed": "wisdom",
    "Angry": "calm",
    "Love": "love",
    "Life": "life"
}

st.header("QUOTES for your MOOD!")
st.subheader("Generate quotes from the internet based on your mood")

selected_mood = st.selectbox(
    "Select your mood",
    list(mood_keywords.keys())
)

if st.button("Generate"):
    keyword = mood_keywords[selected_mood]

    url = f"https://zenquotes.io/api/random/{keyword}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        quote = data[0]["q"]
        author = data[0]["a"]

        st.success(f"Quote for mood: {selected_mood}")

        st.write(f"**“{quote}”**")
        st.write(f"— {author}")

    except requests.exceptions.RequestException as e:
        st.error("Could not fetch quote from the internet.")
        st.write("Technical error:", e)

    except Exception as e:
        st.error("Something went wrong.")
        st.write("Technical error:", e)
