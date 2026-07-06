# Skill: Dịch Tiểu Thuyết Anh → Việt

> **Mục đích**: Dịch tiểu thuyết từ tiếng Anh sang tiếng Việt với chất lượng văn học cao, đảm bảo nhất quán về văn phong, thuật ngữ, nhân vật và ngữ cảnh xuyên suốt toàn bộ tác phẩm.

---

## 1. Tổng Quan Quy Trình

```
┌─────────────────────────────────────────────────────────────┐
│                    QUY TRÌNH DỊCH TIỂU THUYẾT               │
├─────────────────────────────────────────────────────────────┤
│  PHASE 0: Khởi tạo dự án                                    │
│    ├── Đọc toàn bộ/lướt nhanh nguyên tác                    │
│    ├── Xác định thể loại, bối cảnh, giọng văn chủ đạo       │
│    ├── Thiết lập glossary ban đầu                            │
│    ├── Thiết lập character profiles ban đầu                  │
│    └── Chia chapter/đoạn → cập nhật progress tracker         │
│                                                              │
│  PHASE 1..N: Dịch từng đoạn                                 │
│    ├── Đọc lại context files TRƯỚC KHI DỊCH                 │
│    ├── Dịch đoạn hiện tại                                    │
│    ├── Cập nhật glossary nếu gặp thuật ngữ mới              │
│    ├── Cập nhật character profiles nếu có nhân vật mới       │
│    ├── Cập nhật relationships nếu có quan hệ mới            │
│    └── Cập nhật progress tracker                             │
│                                                              │
│  PHASE CUỐI: Rà soát                                         │
│    ├── Kiểm tra tính nhất quán thuật ngữ                     │
│    ├── Kiểm tra tính nhất quán văn phong                     │
│    └── Kiểm tra tính nhất quán xưng hô                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Các File Ngữ Cảnh (Context Files)

Tất cả các file ngữ cảnh nằm trong thư mục `context/` của dự án dịch:

| File | Mục đích | Khi nào cập nhật |
|------|----------|------------------|
| `context/glossary.md` | Tên riêng, địa danh, thuật ngữ, tên skill/phép thuật | Gặp thuật ngữ mới hoặc cần chỉnh sửa bản dịch |
| `context/characters.md` | Nhân vật và văn phong nói chuyện | Gặp nhân vật mới hoặc nhân vật thay đổi cách nói |
| `context/relationships.md` | Mối quan hệ và cách xưng hô | Gặp quan hệ mới hoặc thay đổi quan hệ |
| `progress.md` | Theo dõi tiến độ dịch | Sau mỗi đoạn dịch xong |

---

## 3. Quy Trình Chi Tiết

### 3.1 Khởi Tạo Dự Án Dịch Mới

Khi người dùng yêu cầu dịch một tiểu thuyết mới:

1. **Tạo thư mục dự án**:
   ```
   <novel_name>/
   ├── source/          ← Văn bản gốc tiếng Anh
   │   └── images/      ← Ảnh được extract từ file nguồn
   ├── translated/      ← Bản dịch tiếng Việt
   ├── context/         ← Các file ngữ cảnh
   │   ├── glossary.md
   │   ├── characters.md
   │   └── relationships.md
   └── progress.md      ← Theo dõi tiến độ
   ```

2. **Phân tích sơ bộ nguyên tác**:
   - Đọc lướt hoặc đọc toàn bộ để nắm bắt:
     - Thể loại (fantasy, sci-fi, romance, thriller, v.v.)
     - Bối cảnh thời đại, không gian
     - Giọng văn chủ đạo (trang trọng, hài hước, u ám, v.v.)
     - Ngôi kể (ngôi thứ nhất, thứ ba, v.v.)
   - Ghi nhận vào đầu file `progress.md`

3. **Chia đoạn**:
   - Nếu tiểu thuyết đã chia chapter → mỗi chapter = 1 phase
   - Nếu chapter quá dài (>5000 từ) → chia thành sub-sections
   - Nếu không có chapter → chia theo scene breaks hoặc mỗi ~3000-5000 từ
   - Ghi danh sách phases vào `progress.md`

4. **Khởi tạo glossary**:
   - Quét nhanh tên nhân vật chính, địa danh quan trọng
   - Thống nhất cách dịch/phiên âm ngay từ đầu
   - Ghi vào `context/glossary.md`

5. **Khởi tạo character profiles**:
   - Liệt kê nhân vật chính xuất hiện trong phần đầu
   - Mô tả sơ bộ văn phong nếu đã rõ
   - Ghi vào `context/characters.md`

6. **Khởi tạo relationships**:
   - Ghi nhận các mối quan hệ đã biết
   - Ghi vào `context/relationships.md`

### 3.2 Dịch Từng Đoạn (Phase)

**TRƯỚC KHI DỊCH MỖI ĐOẠN, BẮT BUỘC PHẢI:**

```
┌──────────────────────────────────────────────────────┐
│  ⚠️ CHECKLIST TRƯỚC KHI DỊCH MỖI ĐOẠN              │
│                                                       │
│  □ Đọc context/glossary.md                           │
│  □ Đọc context/characters.md                         │
│  □ Đọc context/relationships.md                      │
│  □ Đọc progress.md (xem đoạn trước đã dịch gì)      │
│  □ Đọc lại 1-2 đoạn dịch trước đó (nếu có)          │
│    để nối tiếp văn phong                              │
│  □ Kiểm tra file nguồn có ảnh không → extract nếu có │
└──────────────────────────────────────────────────────┘
```

**Trong khi dịch:**

1. **Dịch nghĩa, không dịch từ**:
   - Ưu tiên truyền tải ý nghĩa và cảm xúc
   - Không dịch word-by-word, câu phải tự nhiên trong tiếng Việt
   - Giữ nhịp điệu và tốc độ của nguyên tác

2. **Xử lý hội thoại**:
   - Dùng đúng văn phong đã ghi trong `characters.md`
   - Dùng đúng cách xưng hô đã ghi trong `relationships.md`
   - Nếu nhân vật mới xuất hiện → dừng lại, phân tích, cập nhật files

3. **Xử lý thuật ngữ**:
   - Tra `glossary.md` trước khi dịch bất kỳ thuật ngữ nào
   - Nếu thuật ngữ mới → quyết định cách dịch, ghi vào glossary
   - KHÔNG được dịch cùng một thuật ngữ bằng hai cách khác nhau

4. **Xử lý văn hóa**:
   - Thành ngữ, tục ngữ → tìm tương đương tiếng Việt hoặc diễn giải
   - Đơn vị đo lường → giữ nguyên hoặc chuyển đổi (tùy bối cảnh)
   - Tên riêng → theo quy tắc đã ghi trong glossary

**SAU KHI DỊCH XONG MỖI ĐOẠN:**

```
┌───────────────────────────────────────────────────────┐
│  ✅ CHECKLIST SAU KHI DỊCH MỖI ĐOẠN                  │
│                                                        │
│  □ Cập nhật glossary.md (thuật ngữ mới)               │
│  □ Cập nhật characters.md (nhân vật mới/thay đổi)     │
│  □ Cập nhật relationships.md (quan hệ mới)            │
│  □ Cập nhật progress.md (đánh dấu hoàn thành)         │
│  □ Chèn link ảnh vào file dịch (nếu chapter có ảnh)   │
│  □ Đọc lại bản dịch 1 lần để rà soát                  │
└───────────────────────────────────────────────────────┘
```

### 3.3 Xử Lý Ảnh Trong File Nguồn

Khi file nguồn (EPUB, DOCX, PDF, v.v.) chứa ảnh minh họa, bản đồ, hoặc hình ảnh nhân vật:

#### 3.3.1 Quy Trình Extract Ảnh

1. **Phát hiện ảnh**: Khi đọc file nguồn, kiểm tra xem có ảnh nhúng hay không
2. **Extract ảnh**: Trích xuất tất cả ảnh từ file nguồn
3. **Lưu vào thư mục `source/images/`**:
   - Tổ chức theo volume/chapter:
     ```
     source/images/
     ├── vol_1/
     │   ├── ch01_illustration_01.jpg
     │   ├── ch01_map.png
     │   ├── ch05_character_intro.jpg
     │   └── cover.jpg
     ├── vol_2/
     │   └── ...
     └── shared/           ← Ảnh dùng chung (bản đồ thế giới, v.v.)
         └── world_map.png
     ```

4. **Quy tắc đặt tên ảnh**:
   | Loại ảnh | Quy tắc đặt tên | Ví dụ |
   |----------|-----------------|-------|
   | Ảnh bìa | `cover.jpg` | `vol_1/cover.jpg` |
   | Minh họa chapter | `ch{XX}_illustration_{NN}.jpg` | `ch03_illustration_01.jpg` |
   | Bản đồ | `ch{XX}_map.png` hoặc `world_map.png` | `ch01_map.png` |
   | Ảnh nhân vật | `ch{XX}_character_{tên}.jpg` | `ch05_character_kumoko.jpg` |
   | Ảnh khác | Mô tả ngắn gọn bằng tiếng Anh | `ch10_battle_scene.jpg` |

#### 3.3.2 Chèn Ảnh Vào File Dịch

Khi dịch chapter có ảnh, chèn link ảnh vào đúng vị trí tương ứng trong file dịch:

```markdown
<!-- Ví dụ chèn ảnh minh họa trong file translated -->

