A smart Python tool that compares two document versions, highlights changes, and uses Google Gemini AI for a natural-language summary.

Features
Document Diff: Compares two text files (contracts, essays, code, etc.) and shows all line-by-line changes.

AI Summary: Uses Gemini Pro to summarize additions, deletions, and rewrites in clear English.

Easy CLI: Simple prompts and readable output.

Usage
Clone the repo and set up a Python virtual environment.

Install dependencies:

text
pip install google-generativeai python-dotenv
Add your Gemini API key to a .env file:

text
GEMINI_API_KEY=your_api_key_here
Place your two text files (e.g., doc1.txt, doc2.txt) in the folder.

Run:

text
python main.py
Enter file names when prompted and see both the diff and AI summary.

Example Output
text
--- Differences (raw diff) ---
- This is the original document.
+ This is the updated document.
+ Added a new section.

--- Gemini Summary of Differences ---
- Updated opening sentence for clarity.
- Added a new section at the end.
Project Context
Built during my 2025 Summer School Internship at IIT Jammu to showcase practical integration of LLMs for business, law, research, and personal productivity.
