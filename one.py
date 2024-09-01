import os
import glob

def combine_transcripts():
    # Get a list of all transcript files in the current directory 
    files = glob.glob("*.txt")
    
    # Combine all files into a single transcript
    with open(f"z.txt", "w", encoding="utf-8") as combined_file:
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    combined_file.write(line)


combine_transcripts()