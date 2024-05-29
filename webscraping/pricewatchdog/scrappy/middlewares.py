from fake_useragent import UserAgent

class UserAgentMiddleware:
    def __init__(self):
        self.ua = UserAgent()

    def process_request(self, request, spider):
        request.headers['User-Agent'] = self.ua.random
# middleware.py

from scrapy import signals
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.http import Request

class ScrapingAPIMiddleware(HttpProxyMiddleware):
    def __init__(self, settings):
        super().__init__(settings)
        self.proxies = settings.getlist('PROXIES')
        self.api_key = settings.get('SCRAPING_API_KEY')

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls(crawler.settings)
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        return middleware

    def process_request(self, request, spider):
        request.meta['proxy'] = self.proxies.pop(0)
        self.proxies.append(request.meta['proxy'])
        request.headers['Authorization'] = f'Token {self.api_key}'
