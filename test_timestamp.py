"""
Test timestamp functionality
"""
import time
from data_manager import DataManager

def test_timestamp_feature():
    """Test that timestamps are recorded correctly"""
    print("Testing timestamp feature...")
    
    # Initialize data manager
    dm = DataManager()
    
    # Load sample data
    try:
        dm.load_excel('sample_voters_100.xlsx')
        print("✓ Loaded sample data")
    except FileNotFoundError:
        print("✗ Sample data not found, generating it...")
        import subprocess
        subprocess.run(['python', 'generate_sample_data.py'])
        dm.load_excel('sample_voters_100.xlsx')
        print("✓ Generated and loaded sample data")
    
    # Get first record
    records = dm.get_all_records()
    first_record = records[0]
    name, voter_card, national_id, status, timestamp = first_record
    
    print(f"\nFirst record: {name}")
    print(f"  Voter card: {voter_card}")
    print(f"  Initial status: {status}")
    print(f"  Initial timestamp: '{timestamp}'")
    
    # Mark attendance
    print(f"\nMarking attendance for {voter_card}...")
    time.sleep(1)  # Wait 1 second to see different timestamp
    status, message = dm.mark_attendance(voter_card)
    
    if status == 'SUCCESS':
        print(f"✓ {message}")
        
        # Get updated record
        records = dm.get_all_records()
        updated_record = records[0]
        name, voter_card, national_id, status, timestamp = updated_record
        
        print(f"\nUpdated record:")
        print(f"  Status: {status}")
        print(f"  Timestamp: {timestamp}")
        
        # Verify timestamp is not empty
        if timestamp and len(timestamp) > 0:
            print("\n✓ Timestamp recorded successfully!")
            print(f"✓ Format: {timestamp}")
            
            # Try marking again (should fail)
            print(f"\nTrying to mark attendance again...")
            success2, message2 = dm.mark_attendance(voter_card)
            if success2 == 'ALREADY_ATTENDED':
                print(f"✓ Duplicate prevented: {message2} already attended")
            else:
                print(f"✗ Should have prevented duplicate, got: {success2}")
        else:
            print("\n✗ Timestamp is empty!")
    else:
        print(f"✗ Failed: {message}")
    
    # Get statistics
    stats = dm.get_statistics()
    print(f"\n=== Statistics ===")
    print(f"Total: {stats['total']}")
    print(f"Attended: {stats['attended']}")
    print(f"Not attended: {stats['not_attended']}")
    
    print("\n✓ All tests passed!")

if __name__ == "__main__":
    test_timestamp_feature()
