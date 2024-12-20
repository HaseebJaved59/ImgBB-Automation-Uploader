# ImgBB Automation Uploader

This script automates the process of logging into ImgBB, uploading images from your clipboard to a specific album, and performing continuous uploads.

## Features
- Logs into your ImgBB account automatically.
- Uploads clipboard images to a specified album.
- Supports continuous image uploads with customizable album naming.
- Automatically removes the temporary files after upload.

## Requirements
To run this script, you need the following:
- Python 3.x
- Selenium
- Edge WebDriver (for Microsoft Edge browser automation)
- pyautogui (for handling file dialog interactions)
- pyperclip (for copying clipboard contents)
- PIL (Pillow) for handling image processing.

Install the required packages using pip:
```bash
pip install selenium pyautogui pyperclip Pillow
