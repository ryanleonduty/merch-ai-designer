import streamlit as st
from openai import OpenAI
import requests

st.title('🧙 Merch AI Designer: Custom Design Generator')

st.sidebar.header("Design Input")
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
image_description = st.sidebar.text_area("Describe the design you'd like to generate:")
merch_text = st.sidebar.text_area("Enter any text to include in the design (leave blank for no text):")
merch_type = st.sidebar.selectbox("Select merchandise type for context:", 
                                  ["T-Shirt", "Mug", "Poster", "Tote Bag"])
submit_button = st.sidebar.button('Generate Design')

def generate_design(description, merch_type, merch_text, api_key):
    client = OpenAI(api_key=api_key)
    prompt = f"""Create a design for {merch_type}:
        a. Follow the user description: {description}
        b. Include the text: {merch_text if merch_text else 'No text'}
        c. Show only the design as it appears on the {merch_type}, without any standalone illustrations or alternative presentations."""
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="hd",
            style='vivid',
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

if submit_button:
    if not api_key:
        st.error("Please enter your OpenAI API key.")
    elif not image_description:
        st.error("Please enter a design description.")
    else:
        with st.spinner('Generating your design...'):
            image_url = generate_design(image_description, merch_type, merch_text, api_key)
            
            if image_url:
                try:
                    # Fetch the image data
                    response = requests.get(image_url)
                    response.raise_for_status()  # Raises an HTTPError for bad responses
                    img_data = response.content
                    
                    # Display the image
                    st.image(image_url, caption='Your Custom Design')
                    st.success("Design generated successfully!")
                    
                    # Provide download button
                    st.download_button(
                        label="Download Design",
                        data=img_data,
                        file_name="custom_design.png",
                        mime="image/png"
                    )
                except requests.RequestException as e:
                    st.error(f"Failed to fetch the image: {str(e)}")

st.sidebar.info("Note: Your API key is not stored and is only used for this session.")
st.sidebar.markdown("---")
st.sidebar.markdown("""

### How to use:
1. Enter your OpenAI API Key.
2. Describe the design you want.
3. Add text if needed.
4. Select merchandise type for context.
5. Click 'Generate Design'.
6. Download the design for use.
""")
