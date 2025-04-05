import spacy
from spacy_layout import spaCyLayout
from pathlib import Path

def load_model():
    # Create blank English model
    nlp = spacy.blank("en")
    # Initialize spaCyLayout with the NLP object
    layout = spaCyLayout(nlp)
    return layout

def extract_text(file_path: str) -> str:
    # Load the layout processor
    layout = load_model()
    
    # Process the document
    file_path = Path(file_path)
    doc = layout(file_path)
    
    # Return cleaned text with proper structure
    return doc.text

# Optional: Add pipeline components example
def extract_structured_data(file_path: str):
    # Load a full NLP pipeline
    nlp = spacy.load("en_core_web_sm")
    layout = spaCyLayout(nlp)
    
    # Process document and apply NLP pipeline
    doc = layout(Path(file_path))
    doc = nlp(doc.text)
    
    return {
        "text": doc.text,
        "layout": doc._.layout,
        "tables": [table._.data for table in doc._.tables],
        "entities": [(ent.text, ent.label_) for ent in doc.ents]
    }