import scrapy
import numpy as np


class JobAdsSpider(scrapy.Spider):
    """
    This scrapy spider crawls job ads of the defined urls.

    Args:
        scrapy.Spider: The base class for the spider.

    Yields:
        dict: A dictionary containing the extracted job ad data.
    """
    name = "job_ads"
    allowed_domains = ["jobs.porsche.com"]

    def __init__(self, inputfile=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls =  ['https://jobs.porsche.com/index.php?ac=jobad&id=' + str(item) for item in np.load(inputfile)]

    def parse(self, response):
        """
        Parses the job ad webpage and extracts relevant information.

        Args:
            response (scrapy.http.Response): The response object representing the webpage.

        Yields:
            dict: A dictionary containing the extracted job ad data.
        """
        data = {}

        data["title"] = response.css("h1.margin-bottom-gutter::text").get()

        nested_job_content = response.css("span.jobad-base-info-content::text").getall()
        data["code"] = nested_job_content[0]
        data["entry_type"] = nested_job_content[1]
        data["location"] = nested_job_content[2]
        data["company"] = nested_job_content[3]

        tasks = []
        task_elements = response.xpath('//*[@id="aria-panel-task"]/div/ul/li/span')
        for task_element in task_elements:
            task = task_element.xpath("text()").get()
            tasks.append(task)
        data["tasks"] = tasks

        requirements = []
        requirement_elements = response.xpath('//*[@id="aria-panel-your-profile"]/div/ul/li/span')
        for requirement_element in requirement_elements:
            requirement = requirement_element.xpath("text()").get()
            requirements.append(requirement)
        data["requirements"] = requirements

        yield data
