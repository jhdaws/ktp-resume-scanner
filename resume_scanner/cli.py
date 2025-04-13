import argparse
import os
import json
from pathlib import Path
from .parser import extract_text
from .gpt_integration import GPTAnalyzer
from .analyzer import analyze_text
from dotenv import load_dotenv

ROLES = {
    "1": "Software Engineer",
    "2": "Product Manager",
    "3": "Data Scientist",
    "4": "UX Designer",
    "5": "DevOps Engineer",
    "6": "General"
}

def get_user_input(prompt: str, required: bool = True) -> str:
    while True:
        user_input = input(prompt).strip()
        if not required or user_input:
            return user_input
        print("This field is required. Please try again.")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Resume Scanner CLI")
    parser.add_argument("file", type=str, help="Path to the resume file (PDF or DOCX)")
    parser.add_argument("--api-key", type=str, help="OpenAI API key (or set OPENAI_API_KEY env var)")
    args = parser.parse_args()

    # Get API key
    load_dotenv()
    api_key = args.api_key or os.environ["OPENAI_API_KEY"]
    if not api_key:
        print("Error: OpenAI API key is required. Set it via --api-key or OPENAI_API_KEY environment variable.")
        return

    # Extract text from resume
    try:
        resume_text = extract_text(args.file)
        print(f"\nSuccessfully extracted text from {args.file}")
    except Exception as e:
        print(f"Error extracting text: {e}")
        return

    want_analysis = get_user_input("\nWould you like a text analysis of your resume? (y/n): ").lower() == 'y'
    if not want_analysis:
        print("\nNo analysis requested. E")
        return
    
    print("\nAnalyzing resume...")
    basic_analysis = analyze_text(resume_text)

    print("\n=== Basic Text Analysis Results ===")
    for metric, (score, interpretation) in basic_analysis.items():
        if metric == "word_count":
            print(f"\nWord Count: {score} ({interpretation})")
        elif metric == "sentence_count":
            print(f"Sentence Count: {score} ({interpretation})")
        elif metric == "avg_sentence_length":
            print(f"Avg Sentence Length: {score:.1f} words ({interpretation})")
        elif metric == "difficult_words":
            percentage = (score / basic_analysis["word_count"][0]) * 100
            print(f"Difficult Words: {score} ({percentage:.1f}% of total, {interpretation})")
        elif isinstance(score, float):
            print(f"{metric.replace('_', ' ').title()}: {score:.1f} ({interpretation})")
        else:
            print(f"{metric.replace('_', ' ').title()}: {score} ({interpretation})")

    # Ask if user wants analysis
    want_analysis = get_user_input("\nWould you like AI analysis of your resume? (y/n): ").lower() == 'y'
    if not want_analysis:
        print("\nNo analysis requested. Exiting.")
        return

    # Get role selection
    print("\nSelect a role for analysis:")
    for num, role in ROLES.items():
        print(f"{num}. {role}")
    
    role_choice = get_user_input("Enter choice (1-6): ")
    selected_role = ROLES.get(role_choice, "General")

    # Get optional job description
    job_description = None
    if get_user_input("\nWould you like to provide a job description? (y/n): ").lower() == 'y':
        print("\nPaste job description (press Enter then Ctrl+D when done):")
        job_description = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            job_description.append(line)
        job_description = "\n".join(job_description)

    # Perform analysis
    print("\nAnalyzing resume...")
    analyzer = GPTAnalyzer(api_key)
    try:
        results = analyzer.analyze_resume(
            resume_text=resume_text,
            job_description=job_description,
            role=selected_role
        )
        
        print("\n=== ANALYSIS RESULTS ===")
        print(results["analysis"])
        
        # Save results
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        
        output_path = output_dir / f"{Path(args.file).stem}_analysis.txt"
        with open(output_path, "w") as f:
            f.write(results["analysis"])
        
        print(f"\nAnalysis saved to {output_path}")
    except Exception as e:
        print(f"Error during analysis: {e}")

if __name__ == "__main__":
    main()