import pypdf

reader = pypdf.PdfReader("source/vol_9/So I’m a Spider, So What_, Vol. 9.pdf")
print("Page 48 snippet:")
print(reader.pages[48].extract_text()[:400])
print("\n" + "="*40 + "\nPage 59 snippet:")
print(reader.pages[59].extract_text()[-400:])

# Let's extract pages 48 to 59 inclusive
ch2_text = []
for i in range(48, 60):
    text = reader.pages[i].extract_text()
    ch2_text.append(f"--- PAGE {i} (PDF index) ---\n" + text)

output_path = "source/vol_9/02_arrival_at_the_demon_lords_castle.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(ch2_text))
print(f"Extraction complete. Written to {output_path}")
