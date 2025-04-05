# Resume Scanner

Resume Scanner is a command-line interface (CLI) tool designed to extract text from resume files in PDF or DOCX formats. It utilizes `spaCy` and `spacy-layout` for document processing and text extraction.

## Prerequisites

- **Python Version**: Ensure you have Python 3.12.9 installed on your system. You can verify your Python version by running:

  ```bash
  python --version
  ```

  If you don't have Python 3.12.9 installed, consider using a version management tool like [pyenv](https://github.com/pyenv/pyenv) to install and manage multiple Python versions.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/ktp-resume-scanner.git
   cd resume-scanner
   ```

2. **Set Up a Virtual Environment**:

   It's recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment named `.venv`:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use '.venv\Scripts\activate'
   ```

3. **Install Dependencies**:

   Install the required packages using `pip`:

   ```bash
   pip install .
   ```

   This will install all necessary dependencies, including `spaCy` and `spacy-layout`.
   This needs to be run every time changes are made to the project.

4. **Download spaCy Model**:

   The tool requires the `en_core_web_sm` model from spaCy. Download it using:

   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage

To extract text from a resume file, run the following command:

```bash
resume-scanner path/to/resume.pdf
```

Replace `path/to/resume.pdf` with the actual path to your resume file. The extracted text will be saved in the `data` directory within the project folder.

## Project Structure

The project is organized as follows:

```
resume-scanner/
├── resume_scanner/
│   ├── __init__.py
│   ├── cli.py
│   ├── parser.py
│   └── analyzer.py
├── data/
│   └── (extracted text files will be saved here)
├── requirements.txt
├── setup.py
└── README.md
```

- `resume_scanner/`: Contains the main package modules.
  - `cli.py`: Handles command-line interactions.
  - `parser.py`: Manages document parsing and text extraction.
  - `analyzer.py`: (Optional) For future text analysis functionalities.
- `data/`: Directory where extracted text files are stored.
- `requirements.txt`: Lists the project's dependencies.
- `setup.py`: Script for packaging and installation.
- `README.md`: This file.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

_Note: For more detailed guidance on writing effective README files, consider referring to [Creating Great README Files for Your Python Projects](https://realpython.com/readme-python-project/)._ citeturn0search0
