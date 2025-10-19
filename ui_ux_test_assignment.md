# UI/UX Test Assignment - *** Authorization Testing

**Project:** ***  
**Test Type:** UI/UX Automation Testing  
**Framework:** Selenium WebDriver  
**Language:** Python  
**Date:** 2025-10-19

---

## Test Case 1: ავტორიზაცია სწორი მონაცემებით

**Test ID:** UI-001  
**Priority:** High  
**Status:** Ready for Execution

### Description
სკრიპტი ამოწმებს ავტორიზაციის ფუნქციონალს სწორი ელფოსტისა და პაროლის გამოყენებით.

### Test Script

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ბრაუზერის გაშვება
driver = webdriver.Chrome()
driver.get("https://***.ge/")
time.sleep(2)

# ვცდილობთ ვიპოვოთ მთავარი გვერდის "შესვლა" ღილაკი
try:
    login_button = driver.find_element(
        By.XPATH, 
        "//button[contains(text(), 'შესვლა')] | //a[contains(text(), 'შესვლა')] | //button[contains(text(), 'Login')] | //a[contains(text(), 'Login')]"
    )
    login_button.click()
    print("✓ ღილაკი 'შესვლა' დაჭერილია.")
except Exception as e:
    print("✗ ვერ მოიძებნა ღილაკი 'შესვლა' (Login):", e)

time.sleep(2)

# ელფოსტის ველის პოვნა და შევსება
try:
    email_input = driver.find_element(
        By.XPATH, 
        "//input[@type='email'] | //input[contains(@placeholder, 'ელფოსტა')] | //input[contains(@placeholder, 'Email')] | //input[@name='email']"
    )
    email_input.clear()
    email_input.send_keys("testuser@gmail.com")
    print("✓ ელფოსტა შეყვანილია.")
    
    # პაროლის ველის პოვნა და შევსება
    try:
        password_input = driver.find_element(
            By.XPATH, 
            "//input[@type='password'] | //input[contains(@placeholder, 'პაროლი')] | //input[contains(@placeholder, 'Password')] | //input[@name='password']"
        )
        password_input.clear()
        password_input.send_keys("TestUser123!")
        print("✓ პაროლი შეყვანილია.")
        
        # პაროლის შეყვანის შემდეგ ვეცდებით ავტორიზაციის ღილაკზე დაჭერას
        time.sleep(1)
        
        try:
            submit_button = driver.find_element(
                By.XPATH, 
                "//button[contains(text(), 'შესვლა')] | //button[contains(text(), 'Log In')] | //button[@type='submit']"
            )
            submit_button.click()
            print("✓ ავტორიზაციის ღილაკი დაჭერილია.")
        except Exception as e:
            print("✗ ვერ მოიძებნა ავტორიზაციის ღილაკი:", e)
        
        # ავტორიზაციის შემდეგ ვამოწმებთ, წარმატებით შევიდა თუ არა მომხმარებელი
        time.sleep(3)
        
        try:
            profile_element = driver.find_element(
                By.XPATH, 
                "//a[contains(@href, 'profile')] | //div[contains(text(), 'პროფილი')] | //a[contains(text(), 'დეშბორდი')] | //div[contains(text(), 'Dashboard')]"
            )
            print("✓ მომხმარებელი წარმატებით სისტემაშია შესული!")
        except Exception as e:
            print("✗ ავტორიზაცია ვერ მოხერხდა ან პროფილის ელემენტი ვერ მოიძებნა:", e)
            
    except Exception as e:
        print("✗ ვერ მოიძებნა პაროლის ველი:", e)
        
except Exception as e:
    print("✗ ვერ მოიძებნა ელფოსტის ველი:", e)

# ბრაუზერის დახურვა
input("Press Enter to close the browser...")
driver.quit()
```

### Expected Result
- მომხმარებელი წარმატებით ავტორიზდება
- გვერდზე გამოჩნდება პროფილის/დეშბორდის ელემენტი

### Actual Result
- შესავსებია ტესტის შესრულების შემდეგ

---

## Test Case 2: ავტორიზაცია არასწორი მონაცემებით (Negative Test)

**Test ID:** UI-002  
**Priority:** High  
**Status:** Ready for Execution

### Description
სკრიპტი ამოწმებს ავტორიზაციის ფუნქციონალს არასწორი პაროლის გამოყენებით. უნდა გამოჩნდეს შეცდომის შეტყობინება.

### Test Script

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ბრაუზერის გაშვება
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # გვერდის გახსნა
    driver.get("https://***.ge")
    driver.maximize_window()
    time.sleep(2)
    
    # შესვლის ღილაკი
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'შესვლა') or contains(text(), 'Login')]"))
    )
    login_button.click()
    print("✓ შესვლის ღილაკი დაჭერილია")
    time.sleep(2)
    
    # ელფოსტა
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
    )
    email_field.send_keys("testuser@gmail.com")
    print("✓ ელფოსტა შეყვანილია")
    
    # არასწორი პაროლი
    password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password_field.send_keys("WrongPass123!")
    print("✓ არასწორი პაროლი შეყვანილია")
    
    # Log In ღილაკი
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit' or contains(text(), 'Log In')]")
    submit_button.click()
    print("✓ ავტორიზაციის ღილაკი დაჭერილია")
    time.sleep(3)
    
    # შემოწმება - არ უნდა შევიდეს სისტემაში
    if "login" in driver.current_url.lower():
        print("✓ ტესტი წარმატებით გაიარა - არასწორი მონაცემებით არ შევიდა სისტემაში!")
    else:
        print("✗ ტესტი ჩაიშალა - არასწორი მონაცემებით შევიდა სისტემაში!")
        
except Exception as e:
    print(f"✗ შეცდომა: {e}")
    
finally:
    time.sleep(3)
    driver.quit()
    print("✓ ბრაუზერი დახურულია")
```

### Expected Result
- ავტორიზაცია არ უნდა მოხდეს
- მომხმარებელი უნდა დარჩეს login გვერდზე
- შესაძლოა გამოჩნდეს error message

### Actual Result
- შესავსებია ტესტის შესრულების შემდეგ

---

## Test Execution Summary

| Test ID | Test Name | Priority | Status | Result |
|---------|-----------|----------|--------|--------|
| UI-001 | ავტორიზაცია სწორი მონაცემებით | High | Ready | - |
| UI-002 | ავტორიზაცია არასწორი მონაცემებით | High | Ready | - |

---

## Prerequisites
```bash
pip install selenium
pip install webdriver-manager
```

## Notes
- ორივე სკრიპტი იყენებს Selenium WebDriver-ს
- UI-001 ამოწმებს Positive Scenario-ს
- UI-002 ამოწმებს Negative Scenario-ს (არასწორი პაროლი)
- სკრიპტები მზადაა VS Code-ში გასაშვებად