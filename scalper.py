import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client

options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')

# For using Edge
browser = webdriver.Chrome('G:\\Dev\\Auto-checkout\\chromedriver.exe', options=options)

# Bestbuy RTX 3060 Ti page
browser.get("https://www.bestbuy.ca/en-ca/product/nvidia-geforce-rtx-3060-ti-8gb-gddr6-video-card/15166285")

buyButton = False
TWILIO_PHONE_NUMBER = "#GivenNumber"
DIAL_NUMBERS = ["#YourNumber",]
client = Client("#Id", "#Token")
TWIML_INSTRUCTIONS_URL = "http://static.fullstackpython.com/phone-calls-python.xml"

def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")

while not buyButton:
    try:
        # If this works, the button is not open
        addToCartBtn = addButton = browser.find_element_by_class_name("disabled_LqxUL")

        # Restart the script
        print("Button isn't ready yet.")
        time.sleep(10)
        browser.refresh()

    except:
        # If this works, the button is not open
        addToCartBtn = addButton = browser.find_element_by_class_name("button_2m0Gt")

        # Restart the script
        print("Button is clicked.")
        addToCartBtn.click()
        buyButton = True

dial_numbers(DIAL_NUMBERS)