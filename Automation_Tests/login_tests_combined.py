# Selenium-ის გამოყენებით INVU.GE-ზე ავტორიზაციის ტესტები (VALID + INVALID)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def valid_login_test():
    print("\n=== ✅ VALID LOGIN TEST STARTED ===\n")
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
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        email_input.send_keys("testuser@gmail.com")

        # პაროლი
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys("TestUser123!")  # სწორი პაროლი

        # ავტორიზაცია
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit' or contains(text(), 'Log In')]")
        submit_button.click()
        time.sleep(3)

        # შემოწმება, შევიდა თუ არა
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'პროფილი') or contains(text(), 'Dashboard')]"))
            )
            print("✅ ტესტი წარმატებით შესრულდა — მომხმარებელი შევიდა სისტემაში!")
        except:
            print("❌ ტესტი ჩაიშალა — ვერ მოიძებნა პროფილის ელემენტი!")

    except Exception as e:
        print(f"შეცდომა VALID ტესტში: {e}")
    finally:
        driver.quit()


def invalid_login_test():
    print("\n=== ❌ INVALID LOGIN TEST STARTED ===\n")
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

        # პაროლი (არასწორი)
        password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_field.send_keys("WrongPass123!")

        # Log In ღილაკი
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit' or contains(text(), 'Log In')]")
        submit_button.click()
        time.sleep(3)

        # შემოწმება — არ უნდა შევიდეს
        if "login" in driver.current_url.lower():
            print("✅ ტესტი წარმატებით შესრულდა — არ შევიდა (მოსალოდნელი ქცევა).")
        else:
            print("❌ ტესტი ჩაიშალა — მომხმარებელი შევიდა არასწორი მონაცემებით!")

    except Exception as e:
        print(f"შეცდომა INVALID ტესტში: {e}")
    finally:
        time.sleep(3)
        driver.quit()


# =============================
# 🧪 ტესტების გაშვება
# =============================
if __name__ == "__main__":
    valid_login_test()
    invalid_login_test()
