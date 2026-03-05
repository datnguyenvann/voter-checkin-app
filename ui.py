"""
UI Module
Tkinter-based user interface for voter attendance application
Optimized for performance with large datasets
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from typing import Optional, Callable
from data_manager import DataManager


class VoterAttendanceUI:
    """
    Main UI class for voter attendance application
    """
    
    def __init__(self, root: tk.Tk, data_manager: DataManager):
        self.root = root
        self.data_manager = data_manager
        
        # Configure main window
        self.root.title("Hệ thống Điểm danh Cử tri")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 600)
        
        # Flag to track if data has been modified
        self.has_unsaved_changes = False
        
        # Setup close handler
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
        
        # Setup UI components
        self._setup_ui()
        
        # Store reference to selected item
        self.current_selection = None
        
    def _setup_ui(self):
        """Setup all UI components"""
        # Top frame - File operations
        self._create_top_frame()
        
        # Middle frame - Data table
        self._create_table_frame()
        
        # Right frame - Input and statistics
        self._create_right_frame()
        
    def _create_top_frame(self):
        """Create top frame with file operations"""
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Load Excel button
        self.btn_load = ttk.Button(
            top_frame,
            text="📂 Tải file Excel",
            command=self._load_excel_file,
            width=20
        )
        self.btn_load.pack(side=tk.LEFT, padx=5)
        
        # Export button
        self.btn_export = ttk.Button(
            top_frame,
            text="💾 Xuất file Excel",
            command=self._export_excel_file,
            width=20,
            state=tk.DISABLED
        )
        self.btn_export.pack(side=tk.LEFT, padx=5)
        
        # File info label
        self.lbl_file_info = ttk.Label(
            top_frame,
            text="Chưa tải dữ liệu",
            font=('Segoe UI', 9)
        )
        self.lbl_file_info.pack(side=tk.LEFT, padx=20)
        
    def _create_table_frame(self):
        """Create middle frame with data table"""
        # Container frame
        table_container = ttk.Frame(self.root, padding="10")
        table_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Label
        ttk.Label(
            table_container,
            text="Danh sách cử tri",
            font=('Segoe UI', 11, 'bold')
        ).pack(anchor=tk.W, pady=(0, 5))
        
        # Create treeview with scrollbars
        tree_frame = ttk.Frame(table_container)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Vertical scrollbar
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Horizontal scrollbar
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Treeview
        self.tree = ttk.Treeview(
            tree_frame,
            columns=("stt", "name", "voter_card", "national_id", "status", "timestamp"),
            show="headings",
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set,
            height=20
        )
        
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        
        # Define columns
        self.tree.heading("stt", text="STT")
        self.tree.heading("name", text="Họ và tên")
        self.tree.heading("voter_card", text="Số thẻ cử tri")
        self.tree.heading("national_id", text="Số CCCD")
        self.tree.heading("status", text="Trạng thái")
        self.tree.heading("timestamp", text="Thời gian điểm danh")
        
        # Column widths
        self.tree.column("stt", width=50, minwidth=50, anchor=tk.CENTER)
        self.tree.column("name", width=180, minwidth=120)
        self.tree.column("voter_card", width=120, minwidth=100)
        self.tree.column("national_id", width=120, minwidth=100)
        self.tree.column("status", width=120, minwidth=100)
        self.tree.column("timestamp", width=150, minwidth=130)
        
        # Configure tags for styling
        self.tree.tag_configure('attended', background='#d4edda', foreground='#155724')
        self.tree.tag_configure('not_attended', background='#f8f9fa', foreground='#212529')
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
    def _create_right_frame(self):
        """Create right frame with input fields and statistics"""
        right_container = ttk.Frame(self.root, padding="10")
        right_container.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10))
        
        # Section 1: Quick Check-in (Điểm danh nhanh)
        checkin_frame = ttk.LabelFrame(
            right_container,
            text="⚡ Điểm danh nhanh",
            padding="15"
        )
        checkin_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Voter card input for quick check-in
        ttk.Label(
            checkin_frame,
            text="Số thẻ cử tri:",
            font=('Segoe UI', 9, 'bold')
        ).pack(anchor=tk.W, pady=(0, 5))
        
        self.entry_voter_card = ttk.Entry(checkin_frame, width=30, font=('Segoe UI', 11))
        self.entry_voter_card.pack(fill=tk.X, pady=(0, 10))
        self.entry_voter_card.bind('<Return>', lambda e: self._mark_attendance())
        
        # Check-in button
        self.btn_checkin = ttk.Button(
            checkin_frame,
            text="✓ Điểm danh (hoặc nhấn Enter)",
            command=self._mark_attendance,
            state=tk.DISABLED
        )
        self.btn_checkin.pack(fill=tk.X)
        
        # Instruction label
        ttk.Label(
            checkin_frame,
            text="💡 Nhập số thẻ và nhấn Enter",
            font=('Segoe UI', 8),
            foreground='#6c757d'
        ).pack(anchor=tk.W, pady=(5, 0))
        
        # Section 2: Verification (Xác minh)
        verify_frame = ttk.LabelFrame(
            right_container,
            text="🔍 Xác minh thông tin",
            padding="15"
        )
        verify_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Voter card for verification
        ttk.Label(
            verify_frame,
            text="Số thẻ cử tri:",
            font=('Segoe UI', 9, 'bold')
        ).pack(anchor=tk.W, pady=(0, 5))
        
        self.entry_verify_card = ttk.Entry(verify_frame, width=30, font=('Segoe UI', 10))
        self.entry_verify_card.pack(fill=tk.X, pady=(0, 10))
        
        # National ID input
        ttk.Label(
            verify_frame,
            text="Số CCCD:",
            font=('Segoe UI', 9, 'bold')
        ).pack(anchor=tk.W, pady=(0, 5))
        
        self.entry_national_id = ttk.Entry(verify_frame, width=30, font=('Segoe UI', 10))
        self.entry_national_id.pack(fill=tk.X, pady=(0, 10))
        
        # Verify button
        self.btn_verify = ttk.Button(
            verify_frame,
            text="✓ Xác minh",
            command=self._verify_voter,
            state=tk.DISABLED
        )
        self.btn_verify.pack(fill=tk.X)
        
        # Statistics section
        stats_frame = ttk.LabelFrame(
            right_container,
            text="Thống kê",
            padding="15"
        )
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Total voters
        self.lbl_total = self._create_stat_label(
            stats_frame,
            "Tổng số cử tri:",
            "0",
            "#007bff"
        )
        
        # Attended
        self.lbl_attended = self._create_stat_label(
            stats_frame,
            "Đã điểm danh:",
            "0",
            "#28a745"
        )
        
        # Not attended
        self.lbl_not_attended = self._create_stat_label(
            stats_frame,
            "Chưa điểm danh:",
            "0",
            "#6c757d"
        )
        
        # Instructions section
        inst_frame = ttk.LabelFrame(
            right_container,
            text="Hướng dẫn",
            padding="15"
        )
        inst_frame.pack(fill=tk.BOTH, expand=True)
        
        instructions = """
