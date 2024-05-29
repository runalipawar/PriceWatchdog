# pricewatchdog/management/commands/run_spider.py

from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scrapy.settings.default_settings import USER_AGENT

from pricewatchdog.scrappy.spiders.mobile_price_spider import MobilePriceSpider

def run_spider(product_name):  # Add user_email parameter
    print("Running spider...")
    # Initialize Scrapy settings
    process = CrawlerProcess()

    # Add your spider to the process
    process.crawl(MobilePriceSpider, product_name=product_name)

    # Start the process
    process.start()
    print("Spider finished.")

