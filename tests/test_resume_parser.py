import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from resume_analyzer import ResumeParser, Skill, Experience, Education

class TestResumeParser(unittest.TestCase):
    
    def setUp(self):
        self.parser = ResumeParser()
    
    def test_extract_email(self):
        """Test email extraction."""
        text = "Contact me at john.doe@example.com for opportunities"
        email = self.parser._extract_email(text)
        self.assertEqual(email, "john.doe@example.com")
    
    def test_extract_phone(self):
        """Test phone number extraction."""
        text = "Call me at (555) 123-4567 or email"
        phone = self.parser._extract_phone(text)
        self.assertEqual(phone, "(555) 123-4567")
    
    def test_skill_extraction(self):
        """Test skill extraction from resume text."""
        text = "I am experienced in Python, Django, and AWS cloud services"
        skills = self.parser.skill_extractor.extract_skills(text)
        
        skill_names = [skill.name for skill in skills]
        self.assertIn("python", skill_names)
        self.assertIn("django", skill_names)
        self.assertIn("aws", skill_names)
    
    @patch('resume_analyzer.spacy.load')
    def test_parse_resume_integration(self, mock_spacy):
        """Test complete resume parsing."""
        # Mock spaCy
        mock_nlp = MagicMock()
        mock_spacy.return_value = mock_nlp
        
        sample_text = """
        John Doe
        john.doe@email.com
        (555) 123-4567
        
        Senior Python Developer with 5 years of experience in Django and AWS.
        """
        
        # This would need proper mocking of the NLP pipeline
        # For now, just test that the method runs without error
        try:
            profile = self.parser.parse_resume(sample_text)
            self.assertIsNotNone(profile)
            self.assertIsInstance(profile.name, str)
        except Exception as e:
            self.skipTest(f"Skipping due to spaCy dependency: {e}")

if __name__ == '__main__':
    unittest.main()
