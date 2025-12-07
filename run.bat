@echo off
REM Budget Buddy - Windows Run Script

echo Starting Budget Buddy...
echo ========================

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run the application
echo Starting Flask application...
echo Access the app at: http://127.0.0.1:5000
python app.py

pause
