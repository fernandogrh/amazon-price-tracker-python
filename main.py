from bs4 import BeautifulSoup
import smtplib
import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()

url = "https://www.amazon.de/LEGO-42127-Spielzeugauto-Modellauto-Bausatz-Leuchtsteinen/dp/B09BNXPW7K/ref=sr_1_4?dib=eyJ2IjoiMSJ9.hCDNK4wJzqBdU-msH87Wn4GZMN5tglAihYBeeMd3FfM_MzUYwdTKXwKbp8PyTpXgw7EQABaejofGYXWbzDuWh2eaIhNAI97qp_bljughGmFFff62wfD6oOzUgG8zhos0Zcd-Qf5qTVDkoCWu1olcdeOU52SXqcwo2zwuDtpgcqr9Aqt-iY4zNUKlpNnfW-ysj_KBd33pyV2N40NMbs9J3fsqPziFnjiN8eRmbqR5-EhMWsavEqOuLvOfYndGVUrdIwzl8QG4zH5COABkjN5JjCakvK_C1xnPf9NvisPBgRU.wxFTsDOwP58Gf9LH6JXkl_ZDlLBKq50eVFeZwZtgCyM&dib_tag=se&keywords=lego%2Btechnic%2Bbatmobil&qid=1769529474&sr=8-4&th=1"
headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
    sys.exit()
try:
    website = BeautifulSoup(response.text, "html.parser")
    price_tag = website.find(name="span", class_="a-offscreen")
    title_tag = website.find(name="span", id="productTitle")
    if price_tag is None or title_tag is None:
        raise AttributeError
    str_price = price_tag.getText().strip()
    cleaned_price = (str_price.replace("CHF", "").replace("€", "").replace("$", "").replace(",", ".").strip())
    float_price = float(cleaned_price)
    product_name = title_tag.getText().strip()

except (AttributeError, ValueError):
    print("Parsing error: Amazon page structure or price format may have changed.")
    sys.exit()

target_price = 95

if float_price < target_price:
    message = f"The price of {product_name} is {str_price}, below your target price, Buy it now!"

    smtp_address = os.getenv("SMTP_ADDRESS")
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")
    if not all([smtp_address, email_address, email_password]):
        print("Missing one or more email environment variables.")
        sys.exit()
    try:
        with smtplib.SMTP(smtp_address, port=587) as connection:
            connection.starttls()
            connection.login(email_address, email_password)
            connection.sendmail(
                from_addr=email_address,
                to_addrs =email_address,
                msg = f"Subject: Amazon Price Alert\n\n{message}\n{url}".encode("utf-8")
            )
            print("Email alert sent successfully.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication error: {e}")
    except smtplib.SMTPException as e:
        print(f"Email sending failed: {e}")
else:
    print(f"No alert sent. Current price is {str_price}.")


