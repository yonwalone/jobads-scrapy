import scrapy


class EmployerInfoSpider(scrapy.Spider):
    """
    Spider for scraping employer information from a website.

    This spider is responsible for crawling the specified website and extracting employer information,
    including titles and corresponding text. The scraped data is yielded as a dictionary for further processing.

    Args:
        scrapy.Spider: The base class for defining a Scrapy spider.

    Yields:
        dict: A dictionary containing the scraped employer information.
    """
    name = "employer-info"

    def start_requests(self):
        """
        Generates the initial requests to start crawling.

        This method is called by Scrapy when the spider is started, and it generates the initial requests
        to start crawling the specified website.

        Yields:
            scrapy.Request: A request object representing a URL to crawl.
        """
        yield scrapy.Request('https://www.porsche.com/germany/aboutporsche/jobs/', meta={'playwright': True})

    def parse(self, response):
        """
        Parses the response from a crawled URL.

        This method is responsible for extracting the desired information from the response obtained after
        crawling a URL. It uses CSS selectors to locate and extract the title and text information.

        Args:
            response (scrapy.http.Response): The response obtained after crawling a URL.

        Yields:
            dict: A dictionary containing the scraped employer information.
        """
        title = response.css("h3.PcomHeadline__root__6e6b3::text").getall()
        text = response.css("p-text.ExtendedTeaserSlide__text__fad0a::text").getall()
        yield {
            'title': title,
            'text': text
        }
