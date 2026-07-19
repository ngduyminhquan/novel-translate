import os

source_dir = "source/vol_13"
files = sorted([f for f in os.listdir(source_dir) if f.endswith(".txt")])

print(f"{'Filename':<75} | {'Lines':<6} | {'Words':<8} | {'Chars':<8}")
print("-" * 110)
total_words = 0
for file in files:
    path = os.path.join(source_dir, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        lines = len(content.splitlines())
        words = len(content.split())
        chars = len(content)
        total_words += words
        print(f"{file:<75} | {lines:<6} | {words:<8} | {chars:<8}")
print("-" * 110)
print(f"{'Total':<75} | {'':<6} | {total_words:<8} |")
