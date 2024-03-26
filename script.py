from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from datetime import datetime, timedelta

# Set the URL to capture
url = 'https://www.weatherbug.com/traffic-cam/?latlng=38.900007,-77.02976&camId=200162'

# Create a directory to save images if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Create a webdriver instance
driver = webdriver.Chrome()

# Define the total number of screenshots to capture
total_screenshots = 1440

# Iterate to capture screenshots every minute
for i in range(total_screenshots):
    # Navigate to the URL
    driver.get(url)

    # Wait for the page to load completely
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Scroll the page to ensure the element is in view
    driver.execute_script("arguments[0].scrollIntoView(true);", WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'thumbnailImage__Container-sc-1h6xkpy-0'))))

    # Generate timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Locate the div element
    thumbnail_div = driver.find_element(By.CLASS_NAME, 'thumbnailImage__Container-sc-1h6xkpy-0')

    # Take a screenshot of the div element and save it locally with the filename as timestamp.png
    filename = os.path.join('images', f'{timestamp}.png')
    thumbnail_div.screenshot(filename)
    print(i+1)

    # Wait for 60 seconds before capturing the next screenshot
    time.sleep(60)

# Close the webdriver instance
driver.quit()