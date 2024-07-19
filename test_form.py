from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Указываем путь к вашему WebDriver
driver = webdriver.Chrome()

# Открываем ваш сайт
driver.get("http://localhost:3000")

# Заполнение формы'
driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")
driver.find_element(By.ID, "birthDate").send_keys("01 01 1980")
driver.find_element(By.ID, "salary").send_keys("4000")

# Нажатие на кнопку "Add employee"
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

# Ждем, чтобы страница обновилась
#time.sleep(2)

# Нажатие на кнопку "Get status"
driver.find_element(By.ID, "companyStatus").click()

# Явное ожидание появления элементов списка <li>
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#employeesList li"))
)

# Проверяем, что данные появились в списке сотрудников
# Получаем все элементы списка <li>
employees_list_items = driver.find_elements(By.CSS_SELECTOR, "#employeesList li")
if not employees_list_items:
    raise Exception("No employees found in the list")
# Берем последний элемент списка
last_employee = employees_list_items[-1]
last_employee_text = last_employee.text
print("Last employee text:", last_employee_text)
assert "John" in last_employee_text
assert "Doe" in last_employee_text
assert "4000 NIS" in last_employee_text

print("Test passed!")

# Закрываем браузер
driver.quit()
