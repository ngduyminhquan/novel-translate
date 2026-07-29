import pypdf
import os

reader = pypdf.PdfReader("source/vol_14/So I’m a Spider, So What_, Vol. 14.pdf")

chapters = [
    ("00_insert_copyright.txt", 0, 6),
    ("01_l1_the_lord_who_had_no_name.txt", 7, 7),
    ("02_ch1_before_the_battle.txt", 8, 16),
    ("03_b1_reminisce_first_meeting.txt", 17, 23),
    ("04_interlude_potimass_beginning.txt", 24, 24),
    ("05_ch2_the_starting_bell_of_the_final_battle.txt", 25, 37),
    ("06_l2_the_lord_who_was_once_a_lab_rat.txt", 38, 42),
    ("07_interlude_potimass_experiments.txt", 43, 43),
    ("08_b2_ruminate_the_lost_angel_and_the_dragon.txt", 44, 51),
    ("09_ch3_showdown_annihilation.txt", 52, 60),
    ("10_l3_the_lord_who_had_friends.txt", 61, 64),
    ("11_b3_ruminate_blocked_by_the_demon_lord_of_the_business_world.txt", 65, 73),
    ("12_interlude_potimas_and_conjuring.txt", 74, 74),
    ("13_ch4_showdown_spider_vs_robot.txt", 75, 80),
    ("14_l4_the_lord_learns_a_lesson.txt", 81, 88),
    ("15_b4_ruminate_vampires.txt", 89, 100),
    ("16_interlude_potimas_and_vampires.txt", 101, 101),
    ("17_ch5_showdown_spider_vs_mega_robot.txt", 102, 120),
    ("18_l5_the_lord_looks_on.txt", 121, 127),
    ("19_b5_ruminate_ma_energy.txt", 128, 136),
    ("20_interlude_potimas_and_the_popularization_of_ma_energy.txt", 137, 138),
    ("21_ch6_showdown_chance_meeting.txt", 139, 153),
    ("22_interlude_the_old_man_and_the_witchy_little_ladies.txt", 154, 161),
    ("23_l6_the_lord_alone.txt", 162, 181),
    ("24_b6_ruminate_ragnarok.txt", 182, 191),
    ("25_interlude_the_presidents_decision.txt", 192, 196),
    ("26_interlude_potimas_and_the_gods_sacrifice.txt", 197, 198),
    ("27_ch7_showdown_countless_spider_eyes.txt", 199, 206),
    ("28_l7_the_lord_avenged.txt", 207, 222),
    ("29_b7_ruminate_thus_history_moves_again.txt", 223, 226),
    ("30_ch8_end_of_battle_she_who_walks_with_the_lord.txt", 227, 231),
    ("31_afterword.txt", 232, 233),
    ("32_copyright.txt", 234, 236),
    ("33_yen_newsletter.txt", 237, 237),
]

output_dir = "source/vol_14"
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
