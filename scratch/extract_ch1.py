import pypdf

reader = pypdf.PdfReader("source/vol_9/So I’m a Spider, So What_, Vol. 9.pdf")
print("Page 11 snippet:")
print(reader.pages[11].extract_text()[:400])
print("\n" + "="*40 + "\nPage 24 snippet:")
print(reader.pages[24].extract_text()[:400])

# Let's extract pages 11 to 23 inclusive (meaning up to page 23, since page 24 starts the next chapter)
ch1_text = []
for i in range(11, 24):
    text = reader.pages[i].extract_text()
    ch1_text.append(f"--- PAGE {i} (PDF index) ---\n" + text)

with open("source/vol_9/01_arrival_in_the_demon_realm.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(ch1_text))
print("Extraction complete. Written to source/vol_9/01_arrival_in_the_demon_realm.txt")