1. Tải file Excel chứa danh sách cử tri

2. Nhập số thẻ cử tri và nhấn Enter để điểm danh nhanh

3. Để xác minh, nhập cả số thẻ cử tri và số CCCD, sau đó nhấn nút Xác minh

4. Xuất file Excel để lưu kết quả điểm danh
        """
        
        ttk.Label(
            inst_frame,
            text=instructions.strip(),
            justify=tk.LEFT,
            font=('Segoe UI', 8),
            foreground='#6c757d'
        ).pack(anchor=tk.W)
        
    def _create_stat_label(self, parent, label_text: str, value: str, color: str) -> ttk.Label:
        """Create a statistics label with value"""
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(
            frame,
            text=label_text,
            font=('Segoe UI', 9)
        ).pack(side=tk.LEFT)
        
        value_label = ttk.Label(
            frame,
            text=value,
            font=('Segoe UI', 11, 'bold'),
            foreground=color
        )
        value_label.pack(side=tk.RIGHT)
        
        return value_label
        
    def _load_excel_file(self):
        """Handle load Excel file button click"""
        file_path = filedialog.askopenfilename(
            title="Chọn file Excel",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
        )
        
        if not file_path:
            return
        
        # Show loading message
        self.lbl_file_info.config(text="Đang tải dữ liệu...")
        self.root.update()
        
        # Load data
        success, message = self.data_manager.load_excel(file_path)
        
        if success:
            self.lbl_file_info.config(text=message)
            self._populate_table()
            self._update_statistics()
            self.btn_export.config(state=tk.NORMAL)
            self.btn_checkin.config(state=tk.NORMAL)
            self.btn_verify.config(state=tk.NORMAL)
            self.entry_voter_card.focus()  # Auto focus to check-in field
            messagebox.showinfo("Thành công", message)
        else:
            self.lbl_file_info.config(text="Lỗi tải dữ liệu")
            messagebox.showerror("Lỗi", message)
    
    def _populate_table(self):
        """Populate table with data from data manager"""
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get records
        records = self.data_manager.get_all_records()
        
        # Insert records with appropriate tags
        for idx, record in enumerate(records):
            name, voter_card, national_id, status, timestamp = record
            tag = 'attended' if status == 'Đã điểm danh' else 'not_attended'
            # Add row number (STT) as first column
            record_with_stt = (idx + 1, name, voter_card, national_id, status, timestamp)
            self.tree.insert('', tk.END, values=record_with_stt, tags=(tag,), iid=str(idx))
    
    def _update_statistics(self):
        """Update statistics labels"""
        stats = self.data_manager.get_statistics()
        
        self.lbl_total.config(text=str(stats['total']))
        self.lbl_attended.config(text=str(stats['attended']))
        self.lbl_not_attended.config(text=str(stats['not_attended']))
    
    def _mark_attendance(self):
        """Handle attendance marking"""
        if not self.data_manager.is_loaded():
            messagebox.showwarning("Cảnh báo", "Vui lòng tải file Excel trước")
            return
        
        voter_card = self.entry_voter_card.get().strip()
        
        if not voter_card:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập số thẻ cử tri")
            return
        
        # Mark attendance
        status, full_name = self.data_manager.mark_attendance(voter_card)
        
        if status == 'SUCCESS':
            # Update table
            self._update_table_row(voter_card)
            self._update_statistics()
            
            # Mark as having unsaved changes
            self.has_unsaved_changes = True
            
            # Highlight and scroll to row
            self._highlight_voter_card(voter_card)
            
            # Show success message
            messagebox.showinfo(
                "Thành công",
                f"Điểm danh thành công\n\nHọ và tên: {full_name}"
            )
            
            # Clear input
            self.entry_voter_card.delete(0, tk.END)
            self.entry_voter_card.focus()
            
        elif status == 'ALREADY_ATTENDED':
            messagebox.showinfo(
                "Thông báo",
                f"Cử tri này đã điểm danh rồi\n\nHọ và tên: {full_name}"
            )
            self._highlight_voter_card(voter_card)
            
        else:  # NOT_FOUND
            messagebox.showwarning(
                "Không tìm thấy",
                "Không tìm thấy cử tri với số thẻ này"
            )
    
    def _update_table_row(self, voter_card: str):
        """Update specific row in table after attendance marking"""
        idx = self.data_manager.find_record_index(voter_card)
        if idx is not None:
            # Get updated record
            records = self.data_manager.get_all_records()
            if idx < len(records):
                record = records[idx]
                # Add STT to record
                record_with_stt = (idx + 1,) + record
                # Update treeview item
                item_id = str(idx)
                if self.tree.exists(item_id):
                    self.tree.item(item_id, values=record_with_stt, tags=('attended',))
    
    def _highlight_voter_card(self, voter_card: str):
        """Highlight and scroll to voter card in table"""
        idx = self.data_manager.find_record_index(voter_card)
        if idx is not None:
            item_id = str(idx)
            if self.tree.exists(item_id):
                # Select the item
                self.tree.selection_set(item_id)
                self.tree.focus(item_id)
                # Scroll to make it visible
                self.tree.see(item_id)
    
    def _verify_voter(self):
        """Handle voter verification"""
        if not self.data_manager.is_loaded():
            messagebox.showwarning("Cảnh báo", "Vui lòng tải file Excel trước")
            return
        
        voter_card = self.entry_verify_card.get().strip()
        national_id = self.entry_national_id.get().strip()
        
        if not voter_card or not national_id:
            messagebox.showwarning(
                "Cảnh báo",
                "Vui lòng nhập đầy đủ số thẻ cử tri và số CCCD"
            )
            return
        
        # Verify
        status, full_name = self.data_manager.verify_voter(voter_card, national_id)
        
        if status == 'MATCH':
            messagebox.showinfo(
                "Xác minh thành công",
                f"Thông tin khớp chính xác\n\nHọ và tên: {full_name}"
            )
            self._highlight_voter_card(voter_card)
            
        elif status == 'ID_MISMATCH':
            messagebox.showerror(
                "Xác minh thất bại",
                "Số CCCD không khớp với số thẻ cử tri"
            )
            
        else:  # NOT_FOUND
            messagebox.showwarning(
                "Không tìm thấy",
                "Không tìm thấy cử tri với số thẻ cử tri này"
            )
    
    def _export_excel_file(self):
        """Handle export Excel file"""
        if not self.data_manager.is_loaded():
            messagebox.showwarning("Cảnh báo", "Không có dữ liệu để xuất")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Lưu file Excel",
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        
        if not file_path:
            return
        
        success, message = self.data_manager.export_to_excel(file_path)
        
        if success:
            # Reset unsaved changes flag
            self.has_unsaved_changes = False
            messagebox.showinfo("Thành công", message)
        else:
            messagebox.showerror("Lỗi", message)
    
    def _on_closing(self):
        """Handle window close event with save reminder"""
        # Check if there are unsaved changes
        if self.has_unsaved_changes:
            response = messagebox.askyesnocancel(
                "Cảnh báo",
                "Đã có dữ liệu điểm danh chưa được lưu!\n\n"
                "Bạn có muốn lưu dữ liệu trước khi thoát?\n\n"
                "⚠ Nếu không lưu, dữ liệu điểm danh sẽ bị mất!",
                icon='warning'
            )
            
            if response is None:  # Cancel
                return
            elif response:  # Yes - save first
                self._export_excel_file()
                # Only close if save was successful (user didn't cancel save dialog)
                if not self.has_unsaved_changes:
                    self.root.destroy()
            else:  # No - close without saving
                confirm = messagebox.askokcancel(
                    "Xác nhận",
                    "⚠ Bạn chắc chắn muốn thoát mà KHÔNG lưu?\n\n"
                    "Tất cả dữ liệu điểm danh sẽ bị mất!",
                    icon='warning'
                )
                if confirm:
                    self.root.destroy()
        else:
            # No unsaved changes, just close
            self.root.destroy()
