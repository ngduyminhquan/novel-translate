import pypdf
import os

reader = pypdf.PdfReader("source/vol_11/So I’m a Spider, So What_, Vol. 11.pdf")

chapters = [
    ("00_insert_copyright.txt", 0, 9),
    ("01_j1_julius_age_11_beginnings.txt", 10, 20),
    ("02_sophias_diary_1.txt", 21, 21),
    ("03_j2_julius_age_12_first_expedition.txt", 22, 38),
    ("04_special_chapter_the_empire_veteran_and_the_commander.txt", 39, 41),
    ("05_sophias_diary_2.txt", 42, 42),
    ("06_j3_julius_age_12_surprise_attack.txt", 43, 55),
    ("07_special_chapter_the_saint_and_the_empire_veteran.txt", 56, 64),
    ("08_sophias_diary_3.txt", 65, 65),
    ("09_j4_julius_age_12_showdown.txt", 66, 80),
    ("10_special_chapter_the_former_thief_and_the_adventurer.txt", 81, 83),
    ("11_sophias_diary_4.txt", 84, 85),
    ("12_j5_julius_age_13_machinations.txt", 86, 101),
    ("13_special_chapter_the_empire_veterans_final_hours.txt", 102, 116),
    ("14_interlude_the_elf_despises_wasting_time.txt", 117, 119),
    ("15_sophias_diary_5.txt", 120, 121),
    ("16_j6_julius_age_13_life_and_death.txt", 122, 134),
    ("17_interlude_the_pontiff_and_the_reincarnation_spy.txt", 135, 137),
    ("18_sophias_diary_6.txt", 138, 138),
    ("19_j7_julius_age_13_progress.txt", 139, 145),
    ("20_sophias_diary_7.txt", 146, 147),
    ("21_j8_julius_age_14_youth.txt", 148, 157),
    ("22_sophias_diary_8.txt", 158, 159),
    ("23_j9_julius_age_15_partner.txt", 160, 177),
    ("24_sophias_diary_9.txt", 178, 178),
    ("25_j10_julius_age_16_friends.txt", 179, 192),
    ("26_interlude_an_unopposable_force.txt", 193, 204),
    ("27_sophias_diary_10.txt", 205, 206),
    ("28_j11_julius_age_17_accomplishments.txt", 207, 216),
    ("29_j12_julius_age_21_family.txt", 217, 233),
    ("30_timeline.txt", 234, 234),
    ("31_afterword.txt", 235, 237),
    ("32_yen_newsletter.txt", 238, 238),
]

output_dir = "source/vol_11"
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