![Minh họa: Kumoko đối đầu với rồng đất](../../source/images/vol_1/ch12_illustration_01.jpg)

Nàng nhện nhỏ bé đứng trước con quái vật khổng lồ...
```

**Lưu ý khi chèn ảnh:**
- Dùng **đường dẫn tương đối** từ file dịch đến thư mục `source/images/`
- Thêm **caption bằng tiếng Việt** mô tả nội dung ảnh (alt text)
- Đặt ảnh ở **đúng vị trí** như trong nguyên tác (trước/sau đoạn văn tương ứng)
- Nếu ảnh có text tiếng Anh (ví dụ: bản đồ có chú thích), ghi chú dịch bên dưới ảnh

#### 3.3.3 Xử Lý Các Định Dạng File Nguồn

| Định dạng | Cách extract ảnh |
|-----------|------------------|
| **EPUB** | Giải nén file `.epub` (thực chất là ZIP) → ảnh nằm trong thư mục `images/` hoặc `OEBPS/images/` |
| **DOCX** | Giải nén file `.docx` (thực chất là ZIP) → ảnh nằm trong `word/media/` |
| **PDF** | Dùng công cụ như `pdfimages` hoặc thư viện Python (`PyMuPDF`, `pdf2image`) để extract |
| **HTML** | Download ảnh từ các thẻ `<img>` |
| **TXT/MD** | Không có ảnh nhúng, bỏ qua bước này |

---

### 3.4 Xử Lý Khi Gặp Tình Huống Đặc Biệt

#### Nhân vật mới xuất hiện:
1. Đọc lại `context/characters.md` và `context/relationships.md`
2. Phân tích văn phong nói chuyện của nhân vật mới
3. Xác định mối quan hệ với nhân vật đã có
4. Xác định cách xưng hô phù hợp
5. Cập nhật cả 3 file context
6. Tiếp tục dịch

#### Thuật ngữ/khái niệm mới:
1. Đọc lại `context/glossary.md`
2. Kiểm tra xem đã có thuật ngữ tương tự chưa
3. Quyết định cách dịch nhất quán với hệ thống đã có
4. Cập nhật glossary
5. Tiếp tục dịch

#### Thay đổi quan hệ nhân vật:
1. Đọc lại `context/relationships.md`
2. Cập nhật mối quan hệ mới
3. Cập nhật cách xưng hô nếu thay đổi
4. Ghi chú thời điểm thay đổi (từ chapter nào)
5. Tiếp tục dịch

---

## 4. Nguyên Tắc Văn Phong Dịch

### 4.1 Nguyên Tắc Chung

- **Tự nhiên**: Câu dịch phải đọc như văn Việt gốc, không lộ dấu vết dịch
- **Trung thành**: Giữ nguyên ý nghĩa, sắc thái, và nhịp điệu nguyên tác
- **Nhất quán**: Cùng một thuật ngữ/cách xưng hô xuyên suốt tác phẩm
- **Phù hợp thể loại**: Fantasy → có thể dùng ngôn ngữ cổ phong; Modern → ngôn ngữ hiện đại

### 4.2 Quy Tắc Xưng Hô Tiếng Việt

Hệ thống xưng hô tiếng Việt phức tạp hơn tiếng Anh rất nhiều. Cần xác định rõ:

| Yếu tố | Cần xem xét |
|---------|-------------|
| Tuổi tác | Ai lớn hơn? → anh/chị/em, ông/bà/cháu |
| Quan hệ | Gia đình, bạn bè, đồng nghiệp, xa lạ |
| Tình cảm | Thân thiết, trang trọng, thù địch |
| Bối cảnh | Trang trọng hơn trong công việc, thoải mái hơn riêng tư |
| Thời đại | Cổ đại → ta/ngươi, hiện đại → tôi/anh |

### 4.3 Xử Lý Tên Riêng

| Loại | Cách xử lý | Ví dụ |
|------|------------|-------|
| Tên người phương Tây | Giữ nguyên | Harry Potter → Harry Potter |
| Tên người Trung/Nhật/Hàn | Phiên âm Hán-Việt (nếu có) hoặc giữ nguyên | 李白 → Lý Bạch |
| Địa danh thực | Dùng tên Việt nếu có, giữ nguyên nếu không | London → Luân Đôn hoặc London (tùy văn cảnh) |
| Địa danh hư cấu | Giữ nguyên hoặc dịch nghĩa (tùy tác giả) | Hogwarts → Hogwarts |
| Skill/Phép thuật | Dịch nghĩa + ghi chú gốc (lần đầu) | Fireball → Cầu Lửa |

---

## 5. Cách Sử Dụng Skill

### 5.1 Bắt Đầu Dự Án Mới

Người dùng nói:
> "Dịch tiểu thuyết [tên sách]"

→ Thực hiện Phase 0 (Khởi tạo) theo mục 3.1

### 5.2 Tiếp Tục Dịch

Người dùng nói:
> "Tiếp tục dịch" hoặc "Dịch chapter tiếp theo"

→ Đọc `progress.md` → Xác định đoạn tiếp theo → Thực hiện Phase theo mục 3.2

### 5.3 Chỉnh Sửa Thuật Ngữ

Người dùng nói:
> "Đổi cách dịch [thuật ngữ] thành [cách dịch mới]"

→ Cập nhật `glossary.md` → Ghi chú áp dụng từ đoạn nào → Lưu ý khi dịch tiếp

### 5.4 Xem Tiến Độ

Người dùng nói:
> "Tiến độ dịch thế nào?"

→ Đọc và trình bày `progress.md`

---

## 6. Lưu Ý Quan Trọng

> [!IMPORTANT]
> **LUÔN đọc lại tất cả context files trước khi dịch mỗi đoạn mới.**
> Đây là bước KHÔNG ĐƯỢC BỎ QUA để đảm bảo tính nhất quán.

> [!WARNING]
> **KHÔNG BAO GIỜ dịch một thuật ngữ bằng hai cách khác nhau** trừ khi có lý do
> rõ ràng (ví dụ: nhân vật cố tình gọi sai tên).

> [!TIP]
> Khi gặp đoạn khó dịch, hãy:
> 1. Hiểu rõ ý nghĩa trong ngữ cảnh
> 2. Viết ra 2-3 phương án dịch
> 3. Chọn phương án tự nhiên nhất trong tiếng Việt
> 4. Đảm bảo phù hợp với văn phong chung đã thiết lập

---

## 7. Template Prompt Cho Mỗi Phase

Khi bắt đầu dịch một đoạn mới, sử dụng quy trình sau:

```
1. Đọc file: context/glossary.md
2. Đọc file: context/characters.md  
3. Đọc file: context/relationships.md
4. Đọc file: progress.md
5. Đọc đoạn nguồn cần dịch
6. Kiểm tra & extract ảnh từ file nguồn (nếu có) → lưu vào source/images/
7. Dịch đoạn
8. Chèn link ảnh vào file dịch ở đúng vị trí (nếu chapter có ảnh)
9. Rà soát bản dịch
10. Cập nhật các file context nếu cần
11. Cập nhật progress.md
12. Lưu bản dịch vào translated/
```
