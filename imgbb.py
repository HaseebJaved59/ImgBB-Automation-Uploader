from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip
import pyautogui
from PIL import ImageGrab
import os
from selenium.webdriver.support.ui import Select


a= 1
b= 1
# Path to your msedgedriver
driver_path = r'msedgedriver.exe'  # Change this to your actual path

# Initialize the WebDriver for Edge
driver = webdriver.Edge(executable_path=driver_path)

# Open imgbb login page
driver.get("https://imgbb.com/login")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@alt='ImgBB']")))

# Log in to imgbb (replace with your credentials)
username = "jthompsonsbg2@gmail.com"
password = "python"

# Find the username field and enter the username

username_field = driver.find_element(By.NAME, "login-subject")
username_field.send_keys(username)

# Find the password field and enter the password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(password)

# Click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for login to complete
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Autodistproject']")))

# Click the album text
login_button = driver.find_element(By.XPATH, "//span[@data-text='album-label']")
login_button.click()


# Wait for login to complete
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='']//span[@class='user-image default-user-image']//span[@class='icon icon-face-meh']")))


# Click on album
login_button = driver.find_element(By.XPATH, "//a[normalize-space()='A']")
login_button.click()


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='A']")))





# Infinite loop for uploading images
while True:
    # Wait for user input to upload the next image
    inpt = input("Press Enter after you have copied the image path to the clipboard or type 'exit' to quit...")
    print(inpt)
    # Check if the user wants to exit
    if inpt == 'exit':
        break

    elif inpt == 'A':
        
        print("kkkkkasksakasksak")
        # Navigate to the album page
        driver.get("https://imgbb.co/album/3BDP3p")  # replace with your album URL
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Upload to album']"))) 
        # add_images_button = driver.find_element(By.XPATH, "//div[@id='list-most-recent']//div[@class='content-empty']//div//span[@class='btn-text'][normalize-space()='Upload images']")
        # add_images_button.click()
        # Retrieve the image path from the clipboard
            
        # Save the image from the clipboard to a temporary file
        image = ImageGrab.grabclipboard()
        if image is None:
            print("No image found in clipboard. Please copy the image again and try.")
            continue

        temp_image_path = "temp_image.png"
        image.save(temp_image_path, 'PNG')

        # Print the image path to verify it
        print("Image saved to temporary path:", temp_image_path)

        # Find the file input element and click it to open the file dialog
        file_input = driver.find_element(By.XPATH, "//span[normalize-space()='Upload to album']")
        file_input.click()

        # Wait for a short duration to ensure the file dialog is open
        time.sleep(2)

        # Use pyautogui to simulate the file path entry and pressing Enter
        pyperclip.copy(os.path.abspath(temp_image_path))
        pyautogui.hotkey('ctrl', 'v')  # Paste the image path
        pyautogui.press('enter')  # Press Enter to confirm

        # Wait for the upload to complete (this may take some time depending on the file size)
        time.sleep(5)  # You may need to adjust this sleep duration

        dropdown = Select( driver.find_element(By.ID, "upload-album-id")) 

        dropdown.select_by_visible_text("─ "+inpt+str(a)+" (Public)")

            
        file_input = driver.find_element(By.XPATH, "//button[@class='btn btn-big green']")
        file_input.click()

        time.sleep(10)  # You may need to adjust this sleep duration
        a = a + 1

        if(a == 21 ):
            a = 0
        # Remove the temporary file after upload
        os.remove(temp_image_path)

    

    # Wait for the upload to complete (this may take some time depending on the file size)
    time.sleep(10)  # you may need to adjust this sleep duration

# Close the browser
driver.quit()
