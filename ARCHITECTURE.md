# Architecture Documentation
# Voter Attendance Desktop Application

## 📐 System Architecture Overview

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User Interface Layer                     │
│                         (ui.py)                              │
│  - Tkinter GUI Components                                    │
│  - Event Handlers                                            │
│  - User Input Validation                                     │
└──────────────────────┬───────────────────────────────────────┘
                       │
                       │ API Calls
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   Business Logic Layer                       │
│                    (data_manager.py)                         │
│  - Data Loading & Validation                                 │
│  - O(1) Hash Map Indexing                                    │
│  - Attendance Tracking                                       │
│  - Verification Logic                                        │
└──────────────────────┬───────────────────────────────────────┘
                       │
                       │ pandas + openpyxl
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                      Data Layer                              │
│                   (Excel Files)                              │
│  - Input: Voter Registry (.xlsx)                            │
│  - Output: Attendance Records (.xlsx)                        │
└─────────────────────────────────────────────────────────────┘
```

### Application Entry Point

```
main.py
├── Initialize Tkinter root window
├── Create DataManager instance
├── Create VoterAttendanceUI instance
└── Start main event loop
```

---

## 🧩 Component Design

### 1. Data Manager (`data_manager.py`)

**Purpose:** Core business logic and data operations

**Key Features:**
- **O(1) Lookup Performance**: Uses hash map (dict) indexed by voter card number
- **Memory Efficient**: Loads only required columns
- **Data Validation**: Ensures required columns exist
- **String Normalization**: Trims whitespace, handles NaN values

**Data Structure:**
```python
DataManager {
    df: DataFrame              # Pandas DataFrame holding all records
    voter_card_index: Dict     # {voter_card_number: dataframe_index}
    required_columns: List     # Column name validation
}
```

**Performance Characteristics:**
- Load: O(n) - must read all records once
- Search: O(1) - hash map lookup
- Update: O(1) - direct index access
- Export: O(n) - must write all records

**Methods:**
```python
load_excel(file_path)          # Load and validate Excel data
mark_attendance(voter_card)    # O(1) attendance marking
verify_voter(card, id)         # O(1) identity verification
get_all_records()              # Return display data
get_statistics()               # Calculate attendance stats
export_to_excel(file_path)     # Save updated data
```

---

### 2. User Interface (`ui.py`)

**Purpose:** Tkinter-based GUI for user interaction

**Layout Structure:**
```
Main Window (1200x700)
├── Top Frame
│   ├── Load Excel Button
│   ├── Export Excel Button
│   └── File Info Label
├── Left Frame (Table)
│   ├── Label: "Danh sách cử tri"
│   └── Treeview with scrollbars
│       ├── Column: Họ và tên
│       ├── Column: Số thẻ cử tri
│       ├── Column: Số CCCD
│       └── Column: Trạng thái
└── Right Frame
    ├── Input Section
    │   ├── Voter Card Entry (Enter key bound)
    │   ├── National ID Entry
    │   └── Verify Button
    ├── Statistics Section
    │   ├── Total Voters
    │   ├── Attended Count
    │   └── Not Attended Count
    └── Instructions Section
```

**UI Components:**

| Component | Purpose | Optimization |
|-----------|---------|--------------|
| Treeview | Display 5k-20k records | Virtual scrolling (only renders visible rows) |
| Entry Fields | User input | Direct keyboard binding for speed |
| Buttons | Actions | State management (disabled when no data) |
| Labels | Statistics | Real-time updates on attendance changes |

**Event Flow:**
```
User Action → Event Handler → DataManager API → Update UI
                                              → Show Feedback
```

---

### 3. Main Entry Point (`main.py`)

**Purpose:** Application initialization and error handling

**Responsibilities:**
- Create Tkinter root window
- Initialize DataManager
- Initialize UI with dependencies
- Global exception handling
- Start main event loop

---

## 🔄 Data Flow

### Loading Excel File
```
User clicks "Load Excel"
    ↓
FileDialog opens → User selects file
    ↓
DataManager.load_excel(path)
    ↓
Pandas reads Excel → Validate columns → Clean data
    ↓
Build hash map index {voter_card: index}
    ↓
UI.populate_table() → Display all records
    ↓
UI.update_statistics() → Show counts
```

### Marking Attendance
```
User enters voter card + presses Enter
    ↓
UI._mark_attendance() → Validate input
    ↓
DataManager.mark_attendance(card)
    ↓
Hash map lookup O(1) → Find record index
    ↓
Check current status:
    - Not Attended → Mark as Attended → Return SUCCESS
    - Already Attended → Return ALREADY_ATTENDED
    - Not Found → Return NOT_FOUND
    ↓
UI updates:
    - Update table row styling
    - Highlight and scroll to record
    - Update statistics
    - Show message box
    - Clear input field
```

### Verification Flow
```
User enters voter card + national ID + clicks Verify
    ↓
UI._verify_voter() → Validate inputs
    ↓
DataManager.verify_voter(card, id)
    ↓
Hash map lookup O(1) → Find record
    ↓
Compare national IDs:
    - Match → Return MATCH
    - Mismatch → Return ID_MISMATCH
    - Not Found → Return NOT_FOUND
    ↓
