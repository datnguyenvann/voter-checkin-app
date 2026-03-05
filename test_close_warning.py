"""
Test Close Warning Feature
Kiểm tra tính năng cảnh báo lưu file khi tắt ứng dụng
"""

print("=" * 60)
print("HƯỚNG DẪN TEST TÍNH NĂNG CẢNH BÁO LƯU FILE")
print("=" * 60)

print("\n📋 CÁC TRƯỜNG HỢP TEST:\n")

print("1. THOÁT KHI CHƯA CÓ THAY ĐỔI:")
print("   ✓ Mở ứng dụng")
print("   ✓ Tải file Excel")
print("   ✓ Nhấn nút X để thoát")
print("   → Kết quả mong đợi: Thoát ngay, không có cảnh báo\n")

print("2. THOÁT SAU KHI ĐIỂM DANH (CHƯA LƯU):")
print("   ✓ Mở ứng dụng")
print("   ✓ Tải file Excel")
print("   ✓ Điểm danh cho ít nhất 1 cử tri")
print("   ✓ Nhấn nút X để thoát")
print("   → Kết quả mong đợi: Hiện cảnh báo với 3 lựa chọn:")
print("      - Có (Yes): Mở dialog lưu file, sau đó thoát")
print("      - Không (No): Hỏi xác nhận thêm 1 lần, nếu OK thì thoát")
print("      - Hủy (Cancel): Không thoát, quay lại ứng dụng\n")

print("3. THOÁT SAU KHI ĐÃ LƯU:")
print("   ✓ Mở ứng dụng")
print("   ✓ Tải file Excel")
print("   ✓ Điểm danh cho ít nhất 1 cử tri")
print("   ✓ Nhấn 'Xuất Excel' và lưu file")
print("   ✓ Nhấn nút X để thoát")
print("   → Kết quả mong đợi: Thoát ngay, không có cảnh báo\n")

print("4. LƯU NHƯNG HỦY DIALOG:")
print("   ✓ Mở ứng dụng")
print("   ✓ Tải file Excel")
print("   ✓ Điểm danh cho ít nhất 1 cử tri")
print("   ✓ Nhấn nút X để thoát")
print("   ✓ Chọn 'Có' để lưu")
print("   ✓ Nhấn 'Cancel' trong dialog lưu file")
print("   → Kết quả mong đợi: Không thoát, quay lại ứng dụng\n")

print("=" * 60)
print("BẮT ĐẦU TEST")
print("=" * 60)

import subprocess
import sys

try:
    print("\n▶ Đang mở ứng dụng...")
    print("\n📌 Vui lòng test theo các bước trên!")
    print("📌 Nhấn Ctrl+C trong terminal này để dừng test\n")
    
    subprocess.run([sys.executable, "main.py"])
    
except KeyboardInterrupt:
    print("\n\n✓ Test hoàn thành!")
except Exception as e:
    print(f"\n✗ Lỗi: {e}")
