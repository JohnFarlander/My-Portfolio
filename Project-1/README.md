# 🧼 Customer Input Data Cleaning Pipeline

## 📌 Project Overview

In many real-world data science workflows, raw customer text data is too **noisy and inconsistent** to be used directly for analysis.  
This project implements a robust **Natural Language Processing (NLP)** preprocessing pipeline that transforms messy customer feedback into clean, structured, analysis-ready tokens.

The system is optimized to handle:
- Internet slang  
- Repeated characters  
- Emojis  
- HTML tags  
- Punctuation noise  

This ensures that downstream models (e.g., Sentiment Analysis, Keyword Extraction, Classification models) receive high-quality input data.

---

## ✨ Key Technical Features

### 🔹 Modular Pipeline Architecture
Each preprocessing task is implemented as an independent function, improving:
- Code readability
- Maintainability
- Scalability

---

### 🔹 Regex-Based Normalization
Uses advanced **Regular Expressions (Regex)** to:
- Normalize repeated characters  
  - `"soooooo"` → `"soo"`
- Remove unnecessary punctuation
- Standardize text patterns

---

### 🔹 HTML & Emoji Removal
- Removes HTML tags using `BeautifulSoup`
- Strips emojis using the `emoji` library
- Reduces non-semantic noise from user input

---

### 🔹 Vectorized Data Processing
Leverages **Pandas vectorized operations** to efficiently process **1000+ entries** without slow Python loops.

---

### 🔹 Interactive Streamlit GUI
Built with **Streamlit** to allow:
- CSV/Excel file uploads
- Real-time preview of cleaned data
- Downloadable processed output
- Easy use for non-technical stakeholders

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Libraries:**
  - Pandas  
  - NLTK  
  - Streamlit  
  - BeautifulSoup4  
  - Emoji  
  - Openpyxl  

---

## 📂 Project Structure

```
Project-1-Text-Cleaner/
│
├── ML_Project_1.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd Project-1-Text-Cleaner
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run ML_Project_1.py
```

The app will open automatically in your browser.

---

## 📊 Sample Transformation

| Before Cleaning | After Cleaning |
|----------------|---------------|
| `"I am soooooo happy with the service!!! 😀🚀"` | `"happy service"` |
| `"The food was <b>AWESOME</b> but the wait was long."` | `"food awesome wait long"` |

---

## 🎯 Problem Solved

Raw customer feedback is often inconsistent and filled with noise, making NLP models inaccurate or biased.  
This project ensures:

- Cleaner token distribution  
- Reduced dimensionality  
- Improved sentiment analysis accuracy  
- Better model generalization  

---

## 📈 Performance Consideration

- Handles 1,000+ entries efficiently  
- Avoids unnecessary loops  
- Uses optimized Pandas transformations  

---

## 🧠 Future Improvements

- Add lemmatization with spaCy  
- Deploy on cloud (Streamlit Cloud / Render)  
- Add language detection  
- Integrate basic sentiment scoring  

---
