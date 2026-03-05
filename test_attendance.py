"""
Quick test script to verify attendance marking functionality
"""

from data_manager import DataManager
import pandas as pd
import os

def test_attendance_marking():
    """Test attendance marking functionality"""
    print("="*60)
    print("Testing Attendance Marking Functionality")
    print("="*60)
    
    # Create test data
    print("\n[1/5] Creating test data...")
    test_data = pd.DataFrame({
        'Họ và tên': ['Nguyễn Văn A', 'Trần Thị B', 'Lê Văn C'],
        'Số thẻ cử tri': ['12345678', '87654321', '11111111'],
        'Số CCCD': ['001234567890', '009876543210', '001111111111']
    })
    
    test_file = 'test_voters_temp.xlsx'
    test_data.to_excel(test_file, index=False, engine='openpyxl')
    print(f"✓ Created test file: {test_file}")
    
    # Initialize data manager
    print("\n[2/5] Loading data...")
    dm = DataManager()
    success, message = dm.load_excel(test_file)
    
    if not success:
        print(f"✗ Failed to load: {message}")
        return False
    
    print(f"✓ {message}")
    
    # Test 1: Mark attendance
    print("\n[3/5] Testing attendance marking...")
    status, name = dm.mark_attendance('12345678')
    
    if status == 'SUCCESS':
        print(f"✓ Successfully marked attendance for: {name}")
    else:
        print(f"✗ Failed to mark attendance. Status: {status}")
        return False
    
    # Test 2: Check duplicate
    print("\n[4/5] Testing duplicate detection...")
    status, name = dm.mark_attendance('12345678')
    
    if status == 'ALREADY_ATTENDED':
        print(f"✓ Correctly detected duplicate for: {name}")
    else:
        print(f"✗ Failed to detect duplicate. Status: {status}")
        return False
    
    # Test 3: Check statistics
    print("\n[5/5] Checking statistics...")
    stats = dm.get_statistics()
    
    print(f"  Total voters: {stats['total']}")
    print(f"  Attended: {stats['attended']}")
    print(f"  Not attended: {stats['not_attended']}")
    
    if stats['attended'] == 1 and stats['not_attended'] == 2:
        print("✓ Statistics are correct!")
    else:
        print("✗ Statistics are incorrect!")
        return False
    
    # Clean up
    os.remove(test_file)
    print(f"\n✓ Cleaned up test file")
    
    print("\n" + "="*60)
    print("✅ All tests passed! Attendance marking works correctly.")
    print("="*60)
    
    return True

if __name__ == "__main__":
    try:
        test_attendance_marking()
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
