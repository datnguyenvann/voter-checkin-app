# Installation Script for Voter Attendance Application
# Run this script to set up the development environment

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Voter Attendance App - Installation" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python installation
Write-Host "[1/4] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green
    
    # Check if version is 3.9+
    if ($pythonVersion -match "Python 3\.(\d+)") {
        $minorVersion = [int]$matches[1]
        if ($minorVersion -lt 9) {
            Write-Host "⚠ Warning: Python 3.9+ recommended (you have $pythonVersion)" -ForegroundColor Yellow
        }
    }
} catch {
    Write-Host "✗ Python not found. Please install Python 3.9+ from python.org" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Check pip
Write-Host "[2/4] Checking pip..." -ForegroundColor Yellow
try {
    $pipVersion = pip --version 2>&1
    Write-Host "✓ Found: $pipVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ pip not found. Please reinstall Python with pip" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Install dependencies
Write-Host "[3/4] Installing dependencies..." -ForegroundColor Yellow
Write-Host "This may take a few minutes..." -ForegroundColor Gray

try {
    pip install -r requirements.txt --quiet
    Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
} catch {
    Write-Host "✗ Failed to install dependencies" -ForegroundColor Red
    Write-Host "Try running manually: pip install -r requirements.txt" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Verify installation
Write-Host "[4/4] Verifying installation..." -ForegroundColor Yellow

$allGood = $true

# Check pandas
try {
    python -c "import pandas" 2>&1 | Out-Null
    Write-Host "✓ pandas installed" -ForegroundColor Green
} catch {
    Write-Host "✗ pandas not installed" -ForegroundColor Red
    $allGood = $false
}

# Check openpyxl
try {
    python -c "import openpyxl" 2>&1 | Out-Null
    Write-Host "✓ openpyxl installed" -ForegroundColor Green
} catch {
    Write-Host "✗ openpyxl not installed" -ForegroundColor Red
    $allGood = $false
}

# Check pyinstaller
try {
    python -c "import PyInstaller" 2>&1 | Out-Null
    Write-Host "✓ pyinstaller installed" -ForegroundColor Green
} catch {
    Write-Host "✗ pyinstaller not installed" -ForegroundColor Red
    $allGood = $false
}

Write-Host ""

if ($allGood) {
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "✓ Installation Complete!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Yellow
    Write-Host "  1. Run application: python main.py" -ForegroundColor White
    Write-Host "  2. Generate sample data: python generate_sample_data.py" -ForegroundColor White
    Write-Host "  3. Build EXE: pyinstaller --onefile --windowed main.py" -ForegroundColor White
    Write-Host ""
    Write-Host "Documentation:" -ForegroundColor Yellow
    Write-Host "  - PROJECT_SUMMARY.md : Complete overview" -ForegroundColor White
    Write-Host "  - BUILD_GUIDE.md     : Build instructions" -ForegroundColor White
    Write-Host "  - USER_GUIDE_VI.md   : Vietnamese user guide" -ForegroundColor White
    Write-Host "  - ARCHITECTURE.md    : Technical details" -ForegroundColor White
} else {
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "✗ Installation incomplete" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please run manually:" -ForegroundColor Yellow
    Write-Host "  pip install -r requirements.txt" -ForegroundColor White
    exit 1
}
