@echo off
setlocal

set /p bot_token=Enter your bot token:
set /p channel_id=Enter the channel ID to send messages:
set /p include_icon=Do you want to include an icon? (y/n):

set "script_dir=%~dp0"

rem Save bot token to token.txt
echo %bot_token% > "%script_dir%token.txt"

rem Change directory to the script's directory
cd /d "%script_dir%"

rem Run PyInstaller to create the executable with additional data (token.txt)
pyinstaller --onefile --add-data "token.txt;." bot.pyw

pause
