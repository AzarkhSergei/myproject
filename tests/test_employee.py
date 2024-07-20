import sqlite3
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_employees_in_database(db_path, first_name, last_name):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees WHERE firstName=? AND lastName=?", (first_name, last_name))
            employees = cursor.fetchall()
            if employees:
                logger.info("Found %d employees with name %s %s in the database", len(employees), first_name, last_name)
                for employee in employees:
                    logger.info("Employee details: %s", employee)
                return True
            else:
                logger.warning("No employees found in the database with name %s %s", first_name, last_name)
                return False
    except sqlite3.Error as e:
        logger.error("Database error: %s", e)
        return False

def main():
    db_path = '/Users/kadaffi/Sergei/TelRan/myproject/mydatabase.db'
    first_name = "John"
    last_name = "Doe"

    if check_employees_in_database(db_path, first_name, last_name):
        print("Database verification passed!")
    else:
        print("Database verification failed!")

if __name__ == "__main__":
    main()
