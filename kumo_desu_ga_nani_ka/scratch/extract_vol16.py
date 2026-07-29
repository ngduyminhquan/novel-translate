import pypdf
import os

reader = pypdf.PdfReader("source/vol_16/So I’m a Spider, So What_, Vol. 16.pdf")

chapters = [
    ("00_insert_copyright.txt", 0, 15),
    ("01_ariel_1.txt", 16, 26),
    ("02_white_1.txt", 27, 44),
    ("03_shun_1.txt", 45, 68),
    ("04_balto.txt", 69, 86),
    ("05_sophia.txt", 87, 98),
    ("06_kusama.txt", 99, 103),
    ("07_phelmina.txt", 104, 109),
    ("08_merazophis.txt", 110, 113),
    ("09_kunihiko.txt", 114, 119),
    ("10_asaka.txt", 120, 124),
    ("11_wrath.txt", 125, 135),
    ("12_filimes.txt", 136, 146),
    ("13_shun_2.txt", 147, 152),
    ("14_ariel_2.txt", 153, 166),
    ("15_dustin.txt", 167, 180),
    ("16_hyrince.txt", 181, 192),
    ("17_ronandt.txt", 193, 200),
    ("18_fei.txt", 201, 216),
    ("19_shun_3.txt", 217, 227),
    ("20_dark_dragon_reise.txt", 228, 235),
    ("21_ariel_3.txt", 236, 240),
    ("22_white_2.txt", 241, 247),
    ("23_everyones_ever_after.txt", 248, 253),
    ("24_epilogue.txt", 254, 257),
    ("25_afterword.txt", 258, 261),
    ("26_yen_newsletter.txt", 262, 262),
]

output_dir = "source/vol_16"
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
