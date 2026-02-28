# Resume_Screener_Project
# 🤖 AI-Powered Resume Screener

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![NLP](https://img.shields.io/badge/NLP-NLTK-yellow)

## 📋 Overview
An intelligent **AI-powered web application** that automates the resume screening process using Natural Language Processing (NLP) and Machine Learning. This tool helps recruiters quickly identify the best candidates by comparing resumes against job descriptions and calculating match percentages.

## ✨ Features

- 📄 **Multi-format Support**: Upload resumes in PDF, DOCX, or TXT formats
- 🧠 **AI-Powered Analysis**: Uses TF-IDF vectorization and cosine similarity for text comparison
- 🎯 **Skill Extraction**: Automatically identifies and extracts skills from resumes and job descriptions
- 📊 **Match Scoring**: Provides both overall match percentage and skills-specific match percentage
- ✅ **Skill Gap Analysis**: Highlights matched skills and identifies missing requirements
- 🎨 **Beautiful UI**: Clean, modern interface with gradient design
- 🔄 **Real-time Processing**: Instant analysis with uploaded files

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, NLTK
- **Text Processing**: TF-IDF Vectorization, Cosine Similarity
- **File Processing**: PyPDF2, python-docx
- **Frontend**: HTML5, CSS3
- **Version Control**: Git

## 📁 Project Structure
Resume_Screener_Project/
├── app.py # Main Flask application
├── models/
│ └── resume_matcher.py # AI/ML logic for resume matching
├── templates/
│ ├── index.html # Homepage
│ ├── screener.html # Upload page
│ └── results.html # Results display page
├── uploads/ # Temporary file storage
└── requirements.txt # Project dependencies


## 🚀 How It Works

1. **User uploads** a resume (PDF/DOCX/TXT) and pastes a job description
2. **Text extraction** module reads content from the uploaded file
3. **NLP preprocessing** cleans and tokenizes the text
4. **TF-IDF vectorization** converts text to numerical vectors
5. **Cosine similarity** calculates match percentage between resume and job description
6. **Skill extraction** identifies relevant skills from both texts
7. **Results visualization** displays match scores and skill analysis

## 📊 Sample Results

The application provides:
- Overall match percentage
- Skills match percentage
- List of matched skills
- Missing skills analysis
- Complete skill inventory from both resume and job description

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Hanna296-del/Resume_Screener_Project.git
   cd Resume_Screener_Project

Create virtual environment
bash
python -m venv venv
source venv/Scripts/activate  # On Windows

Install dependencies
bash
pip install -r requirements.txt

Download NLTK data
bash
python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('stopwords')
>>> exit()

Run the application
bash
python app.py

Open browser and go to http://127.0.0.1:5000

Dependencies
text
Flask==3.1.3
scikit-learn==1.6.1
nltk==3.9.1
PyPDF2==3.0.1
python-docx==1.1.2
