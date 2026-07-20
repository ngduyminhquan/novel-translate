import pypdf
import os

reader = pypdf.PdfReader("source/vol_15/So I’m a Spider, So What_, Vol. 15.pdf")

chapters = [
    ("00_insert_copyright.txt", 0, 15),
    ("01_ch1_a_new_dawn.txt", 16, 41),
    ("02_s1_waking_to_a_new_world.txt", 42, 47),
    ("03_ch2_the_world_is_terribly_cruel.txt", 48, 70),
    ("04_s2_the_value_of_a_life.txt", 71, 77),
    ("05_ch3_if_you_re_not_strong_enough_you_d_better_get_groveling.txt", 78, 100),
    ("06_s3_there_s_no_point_dwelling_on_past_misfortunes.txt", 101, 118),
    ("07_ch4_friends.txt", 119, 140),
    ("08_interlude_kunihiko_tagawa.txt", 141, 149),
    ("09_interlude_kengo_natsume.txt", 150, 153),
    ("10_interlude_yuri.txt", 154, 156),
    ("11_ch5_world_quest.txt", 157, 173),
    ("12_s4_change_of_scenery.txt", 174, 178),
    ("13_interlude_katia.txt", 179, 189),
    ("14_special_chapter_the_demon_lord_left_behind.txt", 190, 200),
    ("15_s5_an_ever_changing_world.txt", 201, 211),
    ("16_interlude_dustin.txt", 212, 216),
    ("17_special_chapter_the_demon_lord_makes_her_move.txt", 217, 220),
    ("18_interlude_speeches_from_each_side.txt", 221, 225),
    ("19_epilogue_and_prologue.txt", 226, 228),
    ("20_afterword.txt", 229, 234),
    ("21_yen_newsletter.txt", 235, 235),
]

output_dir = "source/vol_15"
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
