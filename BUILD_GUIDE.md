# Build Guide - Voter Attendance Desktop App

## 📋 Table of Contents
1. [Installation](#installation)
2. [Running in Development](#running-in-development)
3. [Building EXE](#building-exe)
4. [Advanced Build Options](#advanced-build-options)
5. [Testing the Release](#testing-the-release)
6. [Troubleshooting](#troubleshooting)
7. [Security Recommendations](#security-recommendations)

---

## 🔧 Installation

### Step 1: Install Python
- Download Python 3.9+ from [python.org](https://www.python.org/downloads/)
- During installation, **check "Add Python to PATH"**
- Verify installation:
  ```powershell
  python --version
  ```

### Step 2: Install Dependencies
Open PowerShell in the project directory and run:

```powershell
pip install -r requirements.txt
```

Or install packages individually:
```powershell
pip install pandas openpyxl pyinstaller
```

---

## 🚀 Running in Development

To test the application before building:

```powershell
python main.py
```

This will launch the GUI application for testing.

---

## 📦 Building EXE

### Basic Build (Single EXE File)

```powershell
pyinstaller --onefile --windowed main.py
```

**Explanation:**
- `--onefile`: Creates a single executable file
- `--windowed`: Hides the console window (GUI only)
- `main.py`: Entry point of the application

**Output:** `dist/main.exe`

### Build with Custom Name

```powershell
pyinstaller --onefile --windowed --name "VoterAttendance" main.py
```

**Output:** `dist/VoterAttendance.exe`

### Build with Custom Icon

First, create or download an `.ico` file (e.g., `app.ico`), then:

```powershell
pyinstaller --onefile --windowed --icon=app.ico --name "VoterAttendance" main.py
```

---

## 🎯 Advanced Build Options

### Complete Build with All Options

```powershell
pyinstaller --onefile `
  --windowed `
  --name "VoterAttendance" `
  --icon=app.ico `
  --add-data "README.md;." `
  --hidden-import=openpyxl `
  --hidden-import=pandas `
  main.py
```

### Handling Hidden Imports

If the EXE fails to run due to missing modules, add them explicitly:

```powershell
pyinstaller --onefile --windowed `
  --hidden-import=openpyxl.cell `
  --hidden-import=openpyxl.styles `
  --hidden-import=pandas._libs `
  main.py
```

### Clean Build (Remove Previous Build Files)

```powershell
# Remove old build files
Remove-Item -Recurse -Force build, dist
Remove-Item *.spec

# Build fresh
pyinstaller --onefile --windowed --name "VoterAttendance" main.py
```

---

## ✅ Testing the Release

### Step 1: Locate the EXE
After building, find your executable in:
```
dist/VoterAttendance.exe
```

### Step 2: Test on Development Machine
1. Navigate to `dist` folder
2. Double-click `VoterAttendance.exe`
3. Test all features:
   - Load Excel file
   - Mark attendance
   - Verify voter
   - Export Excel

### Step 3: Test on Clean Machine (Recommended)
1. Copy `VoterAttendance.exe` to a computer **without Python installed**
2. Run the executable
3. Verify all functionality works

### Step 4: Create Distribution Package
Create a release folder with everything needed:

```
VoterAttendance_Release/
├── VoterAttendance.exe
├── README.txt (user instructions)
└── sample_data.xlsx (optional sample file)
```

---

## 🛠️ Troubleshooting

### Issue: "Failed to execute script main"

**Solution 1:** Add hidden imports
```powershell
pyinstaller --onefile --windowed `
  --hidden-import=openpyxl `
  --hidden-import=pandas `
  main.py
```

**Solution 2:** Use non-windowed mode temporarily to see error
```powershell
pyinstaller --onefile main.py
```
Run the EXE in terminal to see error messages.

### Issue: Large EXE File Size

**Solution:** Use UPX compression (optional)
1. Download UPX from [upx.github.io](https://upx.github.io/)
2. Extract to a folder (e.g., `C:\upx`)
3. Build with UPX:
```powershell
pyinstaller --onefile --windowed --upx-dir="C:\upx" main.py
```

### Issue: Antivirus Flags EXE as Malware

This is common with PyInstaller. **Solutions:**
1. Add exclusion in Windows Defender
2. Submit false positive report to antivirus vendor
3. Sign the executable with a code signing certificate (enterprise)

### Issue: Missing DLL Errors

**Solution:** Include runtime dependencies
```powershell
pyinstaller --onefile --windowed `
  --collect-all openpyxl `
  --collect-all pandas `
  main.py
```

---

## 🔒 Security Recommendations

### Protecting Sensitive Voter Data

1. **File Encryption**
   - Use encrypted Excel files (password-protected)
   - Decrypt only in memory during processing

2. **Access Control**
   - Run application on dedicated, secured computers
   - Use Windows user account restrictions
   - Enable Windows BitLocker for full disk encryption

3. **Data Handling Best Practices**
   - **Never** store voter data on cloud storage
   - Use local storage only
   - Delete exported files after transfer to secure archive
   - Implement audit logging (optional enhancement)

4. **Physical Security**
   - Keep computers in locked rooms
   - Monitor access to voting stations
   - Use privacy screens

5. **Software Updates**
   - Keep Windows updated
   - Update application dependencies regularly:
     ```powershell
     pip install --upgrade pandas openpyxl
     ```

### Optional: Add Basic Encryption

To add password protection to exported files:

```python
# In data_manager.py export_to_excel method
from openpyxl import load_workbook
from openpyxl.workbook.protection import WorkbookProtection

# After saving
wb = load_workbook(file_path)
wb.security = WorkbookProtection(workbookPassword='your_password')
wb.save(file_path)
```

---

## 📝 Quick Reference Commands

### Install Dependencies
```powershell
pip install -r requirements.txt
```

### Run Development
```powershell
python main.py
```

### Build Basic EXE
```powershell
pyinstaller --onefile --windowed main.py
```

### Build Production EXE
```powershell
pyinstaller --onefile --windowed --name "VoterAttendance" --icon=app.ico main.py
```

### Clean Build
```powershell
Remove-Item -Recurse -Force build, dist; Remove-Item *.spec
pyinstaller --onefile --windowed --name "VoterAttendance" main.py
```

---

## 📞 Support

For issues during build or deployment:
1. Check the `build/` folder for build logs
2. Run in non-windowed mode to see console errors
3. Verify all dependencies are installed
4. Test on a clean Windows machine

---

## ✨ Additional Enhancements (Optional)

### Auto-Update Check
Add version checking to notify users of updates

### Database Integration
Replace Excel with SQLite for better performance (>20,000 records)

### Backup Feature
Automatic periodic backups of attendance data

### Multi-Language Support
Add language selection for Vietnamese/English

### Print Support
Generate printable attendance reports

---

**Build Date:** 2026-03-05  
**Version:** 1.0.0  
**Platform:** Windows 10/11  
**Python:** 3.9+
