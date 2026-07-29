import pypdf
import os

reader = pypdf.PdfReader("source/vol_9/So I’m a Spider, So What_, Vol. 9.pdf")

chapters = [
    ("00_insert_copyright.txt", 0, 8),
    ("evil_gods_dont_smile.txt", 9, 10),
    ("01_arrival_in_the_demon_realm.txt", 11, 23),
    ("interlude_the_veteran_demons_secret_feud.txt", 24, 32),
    ("x1_the_former_sword_king_reigar.txt", 33, 47),
    ("02_arrival_at_the_demon_lords_castle.txt", 48, 59),
    ("interlude_the_old_butlers_frightful_experience.txt", 60, 67),
    ("03_arrival_of_the_hooligan.txt", 68, 78),
    ("interlude_the_demon_dukes_distress.txt", 79, 85),
    ("x2_administrator_gyuriedistodiez.txt", 86, 97),
    ("04_arrival_in_heaven.txt", 98, 111),
    ("interlude_the_vampire_princesss_midnight_lesson.txt", 112, 122),
    ("05_arrival_at_the_great_elroe_labyrinth.txt", 123, 133),
    ("x3_ice_dragon_nia.txt", 134, 140),
    ("06_arrival_at_mr_onis_place.txt", 141, 170),
    ("o_wrath.txt", 171, 199),
    ("07_arrival_in_japan.txt", 200, 206),
    ("evil_gods_dont_laugh.txt", 207, 224),
    ("evil_elves_do_sneer.txt", 225, 227),
    ("afterword.txt", 228, 230),
    ("yen_newsletter.txt", 231, 231),
]

output_dir = "source/vol_9"
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
