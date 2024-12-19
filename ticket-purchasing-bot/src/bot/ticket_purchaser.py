from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TicketPurchaser:
    def __init__(self):
        self.driver = None

    def initialize_driver(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self, username, password):
        self.driver.get("https://example.com/login")
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def select_event(self):
        self.driver.get("https://www.eventim.com.br/campaign/systemofadown")
        while True:
            try:
                event_link = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "SÃO PAULO 10/05/2025"))
                )
                event_link.click()
                print("Event link clicked!")
                break
            except Exception as e:
                print("Event link not available yet, refreshing...")
                self.driver.refresh()
                time.sleep(5)  # Wait for 5 seconds before refreshing

    def select_tickets(self):
        # Add logic to handle the modal and select tickets
        pass

    def purchase_tickets(self):
        # Add logic to complete the purchase
        pass

    def close(self):
        self.driver.quit()