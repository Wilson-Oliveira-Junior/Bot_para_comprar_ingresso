def wait_for_element(driver, xpath, timeout=10):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException

    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        print(f"Element with xpath {xpath} not found within {timeout} seconds.")
        return None

def handle_exception(e):
    print(f"An error occurred: {str(e)}")

def log_action(action):
    print(f"Action: {action}")