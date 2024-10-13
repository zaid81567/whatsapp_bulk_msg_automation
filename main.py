from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as pc
import time


# Helper function to log skipped numbers (those not registered on WhatsApp)
def saveSkippedNumber(num):
    with open("other/skipped_nums.txt", "a") as file:
        file.write(str(num) + '\n')

# Configuration variables
login_t = 30  # Time to allow for manual login (adjust if needed)
country_code = 91  # Enter your country code

# Initialize variable for counting skipped numbers
count_skipped_num = 0

# Function for explicit waits, useful for waiting until an element is present on the page
def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

# Create Selenium Chrome driver instance (ChromeDriver is managed automatically)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the image path from the file
with open("other/img_path.txt") as file:
    img_path = file.readline().rstrip()

# Load the message from the file (supports UTF-8 encoding for non-ASCII characters)
msg = ''
with open("other/message.txt", encoding="utf-8") as file:
    for line in file.readlines():
        msg += line

# Load phone numbers from the file
numbers = []
with open("other/numbers.txt") as file:
    for num in file.readlines():
        numbers.append(num.rstrip())

# Open WhatsApp Web and wait for manual login
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_t)  # Time for manual login
print("Logged In")

# Start processing each number
s_time = time.time()  # Start timer for execution time logging
for i, num in enumerate(numbers, 1):
    # Copy the phone number to the clipboard
    pc.copy(num)

    # Print current number being processed to the console
    print(f"===={i}. {num}====")

    # Open a new chat with the contact
    try:
        new_chat_el = wait_for_element(driver, (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/header/header/div/span/div/span/div[1]/div/span'))
        new_chat_el.click()
    except:
        print("TimeOut: New Chat button missing.")
        break  # Exit if the New Chat button is missing

    # Paste the number and attempt to start the chat
    new_chat_input_el = wait_for_element(driver, (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]/p'))
    new_chat_input_el.send_keys(Keys.CONTROL, "v")
    time.sleep(1)
    new_chat_input_el.send_keys(Keys.ENTER)

    # Check if the number is not a registered WhatsApp contact
    try:
        back_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/header/div/div[1]/div/span')
        back_btn.click()
        print("Clicked back")
        saveSkippedNumber(num)  # Log skipped number
        count_skipped_num += 1
        print("::: Message skipped :::")
        time.sleep(1)
        continue  # Skip to the next number if not found
    except:
        pass  # If the number exists, proceed to message sending

    # Short wait to allow chat to load
    time.sleep(1)

    # Attach the image
    attach_btn = wait_for_element(driver, (By.CSS_SELECTOR, '.xqmb7z'))
    attach_btn.click()

    attach_input = wait_for_element(driver, (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input'))
    attach_input.send_keys(img_path)
    print('-> Image attachment done')
    time.sleep(2)  # Allow time for the image to be uploaded

    # Paste the text message
    msg_input = wait_for_element(driver, (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p'))
    pc.copy(msg)
    msg_input.send_keys(Keys.CONTROL, "v")
    print("-> Message attached")
    msg_input.send_keys(Keys.ENTER)  # Send the message

    print("::: Message sent :::")

    # Short wait to ensure the message is sent before moving to the next number
    time.sleep(1)

# End of processing, log the total execution time
e_time = time.time()
print("::: ::: Execution Time:", round((e_time - s_time), 2), "s.")

# Short delay before closing the browser
time.sleep(5)

# Close the browser and end the program
print("==== PROGRAM SUCCESSFULLY EXECUTED ====")
driver.quit()
