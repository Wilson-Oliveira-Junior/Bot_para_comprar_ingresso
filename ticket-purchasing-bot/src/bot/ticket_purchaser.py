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
        try:
            # Wait for the modal to appear and select the number of tickets
            ticket_modal = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "ticket-modal"))
            )
            ticket_dropdown = ticket_modal.find_element(By.ID, "ticket-quantity")
            ticket_dropdown.click()
            ticket_dropdown.find_element(By.XPATH, "//option[text()='2']").click()  # Select 2 tickets

            # Confirm ticket selection
            confirm_button = ticket_modal.find_element(By.ID, "confirm-tickets")
            confirm_button.click()
            print("Tickets selected!")

            # Proceed to the purchase page
            proceed_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "proceed-to-purchase"))
            )
            proceed_button.click()
            print("Proceeded to purchase page!")
        except Exception as e:
            print(f"Error selecting tickets: {e}")

    def purchase_tickets(self):
        try:
            # Wait for the purchase page to load and fill in payment details
            payment_form = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "payment-form"))
            )
            payment_form.find_element(By.ID, "card-number").send_keys("4111111111111111")
            payment_form.find_element(By.ID, "expiry-date").send_keys("12/25")
            payment_form.find_element(By.ID, "cvv").send_keys("123")

            # Confirm purchase
            purchase_button = payment_form.find_element(By.ID, "purchase-button")
            purchase_button.click()
            print("Purchase completed!")
        except Exception as e:
            print(f"Error completing purchase: {e}")

    def close(self):
        self.driver.quit()