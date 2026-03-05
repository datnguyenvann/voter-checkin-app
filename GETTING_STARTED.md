# 🚀 GETTING STARTED - Quick Setup Guide

## For First-Time Users

This guide will get you from zero to running application in **5 minutes**.

---

## ⚡ Fast Track (3 Steps)

### 1️⃣ Install Python
- Download: https://www.python.org/downloads/
- ✅ Check "Add Python to PATH" during installation
- Click "Install Now"

### 2️⃣ Install Dependencies
Open PowerShell in this folder and run:
```powershell
.\install.ps1
```

OR manually:
```powershell
pip install -r requirements.txt
```

### 3️⃣ Run Application
```powershell
python main.py
```

**🎉 Done! The application should now be running.**

---

## 📋 Step-by-Step Instructions

### Prerequisites Check

Open PowerShell and verify:

```powershell
# Check Python (should be 3.9+)
python --version

# Check pip
pip --version
```

If both work, you're good to go! ✅

### Installation Options

**Option A: Automated (Recommended)**
```powershell
.\install.ps1
```
This script checks everything and installs dependencies automatically.

**Option B: Manual**
```powershell
pip install pandas openpyxl pyinstaller
```

### Running the Application

**Development Mode:**
```powershell
python main.py
```
Launches the GUI application for testing and use.

**Generate Sample Data:**
```powershell
python generate_sample_data.py
```
Creates test Excel files with fake voter data.

---

## 🏗️ Building EXE (Optional)

### Quick Build
```powershell
.\build.ps1
```
Creates `dist\VoterAttendance.exe`

### Manual Build
```powershell
pyinstaller --onefile --windowed --name VoterAttendance main.py
```

### Find Your EXE
```
voter-checkin-app/
└── dist/
    └── VoterAttendance.exe  ← Here!
```

---

## 🎯 First Use Tutorial

### Step 1: Launch Application
- Double-click `main.py` or run `python main.py`
- Application window opens

### Step 2: Generate Test Data
In PowerShell:
```powershell
python generate_sample_data.py
```
This creates `sample_voters_100.xlsx`

### Step 3: Load Data
- Click **"Tải file Excel"** button
- Select `sample_voters_100.xlsx`
- See 100 voters loaded in table

### Step 4: Mark Attendance
- Enter a voter card number from the table (e.g., any 8-digit number shown)
- Press **Enter** key
- See confirmation popup
- Notice row turns green

### Step 5: Export Results
- Click **"Xuất file Excel"** button
- Save as `output.xlsx`
- Open in Excel to see attendance column

**🎉 You've completed the full workflow!**

---

## 📖 Documentation Reference

| Document | Purpose | When to Read |
|----------|---------|--------------|
| **PROJECT_SUMMARY.md** | Complete overview | Start here |
| **README.md** | Project introduction | Quick reference |
| **BUILD_GUIDE.md** | EXE building steps | Before deployment |
| **USER_GUIDE_VI.md** | Vietnamese user guide | For operators |
| **ARCHITECTURE.md** | Technical details | For developers |

---

## 🧪 Testing Your Setup

### Quick Test Checklist

- [ ] Python 3.9+ installed
- [ ] Dependencies installed (pandas, openpyxl)
- [ ] `python main.py` launches GUI
- [ ] Can load sample Excel file
- [ ] Can mark attendance
- [ ] Can export results
- [ ] EXE builds successfully (if building)

### Sample Test Data

After running `generate_sample_data.py`, you'll have:

| File | Records | Use Case |
|------|---------|----------|
| sample_voters_100.xlsx | 100 | Quick testing |
| sample_voters_1000.xlsx | 1,000 | Medium testing |
| sample_voters_5000.xlsx | 5,000 | Performance testing |

---

## 🐛 Common First-Time Issues

### Issue: "python is not recognized"
**Cause:** Python not in PATH
**Fix:** Reinstall Python, ensure "Add to PATH" is checked

### Issue: "No module named 'pandas'"
**Cause:** Dependencies not installed
**Fix:** Run `pip install -r requirements.txt`

### Issue: "Missing required columns"
**Cause:** Excel file doesn't have required Vietnamese column names
**Fix:** Use sample data files or ensure your Excel has:
- Họ và tên
- Số thẻ cử tri
- Số CCCD

### Issue: Application window blank
**Cause:** Tkinter issue
**Fix:** Restart application, check Python version

---

## 💡 Tips for New Users

### Speed Tips
- Use **Enter key** instead of clicking buttons
- Input field auto-clears after each attendance
- Table auto-scrolls to highlight marked voter

### Data Preparation
- Prepare Excel file before election day
- Test with sample data first
- Verify column names are exact (case-sensitive, with Vietnamese diacritics)

### Performance
- Application handles 20,000 records smoothly
- Load time: ~4 seconds for 20,000 voters
- Lookup time: < 1 millisecond (instant)

---

## 🎓 Learning Path

### Beginner
1. Run `python main.py`
2. Load sample data
3. Try marking attendance
4. Export results

### Intermediate
1. Generate custom sample data
2. Test verification feature
3. Try with larger datasets (5,000+ records)
4. Build EXE file

### Advanced
1. Read ARCHITECTURE.md
2. Understand O(1) hash map indexing
3. Modify UI or add features
4. Implement security enhancements

---

## 🔧 Development Workflow

```
1. Edit code in ui.py or data_manager.py
2. Run: python main.py
3. Test changes
4. Repeat until satisfied
5. Build: .\build.ps1
6. Test EXE
7. Deploy
```

---

## 📞 Need Help?

### Quick Fixes
1. Restart application
2. Check Python version (`python --version`)
3. Reinstall dependencies (`pip install -r requirements.txt`)
4. Read error messages carefully

### Documentation
- **User questions:** USER_GUIDE_VI.md
- **Build problems:** BUILD_GUIDE.md
- **Technical questions:** ARCHITECTURE.md
- **General overview:** PROJECT_SUMMARY.md

---

## ✅ You're Ready When...

- [ ] Can launch application (`python main.py` works)
- [ ] Can load Excel file (sample data loads successfully)
- [ ] Can mark attendance (Enter key marks voter)
- [ ] Can export results (creates new Excel file)
- [ ] Understand Vietnamese column names requirement
- [ ] Know how to generate test data

---

## 🚀 Next Steps

**For Development:**
- Read ARCHITECTURE.md to understand code structure
- Experiment with sample data
- Try building EXE

**For Deployment:**
- Read BUILD_GUIDE.md
- Build production EXE
- Test on computer without Python
- Read security recommendations

**For Operation:**
- Share USER_GUIDE_VI.md with operators
- Prepare real voter data Excel file
- Conduct training session
- Plan election day workflow

---

## 🎯 Success Checklist

After following this guide, you should have:

✅ Python environment set up
✅ All dependencies installed
✅ Application running successfully
✅ Sample data generated
✅ Tested full workflow
✅ Understanding of basic operations
✅ Knowledge of where to find help

**Congratulations! You're ready to use the Voter Attendance Application!** 🎉

---

**Estimated setup time:** 5-10 minutes  
**Skill level required:** Basic (can use PowerShell)  
**Support:** See documentation files in project folder
