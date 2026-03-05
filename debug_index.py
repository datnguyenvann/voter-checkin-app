"""
Simple debug script to check voter card index
"""

from data_manager import DataManager
import pandas as pd
import os

# Create test data
test_data = pd.DataFrame({
    'Họ và tên': ['Nguyễn Văn A', 'Trần Thị B', 'Lê Văn C'],
    'Số thẻ cử tri': ['12345678', '87654321', '11111111'],
    'Số CCCD': ['001234567890', '009876543210', '001111111111']
})

test_file = 'test_check.xlsx'
test_data.to_excel(test_file, index=False, engine='openpyxl')

# Load with data manager
dm = DataManager()
success, message = dm.load_excel(test_file)

print(f"Load success: {success}")
print(f"Message: {message}")
print(f"\nDataFrame content:")
print(dm.df)
print(f"\nDataFrame dtypes:")
print(dm.df.dtypes)
print(f"\nVoter card index dictionary:")
for card, idx in dm.voter_card_index.items():
    print(f"  '{card}' -> {idx}")

print(f"\nTest lookups:")
test_cards = ['12345678', '87654321', '11111111', '99999999']
for card in test_cards:
    result = dm.voter_card_index.get(card)
    print(f"  '{card}' -> {result}")

# Test attendance marking
print(f"\n\nTesting attendance marking:")
status, name = dm.mark_attendance('12345678')
print(f"  Status: {status}")
print(f"  Name: {name}")

print(f"\nDataFrame after marking:")
print(dm.df)

# Cleanup
os.remove(test_file)
