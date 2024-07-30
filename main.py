from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip as pc
import time

# config
login_t = 30
new_msg_t = 10
msg_send_t = 5
country_code = 91
img_path = r"D:\Downloads\efh_20240727042202_563164_131bf_5e686.png"

# create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# create action chain obj to perform needed key presses
actions = ActionChains(driver)

# encode message
msg = "And what you'll hold?"

# get all numbers
numbers = []
with open("numbers.txt") as file:
    for num in file.readlines():
        numbers.append(num.rstrip())
print(numbers)

# open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_t)
print("Logged In")

for i, num in zip(range(len(numbers)), numbers):
    # copying number in clipboard
    pc.copy(num)

    # showing num info on terminal
    print(f"===={i+1}. {num}====")

    # opening new chat
    new_chat_el = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[4]/div/span')
    new_chat_el.click()
    time.sleep(2)
    new_chat_input_el = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]/p')
    new_chat_input_el.send_keys(Keys.CONTROL, "v")
    new_chat_input_el.send_keys(Keys.ENTER)

    # attach image
    attach_btn = driver.find_element(By.CSS_SELECTOR, '.xqmb7z')
    attach_btn.click()
    time.sleep(2)
        # Get the input element for attaching the image
    attach_input = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
    attach_input.send_keys(img_path)
    print('-> img attachment done')
    time.sleep(2)  

    # add text message
    msg_input = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
    pc.copy(msg)
    msg_input.send_keys(Keys.CONTROL, "v")
    print("-> msg attachment done")
    time.sleep(1)
    msg_input.send_keys(Keys.ENTER)

    print(":::    message sent    :::")

# sleep time before terminating the program
time.sleep(20)

# close the driver
print("====PROGRAM SUCCESSFULLY INTERPRATED====")
driver.quit()
