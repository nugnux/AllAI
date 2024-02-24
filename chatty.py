import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to interact with OpenAI for text generation
def generate_text(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Streamlit app
def main():
    st.title("Nugroho (Text Generation with OpenAI)")
    st.write("Enter your prompt below:")

    user_input = st.text_area("Prompt:", "")
    if st.button("Generate"):
        if user_input:
            response = generate_text(user_input)
            st.text_area("Generated Text:", value=response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    main()

