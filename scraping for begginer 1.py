#import necessary libraries #استدعاء المكتبات 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Path to your Chrome webdriver executable (chrome\mozila\etc..) 
# استدعاء مكان ال web driver على حسب متصفح المختار 
driver = webdriver.Chrome()

# URL to scrape 
#رابط المستهدف 
url = "https://russian-art.net/workshops/workshop-07/"


# Load the URL
#جلب معلومات الموقع 
driver.get(url)

# Find and extract text 
#استخراج المعلومات حسب الاستهداف
text_elements = driver.find_elements(By.CSS_SELECTOR, 'p')  # Change selector as needed
text = "\n".join([element.text for element in text_elements])

# Print extracted text
print(text)

# Close the browser
driver.quit()
