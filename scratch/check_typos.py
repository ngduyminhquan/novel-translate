import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

context_dirs = [r"d:\workspace\novel-translate\context", r"d:\workspace\novel-translate\translated\vol_13"]
files = []
for d in context_dirs:
    files.extend([os.path.join(d, f) for f in os.listdir(d) if f.endswith(".md")])

# Vietnamese vowels with tone marks to check for duplicate accents/vowels
pattern = re.compile(r'([a-zA-Zàáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ])\1{2,}', re.IGNORECASE)
# This finds 3+ repeating letters. We should also check for duplicate tone marks like ấấ, ếế, ắắ, etc.
accent_pattern = re.compile(r'[àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵ]{2,}', re.IGNORECASE)

for file_path in files:
    print(f"Checking {os.path.basename(file_path)}...")
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for idx, line in enumerate(lines, 1):
            # Find duplicate accents that shouldn't be repeating
            for match in accent_pattern.finditer(line):
                # Note: some like "yêu", "oai", "oao" are normal, but duplicate same accented char like "ấấ" or "ầầ" is a typo
                word = match.group()
                # If there are repeating identical accented characters (e.g. ấấ, ếế)
                for char in set(word):
                    if word.count(char) > 1:
                        print(f"Line {idx}: potential typo '{word}' in: {line.strip()}")
            # Find 3+ repeating characters
            for match in pattern.finditer(line):
                print(f"Line {idx}: repeating chars '{match.group()}' in: {line.strip()}")
