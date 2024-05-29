# #mobile_price_spider.py
# import scrapy
# from scrapy.crawler import CrawlerProcess
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
#
#
# class MobilePriceSpider(scrapy.Spider):
#     name = 'mobile_price_spider'
#
#     custom_settings = {
#         'SIGNALS_ENABLED': False  # Disable signal handling in Scrapy
#     }
#
#     def __init__(self, product_name=None, *args, **kwargs):
#         super(MobilePriceSpider, self).__init__(*args, **kwargs)
#         # self.proxy_pool = ['159.203.162.25', '102.69.176.98', '157.245.48.103', '157.230.82.155']
#         self.product_name = product_name
#         self.user_email = None
#
#     def start_requests(self):
#         if self.product_name:
#             # Construct the URL using the selected product name
#             url = f'https://amazon.in/s?k={self.product_name}'
#             print(f"The url is : {url}")
#             self.logger.info(f"The url is : {url}")
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         if 'amazon.in' in response.url:
#             # Extracting price from Amazon
#             price = response.css('.a-price .a-offscreen::text').extract_first()
#             if price:
#                 self.amazon_price = float(
#                     price.replace('₹', '').replace(',', ''))  # Convert to float (remove currency symbol and commas)
#                 self.logger.info(f"Amazon price: {self.amazon_price}")
#                 self.send_email_to_user(f"Amazon Price Update: ₹{self.amazon_price}")
#
#             else:
#                 self.logger.warning("Price not found on Amazon page")
#
#     def send_email_to_user(self, message):
#         if self.user_email:  # Check if user_email is not None
#             # Email configurations
#             sender_email = "pricewatchdog1@gmail.com"
#             password = "zuys wmea hbtw uoin"
#
#             # Setup the MIME
#             msg = MIMEMultipart()
#             msg['From'] = sender_email
#             msg['To'] = self.user_email  # Use the user's email here
#             msg['Subject'] = "Amazon Product Price Update"
#
#             # Attach the message to the email
#             msg.attach(MIMEText(message, 'plain'))
#
#             # Create SMTP session for sending the mail
#             with smtplib.SMTP('smtp.gmail.com', 587) as session:
#                 session.starttls()  # Enable security
#                 session.login(sender_email, password)  # Login
#                 text = msg.as_string()
#                 session.sendmail(sender_email, self.user_email, text)
#                 self.logger.info("Message sent.")
#         else:
#             self.logger.warning("User email is not available. Cannot send email.")

#mobile_price_spider.py
import scrapy
from scrapy.crawler import CrawlerProcess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class MobilePriceSpider(scrapy.Spider):
    name = 'mobile_price_spider'

    custom_settings = {
        'SIGNALS_ENABLED': False  # Disable signal handling in Scrapy
    }

    def _init_(self, product_name=None, *args, **kwargs):
        super(MobilePriceSpider, self)._init_(*args, **kwargs)
        self.product_name = product_name

    def start_requests(self):
        if self.product_name:
            # Construct the URL using the selected product name
            url = f'https://amazon.in/s?k={self.product_name}'
            print(f"The url is : {url}")
            self.logger.info(f"The url is : {url}")
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if 'amazon.in' in response.url:
            # Extracting price from Amazon
            price = response.css('.a-price .a-offscreen::text').extract_first()
            if price:
                self.amazon_price = float(
                    price.replace('₹', '').replace(',', ''))  # Convert to float (remove currency symbol and commas)
                self.logger.info(f"Amazon price: {self.amazon_price}")
                self.send_email(f"Amazon Price Update: ₹{self.amazon_price}")
            else:
                self.logger.warning("Price not found on Amazon page")

    def send_email(self, message):
        # Email configurations
        sender_email = "pricewatchdog1@gmail.com"
        receiver_email = "harshali6466@gmail.com"
        password = "zuys wmea hbtw uoin"

        # Setup the MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Amazon Product Price Update"

        # Attach the message to the email
        msg.attach(MIMEText(message, 'plain'))

        # Create SMTP session for sending the mail
        with smtplib.SMTP('smtp.gmail.com', 587) as session:
            session.starttls()  # Enable security
            session.login(sender_email, password)  # Login
            text = msg.as_string()
            session.sendmail(sender_email, receiver_email, text)
            self.logger.info("message sent")