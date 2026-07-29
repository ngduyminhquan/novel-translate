# Agent Skill: Translation Protocol (English → Vietnamese Novel Translation)

> **Mục đích**: Quy trình và quy tắc dành cho AI Agent khi dịch tiểu thuyết từ tiếng Anh sang tiếng Việt, đảm bảo chất lượng văn học, nhất quán ngữ cảnh, thuật ngữ và xưng hô.

---

## 1. DIRECTORY ARCHITECTURE & FILE ROLES

Mỗi dự án dịch tiểu thuyết phải tuân thủ đúng cấu trúc thư mục và vai trò file dưới đây:

- `<novel_root>/source/`: Chứa file văn bản gốc tiếng Anh (`.txt`, `.md`, `.epub`, `.pdf`, `.docx`).
- `<novel_root>/source/images/<vol_id>/`: Chứa ảnh minh họa, bản đồ, hình nhân vật được extract từ file nguồn.
- `<novel_root>/translated/<vol_id>/`: Chứa file bản dịch tiếng Việt đã hoàn thành.
- `<novel_root>/context/`: Nơi lưu trữ thông tin ngữ cảnh duy nhất (Single Source of Truth).
  - `glossary.md`: Danh mục thuật ngữ, tên riêng, địa danh, skill, phép thuật.
  - `characters.md`: Hồ sơ nhân vật, tính cách, giọng văn, cách nói chuyện.
  - `relationships.md`: Ma trận mối quan hệ và quy tắc xưng hô giữa từng cặp nhân vật.
- `<novel_root>/progress_<vol_id>.md` (hoặc `progress.md`): File theo dõi tiến độ, danh sách các chunk/phase và metadata dự án.

---

## 2. EXECUTION PROTOCOL (WORKFLOW PHASES)

### Phase 0: Project Initialization (Khởi tạo dự án)
**Trigger**: Người dùng yêu cầu dịch một tác phẩm/tập truyện mới.

1. **Tạo cấu trúc thư mục**: Dựng đủ các thư mục `source/`, `translated/`, `context/` và file `progress.md`.
2. **Phân tích nguyên tác**: Quét file nguồn để xác định thể loại, bối cảnh, ngôi kể (ngôi 1 hay 3), giọng văn chủ đạo.
3. **Phân chia đoạn (Chunking)**:
   - Đơn vị mặc định: 1 chapter = 1 phase.
   - Trường hợp chapter > 5000 từ: Chia thành các sub-sections (3000-5000 từ/chunk).
4. **Khởi tạo progress log**: Đưa metadata (tên gốc, tên dịch, tác giả, tổng số từ, ngày bắt đầu) và danh sách phases vào `progress.md`.
5. **Khởi tạo context files ban đầu**:
   - `context/glossary.md`: Nạp tên nhân vật chính, địa danh lớn, thuật ngữ nổi bật.
   - `context/characters.md`: Nạp hồ sơ nhân vật chính và phong cách thoại sơ bộ.
   - `context/relationships.md`: Nạp các mối quan hệ ban đầu và cặp xưng hô dự kiến.

---

### Phase 1..N: Translation Loop (Vòng lặp dịch từng Chunk/Chapter)
**Trigger**: Bắt đầu dịch một đoạn/chapter mới.

#### Step 1: Pre-Execution Context Loading (BẮT BUỘC TRƯỚC KHI DỊCH)
Agent phải đọc và nạp toàn bộ nội dung của các file sau vào context memory:
1. `context/glossary.md`
2. `context/characters.md`
3. `context/relationships.md`
4. `progress.md` (kiểm tra phase hiện tại và đọc lại context 1-2 đoạn liền trước để nối mạch văn).

#### Step 2: Asset Extraction & Pre-processing
1. Đọc văn bản nguồn của chunk từ `source/`.
2. Kiểm tra xem file nguồn có chứa hình ảnh hay không:
   - Nếu có (EPUB/DOCX/PDF/HTML): Trích xuất ảnh vào `source/images/<vol_id>/`.
   - Quy tắc đặt tên file ảnh:
     - Cover: `cover.jpg`
     - Minh họa chapter: `ch{XX}_illustration_{NN}.jpg`
     - Bản đồ: `ch{XX}_map.png` hoặc `world_map.png`
     - Giới thiệu nhân vật: `ch{XX}_character_{tên}.jpg`
     - Khác: `ch{XX}_{mô_tả_ngắn}.jpg`

#### Step 3: Translation Generation & In-Flight Handlers
1. **Dịch thuật**: Direct translation sang tiếng Việt tự nhiên, truyền tải đúng sắc thái và ý nghĩa, không dịch word-by-word.
2. **Áp dụng Context**:
   - Thuật ngữ, địa danh, tên skill: Tra và áp dụng chính xác từ `glossary.md`.
   - Giọng văn nhân vật: Khai thác đúng đặc trưng khẩu khí từ `characters.md`.
   - Xưng hô thoại: Tra cặp xưng hô tương ứng giữa 2 nhân vật từ `relationships.md`.
