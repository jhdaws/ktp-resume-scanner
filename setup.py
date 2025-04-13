from setuptools import setup, find_packages

setup(
    name="resume_scanner",
    version="0.1",
    description="A CLI tool to scan resumes using spaCy, spaCy-Layout, textstat, and more.",
    packages=find_packages(),
    install_requires=[
        "spacy>=3.0.0",
        "spacy-layout",
        "textstat",
        "python-docx",
        "PyMuPDF",
        "openai",
        "dotenv",
    ],
    entry_points={
        "console_scripts": [
            "resume-scanner=resume_scanner.cli:main",
        ],
    },
)
