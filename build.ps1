# Build Script for Voter Attendance Application
# Creates standalone EXE file for distribution

param(
    [string]$BuildType = "production",
    [string]$IconPath = ""
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Voter Attendance App - Build Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if PyInstaller is installed
Write-Host "Checking PyInstaller..." -ForegroundColor Yellow
try {
    pyinstaller --version | Out-Null
    Write-Host "✓ PyInstaller found" -ForegroundColor Green
} catch {
    Write-Host "✗ PyInstaller not installed" -ForegroundColor Red
    Write-Host "Run: pip install pyinstaller" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Clean previous builds
Write-Host "Cleaning previous builds..." -ForegroundColor Yellow
if (Test-Path "build") {
    Remove-Item -Recurse -Force "build"
    Write-Host "✓ Removed build/ folder" -ForegroundColor Green
}
if (Test-Path "dist") {
    Remove-Item -Recurse -Force "dist"
    Write-Host "✓ Removed dist/ folder" -ForegroundColor Green
}
if (Test-Path "*.spec") {
    Remove-Item -Force "*.spec"
    Write-Host "✓ Removed .spec files" -ForegroundColor Green
}

Write-Host ""

# Build command
$buildCmd = "pyinstaller --onefile --windowed --name VoterAttendance"

if ($IconPath -and (Test-Path $IconPath)) {
    $buildCmd += " --icon=$IconPath"
    Write-Host "Using custom icon: $IconPath" -ForegroundColor Cyan
}

# Add hidden imports for better compatibility
$buildCmd += " --hidden-import=openpyxl"
$buildCmd += " --hidden-import=pandas"

$buildCmd += " main.py"

# Build
Write-Host "Building application..." -ForegroundColor Yellow
Write-Host "Command: $buildCmd" -ForegroundColor Gray
Write-Host ""

try {
    Invoke-Expression $buildCmd
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "✓ Build Complete!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Executable location:" -ForegroundColor Yellow
    Write-Host "  dist\VoterAttendance.exe" -ForegroundColor White
    Write-Host ""
    
    # Show file size
    if (Test-Path "dist\VoterAttendance.exe") {
        $fileSize = (Get-Item "dist\VoterAttendance.exe").Length / 1MB
        Write-Host "File size: $([math]::Round($fileSize, 2)) MB" -ForegroundColor Cyan
    }
    
    Write-Host ""
    Write-Host "Testing recommendations:" -ForegroundColor Yellow
    Write-Host "  1. Navigate to dist\ folder" -ForegroundColor White
    Write-Host "  2. Run VoterAttendance.exe" -ForegroundColor White
    Write-Host "  3. Test with sample data files" -ForegroundColor White
    Write-Host "  4. Test on computer without Python" -ForegroundColor White
    
} catch {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Red
    Write-Host "✗ Build Failed" -ForegroundColor Red
    Write-Host "========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Troubleshooting:" -ForegroundColor Yellow
    Write-Host "  1. Check build\ folder for error logs" -ForegroundColor White
    Write-Host "  2. Try: pyinstaller --onefile main.py (without --windowed)" -ForegroundColor White
    Write-Host "  3. See BUILD_GUIDE.md for more help" -ForegroundColor White
    exit 1
}
