@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
    py -3 start.py
) else (
    where python >nul 2>nul
    if errorlevel 1 (
        echo Instala Python 3.10 o posterior y activa Add Python to PATH.
        pause
        exit /b 1
    )
    python start.py
)
set "start_result=%errorlevel%"
if not "%start_result%"=="0" pause
exit /b %start_result%
