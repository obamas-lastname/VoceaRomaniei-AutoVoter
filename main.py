import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tempmail import EMail  
from bs4 import BeautifulSoup  

# Path to the WebDriver
CHROME_DRIVER_PATH = "chromedriver.exe"  # !!! Update with your ChromeDriver path !!!

chrome_options = Options()
chrome_options.add_argument("--start-maximized") 
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

contestant = '1' # !!! Replace here with contestant position !!!
path = "//div[@class='div" + contestant + "']/a[@onclick='getVoteForm(19)']"

def generate_temp_email():
    """
    Generate a temporary email using tempmail-python library.
    """
    email = EMail()
    temp_email = email.address
    print(f"Generated temporary email: {temp_email}")
    return email

def automate_voting(temp_email):
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://voteazavocea.protv.ro") 

        try:
            resping_toate_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'RESPING TOATE')]"))
            )
            resping_toate_button.click()
            print("Clicked 'RESPING TOATE' button on the cookie banner.")
        except Exception as e:
            print(f"No cookie banner or issue handling it: {e}")

        contestant_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, path))
        )
        contestant_button.click()
        print("Clicked on contestant vote button.")
        time.sleep(2)

        email_input_field = wait.until(
            EC.element_to_be_clickable((By.NAME, "email"))  
        )

        email_input_field.click()
        print("Focused on the email input field.")

        email_input_field.send_keys(temp_email)
        print(f"Entered email: {temp_email}")

        email_input_field.send_keys("\ue007") 
        print("Submitted email.")

        time.sleep(3)

    except Exception as e:
        print(f"An error occurred: {e}")

def extract_href_from_email(email):
    inbox = email.get_inbox()

    for msg_info in inbox:
        message = email.get_message(msg_info.id)
        
        if message and hasattr(message, 'body'):
            soup = BeautifulSoup(message.body, 'html.parser')
            a_tag = soup.find('a', {'style': 'text-transform: uppercase; color: #1f55ff; text-decoration: underline;'})
            if a_tag and 'href' in a_tag.attrs:
                return a_tag.attrs['href']
    return None 

def visit_href_link(href):
    if href:
        print(f"Visiting URL: {href}")
        driver.get(href)
    else:
        print("No valid link found in the email body.")

def main():
    repeat_times = 20 # !!! Number of times to loop !!!

    for i in range(repeat_times):
        print(f"\nIteration {i + 1}/{repeat_times}:\n")

        email = generate_temp_email()

        automate_voting(email.address)

        time.sleep(5) 

        href = extract_href_from_email(email)
        visit_href_link(href)

        time.sleep(3)

if __name__ == "__main__":
    main()
