"""
Test script with comprehensive logging
"""

import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import sys
import os

# Add debug mode
DEBUG = True

def debug_print(msg):
    if DEBUG:
        print(f"[DEBUG] {msg}")

# Import after debug setup
from data_manager import DataManager

# Create simple test file
test_data = pd.DataFrame({
    'Họ và tên': ['Nguyễn Văn A', 'Trần Thị B'],
    'Số thẻ cử tri': ['12345678', '87654321'],
    'Số CCCD': ['001234567890', '009876543210']
})
test_file = 'test_simple.xlsx'
test_data.to_excel(test_file, index=False, engine='openpyxl')
debug_print(f"Created test file: {test_file}")

# Create UI
root = tk.Tk()
root.title("Test Attendance - Debug Mode")
root.geometry("900x600")

dm = DataManager()

# Load data
debug_print("Loading data...")
success, message = dm.load_excel(test_file)
debug_print(f"Load result: {success} - {message}")

if not success:
    print(f"FAILED TO LOAD: {message}")
    sys.exit(1)

# Display loaded data
debug_print("\nLoaded DataFrame:")
debug_print(str(dm.df))
debug_print("\nVoter card index:")
for card, idx in dm.voter_card_index.items():
    debug_print(f"  '{card}' -> {idx}")

# Create tree
tree_frame = ttk.Frame(root)
tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tree = ttk.Treeview(
    tree_frame,
    columns=("name", "voter_card", "national_id", "status"),
    show="headings",
    height=10
)

tree.heading("name", text="Họ và tên")
tree.heading("voter_card", text="Số thẻ cử tri")
tree.heading("national_id", text="Số CCCD")
tree.heading("status", text="Trạng thái")

tree.column("name", width=200)
tree.column("voter_card", width=120)
tree.column("national_id", width=150)
tree.column("status", width=150)

tree.tag_configure('attended', background='#d4edda', foreground='#155724')
tree.tag_configure('not_attended', background='#f8f9fa', foreground='#212529')

tree.pack(fill=tk.BOTH, expand=True)

# Populate tree
def populate_tree():
    debug_print("\n=== Populating tree ===")
    for item in tree.get_children():
        tree.delete(item)
    
    records = dm.get_all_records()
    debug_print(f"Got {len(records)} records")
    
    for idx, record in enumerate(records):
        name, voter_card, national_id, status = record
        tag = 'attended' if status == 'Đã điểm danh' else 'not_attended'
        tree.insert('', tk.END, values=record, tags=(tag,), iid=str(idx))
        debug_print(f"  [{idx}] Card:{voter_card} Name:{name} Status:{status} Tag:{tag}")

populate_tree()

# Input frame
input_frame = ttk.Frame(root)
input_frame.pack(fill=tk.X, padx=10, pady=10)

ttk.Label(input_frame, text="Số thẻ cử tri:", font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=5)
entry = ttk.Entry(input_frame, width=25, font=('Arial', 11))
entry.pack(side=tk.LEFT, padx=5)

# Status label
status_label = ttk.Label(input_frame, text="", foreground='blue', font=('Arial', 9))
status_label.pack(side=tk.LEFT, padx=20)

def mark_attendance():
    debug_print("\n" + "="*60)
    debug_print("MARK ATTENDANCE CALLED")
    
    voter_card = entry.get().strip()
    debug_print(f"Input value: '{voter_card}'")
    
    if not voter_card:
        debug_print("Empty input!")
        status_label.config(text="❌ Vui lòng nhập số thẻ", foreground='red')
        return
    
    debug_print(f"Calling dm.mark_attendance('{voter_card}')...")
    status, name = dm.mark_attendance(voter_card)
    debug_print(f"Result: status={status}, name={name}")
    
    if status == 'SUCCESS':
        debug_print("✓ SUCCESS - Updating UI...")
        
        # Find index
        idx = dm.find_record_index(voter_card)
        debug_print(f"  Record index: {idx}")
        
        # Get updated record
        records = dm.get_all_records()
        if idx is not None and idx < len(records):
            record = records[idx]
            item_id = str(idx)
            
            debug_print(f"  Item ID: {item_id}")
            debug_print(f"  New record: {record}")
            debug_print(f"  Tree exists: {tree.exists(item_id)}")
            
            if tree.exists(item_id):
                debug_print("  Updating tree item...")
                tree.item(item_id, values=record, tags=('attended',))
                tree.selection_set(item_id)
                tree.see(item_id)
                debug_print("  ✓ Tree item updated")
                
                # Verify
                item_data = tree.item(item_id)
                debug_print(f"  Verification - Values: {item_data['values']}")
                debug_print(f"  Verification - Tags: {item_data['tags']}")
            
        status_label.config(text=f"✓ Đã điểm danh: {name}", foreground='green')
        messagebox.showinfo("Thành công", f"Điểm danh thành công\n\n{name}")
        entry.delete(0, tk.END)
        
    elif status == 'ALREADY_ATTENDED':
        debug_print("⚠ ALREADY_ATTENDED")
        status_label.config(text=f"⚠ Đã điểm danh rồi: {name}", foreground='orange')
        messagebox.showinfo("Thông báo", f"Cử tri này đã điểm danh rồi\n\n{name}")
        
    else:
        debug_print("✗ NOT_FOUND")
        status_label.config(text="❌ Không tìm thấy", foreground='red')
        messagebox.showwarning("Không tìm thấy", "Không tìm thấy cử tri với số thẻ này")
    
    debug_print("="*60)

btn = ttk.Button(input_frame, text="Điểm danh (hoặc nhấn Enter)", command=mark_attendance)
btn.pack(side=tk.LEFT, padx=5)

entry.bind('<Return>', lambda e: mark_attendance())
entry.focus()

# Info label
info = ttk.Label(root, text="Số thẻ test: 12345678 hoặc 87654321", 
                 font=('Arial', 10, 'bold'), foreground='blue')
info.pack(pady=5)

# Cleanup on close
def on_close():
    if os.path.exists(test_file):
        os.remove(test_file)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

debug_print("\n" + "="*60)
debug_print("UI READY - Try entering: 12345678 or 87654321")
debug_print("="*60 + "\n")

root.mainloop()
