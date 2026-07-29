import pypdf
import os

reader = pypdf.PdfReader("source/vol_13/So I’m a Spider, So What_, Vol. 13.pdf")

chapters = [
    ("00_insert_copyright.txt", 0, 9),
    ("01_ch1_exterminating_monsters_for_a_living.txt", 10, 33),
    ("02_ch2_dealing_with_the_hero_for_a_living.txt", 34, 43),
    ("03_v1_working_for_the_mastermind.txt", 44, 57),
    ("04_conversation_the_elfs_tragedy.txt", 58, 64),
    ("05_ch3_overthrowing_a_kingdom_for_a_living.txt", 65, 74),
    ("06_ch4_negotiating_with_bigwigs_for_a_living.txt", 75, 82),
    ("07_special_the_path_of_the_oni.txt", 83, 99),
    ("08_ch5_doing_traffic_control_and_executions_for_a_living.txt", 100, 119),
    ("09_interlude_the_pontiff_and_the_administrator_share_a_drink.txt", 120, 135),
    ("10_ch6_watching_over_the_heros_party_for_a_living.txt", 136, 151),
    ("11_interlude_the_heros_sister_the_evil_gods_puppet_and_the_hunting_dog.txt", 152, 157),
    ("12_ch7_summing_things_up_and_planning_what_comes_next_for_a_living.txt", 158, 176),
    ("13_special_a_grandma_admires_her_progenys_hard_work.txt", 177, 178),
    ("14_ch8_picking_fight_with_the_system_for_a_living.txt", 179, 216),
    ("15_interlude_question_marks.txt", 217, 217),
    ("16_final_destroying_the_elves_for_a_living.txt", 218, 219),
    ("17_afterword.txt", 220, 223),
    ("18_yen_newsletter.txt", 224, 224),
]

output_dir = "source/vol_13"
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
