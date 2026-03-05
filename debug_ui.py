"""
Debug script to test attendance marking in UI
"""

import tkinter as tk
from tkinter import ttk
import pandas as pd
import os
from data_manager import DataManager

def test_ui_attendance():
    """Test attendance marking with simplified UI"""
    
    # Create test data
    print("Creating test data...")
    test_data = pd.DataFrame({
        'Họ và tên': ['Nguyễn Văn A', 'Trần Thị B', 'Lê Văn C'],
        'Số thẻ cử tri': ['12345678', '87654321', '11111111'],
        'Số CCCD': ['001234567890', '009876543210', '001111111111']
    })
    
    test_file = 'test_debug.xlsx'
    test_data.to_excel(test_file, index=False, engine='openpyxl')
    
    # Create window
    root = tk.Tk()
    root.title("Debug Attendance Test")
    root.geometry("800x500")
    
    # Create data manager
    dm = DataManager()
    success, message = dm.load_excel(test_file)
    print(f"Load result: {success} - {message}")
    
    # Create treeview
    tree = ttk.Treeview(
        root,
        columns=("name", "voter_card", "national_id", "status"),
        show="headings"
    )
    
    tree.heading("name", text="Họ và tên")
    tree.heading("voter_card", text="Số thẻ cử tri")
    tree.heading("national_id", text="Số CCCD")
    tree.heading("status", text="Trạng thái")
    
    tree.tag_configure('attended', background='#d4edda', foreground='#155724')
    tree.tag_configure('not_attended', background='#f8f9fa', foreground='#212529')
    
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Populate table
    def populate_table():
        # Clear existing
        for item in tree.get_children():
            tree.delete(item)
        
        # Get records
        records = dm.get_all_records()
        print(f"\nPopulating table with {len(records)} records:")
        
        # Insert with index as iid
        for idx, record in enumerate(records):
            name, voter_card, national_id, status = record
            tag = 'attended' if status == 'Đã điểm danh' else 'not_attended'
            tree.insert('', tk.END, values=record, tags=(tag,), iid=str(idx))
            print(f"  [{idx}] {voter_card} - {name} - {status} (tag: {tag})")
    
    populate_table()
    
    # Create input and button
    input_frame = ttk.Frame(root)
    input_frame.pack(fill=tk.X, padx=10, pady=5)
    
    ttk.Label(input_frame, text="Số thẻ cử tri:").pack(side=tk.LEFT, padx=5)
    entry = ttk.Entry(input_frame, width=20)
    entry.pack(side=tk.LEFT, padx=5)
    
    def mark_attendance():
        voter_card = entry.get().strip()
        print(f"\n=== Marking attendance for: {voter_card} ===")
        
        # Mark in data manager
        status, name = dm.mark_attendance(voter_card)
        print(f"Status: {status}, Name: {name}")
        
        if status == 'SUCCESS':
            # Find index
            idx = dm.find_record_index(voter_card)
            print(f"Found at index: {idx}")
            
            # Get updated record
            records = dm.get_all_records()
            if idx is not None and idx < len(records):
                record = records[idx]
                item_id = str(idx)
                
                print(f"Updating treeview item {item_id}")
                print(f"  New values: {record}")
                print(f"  Tree exists: {tree.exists(item_id)}")
                
                if tree.exists(item_id):
                    # Update the item
                    tree.item(item_id, values=record, tags=('attended',))
                    tree.selection_set(item_id)
                    tree.see(item_id)
                    print(f"  ✓ Updated successfully")
                    
                    # Verify the update
                    item_values = tree.item(item_id)
                    print(f"  Verification - Values: {item_values['values']}")
                    print(f"  Verification - Tags: {item_values['tags']}")
                else:
                    print(f"  ✗ Item {item_id} does not exist!")
            
            print(f"✓ Attendance marked for {name}")
        elif status == 'ALREADY_ATTENDED':
            print(f"⚠ Already attended: {name}")
        else:
            print(f"✗ Not found")
        
        entry.delete(0, tk.END)
    
    btn = ttk.Button(input_frame, text="Điểm danh", command=mark_attendance)
    btn.pack(side=tk.LEFT, padx=5)
    
    # Refresh button to repopulate
    def refresh():
        print("\n=== Refreshing table ===")
        populate_table()
    
    btn_refresh = ttk.Button(input_frame, text="Refresh", command=refresh)
    btn_refresh.pack(side=tk.LEFT, padx=5)
    
    # Close button
    def on_close():
        if os.path.exists(test_file):
            os.remove(test_file)
        root.destroy()
    
    btn_close = ttk.Button(input_frame, text="Close", command=on_close)
    btn_close.pack(side=tk.RIGHT, padx=5)
    
    root.protocol("WM_DELETE_WINDOW", on_close)
    
    print("\n" + "="*60)
    print("Debug UI loaded")
    print("Try entering: 12345678 or 87654321 or 11111111")
    print("="*60)
    
    root.mainloop()

if __name__ == "__main__":
    test_ui_attendance()
