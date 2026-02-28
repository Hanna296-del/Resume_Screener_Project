from flask import Flask, render_template, request
import os
from models.resume_matcher import ResumeMatcher

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize our AI matcher
matcher = ResumeMatcher()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/screener', methods=['GET', 'POST'])
def screener():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'resume' not in request.files:
            return "No file uploaded", 400
        
        file = request.files['resume']
        job_description = request.form.get('job_description', '')
        
        if file.filename == '':
            return "No file selected", 400
        
        if file:
            # Save the uploaded file
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # Extract text from resume
            resume_text = matcher.extract_text(filepath)
            
            if not resume_text:
                return "Could not extract text from the file. Please make sure it's a valid text, PDF, or DOCX file."
            
            # Calculate match using AI
            result = matcher.calculate_match(resume_text, job_description)
            
            # Clean up - delete the uploaded file after processing
            try:
                os.remove(filepath)
            except:
                pass
            
            # Display results
            return render_template('results.html', 
                                  filename=file.filename,
                                  result=result)
    
    return render_template('screener.html')

if __name__ == '__main__':
    app.run(debug=True)