import os
import re

glossary_path = "context/glossary.md"
characters_path = "context/characters.md"
relationships_path = "context/relationships.md"
translated_dir = "translated/vol_16"

print("--- Running consistency checks ---")

# 1. Read glossary terms
terms = []
with open(glossary_path, "r", encoding="utf-8") as f:
    for line in f:
        if "|" in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 4 and parts[1] != "#" and parts[1] != "---" and parts[1] != "":
                eng = parts[2]
                vie = parts[3]
                terms.append((eng, vie))

print(f"Loaded {len(terms)} terms from glossary.")

# 2. Check for common formatting issues in context files
for path in [glossary_path, characters_path, relationships_path]:
    if not os.path.exists(path):
        continue
    print(f"Checking formatting for {path}...")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
        # Check for double spaces
        double_spaces = len(re.findall(r"[^\s]  [^\s]", content))
        if double_spaces > 0:
            print(f"  [Warning] Found {double_spaces} double spaces (excluding indentation).")
            
        # Check for spaces before punctuation (e.g., " ,", " .")
        punc_spaces = len(re.findall(r"\s+[,\.\?!]", content))
        # Note: markdown tables might trigger space before | which is fine, but check comma, period, question, exclamation.
        punc_comma = len(re.findall(r"\s+,", content))
        punc_period = len(re.findall(r"\s+\.", content))
        punc_excl = len(re.findall(r"\s+!", content))
        punc_ques = len(re.findall(r"\s+\?", content))
        if punc_comma or punc_period or punc_excl or punc_ques:
            print(f"  [Warning] Spaces before punctuation: commas={punc_comma}, periods={punc_period}, exclamation={punc_excl}, question={punc_ques}")

# 3. Scan translated files for any non-Vietnamese characters or typical untranslated placeholders
print("Checking translated files for placeholders or consistency...")
for root, dirs, files in os.walk(translated_dir):
    for file in files:
        if not file.endswith(".md"):
            continue
        file_path = os.path.join(root, file)
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                # Check for "Goldenagato" or "mp4directs" or similar watermark remains
                if "mp4directs" in line or "Goldenagato" in line:
                    print(f"  [Error] Watermark in {file}:{idx+1}: {line.strip()}")
                
                # Check for common untranslated terms
                # E.g. using "Feirune" instead of "Fei" or similar
                if "Feirune" in line:
                    print(f"  [Warning] Feirune found in {file}:{idx+1}: {line.strip()}")
                if "Wakaba Hiiro" in line and "Wakaba" not in glossary_path: # Hiiro Wakaba is ok depending on context
                    pass

print("Checks completed.")
