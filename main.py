from bs4 import BeautifulSoup
import smtplib
import requests
import os
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
    exit()
try:
    website = BeautifulSoup(response.text, "html.parser")
    str_price = website.find(name="span", class_="a-offscreen").getText()
    float_price = float(str_price.replace("CHF", "").replace(",", ".").strip())
    product_name = website.find(name="span", id="productTitle").getText().strip()
except AttributeError:
    print("Parsing error: Amazon page structure may have changed.")
    exit()

target_price = 95

if float_price < target_price:
    message = f"The price of {product_name} is {str_price}, below your target price, Buy it now!"
    try:
        with smtplib.SMTP(os.getenv("SMTP_ADDRESS"), port=587) as connection:
            connection.starttls()
            connection.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD")),
            connection.sendmail(
                from_addr=os.getenv("EMAIL_ADDRESS"),
                to_addrs =os.getenv("EMAIL_ADDRESS"),
                msg = f"Subject: Amazon Price Alert\n\n{message}\n{url}".encode("utf-8")
            )
            print("Email alert sent successfully.")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication error: {e}")

    except smtplib.SMTPException as e:
        print(f"Email sending failed: {e}")


