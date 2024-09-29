import streamlit as st
import nltk
import dill
import requests
import io

nltk.download('punkt')
nltk.download('stopwords')

# Define the URL of the model file
model_url = 'https://raw.githubusercontent.com/Kanishk-mittal/k-spam-detector/refs/heads/main/model.pkl'  # Replace with your actual URL

# Function to load the model directly from the URL
def load_model_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Load the model using dill from the response content
        return dill.loads(response.content)
    else:
        st.error('Failed to download the model. Please check the URL.')
        return None

# Load the model
model = load_model_from_url(model_url)

# Check if the model was loaded successfully
if model is not None:
    # Create the UI
    st.title('SMS Spam Classifier')
    input_sms = st.text_area('Enter the message', key='msg')
    if st.button('Predict'):
        result = int(model.predict([input_sms])[0])
        if result:
            st.header('Spam')
        else:
            st.header('Not Spam')
