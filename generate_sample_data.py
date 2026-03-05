"""
Sample Data Generator
Creates sample Excel file with Vietnamese voter data for testing
"""

import pandas as pd
import random

def generate_sample_data(num_records=100, filename="sample_voters.xlsx"):
    """
    Generate sample voter data for testing
    
    Args:
        num_records: Number of voter records to generate
        filename: Output Excel filename
    """
    
    # Vietnamese first names
    first_names = [
        "Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng",
        "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý", "Mai", "Đinh", "Tô", "Trương"
    ]
    
    middle_names = [
        "Văn", "Thị", "Đức", "Minh", "Quốc", "Hồng", "Thanh", "Phương", "Anh", "Tuấn"
    ]
    
    last_names = [
        "Hùng", "Linh", "Anh", "Dũng", "Hương", "Thảo", "Phúc", "Trang", "Khoa", "Lan",
        "Nam", "Hà", "Quân", "Hoa", "Long", "Hiền", "Bình", "Mai", "Sơn", "Nga"
    ]
    
    # Generate data
    data = []
    used_voter_cards = set()
    used_national_ids = set()
    
    for i in range(num_records):
        # Generate unique voter card number (8 digits)
        while True:
            voter_card = f"{random.randint(10000000, 99999999)}"
            if voter_card not in used_voter_cards:
                used_voter_cards.add(voter_card)
                break
        
        # Generate unique national ID (12 digits)
        while True:
            national_id = f"{random.randint(100000000000, 999999999999)}"
            if national_id not in used_national_ids:
                used_national_ids.add(national_id)
                break
        
        # Generate full name
        first = random.choice(first_names)
        middle = random.choice(middle_names)
        last = random.choice(last_names)
        full_name = f"{first} {middle} {last}"
        
        data.append({
            "Họ và tên": full_name,
            "Số thẻ cử tri": voter_card,
            "Số CCCD": national_id
        })
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Save to Excel
    df.to_excel(filename, index=False, engine='openpyxl')
    
    print(f"✓ Generated {num_records} sample records")
    print(f"✓ Saved to: {filename}")
    print(f"\nSample records:")
    print(df.head(10).to_string(index=False))
    print(f"\n... and {num_records - 10} more records")


if __name__ == "__main__":
    # Generate different sizes for testing
    print("Generating sample data files...\n")
    
    # Small dataset for quick testing
    generate_sample_data(100, "sample_voters_100.xlsx")
    print("\n" + "="*60 + "\n")
    
    # Medium dataset
    generate_sample_data(1000, "sample_voters_1000.xlsx")
    print("\n" + "="*60 + "\n")
    
    # Large dataset for performance testing
    generate_sample_data(5000, "sample_voters_5000.xlsx")
    print("\n" + "="*60 + "\n")
    
    print("✓ All sample files generated successfully!")
    print("\nUse these files to test the voter attendance application.")
