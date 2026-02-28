import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import PyPDF2
import docx
import os

class ResumeMatcher:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = TfidfVectorizer(max_features=1000)
        
    def extract_text_from_pdf(self, pdf_path):
        """Extract text from PDF file"""
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text()
        except Exception as e:
            print(f"Error reading PDF: {e}")
        return text
    
    def extract_text_from_docx(self, docx_path):
        """Extract text from DOCX file"""
        text = ""
        try:
            doc = docx.Document(docx_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        except Exception as e:
            print(f"Error reading DOCX: {e}")
        return text
    
    def extract_text_from_txt(self, txt_path):
        """Extract text from TXT file"""
        try:
            with open(txt_path, 'r', encoding='utf-8') as file:
                text = file.read()
        except:
            # Try different encoding if utf-8 fails
            try:
                with open(txt_path, 'r', encoding='latin-1') as file:
                    text = file.read()
            except:
                text = ""
        return text
    
    def extract_text(self, file_path):
        """Extract text based on file extension"""
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.pdf':
            return self.extract_text_from_pdf(file_path)
        elif ext == '.docx':
            return self.extract_text_from_docx(file_path)
        elif ext == '.txt':
            return self.extract_text_from_txt(file_path)
        else:
            return ""
    
    def preprocess_text(self, text):
        """Clean and preprocess text"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Remove numbers
        text = re.sub(r'\d+', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords
        tokens = [token for token in tokens if token not in self.stop_words and len(token) > 2]
        
        return ' '.join(tokens)
    
    def extract_skills(self, text):
        """Extract potential skills from text (simplified version)"""
        # Common tech skills (you can expand this list)
        common_skills = [
            'python', 'java', 'javascript', 'c++', 'sql', 'html', 'css',
            'flask', 'django', 'tensorflow', 'pytorch', 'scikit-learn',
            'pandas', 'numpy', 'matplotlib', 'git', 'docker', 'aws',
            'machine learning', 'deep learning', 'nlp', 'computer vision',
            'data analysis', 'data science', 'ai', 'artificial intelligence',
            'react', 'node.js', 'mongodb', 'postgresql', 'mysql',
            'rest api', 'graphql', 'linux', 'bash', 'excel', 'tableau'
        ]
        
        found_skills = []
        text_lower = text.lower()
        
        for skill in common_skills:
            if skill in text_lower:
                found_skills.append(skill)
        
        return found_skills
    
    def calculate_match(self, resume_text, job_description):
        """Calculate match percentage between resume and job description"""
        
        # Preprocess both texts
        processed_resume = self.preprocess_text(resume_text)
        processed_job = self.preprocess_text(job_description)
        
        # Combine texts for vectorization
        texts = [processed_resume, processed_job]
        
        try:
            # Create TF-IDF vectors
            tfidf_matrix = self.vectorizer.fit_transform(texts)
            
            # Calculate cosine similarity
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
            match_percentage = round(similarity[0][0] * 100, 2)
        except:
            # Fallback if vectorization fails
            match_percentage = 0
        
        # Extract skills from both
        resume_skills = self.extract_skills(resume_text)
        job_skills = self.extract_skills(job_description)
        
        # Calculate skills match
        common_skills = set(resume_skills) & set(job_skills)
        missing_skills = set(job_skills) - set(resume_skills)
        
        skills_match_percent = 0
        if len(job_skills) > 0:
            skills_match_percent = round(len(common_skills) / len(job_skills) * 100, 2)
        
        return {
            'overall_match': match_percentage,
            'skills_match': skills_match_percent,
            'common_skills': list(common_skills),
            'missing_skills': list(missing_skills),
            'resume_skills': resume_skills,
            'job_skills': job_skills
        }