3. **Định dạng bảng trạng thái (Status Screen)**: Chuyển đổi toàn bộ các khối Status Screen thô/dính dòng sang định dạng bảng Markdown (Markdown Table) chuẩn.
4. **Chèn ảnh minh họa**: Đặt link ảnh dạng markdown `![Mô tả tiếng Việt](../../source/images/<vol_id>/<file_ảnh>)` vào đúng vị trí tương ứng trong bản dịch.
5. **Xử lý ngắt ngữ cảnh (Dynamic Context Interrupts)**:
   - IF phát hiện nhân vật mới: Phân tích giọng văn/mối quan hệ -> cập nhật `characters.md` & `relationships.md`.
   - IF phát hiện thuật ngữ/skill/địa danh mới: Thống nhất cách dịch -> cập nhật `glossary.md`.
   - IF mối quan hệ nhân vật biến đổi (thù thành bạn, xưng hô thay đổi): Cập nhật `relationships.md` kèm mốc chapter thay đổi.

#### Step 4: Post-Execution Synchronization (BẮT BUỘC SAU KHI DỊCH)
1. Ghi kết quả bản dịch vào file `translated/<vol_id>/<chapter_name>.md`.
2. Đồng bộ tất cả thay đổi mới vào `context/glossary.md`, `context/characters.md`, `context/relationships.md`.
3. Cập nhật `progress.md`: Đánh dấu hoàn thành phase hiện tại.

---

### Phase Final: Quality Audit (Rà soát tổng thể)
1. Quét toàn bộ các file trong `translated/` đối chiếu với `context/glossary.md` để phát hiện bất kỳ sự bất nhất nào về thuật ngữ.
2. Kiểm tra tính đồng nhất về xưng hô và văn phong xuyên suốt các volume.

---

## 3. TRANSLATION RULES & STYLISTIC CONSTRAINTS

### 3.1 Quy tắc Văn phong & Cấu trúc Câu
- **Chất lượng văn học**: Chuyển đổi cấu trúc câu bị động/phức tạp của tiếng Anh thành câu chủ động, diễn đạt gãy gọn, tự nhiên theo ngữ pháp tiếng Việt.
- **Phù hợp thể loại**:
  - Fantasy/Cổ đại: Sử dụng từ Hán-Việt hợp lý để tạo không khí trang trọng hoặc cổ kính.
  - Modern/Isekai/Comedy: Sử dụng ngôn từ hiện đại, hài hước, linh hoạt theo giọng văn nguyên tác.

### 3.2 Quy tắc Giải quyết Xưng hô Tiếng Việt
Xác định cặp xưng hô dựa trên 5 yếu tố ưu tiên:
1. **Thứ bậc / Tuổi tác**: Ai lớn/cao hơn? (anh/chị/em, ông/bà/cháu, ngài/ta).
2. **Mức độ thân sơ**: Thân thiết vs Trang trọng vs Thù địch.
3. **Bối cảnh thời đại**: Cổ đại (ta/ngươi, bổn vương) vs Hiện đại (tôi/cậu, tớ/cậu, anh/em).
4. **Ngữ cảnh trò chuyện**: Trang trọng trong họp hành/công việc vs Thoải mái khi riêng tư.
5. **Giới tính & Tính cách nhân vật**: Thể hiện nét đặc trưng cá tính (kiêu ngạo, rụt rè, thô lố, bốc đồng).

### 3.3 Quy tắc Xử lý Tên riêng & Thuật ngữ
- **Tên người phương Tây**: Giữ nguyên gốc tiếng Anh (vd: Harry Potter, Edward).
- **Tên người Đông Á (Nhật/Trung/Hàn)**: Dùng phiên âm Hán-Việt chuẩn hoặc giữ nguyên dạng Romaji theo quy định chung trong glossary.
- **Địa danh hư cấu**: Giữ nguyên tên gốc hoặc dịch nghĩa tùy theo quy ước trong `glossary.md`.
- **Skill / Phép thuật / Vật phẩm**: Dịch nghĩa tiếng Việt + ghi chú tên gốc tiếng Anh trong ngoặc đơn ở lần xuất hiện đầu tiên (vd: *Cầu Lửa (Fireball)*).

---

## 4. AGENT TASK DISPATCH HANDLERS

Khi nhận yêu cầu từ người dùng, Agent kích hoạt nhánh xử lý tương ứng:

- **Mệnh lệnh**: *"Dịch tiểu thuyết [Tên]"* hoặc *"Khởi tạo dự án dịch"*
  -> **Action**: Thực thi **Phase 0 (Project Initialization)**.

- **Mệnh lệnh**: *"Tiếp tục dịch"* hoặc *"Dịch chapter [X]"*
  -> **Action**: Thực thi **Phase 1..N (Translation Loop)** cho chunk tương ứng.

- **Mệnh lệnh**: *"Đổi cách dịch [Thuật ngữ A] thành [Thuật ngữ B]"*
  -> **Action**: Cập nhật `context/glossary.md`, ghi rõ mốc chapter áp dụng thay đổi, và thực hiện rà soát/sửa đổi các file đã dịch nếu người dùng yêu cầu.

- **Mệnh lệnh**: *"Tiến độ dịch thế nào?"*
  -> **Action**: Đọc `progress.md` và tóm tắt trạng thái hoàn thành.

