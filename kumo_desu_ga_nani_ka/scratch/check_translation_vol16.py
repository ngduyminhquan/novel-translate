import os
import re
import sys

# Reconfigure stdout to use utf-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Path to the translated volume 16
translated_dir = r"d:\workspace\translate\translated\vol_16"

# Common English words that shouldn't appear in normal Vietnamese translation text
english_words = {
    " the ", " and ", " was ", " were ", " with ", " from ", " they ", " them ", 
    " she ", " his ", " her ", " you ", " would ", " could ", " should ", " their ", 
    " there ", " this ", " that ", " about ", " because ", " but ", " have ", " had "
}

# Vietnamese vowels/chars to exclude from simple double-letter matching if they are valid
valid_double_letters = {"oo", "ee", "gg"} # e.g. "xoong", "kính coong", "coong"

def is_line_metadata_or_link(line):
    line_strip = line.strip()
    if not line_strip:
        return True
    if line_strip.startswith("#") or line_strip.startswith("!") or line_strip.startswith("-") or line_strip.startswith("["):
        return True
    if "http" in line_strip or ".com" in line_strip or "@" in line_strip:
        return True
    if re.match(r'^ISBN\b', line_strip, re.IGNORECASE):
        return True
    if re.match(r'^LCCN\b', line_strip, re.IGNORECASE):
        return True
    return False

def clean_line_of_names_and_code(line):
    # Remove things inside brackets/parentheses
    line = re.sub(r'\(.*?\)', '', line)
    line = re.sub(r'\[.*?\]', '', line)
    # Remove English names we know
    names_to_remove = [
        "Ariel", "Sophia", "White", "Wrath", "Dustin", "Potimas", "Sariel", "Daztrudia", "Foduey", "Keren",
        "Jenny McKeon", "Tsukasa Kiryu", "Okina Baba", "Payton Campbell", "Wendy Chan", "Yen Press", "Yen On",
        "KADOKAWA", "TUTTLE-MORI", "AGENCY", "LCC", "PZ7", "DDC", "LCCN"
    ]
    for name in names_to_remove:
        line = re.sub(rf'\b{name}\b', '', line, flags=re.IGNORECASE)
    return line

results = []

for filename in sorted(os.listdir(translated_dir)):
    if not filename.endswith(".md") or filename == "README.md":
        continue
    
    filepath = os.path.join(translated_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines, 1):
        if is_line_metadata_or_link(line):
            continue
            
        cleaned = clean_line_of_names_and_code(line)
        
        # 1. Search for English words
        found_eng = []
        for eng in english_words:
            if eng in f" {cleaned.lower()} ":
                # Double check to avoid false positives (e.g. "she" inside "shelter")
                if re.search(r'\b' + eng.strip() + r'\b', cleaned.lower()):
                    found_eng.append(eng.strip())
                    
        # 2. Search for Telex double vowels/letters (like 'oo', 'ee', 'aa', 'dd' in inappropriate places)
        # Check for repeated letters that are common typos: aa, ee, oo, dd, uu, ii
        typos = []
        words = re.findall(r'\b[a-zA-ZđĐáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ]+\b', cleaned)
        for w in words:
            w_lower = w.lower()
            # Check for double letters
            for char in ['a', 'e', 'o', 'd', 'u', 'i', 's', 'r', 'x', 'j']:
                double = char + char
                if double in w_lower:
                    # Check if it's a known valid word or name
                    if w_lower not in ["coong", "xoong", "kính coong", "green", "agree", "queen", "wood", "good", "blood", "indeed", "see", "meet", "seek", "feel", "look", "book", "door", "foot", "free", "need", "week", "deep", "keep", "sleep", "seem", "feed", "seed", "beef", "beer", "deer", "jeep", "peer", "reel", "teen", "weep", "doom", "fool", "gloom", "loop", "mood", "pool", "roof", "tool", "zoom", "cool", "food", "foot", "hook", "hoop", "noon", "soon", "spoon", "wool", "add", "odd", "buddy", "daddy", "fiddler", "saddle", "sudden", "address", "goddess"]:
                        # Also check for double 'd' or double 's' or 'f' or 'r' which are typings
                        typos.append(f"Double '{char}' in word '{w}'")
            # Check for double accents or telex keys at the end of word or weird characters
            if re.search(r'[aeouiyđ][srxjf]{2,}', w_lower):
                typos.append(f"Possible Telex typo in word '{w}'")
        
        if found_eng or typos:
            results.append({
                "file": filename,
                "line_num": i,
                "line": line.strip(),
                "eng_words": found_eng,
                "typos": typos
            })

report_path = r"d:\workspace\translate\scratch\report_vol16.txt"
with open(report_path, "w", encoding="utf-8") as rf:
    rf.write(f"Total potential issues found: {len(results)}\n")
    for res in results:
        rf.write(f"File: {res['file']} | Line: {res['line_num']}\n")
        rf.write(f"  Line content: {res['line']}\n")
        if res['eng_words']:
            rf.write(f"  English words: {res['eng_words']}\n")
        if res['typos']:
            rf.write(f"  Potential typos: {res['typos']}\n")
        rf.write("-" * 40 + "\n")

print(f"Total potential issues found: {len(results)}")
print(f"Report written to: {report_path}")
