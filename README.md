# Amazon Price Tracker Documentation

This Python program tracks the price of a product on Amazon and sends an email notification if the price drops below a 
specified maximum price. It utilizes various libraries such as `BeautifulSoup`, `requests`, and `smtplib` for web scraping, HTTP requests, and email functionality respectively.

## Prerequisites
1. **Python Environment:** Make sure you have Python installed on your system. This program requires at least Python 3.

2. **Required Libraries:**
- `bs4` (BeautifulSoup): A library for web scraping and extracting information from HTML and XML documents.
- `requests`: A library for making HTTP requests.
- `smtplib`: A library for sending emails.
- `os`: A built-in library for interacting with the operating system.

3. **User Account Information:**

- To use this program, you need to have a Gmail account with less secure apps enabled.
- Set the following environment variables with your Gmail credentials and other information:
- `EMAIL`: Your Gmail email address.
- `PASSWORD`: You have to generate your app password in Google Settings. Full tutorial by Peter Xie here: https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317
- `USER_AGENT`: Your browser's user agent. You can find it by visiting https://myhttpheader.com/
- `LANGUAGE`: Your language for HTTP requests. You can find it by visiting https://myhttpheader.com/
- `MAX_PRICE`: The maximum price threshold for which you want to receive a notification.

## Usage
 
1. **Setting Up Environment Variables:**

- Ensure you've set up the required environment variables (`EMAIL`, `PASSWORD`, `USER_AGENT`, `LANGUAGE`, and `MAX_PRICE`) with appropriate values.
2. **Amazon Product Link:**
- Modify the `amazon_link` variable to contain the URL of the Amazon product you want to track. You can find this link on the Amazon product page.

3. **Running the Program:**

- Run the program using a Python interpreter (Python 3 recommended).
- The program performs the following steps:
- Sends an HTTP request to the Amazon product page using the provided headers.
- Parses the HTML content of the response using BeautifulSoup.
- Extracts the price and product title from the parsed HTML.
- Compares the price with the maximum price threshold.
- If the price is lower or equal to the maximum price, it sends an email notification.

## Note
- Since this program uses your Gmail credentials directly, it's recommended to use a throwaway Gmail account with less secure apps enabled to avoid exposing your primary account's credentials.
- Keep in mind that web scraping might violate Amazon's terms of service. Use this program responsibly and avoid excessive scraping to prevent any potential issues.
- This documentation assumes basic familiarity with Python and environment variables.

## Disclaimer
This program is provided as-is and the author does not take responsibility for any consequences or actions resulting from its use. Use it responsibly and in compliance with the terms of service of any website you interact with.