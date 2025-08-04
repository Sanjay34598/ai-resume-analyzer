# 🤖 AI Resume Analyzer + Job Matcher

An intelligent resume analysis and job matching system powered by NLP and machine learning.

## 🌟 Features

- **Smart Resume Parsing**: Extracts skills, experience, and education from PDF resumes
- **AI-Powered Skill Analysis**: Uses spaCy NLP to identify and categorize skills
- **Proficiency Assessment**: Estimates skill levels based on context analysis
- **Intelligent Job Matching**: ML-based matching algorithm with similarity scoring
- **Gap Analysis**: Identifies missing skills for target roles
- **Interactive Dashboard**: Beautiful Streamlit web interface
- **Data Persistence**: MongoDB integration for storing profiles and analytics

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MongoDB (optional, for data persistence)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-resume-analyzer.git
   cd ai-resume-analyzer
2. Install dependencies
bashpip install -r requirements.txt
python -m spacy download en_core_web_sm

3. Set up MongoDB (optional)
bash# Install MongoDB or use MongoDB Atlas
# Update connection string in config.json

4. Run the application
bashstreamlit run resume_analyzer.py


📖 Usage
Web Interface

Navigate to http://localhost:8501
Upload your PDF resume
View detailed skill analysis and proficiency scores
Get personalized job recommendations
Analyze skill gaps for target roles
