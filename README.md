# Voter Attendance Desktop Application

A lightweight, fully offline Windows desktop application for tracking voter attendance at polling stations. Built with Python and Tkinter for optimal performance on low-spec computers.

## ✨ Features

- **Fully Offline**: No internet or server connection required
- **Fast Performance**: Handles 5,000-20,000 voter records efficiently
- **Simple UI**: Clean interface designed for non-technical users
- **Quick Check-in**: Enter voter card number and press Enter
- **Identity Verification**: Cross-check voter card with national ID
- **Real-time Statistics**: Track attendance counts instantly
- **Excel Integration**: Import and export voter data
- **Portable EXE**: Single executable file for easy deployment

## 🏗️ Architecture

```
voter-checkin-app/
├── main.py              # Application entry point
├── data_manager.py      # Data operations (O(1) lookup with hash maps)
├── ui.py                # Tkinter user interface
├── requirements.txt     # Python dependencies
├── BUILD_GUIDE.md       # Complete build and deployment guide
└── generate_sample_data.py  # Sample data generator for testing
```

### Design Principles

1. **Performance First**: Hash map indexing for O(1) voter lookup
2. **Memory Efficient**: Loads only required columns from Excel
3. **Error Resilient**: Comprehensive exception handling
4. **User-Friendly**: Vietnamese interface with clear feedback

## 🚀 Quick Start

### Installation

```powershell
# Install dependencies
pip install -r requirements.txt
```

### Run Application

```powershell
python main.py
```

### Generate Sample Data

```powershell
python generate_sample_data.py
```

This creates test files:
- `sample_voters_100.xlsx` (100 records)
- `sample_voters_1000.xlsx` (1,000 records)
- `sample_voters_5000.xlsx` (5,000 records)

## 📋 Usage Guide

### 1. Load Voter Data
- Click **"Tải file Excel"** (Load Excel File)
- Select Excel file with required columns:
  - `Họ và tên` (Full Name)
  - `Số thẻ cử tri` (Voter Card Number)
  - `Số CCCD` (National ID)

### 2. Mark Attendance
- Enter voter card number in input field
- Press **Enter** key
- System will:
  - ✅ Mark voter as attended (if not already)
  - ⚠️ Alert if already checked in
  - ❌ Warn if voter not found

### 3. Verify Identity (Optional)
- Enter both voter card number AND national ID
- Click **"Xác minh thông tin"** (Verify)
- System validates both identifiers match

### 4. Export Results
- Click **"Xuất file Excel"** (Export Excel)
- Save updated file with attendance status

## 🔧 Building EXE

### Basic Build

```powershell
pyinstaller --onefile --windowed main.py
```

### Production Build

```powershell
pyinstaller --onefile --windowed --name "VoterAttendance" --icon=app.ico main.py
```

Output: `dist/VoterAttendance.exe`

**See [BUILD_GUIDE.md](BUILD_GUIDE.md) for complete build instructions**

## 📦 Dependencies

- **Python 3.9+**
- **pandas** - Excel file processing
- **openpyxl** - Excel read/write engine
- **pyinstaller** - EXE compilation

## 🎨 User Interface

```
┌─────────────────────────────────────────────────────────────┐
│ [Tải file Excel]  [Xuất file Excel]  | Loaded: 5,000 voters │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Danh sách cử tri                  │ Điểm danh & Xác minh   │
│  ┌────────────────────────────────┐│ ┌────────────────────┐ │
│  │ Họ và tên    │ Số thẻ │ Trạng  ││ │ Số thẻ cử tri:     │ │
│  │──────────────┼────────┼────────││ │ [____________]     │ │
│  │ Nguyễn Văn A │ 1234.. │ Đã...  ││ │                    │ │
│  │ Trần Thị B   │ 5678.. │ Chưa.. ││ │ Số CCCD:           │ │
│  │ ...          │ ...    │ ...    ││ │ [____________]     │ │
│  └────────────────────────────────┘│ │                    │ │
│                                     │ │ [Xác minh]         │ │
│                                     │ └────────────────────┘ │
│                                     │ Thống kê              │
│                                     │ Tổng: 5,000           │
│                                     │ Đã điểm danh: 1,234   │
│                                     │ Chưa điểm danh: 3,766 │
└─────────────────────────────────────────────────────────────┘
```

## 🔒 Security Recommendations

### Data Protection
- ✅ Run on air-gapped (offline) computers
- ✅ Use Windows BitLocker for full disk encryption
- ✅ Password-protect Excel files
- ✅ Implement physical access controls
- ✅ Delete data after election completion

### Best Practices
- Keep application on dedicated voting computers
- Use local storage only (no cloud/network drives)
- Maintain audit logs of file access
- Regularly update dependencies for security patches

## ⚡ Performance Characteristics

| Records | Load Time | Lookup Time | Memory Usage |
|---------|-----------|-------------|--------------|
| 5,000   | ~1s       | < 1ms       | ~50 MB       |
| 10,000  | ~2s       | < 1ms       | ~80 MB       |
| 20,000  | ~4s       | < 1ms       | ~150 MB      |

*Tested on: Intel i5, 8GB RAM, Windows 10*

## 🐛 Troubleshooting

### Application won't start
- Verify Python 3.9+ is installed
- Run: `pip install -r requirements.txt`
- Check for error messages in terminal

### Excel file won't load
- Ensure file has required columns (exact names)
- Check file isn't open in another program
- Verify file format is `.xlsx`

### EXE build fails
- Update PyInstaller: `pip install --upgrade pyinstaller`
- Add hidden imports (see BUILD_GUIDE.md)
- Try clean build: delete `build/`, `dist/`, `*.spec`

## 📄 License

This application is provided as-is for election management purposes. Ensure compliance with local data protection and election laws.

## 🤝 Contributing

Suggested enhancements:
- SQLite integration for >20,000 records
- Biometric integration support
- Multi-station data synchronization
- Printable attendance reports
- Audit trail logging

## 📞 Support

For technical issues:
1. Check BUILD_GUIDE.md troubleshooting section
2. Verify all dependencies are installed
3. Test with sample data files
4. Review error logs in `build/` folder

---

**Version:** 1.0.0  
**Last Updated:** March 5, 2026  
**Platform:** Windows 10/11  
**Language:** Vietnamese (UI), English (Code)
