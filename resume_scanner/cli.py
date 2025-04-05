import argparse
import os
from .parser import extract_text
from .analyzer import analyze_text

def main():
    parser = argparse.ArgumentParser(description="Resume Scanner CLI")
    parser.add_argument("file", type=str, help="Path to the resume file (PDF or DOCX)")
    args = parser.parse_args()

    # Extract text from the file
    text = extract_text(args.file)

    data_dir = "data"

    # Ensure the 'data' directory exists
    os.makedirs(data_dir, exist_ok=True)

    # Define the output file path
    output_filename = os.path.basename(args.file) + ".txt"
    output_file_path = os.path.join(data_dir, output_filename)

    # Save the extracted text to the output file
    with open(output_file_path, "w") as f:
        f.write(text)

    print(f"Extracted text saved to {output_file_path}")

    analysis_results = analyze_text(text)
    print("Analysis Results:")
    for metric, value in analysis_results.items():
        print(f"{metric}: {value}")

if __name__ == "__main__":
    main()
