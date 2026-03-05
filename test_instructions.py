"""
Manual test instructions for attendance marking
"""

print("""
╔════════════════════════════════════════════════════════════╗
║          HƯỚNG DẪN TEST CHỨC NĂNG ĐIỂM DANH                ║
╚════════════════════════════════════════════════════════════╝

Bước 1: Chạy ứng dụng
    python main.py

Bước 2: Tải file Excel
    - Click nút "Tải file Excel"
    - Chọn file: sample_voters_100.xlsx
    - Xem danh sách 100 cử tri hiển thị

Bước 3: Test điểm danh
    - Mở file sample_voters_100.xlsx
    - Copy một số thẻ cử tri từ cột "Số thẻ cử tri"
    - Paste vào ô "Số thẻ cử tri" trong ứng dụng
    - Nhấn Enter

Kết quả mong đợi:
    ✓ Popup hiện "Điểm danh thành công - [Tên cử tri]"
    ✓ Dòng trong bảng chuyển sang màu xanh
    ✓ Cột "Trạng thái" đổi thành "Đã điểm danh"
    ✓ Thống kê cập nhật: "Đã điểm danh" tăng lên 1

Bước 4: Test trùng lặp
    - Nhập lại cùng số thẻ cử tri
    - Nhấn Enter

Kết quả mong đợi:
    ⚠ Popup hiện "Cử tri này đã điểm danh rồi"

Bước 5: Test không tìm thấy
    - Nhập số thẻ không tồn tại: 99999999
    - Nhấn Enter

Kết quả mong đợi:
    ❌ Popup hiện "Không tìm thấy cử tri với số thẻ này"

╔════════════════════════════════════════════════════════════╗
║                  DANH SÁCH SỐ THẺ MẪU                      ║
╚════════════════════════════════════════════════════════════╝
""")

# Read and display some sample voter cards
import pandas as pd

try:
    df = pd.read_excel('sample_voters_100.xlsx')
    print("Một số số thẻ cử tri để test:\n")
    for i in range(min(10, len(df))):
        voter_card = df.iloc[i]['Số thẻ cử tri']
        name = df.iloc[i]['Họ và tên']
        print(f"  {voter_card:>10}  -  {name}")
    
    print(f"\n... và {len(df) - 10} cử tri khác")
    
except Exception as e:
    print(f"Lưu ý: Chạy 'python generate_sample_data.py' trước để tạo file test")

print("""
╔════════════════════════════════════════════════════════════╗
║                    CÁCH DEBUG                              ║
╚════════════════════════════════════════════════════════════╝

Nếu vẫn không điểm danh được:

1. Kiểm tra file Excel có đúng 3 cột:
   - Họ và tên
   - Số thẻ cử tri  
   - Số CCCD

2. Kiểm tra số thẻ cử tri:
   - Không có khoảng trắng thừa
   - Là số nguyên 8 chữ số
   - Khớp chính xác với file Excel

3. Kiểm tra trong console có lỗi gì không

4. Thử refresh lại bảng:
   - Click "Tải file Excel" lại
   - Xem bảng có load đúng không

╔════════════════════════════════════════════════════════════╗
""")
