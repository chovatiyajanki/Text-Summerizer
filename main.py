import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time 

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Google API key not found! Please check your .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI

# Page configuration
st.set_page_config(
    page_title="Text Summarizer", 
    layout="centered")

# Title
st.title("Text Summarizer")
st.write("Enter your text below and customize the summary.")

# Text Input
st.subheader("Enter Text Here:")

user_input = st.text_area(
    "Enter Your Text Area", 
    height=200,
    placeholder="Enter Or Paste Your Text....")

# Word count 
if user_input:
    st.info(f"Word Count: {len(user_input.split())}")

# Summary Length Option
length_option = st.selectbox(
    "Select Summary Length:",
    ["Select Length","Short", "Medium", "Long"]
)

# Tone Option
tone_option = st.selectbox(
    "Select Tone of Voice:",
    ["Select Tone","Formal", "Casual", "Professional", "Friendly","Funny"]
)

# Generate Summary

if st.button("Generate Summary", use_container_width=True):

    if not user_input:
        st.warning("Please Enter Some Text.")
    else:
        try:
            with st.spinner("Generating Summary...."):

                prompt = f"""
                You are an expert text summerizer.
                
                Summarize the following text.
                
                Requirements:
                -  Length: {length_option}
                -  Tone: {tone_option}
                -  Keep important information only
                -  Return only the summary

                Text:
                {user_input}
                """

                response = model.generate_content(prompt)

                st.success("Summary Genearted Successfully!")

                st.subheader("Generated Summary")

                st.text_area(
                    "Summary Output",
                    value=response.text,
                    height=250
                )
        except Exception as e:
            error_message = str(e)
            if "429" in error_message:
                st.error("""
                            Gemini API quota exceeded.
                            You Have reached the free-tier request limit.

                            Please:
                            1. Wait about 1 minute.
                            2. Try Again.
                            3. Or upgrade our gemini API plan.
                            This is not a codeing error. 
                         """
                        )
            elif "API_KEY" in error_message.upper():
                st.error("Invalid Gemini API key.")
            else:
                st.error(f"Error : {error_message}")
# Footer 
st.markdown("----")
st.caption("Bulit with stramlit and Google Gemini AI")
    


   