import os

file_path = r"d:\workspace\translate\context\relationships.md"

with open(file_path, "r", encoding="utf-8", errors="surrogateescape") as f:
    content = f.read()

target = "White phát hiện thanh Anh Hùng Kiếm vẫn kết thúc ở thắt lưng của Yamada do Hyrince chuyển giao (dưới danh nghĩa di nguyện của Julius) và cảm thấy cực kỳ bực bội trước hành động thiếu trách nhiệm của ông ta khi trao vũ khí chống thần cực kỳ nguy hiểm này cho người khác. |"
replacement = "White phát hiện thanh Anh Hùng Kiếm vẫn kết thúc ở thắt lưng của Yamada do Hyrince chuyển giao (dưới danh nghĩa di nguyện của Julius) và cảm thấy cực kỳ bực bội trước hành động thiếu trách nhiệm của ông ta khi trao vũ khí chống thần cực kỳ nguy hiểm này cho người khác.<br><br>*Sự kiện Volume 15:* Trong Chương 5, sau khi Nhiệm vụ Thế giới kích hoạt, Güliedistodiez chủ động tấn công cô và lôi cô vào kết giới dị không gian do mình thiết lập để chiến đấu nhằm bảo vệ ý nguyện bảo hộ loài người của Nữ thần Sariel. Cả hai bắt đầu trận chiến bào mòn năng lượng kéo dài. Trong Vĩ thanh & Mở đầu (Chương 19), cả hai cùng lắng nghe bài phát biểu của Ariel và Giáo hoàng Dustin qua Thần ngôn. Hắc thừa nhận không thể để thua vì lý tưởng bảo vệ nguyện ước của Sariel và gánh vác hy vọng của nhân loại. White bày tỏ sự tôn trọng và khẳng định sẽ chiến đấu hết mình để giành chiến thắng. Trận chiến giữa họ tiếp tục tiếp diễn. |"

if target in content:
    new_content = content.replace(target, replacement)
    with open(file_path, "w", encoding="utf-8", errors="surrogateescape") as f:
        f.write(new_content)
    print("SUCCESS: Successfully updated relationships.md preserving binary bytes.")
else:
    print("ERROR: Target content not found in relationships.md")
