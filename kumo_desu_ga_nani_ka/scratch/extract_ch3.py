import pypdf

reader = pypdf.PdfReader("source/vol_9/So I’m a Spider, So What_, Vol. 9.pdf")

# We want pages 68 to 78 inclusive (which is range(68, 79))
ch3_text = []
for i in range(68, 79):
    text = reader.pages[i].extract_text()
    ch3_text.append(f"--- PAGE {i} (PDF index) ---\n" + text)

output_path = "source/vol_9/03_arrival_of_the_hooligan.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n\n".join(ch3_text))

print(f"Extraction complete. Written to {output_path}")
