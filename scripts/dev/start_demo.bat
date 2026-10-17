@echo off
rem UK Baseline data catalogue - local demo.
rem Serves the "site" folder next to this file on http://localhost:8010/
rem (or the next free port) and opens your browser. Close this window to stop.
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "%~dp0serve_demo.py"
  goto done
)
where python >nul 2>nul
if %errorlevel%==0 (
  python "%~dp0serve_demo.py"
  goto done
)
echo Python 3 was not found on this computer, so the demo cannot start.
:done
pause
endlocal
