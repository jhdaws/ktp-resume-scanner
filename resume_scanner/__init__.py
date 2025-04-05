"""
Resume Scanner Package

This package provides tools to parse and analyze resumes using spaCy, spaCy-Layout, and textstat.
"""

from .parser import extract_text
from .analyzer import analyze_text

__all__ = ['extract_text', 'analyze_text']
