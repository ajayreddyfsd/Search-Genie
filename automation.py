from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome WebDriver
driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed

try:
    # Navigate to the webpage
    url = "https://www.google.ca/"
    driver.get(url)

    # Fetch the page title
    title = driver.title
    print(f"Page Title: {title}")

    # Wait for the search input to be visible and interactable
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )

    # Enter text into the search input
    search_input.send_keys('Hello, World!')

    # Wait for the search button to be clickable
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "btnI"))
    )

    # Click the search button
    search_button.click()

    # Wait for some time to observe the results
    WebDriverWait(driver, 10).until(
        EC.title_contains("Hello, World!")
    )

    # Print the new page title
    print(f"New Page Title: {driver.title}")


    # Wait for user input to keep the browser open
    input("Press Enter to close the browser...")  # Keeps the browser open until you press Enter

finally:
    # Close the driver
    driver.quit()
