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

Python API
pythonfrom resume_analyzer import ResumeAnalyzer

# Initialize analyzer
analyzer = ResumeAnalyzer()

# Analyze resume
result = analyzer.analyze_resume_from_file("path/to/resume.pdf")

# Get profile and matches
profile = result["profile"]
matches = result["matches"]

# Print top match
print(f"Best match: {matches[0].job_role.title} - {matches[0].match_score:.2%}")
🏗️ Architecture
├── resume_analyzer.py      # Main application file
├── models/
│   ├── skill_extractor.py  # NLP skill extraction
│   ├── job_matcher.py      # ML job matching
│   └── database.py         # Database operations
├── data/
│   ├── job_roles.json      # Sample job database
│   └── skill_categories.json
├── tests/
│   ├── test_parser.py
│   ├── test_matcher.py
│   └── sample_resumes/
└── config.json            # Configuration file
🔧 Configuration
Create a config.json file:
json{
  "mongodb_uri": "mongodb://localhost:27017/",
  "database_name": "resume_analyzer",
  "max_file_size_mb": 10,
  "skill_confidence_threshold": 0.3,
  "match_score_threshold": 0.4
}
📊 API Endpoints
The system can be extended with REST API endpoints:

POST /analyze - Analyze resume from uploaded file
GET /profile/{id} - Get stored profile
POST /match - Get job matches for profile
GET /jobs - List available job roles
GET /analytics - Get platform analytics

🧪 Testing
bash# Run tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=resume_analyzer tests/
🤝 Contributing

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

spaCy for NLP processing
Streamlit for the web interface
scikit-learn for ML algorithms
MongoDB for data persistence

🚀 Future Enhancements

 BERT-based embeddings for better semantic matching
 Real-time job scraping from job boards
 Resume optimization suggestions
 Interview preparation recommendations
 Salary prediction models
 Multi-language support
 REST API development
 Docker containerization
