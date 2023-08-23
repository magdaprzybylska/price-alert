from bs4 import BeautifulSoup
import requests
import smtplib
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
USER_AGENT = os.environ["USER-AGENT"]
LANGUAGE = os.environ["LANGUAGE"]
MAX_PRICE = 650

# Example Amazon link
amazon_link = "https://www.amazon.com/NUOBESTY-Stuffed-Halloween-Decoration-Supplies/dp/B0BB21RX3S/ref=sr_1_6?crid=38DDSAXVZ4GMT&keywords=python+mascot&qid=1692624298&sprefix=python+masco%2Caps%2C194&sr=8-6"
# You can find your User Agent and Accept Language here: https://myhttpheader.com/
headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": LANGUAGE
}


def send_email(link, current_price, title):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(EMAIL, PASSWORD)
    server.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:Price alert!\n\nPrice for {title}\n({link})\nhas dropped "
                                                         f"to ${current_price}. You can buy it now! ")
    server.close()


response = requests.get(amazon_link, headers=headers)
response.raise_for_status()

with open("amazon.html", "w") as file:
    file.write(response.text)

with open("amazon.html", "r") as file:
    soup = BeautifulSoup(file, "lxml")
    price_whole = soup.find(name="span", class_="a-price-whole")
    price_fraction = soup.find(name="span", class_="a-price-fraction")
    product_title = soup.find(name="span", id="productTitle")
    price = float(price_whole.text + price_fraction.text)
    title = product_title.text.strip().encode("UTF-8")


if price <= MAX_PRICE:
    send_email(amazon_link, price, title)