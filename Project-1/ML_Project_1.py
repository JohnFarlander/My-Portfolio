import pandas as pd
import re
import emoji
import streamlit as st
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
# Initialize NLTK resources automatically
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
# Define global stopwords
STOP_WORDS = set(stopwords.words('english'))
#1. Cleaning Function
def expand_contractions(text):
    contractions = {
        "can't": "cannot", "won't": "will not", "didn't": "did not",
        "don't": "do not", "it's": "it is", "i'm": "i am",
        "they're": "they are", "you've": "you have"
    }
    words = text.split()
    converted = [contractions.get(word.lower(), word) for word in words]
    return " ".join(converted)
def clean_text(text):
    if not isinstance(text, str) or text.strip() == "":
        return ""
    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()
    # Remove Emojis
    text = emoji.replace_emoji(text, replace='')
    # Expand contractions and lowercase
    text = expand_contractions(text.lower())
    # Normalize repeated chars (e.g., "goooood" -> "good")
    text = re.sub(r'(.)\1+', r'\1\1', text)
    # Remove non-alphabetic
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Stopword removal
    words = text.split()
    text = " ".join([w for w in words if w not in STOP_WORDS])
    return text.strip()

#2. Streamlit App
st.set_page_config(page_title="Text Cleaner", layout="wide")
st.title("🧼 Customer Data Cleaning Pipeline")
uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=['csv', 'xlsx'])
if uploaded_file:
    # Load data
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.write("### Data Preview")    # Data Preview
    st.dataframe(df.head(5))        # Shows the user what the columns look like first
    all_columns = df.columns.tolist()
    target_col = st.selectbox("Which column contains the text to clean?", all_columns)

    # 3. Proceed with cleaning logic
    if target_col:
        if st.button("Start Cleaning Process"):
            with st.spinner('Cleaning in progress...'):
                # Metadata before
                df['word_count_before'] = df[target_col].apply(lambda x: len(str(x).split()))
                # Apply Cleaning
                df['cleaned_comment'] = df[target_col].apply(clean_text)   
                # Metadata after
                df['word_count_after'] = df['cleaned_comment'].apply(lambda x: len(str(x).split()))
                df['cleaning_success'] = df['cleaned_comment'].apply(lambda x: len(x) > 0)
            st.balloons()
            st.write("### Preview of Results", df.head(10))
            csv = df.to_csv(index=False).encode('utf-8')       # Download Button
            st.download_button(
                label="📥 Download Cleaned Data",
                data=csv,
                file_name="cleaned_data.csv",
                mime="text/csv"
            )
            csv_data = df.to_csv(index=False).encode('utf-8')  # Download as CSV
            st.download_button("📥 Download Results", csv_data, "cleaned_data.csv", "text/csv")
    else:
        st.error("Missing column: Please ensure your file has a 'Comment' column.")