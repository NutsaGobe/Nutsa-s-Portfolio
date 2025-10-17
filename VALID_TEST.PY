
# Selenium-ის გამოყენებით INVU.GE-ზე ავტორიზაცია სწორი ინდენტაციით
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://invu.ge/")
time.sleep(2)

# ვცდილობთ ვიპოვოთ მთავარი გვერდის "შესვლა" ღილაკი
try:
	login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'შესვლა')] | //a[contains(text(), 'შესვლა')] | //button[contains(text(), 'Login')] | //a[contains(text(), 'Login')]")
	login_button.click()
	print("ღილაკი 'შესვლა' დაჭერილია.")
except Exception as e:
	print("ვერ მოიძებნა ღილაკი 'შესვლა' (Login):", e)

time.sleep(2)

# ელფოსტის ველის პოვნა და შევსება
try:
	email_input = driver.find_element(By.XPATH, "//input[@type='email'] | //input[contains(@placeholder, 'ელფოსტა')] | //input[contains(@placeholder, 'Email')] | //input[@name='email']")
	email_input.clear()
	email_input.send_keys("testuser@gmail.com")
	print("ელფოსტა შეყვანილია.")
	# პაროლის ველის პოვნა და შევსება
	try:
		password_input = driver.find_element(By.XPATH, "//input[@type='password'] | //input[contains(@placeholder, 'პაროლი')] | //input[contains(@placeholder, 'Password')] | //input[@name='password']")
		password_input.clear()
		password_input.send_keys("TestUser123!")
		print("პაროლი შეყვანილია.")
		# პაროლის შეყვანის შემდეგ ვეცდებით ავტორიზაციის ღილაკზე დაჭერას
		time.sleep(1)
		try:
			submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'შესვლა')] | //button[contains(text(), 'Log In')] | //button[@type='submit']")
			submit_button.click()
			print("ავტორიზაციის ღილაკი დაჭერილია.")
		except Exception as e:
			print("ვერ მოიძებნა ავტორიზაციის ღილაკი:", e)
		# ავტორიზაციის შემდეგ ვამოწმებთ, წარმატებით შევიდა თუ არა მომხმარებელი
		time.sleep(3)
		try:
			profile_element = driver.find_element(By.XPATH, "//a[contains(@href, 'profile')] | //div[contains(text(), 'პროფილი')] | //a[contains(text(), 'დეშბორდი')] | //div[contains(text(), 'Dashboard')]")
			print("მომხმარებელი წარმატებით სისტემაშია შესული!")
		except Exception as e:
			print("ავტორიზაცია ვერ მოხერხდა ან პროფილის ელემენტი ვერ მოიძებნა:", e)
	except Exception as e:
		print("ვერ მოიძებნა პაროლის ველი:", e)
except Exception as e:
	print("ვერ მოიძებნა ელფოსტის ველი:", e)

input("Press Enter to close the browser...")
driver.quit()
