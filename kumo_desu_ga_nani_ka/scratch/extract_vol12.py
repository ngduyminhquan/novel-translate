import pypdf
import os

reader = pypdf.PdfReader("source/vol_12/So I’m a Spider, So What_, Vol. 12.pdf")

chapters = [
    ("00_insert_copyright.txt", 0, 14),
    ("01_prologue.txt", 15, 16),
    ("02_white_1.txt", 17, 22),
    ("03_sanatoria.txt", 23, 32),
    ("04_huey.txt", 33, 42),
    ("05_ronandt.txt", 43, 52),
    ("06_kunihiko.txt", 53, 66),
    ("07_asaka.txt", 67, 80),
    ("08_aurel.txt", 81, 89),
    ("09_merazophis.txt", 90, 97),
    ("10_phelmina.txt", 98, 111),
    ("11_wald.txt", 112, 119),
    ("12_sophia.txt", 120, 125),
    ("13_wrath.txt", 126, 130),
    ("14_hawkin.txt", 131, 142),
    ("15_agner.txt", 143, 155),
    ("16_jeskan.txt", 156, 175),
    ("17_bloe.txt", 176, 194),
    ("18_balto.txt", 195, 201),
    ("19_yaana.txt", 202, 222),
    ("20_julius.txt", 223, 240),
    ("21_white_2.txt", 241, 245),
    ("22_epilogue.txt", 246, 246),
    ("23_afterword.txt", 247, 251),
    ("24_yen_newsletter.txt", 252, 252),
]

output_dir = "source/vol_12"
os.makedirs(output_dir, exist_ok=True)

for filename, start, end in chapters:
    print(f"Extracting {filename} (Pages {start} to {end})...")
    ch_text = []
    for i in range(start, end + 1):
        text = reader.pages[i].extract_text()
        ch_text.append(f"--- PAGE {i} (PDF index) ---\n" + text)
    
    output_path = os.path.join(output_dir, filename)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(ch_text))
    print(f"  Saved to {output_path}")

print("All extractions completed successfully!")
