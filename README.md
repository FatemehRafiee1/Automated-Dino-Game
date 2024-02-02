# Automated-Dino-Game

Overview:

This Python script utilizes the PyAutoGUI and Pillow libraries to automate gameplay in a side-scrolling game, specifically for controlling a character (e.g., jumping) based on visual cues within the game environment.
Features:

    Image Recognition:
        Uses PyAutoGUI's locateOnScreen function to locate specific images on the screen with a confidence threshold.
        Handles the case where an image cannot be found using ImageNotFoundException.

    Mouse Click Automation:
        Clicks on specified images on the screen.

    Screenshot Capture and Pixel Analysis:
        Captures a specific region of the screen using Pillow's ImageGrab.grab.
        Checks for the presence of a specific pixel color (e.g., green) within the captured region.

How to Use:

    Requirements:
        Ensure Python is installed on your system.
        Install required libraries using pip install pyautogui Pillow.

    Run the Script:
        Execute the script using python script_name.py.
        Make sure the game window is in focus and visible on the screen.

    Gameplay Automation:
        The script will locate and click on specific images based on their paths.
        Monitors the screen for a specific pixel color within a designated region and triggers a spacebar press if the condition is met.

    Customization:
        Modify image paths, pixel color conditions, and capture region coordinates as needed for your specific game.

Notes:

    The script may need adjustments based on the characteristics of the game being automated.
    Always respect the terms of service of the game and ensure that the automation aligns with fair play policies.