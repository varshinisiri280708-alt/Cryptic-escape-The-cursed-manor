
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Cryptic Escape", layout="wide")

st.title("🎮 Cryptic Escape — The Cursed Manor")
st.write("Enter the manor and solve the mystery!")

game_url = st.text_input(
    "Game URL",
    placeholder="Paste your browser game URL here"
)

if game_url.startswith("https://"):
    components.iframe(game_url, height=700, scrolling=True)
else:
    st.info("Your browser game URL will appear here.")
