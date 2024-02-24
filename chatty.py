import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"


# Function to interact with ChatGPT
def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response['choices'][0]['message']['content']

# Streamlit app
def main():
    st.title("Chat Nugroho (assisted by ChatGPT)")
    st.write("Enter your message below:")

    user_input = st.text_input("You:", "")
    if st.button("Send"):
        if user_input:
            response = chat_with_gpt(user_input)
            st.text_area("ChatGPT:", value=response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    main()

