import textstat
from typing import Dict, Tuple

def analyze_text(text: str) -> Dict[str, Tuple[float, str]]:
    """
    Analyze text with multiple readability metrics and provide interpretations.
    
    Returns:
        Dict where keys are metric names and values are tuples of (score, interpretation)
    """
    if not text.strip():
        return {"error": "Empty text provided for analysis"}
    
    results = {}
    
    # Basic statistics
    results["word_count"] = (len(text.split()), "Total number of words in the text")
    results["sentence_count"] = (textstat.sentence_count(text), "Total number of sentences")
    results["avg_sentence_length"] = (
        textstat.avg_sentence_length(text),
        "Average number of words per sentence (optimal: 15-20)"
    )
    
    # Readability scores
    results["flesch_reading_ease"] = (
        textstat.flesch_reading_ease(text),
        _interpret_flesch(textstat.flesch_reading_ease(text))
    )
    
    results["flesch_kincaid_grade"] = (
        textstat.flesch_kincaid_grade(text),
        f"U.S. school grade level needed to understand (optimal for resumes: 8-10)"
    )
    
    results["smog_index"] = (
        textstat.smog_index(text),
        f"Years of education needed to understand (optimal for resumes: 8-10)"
    )
    
    results["coleman_liau_index"] = (
        textstat.coleman_liau_index(text),
        "U.S. school grade level needed to understand"
    )
    
    results["automated_readability_index"] = (
        textstat.automated_readability_index(text),
        "Approximate age needed to understand (optimal: 12-15)"
    )
    
    # Complexity metrics
    results["difficult_words"] = (
        textstat.difficult_words(text),
        f"Number of complex words (optimal for resumes: <10% of total words)"
    )
    
    results["dale_chall_readability_score"] = (
        textstat.dale_chall_readability_score(text),
        _interpret_dale_chall(textstat.dale_chall_readability_score(text))
    )
    
    results["linsear_write_formula"] = (
        textstat.linsear_write_formula(text),
        "Readability score for English writing samples"
    )
    
    results["gunning_fog"] = (
        textstat.gunning_fog(text),
        "Years of formal education needed to understand (optimal: 8-10)"
    )
    
    # Text composition
    char_count = len(text.replace(" ", ""))
    syllable_count = textstat.syllable_count(text)
    results["avg_syllables_per_word"] = (
        syllable_count / results["word_count"][0] if results["word_count"][0] > 0 else 0,
        "Average syllables per word (optimal: 1.4-1.6)"
    )
    
    results["avg_letters_per_word"] = (
        char_count / results["word_count"][0] if results["word_count"][0] > 0 else 0,
        "Average letters per word (optimal: 4-5)"
    )
    
    return results

def _interpret_flesch(score: float) -> str:
    """Interpret Flesch Reading Ease score"""
    if score >= 90:
        return "Very easy to read (5th grade level)"
    elif score >= 80:
        return "Easy to read (6th grade level)"
    elif score >= 70:
        return "Fairly easy to read (7th grade level)"
    elif score >= 60:
        return "Plain English (8th-9th grade level) - Ideal for resumes"
    elif score >= 50:
        return "Fairly difficult to read (10th-12th grade level)"
    elif score >= 30:
        return "Difficult to read (college level)"
    else:
        return "Very difficult to read (university graduate level)"

def _interpret_dale_chall(score: float) -> str:
    """Interpret Dale-Chall readability score"""
    if score <= 4.9:
        return "Easily understood by 4th-grade students"
    elif score <= 5.9:
        return "Easily understood by 5th-6th graders - Good for resumes"
    elif score <= 6.9:
        return "Easily understood by 7th-8th graders"
    elif score <= 7.9:
        return "Average difficulty (9th-10th grade)"
    elif score <= 8.9:
        return "Difficult (11th-12th grade)"
