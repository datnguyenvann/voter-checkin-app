"""
Voter Attendance Desktop Application
Main entry point for the application

A lightweight, offline desktop application for voter attendance tracking
Built with Python and Tkinter for Windows deployment
"""

import tkinter as tk
from tkinter import messagebox
import sys
from data_manager import DataManager
from ui import VoterAttendanceUI


def main():
    """
    Main application entry point
    """
    try:
        # Create root window
        root = tk.Tk()
        
        # Initialize data manager
        data_manager = DataManager()
        
        # Create UI
        app = VoterAttendanceUI(root, data_manager)
        
        # Start application
        root.mainloop()
        
    except Exception as e:
        messagebox.showerror(
            "Lỗi khởi động",
            f"Không thể khởi động ứng dụng:\n{str(e)}"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
