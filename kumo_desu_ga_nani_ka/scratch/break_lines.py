import os

translated_dir = r"D:\workspace\translate\translated\vol_11"

for filename in os.listdir(translated_dir):
    if not filename.endswith(".md"):
        continue
    
    file_path = os.path.join(translated_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)
        
        # Check if we should insert a blank line after this line
        if i < len(lines) - 1:
            next_line = lines[i+1]
            
            # If current line and next line are both table rows, do NOT insert blank line
            is_curr_table = line.strip().startswith("|") and line.strip().endswith("|")
            is_next_table = next_line.strip().startswith("|") and next_line.strip().endswith("|")
            
            if is_curr_table and is_next_table:
                # Keep them together
                pass
            else:
                # If neither is empty, we insert a blank line
                if line.strip() != "" and next_line.strip() != "":
                    new_lines.append("")
        
        i += 1
        
    # Write back
    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(new_lines) + "\n")
        
print("Done formatting all files!")
