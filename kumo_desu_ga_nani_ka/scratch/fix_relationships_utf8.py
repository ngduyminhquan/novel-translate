import os

file_path = 'd:/workspace/translate/context/relationships.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace from '### QH-028: Ronandt ↔ Tôi (Nhện)' to '### QH-031: Hugo ↔ Sue (bị tẩy não)'
start_tag = '### QH-028: Ronandt ↔ Tôi (Nhện)'
end_tag = '### QH-031: Hugo ↔ Sue (bị tẩy não)'

start_idx = content.find(start_tag)
end_idx = content.find(end_tag)

print("Start index:", start_idx)
print("End index:", end_idx)

if start_idx != -1 and end_idx != -1:
    replacement = (
        "### QH-028: Ronandt ↔ Tôi (Nhện)\n\n"
        "| Thuộc tính | Chi tiết |\n"
        "|------------|----------|\n"
        "| **Quan hệ** | Người chứng kiến và Quái vật huyền thoại (Ronandt tôn xưng Nhện là \"sư phụ\") |\n"
        "| **Ronandt gọi Nhện** | Vị sư phụ đó (That master) / Người đó / Thực thể đó |\n"
        "| **Nhện gọi Ronandt** | Ông già loài người (sau này gặp trực tiếp) |\n"
        "| **Ronandt xưng** | Ta |\n"
        "| **Nhện xưng** | Ta / Tôi |\n"
        "| **Trạng thái** | 16 năm trước (theo trục thời gian loài người), Ronandt chạm trán Nhện nhỏ trong Mê cung Lớn Elroe và suýt chết. Nhìn thấy ma pháp tối thượng của Nhện, Ronandt hoàn toàn bị thuyết phục và tôn sùng cô như một vị thần ma pháp, từ bỏ mọi kiêu ngạo của bản thân để học hỏi từ xa. |\n"
        "| **Ghi chú** | Cuộc gặp gỡ này đã thay đổi hoàn toàn cuộc đời và tư duy ma pháp của Ronandt. |\n\n"
        "---\n\n"
        "### QH-029: Potimas ↔ Cô Oka (Filimõs)\n\n"
        "| Thuộc tính | Chi tiết |\n"
        "|------------|----------|\n"
        "| **Quan hệ** | Con gái và Cha ruột (mâu thuẫn, lợi dụng, đề phòng sinh tử) |\n"
        "| **Cô Oka gọi Potimas** | Cha / Ngài Potimas (khi xa cách) |\n"
        "| **Potimas gọi Cô Oka** | Con / Filimõs |\n"
        "| **Cô Oka xưng** | Con / Tôi |\n"
        "| **Potimas xưng** | Ta |\n"
        "| **Trạng thái** | Xa cách, thực dụng và căng thẳng ngầm. Cô Oka tuy là con gái Potimas nhưng hiểu rất rõ bản chất tàn nhẫn của ông ta. Cô biết rằng nếu mình xóa kỹ năng bằng [Xóa Kỹ Năng] (đồng nghĩa với việc dâng nộp sức mạnh cho các quản trị viên, kẻ thù của tộc Elf), Potimas sẽ sẵn sàng thanh trừng cô mà không hề biến sắc. Cô Oka vừa phải lợi dụng quyền lực của cha để bảo hộ các học sinh, vừa phải giữ lại các kỹ năng của mình để tự vệ và tránh bị thanh trừng, đồng thời bảo vệ các học sinh khỏi việc bị tộc Elf lợi dụng hay vứt bỏ. Trong Chương cuối Volume 7, sau khi White hóa thần, Potimas quyết tâm trả thù và đã ra lệnh mang Oka theo cùng lực lượng quân đội tộc Elf để dàn dựng cảnh các người tái sinh tự tàn sát lẫn nhau, một kế hoạch tàn độc mà hắn cho rằng sẽ rất thú vị và gây ra đau khổ tột cùng cho cả Oka lẫn White.<br><br>*Sự kiện Volume 13:* Việc cô Oka kích hoạt quyền hạn thống trị của `[Nhân Ái]` để cứu học sinh của mình đã vô tình tiêu thụ phần linh hồn ký sinh của Potimas bám trên cô, giúp cô thoát khỏi sự kiểm soát của hắn. |\n\n"
        "---\n\n"
        "### QH-030: Hugo ↔ Cylis\n\n"
        "| Thuộc tính | Chi tiết |\n"
        "|------------|----------|\n"
        "| **Quan hệ** | Đồng minh phản phản biến / Lợi dụng lẫn nhau |\n"
        "| **Hugo gọi Cylis** | Cylis / Các hạ |\n"
        "| **Cylis gọi Hugo** | Hugo |\n"
        "| **Hugo xưng** | Ta / Tôi |\n"
        "| **Cylis xưng** | Ta / Tôi |\n"
        "| **Trạng thái** | Đồng minh phản biến nhưng bị phản bội; Hugo lợi dụng tham vọng của Cylis rồi dùng [Ái Dục] tẩy não hủy hoại hoàn toàn tâm trí anh ta ngay khi đại sự thành. |\n\n"
        "---\n\n"
    )
    
    new_content = content[:start_idx] + replacement + content[end_idx:]
    with open(file_path, 'w', encoding='utf-8') as outf:
        outf.write(new_content)
    print("Relationships file successfully repaired using UTF-8!")
else:
    print("Could not find start or end tags.")
