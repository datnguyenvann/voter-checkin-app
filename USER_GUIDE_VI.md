# HƯỚNG DẪN SỬ DỤNG
## Ứng dụng Điểm danh Cử tri

---

## 📱 Bắt đầu nhanh

### Bước 1: Khởi động ứng dụng
- Nhấp đúp vào `VoterAttendance.exe`
- Ứng dụng sẽ mở cửa sổ chính

### Bước 2: Tải danh sách cử tri
1. Nhấp nút **"Tải file Excel"**
2. Chọn file Excel chứa danh sách cử tri
3. File phải có 3 cột:
   - **Họ và tên**
   - **Số thẻ cử tri**
   - **Số CCCD**

### Bước 3: Điểm danh cử tri
1. Nhập số thẻ cử tri vào ô "Số thẻ cử tri"
2. Nhấn phím **Enter**
3. Hệ thống sẽ:
   - ✅ Đánh dấu đã điểm danh (nếu chưa)
   - ⚠️ Thông báo nếu đã điểm danh
   - ❌ Cảnh báo nếu không tìm thấy

### Bước 4: Xuất kết quả
1. Nhấp nút **"Xuất file Excel"**
2. Chọn vị trí lưu file
3. File mới sẽ có cột "Trạng thái" bổ sung

---

## 🔍 Xác minh danh tính

### Khi cần xác minh thông tin cử tri:
1. Nhập **Số thẻ cử tri**
2. Nhập **Số CCCD**
3. Nhấp nút **"Xác minh thông tin"**
4. Hệ thống kiểm tra:
   - ✅ Cả hai số khớp với nhau
   - ❌ Số CCCD không đúng
   - ⚠️ Không tìm thấy cử tri

---

## 📊 Thống kê

Phần thống kê hiển thị:
- **Tổng số cử tri**: Tổng cộng trong danh sách
- **Đã điểm danh**: Số cử tri đã check-in
- **Chưa điểm danh**: Số cử tri chưa đến

---

## ⚠️ Xử lý lỗi thường gặp

### Lỗi: "Missing required columns"
**Nguyên nhân:** File Excel thiếu cột bắt buộc

**Giải pháp:**
- Đảm bảo file có đúng 3 cột:
  - Họ và tên
  - Số thẻ cử tri
  - Số CCCD
- Tên cột phải viết chính xác (có dấu)

### Lỗi: "File not found"
**Nguyên nhân:** File đã bị xóa hoặc di chuyển

**Giải pháp:**
- Kiểm tra file còn tồn tại
- Chọn lại file đúng vị trí

### Lỗi: "This voter has already checked in"
**Không phải lỗi** - Cử tri này đã điểm danh rồi

---

## 💡 Mẹo sử dụng

### Tăng tốc độ điểm danh:
1. Sử dụng phím **Enter** thay vì nhấp chuột
2. Ô nhập liệu tự động clear sau mỗi lần điểm danh
3. Focus luôn quay về ô nhập để nhập tiếp

### Tìm cử tri trong danh sách:
- Sau khi điểm danh hoặc xác minh thành công
- Hệ thống tự động **highlight** và **scroll** đến dòng đó

### Theo dõi tiến độ:
- Xem phần "Thống kê" để biết đã điểm danh bao nhiêu
- Màu xanh: Đã điểm danh
- Màu xám: Chưa điểm danh

---

## 🔒 Bảo mật dữ liệu

### Khuyến nghị:
✅ Chỉ chạy trên máy tính không kết nối Internet
✅ Đặt mật khẩu cho file Excel
✅ Xóa file sau khi hoàn tất bầu cử
✅ Không sao chép dữ liệu ra ngoài
✅ Khóa phòng có máy tính chạy ứng dụng

---

## 📞 Hỗ trợ kỹ thuật

### Nếu gặp vấn đề:
1. Đóng ứng dụng
2. Khởi động lại
3. Tải lại file Excel
4. Liên hệ bộ phận IT nếu vẫn lỗi

---

## ✅ Checklist trước khi sử dụng

- [ ] Đã cài đặt ứng dụng trên máy tính
- [ ] Đã chuẩn bị file Excel với danh sách cử tri
- [ ] Đã kiểm tra 3 cột bắt buộc có đầy đủ
- [ ] Đã test thử với vài cử tri mẫu
- [ ] Đã hiểu cách điểm danh và xác minh
- [ ] Đã biết cách xuất kết quả

---

**Phiên bản:** 1.0.0  
**Ngày cập nhật:** 05/03/2026  
**Hệ điều hành:** Windows 10/11
