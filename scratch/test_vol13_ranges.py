import pypdf

reader = pypdf.PdfReader("source/vol_13/So I’m a Spider, So What_, Vol. 13.pdf")

chapters = [
    ("00_insert_copyright", 0, 9),
    ("01_ch1_exterminating_monsters_for_a_living", 10, 33),
    ("02_ch2_dealing_with_the_hero_for_a_living", 34, 43),
    ("03_v1_working_for_the_mastermind", 44, 57),
    ("04_conversation_the_elfs_tragedy", 58, 64),
    ("05_ch3_overthrowing_a_kingdom_for_a_living", 65, 74),
    ("06_ch4_negotiating_with_bigwigs_for_a_living", 75, 82),
    ("07_special_the_path_of_the_oni", 83, 99),
    ("08_ch5_doing_traffic_control_and_executions_for_a_living", 100, 119),
    ("09_interlude_the_pontiff_and_the_administrator_share_a_drink", 120, 135),
    ("10_ch6_watching_over_the_heros_party_for_a_living", 136, 151),
    ("11_interlude_the_heros_sister_the_evil_gods_puppet_and_the_hunting_dog", 152, 157),
    ("12_ch7_summing_things_up_and_planning_what_comes_next_for_a_living", 158, 176),
    ("13_special_a_grandma_admires_her_progenys_hard_work", 177, 178),
    ("14_ch8_picking_fight_with_the_system_for_a_living", 179, 216),
    ("15_interlude_question_marks", 217, 217),
    ("16_final_destroying_the_elves_for_a_living", 218, 219),
    ("17_afterword", 220, 223),
    ("18_yen_newsletter", 224, 224),
]

for name, start, end in chapters:
    print(f"=== {name} ({start} -> {end}) ===")
    # Print the first line of the start page
    start_text = reader.pages[start].extract_text().strip()
    first_lines = [line.strip() for line in start_text.split("\n") if line.strip()]
    if first_lines:
        print("  Start:", first_lines[:3])
    else:
        print("  Start: [Empty Page or Image]")
        
    # Print the last line of the end page
    end_text = reader.pages[end].extract_text().strip()
    last_lines = [line.strip() for line in end_text.split("\n") if line.strip()]
    if last_lines:
        print("  End:  ", last_lines[-3:])
    else:
        print("  End:   [Empty Page or Image]")
    print()
