import difflib
import os
from dotenv import load_dotenv
import google.generativeai as genai

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == "__main__":
    # Load your Gemini API key from .env
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env file.")
        exit(1)
    genai.configure(api_key=api_key)
    
    # Prompt user for file names
    file1 = input("Enter the first filename (e.g., doc1.txt): ")
    file2 = input("Enter the second filename (e.g., doc2.txt): ")

    try:
        lines1 = read_file(file1)
        lines2 = read_file(file2)
    except FileNotFoundError as e:
        print(f"File error: {e}")
        exit(1)

    diff = list(difflib.unified_diff(
        lines1, lines2, fromfile=file1, tofile=file2, lineterm=''
    ))

    print("\n--- Differences (raw diff) ---")
    if diff:
        for line in diff:
            print(line)
    else:
        print("No differences found.")

    # Only analyze if differences exist
    changed_lines = [line for line in diff if line.startswith('+') or line.startswith('-')]
    diff_text = '\n'.join(changed_lines)
    
    if diff_text.strip():
        prompt = (
            "The following is a diff (using unified diff notation) between two document versions. "
            "Summarize in clear plain English what changed (key additions, removals, rewrites). "
            "Avoid vague phrases—be specific:\n"
            f"{diff_text}\nSummary:"
        )
        # Use Gemini 2.5 Pro model (update if needed for your account)
        model_name = "gemini-2.5-pro"
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            # Gemini SDK may return .text, .result, or .candidates; handle accordingly
            summary = getattr(response, "text", None) or getattr(response, "result", None) or "No summary generated."
            print("\n--- Gemini Summary of Differences ---")
            print(summary.strip())
        except Exception as e:
            print(f"\nError when calling Gemini: {e}")
    else:
        print("\nNo changes to summarize.")
