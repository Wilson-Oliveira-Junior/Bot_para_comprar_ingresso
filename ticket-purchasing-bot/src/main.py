from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def main():
    from bot.ticket_purchaser import TicketPurchaser

    purchaser = TicketPurchaser()
    purchaser.initialize_driver()
    try:
        purchaser.select_event()
        purchaser.select_tickets()
        purchaser.purchase_tickets()
    finally:
        purchaser.close()

if __name__ == "__main__":
    main()