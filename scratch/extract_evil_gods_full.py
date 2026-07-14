import pypdf

reader = pypdf.PdfReader("source/vol_9/So I’m a Spider, So What_, Vol. 9.pdf")
print("PAGE 9:")
print(reader.pages[9].extract_text())
print("\n" + "="*80 + "\nPAGE 10:")
print(reader.pages[10].extract_text())
