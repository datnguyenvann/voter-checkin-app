# Release Notes - Voter Attendance Application

## Version 2.0 - March 5, 2026

### 🎉 New Features

#### Real-time Timestamp Tracking
- **Automatic Time Recording**: Every attendance check-in is now automatically timestamped
- **Format**: `YYYY-MM-DD HH:MM:SS` (e.g., "2026-03-05 09:38:39")
- **Display**: New column "Thời gian điểm danh" (Check-in Time) in the main table
- **Export Support**: Timestamps are included when exporting to Excel
- **Audit Trail**: Provides complete audit trail for election compliance

### ✨ Benefits

1. **Compliance**: Meets election regulations requiring time-stamped attendance records
2. **Transparency**: Clear documentation of when each voter checked in
3. **Security**: Prevents backdating or time manipulation of attendance records
4. **Analytics**: Enables analysis of voter turnout patterns by time of day

### 🔧 Technical Details

- Timestamp captured using system time at moment of check-in
- Stored in DataFrame alongside voter information
- Visible in 6th column of the main table
- Exported to Excel in "Thời gian điểm danh" column
- Empty for voters who haven't checked in yet

### 📊 Updated Table Structure

The main table now displays 6 columns:

1. **STT**: Row number
2. **Họ và tên**: Full name
3. **Số thẻ cử tri**: Voter card number
4. **Số CCCD**: National ID number
5. **Trạng thái**: Status (Đã điểm danh / Chưa điểm danh)
6. **Thời gian điểm danh**: Check-in timestamp (NEW!)

### 💾 File Information

- **Executable**: `VoterAttendance.exe`
- **Size**: ~104.5 MB (109,558,600 bytes)
- **Build Date**: March 5, 2026
- **Location**: `dist\VoterAttendance.exe`

### 🚀 How to Use

1. **Load Excel file** with voter data
2. **Enter voter card number** in the quick check-in field
3. **Press Enter** to mark attendance
4. **View timestamp** in the new column showing exact check-in time
5. **Export to Excel** to save records with timestamps

### ⚠️ Important Notes

- Timestamps are recorded only when attendance is marked
- Empty timestamp field indicates voter has not checked in
- System time must be accurate for reliable timestamps
- Exported Excel files will include the timestamp column

### 🔄 Upgrade Instructions

Simply replace your old `VoterAttendance.exe` with the new version. No data migration needed.

### 🐛 Bug Fixes

No bugs fixed in this release (new feature release only).

---

## Version 1.0 - Initial Release

### Core Features

- Fully offline operation
- Fast Excel data loading
- O(1) attendance marking with hash map indexing
- Identity verification (voter card + national ID)
- Real-time statistics
- Export to Excel
- Clean Vietnamese UI
- Standalone EXE (104 MB)

### Performance

- Handles 5,000-20,000 voter records efficiently
- Instant lookup with hash map indexing
- Optimized for low-spec computers

---

For questions or support, refer to the documentation files:
- `README.md` - Project overview
- `USER_GUIDE_VI.md` - Vietnamese user guide
- `BUILD_GUIDE.md` - Build and deployment instructions
- `ARCHITECTURE.md` - Technical architecture details
