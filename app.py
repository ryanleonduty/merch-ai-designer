import streamlit as st
from openai import OpenAI

st.title('🧙 Merch AI Designer: Custom Design Generator')
st.subheader("Create Unique, Print-Ready Designs for Your Merchandise")

st.sidebar.header("Design Input")

api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
image_description = st.sidebar.text_area("Describe the design you'd like to generate:")
merch_text = st.sidebar.text_area("Enter any text to include in the design (leave blank for no text):")
merch_type = st.sidebar.selectbox("Select merchandise type for context:", 
                                  ["T-Shirt", "Mug", "Poster", "Tote Bag"])
submit_button = st.sidebar.button('Generate Design')

def generate_design(description, merch_type, merch_text, api_key):
    client = OpenAI(api_key=api_key)
    prompt = f"""Create ONLY the design artwork for {merch_type}, without any mockup, background, or software interface:
    1. Content: {description}
    2. Text: {merch_text if merch_text else 'No text'}
    3. Style: Vector-like, clean lines, professional look
    4. Background: Transparent (represented as white in the image)
    5. Format: Single, centered design element
    6. Size: Design should fill most of the image area
    7. Colors: Vibrant, print-friendly
    8. IMPORTANT: Do NOT include any t-shirt outlines, mockups, software interfaces or split the design into multiple parts
    9. Output: Only the artwork itself, as if it were a PNG file ready for printing
    10. Perspective: Flat, front-facing design only

    Remember: Generate ONLY the artwork itself, with no product or software representation whatsoever
    Temperature: 0.1"""

    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="hd",
            style="vivid",
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
                st.image(image_url, caption='Your Custom Design')
                st.success("Design generated successfully!")
                st.download_button(
                    label="Download Design",
                    data=image_url,
                    file_name="custom_design.png",
                    mime="image/png"
                )

st.sidebar.info("Note: Your API key is not stored and is only used for this session.")
st.sidebar.markdown("---")

st.sidebar.markdown("""
### How to use:
1. Enter your OpenAI API key.
2. Describe the design you want.
3. Add text if needed.
4. Select merchandise type for context.
5. Click 'Generate Design'.
6. Download the design for use.
""")
