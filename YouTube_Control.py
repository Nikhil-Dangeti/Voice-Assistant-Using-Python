import webbrowser
import pyautogui
import time
import psutil
import os

def play_youtube_video(video_name):
    search_url = f"https://www.youtube.com/results?search_query={video_name.replace(' ', '+')}"
    webbrowser.open(search_url)  # Open YouTube search

    time.sleep(5)  # Wait for the page to load

    for _ in range(10):
        pyautogui.press("tab")  # Navigate to the first video

    pyautogui.press("enter")  # Play the first video
    print(f"Playing {video_name} on YouTube.")

def stop_youtube_video():
    pyautogui.press("space")  # Toggle play/pause
    print("Paused/Resumed the YouTube video.")

def close_youtube():
    browser_names = ["chrome.exe", "firefox.exe", "msedge.exe"]
    
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'].lower() in browser_names:
            os.system(f"taskkill /F /PID {process.info['pid']}")  # Close browser
            print("Closed YouTube.")




  # Import the YouTube control module

