from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

# sending message using driver
print("sending message")
link2 = f'https://web.whatsapp.com/send/?phone={country_code}{numbers[0]}'
driver.get(link2)
time.sleep(new_msg_t)

# attach image
attach_btn = driver.find_element(By.CSS_SELECTOR, '.xqmb7z')
attach_btn.click()  
time.sleep(2)

# Get the input element for attaching the image
attach_input = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
attach_input.send_keys(img_path)
time.sleep(2)  # Wait for the image to be attached
print('img insertion done')

# Find the message input field and inject the message
msg_input = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')
pc.copy(msg)
msg_input.send_keys(Keys.CONTROL, "v")
time.sleep(1)
# driver.execute_script("arguments[0].innerHTML = arguments[1];", msg_input, msg)
msg_input.send_keys(Keys.ENTER)
print("msg insertion done")

# Wait to observe the action
time.sleep(20)

# close the driver
driver.quit()