UI shows appropriate message box
```

---

## 🚀 Performance Optimizations

### 1. Hash Map Indexing
```python
# Build once on load: O(n)
voter_card_index = {row['Số thẻ cử tri']: idx for idx, row in df.iterrows()}

# Lookup: O(1)
idx = voter_card_index.get(voter_card_number)
```

**Benefits:**
- Eliminates linear search O(n) for every lookup
- Critical for 20,000 records: 20,000 comparisons → 1 lookup

### 2. Treeview Virtual Scrolling
Tkinter Treeview automatically renders only visible rows, not all 20,000 at once.

### 3. Selective Column Loading
```python
# Only load required columns, not entire Excel sheet
df = pd.read_excel(file_path)[required_columns]
```

### 4. In-Place Updates
```python
# Direct index access instead of searching
df.at[idx, 'Trạng thái'] = 'Đã điểm danh'
```

### 5. Batch Statistics Calculation
```python
# Vectorized pandas operation, not row-by-row
attended = len(df[df['Trạng thái'] == 'Đã điểm danh'])
```

---

## 🔒 Security Architecture

### Data Protection Layers

1. **Application Level**
   - No network connectivity
   - No external API calls
   - All processing in-memory

2. **File Level**
   - Support for password-protected Excel files (openpyxl)
   - Local storage only
   - No cloud sync

3. **System Level** (Deployment Recommendations)
   - Windows BitLocker encryption
   - User access controls
   - Physical security measures

### Sensitive Data Handling

```python
# Data is never logged or cached
# Voter information stays in memory only during session
# No persistent storage except explicit export
```

---

## 📦 Deployment Architecture

### PyInstaller Build Process

```
Source Code (.py files)
    ↓
PyInstaller Analysis
    ↓
Collect Dependencies:
    - Python interpreter
    - pandas, openpyxl
    - Tkinter (bundled with Python)
    ↓
Bundle into single executable
    ↓
Output: VoterAttendance.exe (single file)
```

**Bundle Contents:**
- Python 3.9+ runtime
- All required libraries
- Application code
- No external dependencies needed

---

## 🧪 Testing Strategy

### Unit Testing Approach
```python
# Test data_manager.py
- test_load_valid_excel()
- test_load_missing_columns()
- test_mark_attendance_success()
- test_mark_attendance_duplicate()
- test_verify_voter_match()
- test_verify_voter_mismatch()

# Test ui.py
- test_ui_initialization()
- test_table_population()
- test_statistics_update()
```

### Performance Testing
```python
# Test with various dataset sizes
test_5000_records()   # Load time < 2s
test_10000_records()  # Load time < 4s
test_20000_records()  # Load time < 8s
```

### Integration Testing
```python
# End-to-end workflows
test_complete_attendance_workflow()
test_export_after_attendance()
test_verification_workflow()
```

---

## 🔧 Extension Points

### Future Enhancements

1. **Database Backend**
```python
# Replace pandas DataFrame with SQLite
class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
    
    # Much faster for >20,000 records
```

2. **Biometric Integration**
```python
# Add fingerprint verification
def verify_biometric(voter_card, fingerprint_data):
    # Integration with fingerprint scanner
    pass
```

3. **Network Sync** (Optional)
```python
# Multi-station synchronization
def sync_attendance_data(stations):
    # Merge attendance from multiple stations
    pass
```

4. **Audit Logging**
```python
# Track all operations
def log_operation(action, user, timestamp, details):
    # Write to audit log file
    pass
```

---

## 📊 Scalability Considerations

| Records | Current Architecture | SQLite Alternative |
|---------|---------------------|-------------------|
| < 5,000 | ✅ Excellent | Overkill |
| 5k - 20k | ✅ Good | ✅ Better |
| > 20k | ⚠️ Slower load | ✅ Recommended |

**Recommendation:** Current architecture is optimal for specified range (5,000-20,000 records).

---

## 🛠️ Development Environment

### Required Tools
- Python 3.9+
- pip (package manager)
- Code editor (VS Code recommended)
- Windows 10/11

### Development Workflow
```
1. Edit source files
2. Test with: python main.py
3. Generate sample data: python generate_sample_data.py
4. Build EXE: pyinstaller --onefile --windowed main.py
5. Test EXE in dist/ folder
```

---

## 📝 Code Quality Standards

### Style Guide
- PEP 8 compliance
- Type hints for function signatures
- Comprehensive docstrings
- Clear variable names

### Documentation
- Module-level docstrings
- Function-level docstrings
- Inline comments for complex logic
- README and BUILD_GUIDE for users

### Error Handling
```python
# Always provide user-friendly error messages
try:
    # operation
except SpecificException as e:
    return False, f"User-friendly message: {str(e)}"
```

---

## 🔍 Monitoring & Diagnostics

### Built-in Diagnostics
- File info label shows load status
- Statistics provide real-time feedback
- Message boxes confirm all operations
- Treeview highlighting shows current selection

### Debugging Tips
```powershell
# Run without --windowed to see console output
pyinstaller --onefile main.py

# Console shows:
# - Exception traces
# - pandas warnings
# - File operation status
```

---

**Document Version:** 1.0.0  
**Last Updated:** March 5, 2026  
**Architecture Pattern:** Model-View (MV) with Data Manager  
**Primary Language:** Python 3.9+  
**UI Framework:** Tkinter (stdlib)  
**Data Processing:** pandas + openpyxl
