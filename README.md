# 🧙 Merch AI Designer: Custom Design Generator

Merch AI Designer is a Streamlit application that enables users to generate custom designs for various types of merchandise such as T-Shirts, Mugs, Posters, and Tote Bags using the power of OpenAI's image generation API.

## Features

- **Custom Design Generation**: Users can describe the design they want to generate and optionally include text to be integrated into the design.
- **Support for Multiple Merchandise Types**: Choose from different types of merchandise to apply your design to, including T-Shirts, Mugs, Posters, and Tote Bags.
- **API Integration**: Uses OpenAI's API to generate high-quality designs based on user descriptions.
- **Interactive UI**: Easy-to-use sidebar for inputting design specifications and generating designs.
- **Secure API Key Handling**: The API key is only used for the session and is not stored, ensuring user credentials remain secure.
- **Image Preview and Download**: Users can preview the generated design and download it directly from the app.

## Getting Started

### Prerequisites

- An OpenAI API key. You can obtain one by creating an account on [OpenAI's platform](https://platform.openai.com/signup).

### Installation

To run this application locally, you need to have Python and Streamlit installed. If you don't have Streamlit installed, you can install it using pip:

```bash
pip install requirements.txt
```

### How to Run

1. Clone the repository or download the source code.
2. Navigate to the directory containing the app script.
3. Run the application using Streamlit:

```bash
streamlit run app.py
```

### Usage

1. **Enter Your OpenAI API Key**: Securely input your API key in the sidebar.
2. **Describe Your Design**: Provide a detailed description of the design you want to generate.
3. **Add Optional Text**: If you want text included in your design, enter it in the sidebar.
4. **Select Merchandise Type**: Choose the type of merchandise for your design context.
5. **Generate Design**: Click the 'Generate Design' button to process your request.
6. **Download Your Design**: Once generated, you can preview and download your custom design.

## Security Note

Your API key is not stored and is only used for the current session to ensure security.
