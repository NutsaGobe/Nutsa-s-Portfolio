from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://invu.ge")
    driver.maximize_window()
    time.sleep(2)
    
    # შესვლის ღილაკი
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'შესვლა') or contains(text(), 'Login')]"))
    )
    login_button.click()
    time.sleep(2)
    
    # ელფოსტა
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
    )
    email_field.send_keys("testuser@gmail.com")
    
    # პაროლი
    password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password_field.send_keys("WrongPass123!")
    
    # Log In ღილაკი
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit' or contains(text(), 'Log In')]")
    submit_button.click()
    time.sleep(3)
    
    # შემოწმება
    if "login" in driver.current_url.lower():
        print("✓ ტესტი გაიარა - არ შევიდა!")
    else:
        print("✗ ტესტი ჩაიშალა - შევიდა!")

except Exception as e:
    print(f"შეცდომა: {e}")

finally:
    time.sleep(3)
    driver.quit()