import pypdf

reader = pypdf.PdfReader("source/vol_9/So I’m a Spider, So What_, Vol. 9.pdf")
print("Page 33 snippet:")
print(reader.pages[33].extract_text()[:400])
print("\n" + "="*40 + "\nPage 47 snippet:")
print(reader.pages[47].extract_text()[-400:])

# Let's extract pages 33 to 47 inclusive
x1_text = []
for i in range(33, 48):
    text = reader.pages[i].extract_text()
    x1_text.append(f"--- PAGE {i} (PDF index) ---\n" + text)

output_path = "source/vol_9/x1_the_former_sword_king_reigar.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(x1_text))
print(f"Extraction complete. Written to {output_path}")
