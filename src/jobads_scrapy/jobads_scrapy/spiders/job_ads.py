import scrapy
import os
import numpy as np
from config import DATA_PATH
import subprocess


#IDS = np.load(os.path.join(DATA_PATH, "job_ids.npy"))

class JobAdsSpider(scrapy.Spider):
    name = "job_ads"
    allowed_domains = ["jobs.porsche.com"]

    def __init__(self, inputfile=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls =  ['https://jobs.porsche.com/index.php?ac=jobad&id=' + str(item) for item in np.load(inputfile)]

    def parse(self, response):
        data = {}

        # Extract title, code, entry_type, location, and company
        data["title"] = response.css("h1.margin-bottom-gutter::text").get()
        data["code"] = response.xpath("/html/body/div[1]/main/div[5]/div/article/div/div[1]/ul/li[1]/span/text()").get()
        data["entry_type"] = response.xpath("/html/body/div[1]/main/div[5]/div/article/div/div[1]/ul/li[2]/span/text()").get()
        data["location"] = response.xpath("/html/body/div[1]/main/div[5]/div/article/div/div[1]/ul/li[3]/span/text()").get()
        data["company"] = response.xpath("/html/body/div[1]/main/div[5]/div/article/div/div[1]/ul/li[4]/span/text()").get()

        # Extract tasks dynamically
        tasks = []
        task_elements = response.xpath("/html/body/div[1]/main/div[5]/div/article/div/div[2]/div[1]/div[1]/div/div/div/ul/li/span")
        for element in task_elements:
            task = element.xpath("text()").get()
            tasks.append(task)
        data["tasks"] = tasks

        # Extract requirements dynamically
        requirements = []
        requirement_elements = response.xpath("/html/body/div[1]/main/div[5]/div/article/div/div[2]/div[1]/div[2]/div/div/div/ul/li/span")
        for element in requirement_elements:
            requirement = element.xpath("text()").get()
            requirements.append(requirement)
        data["requirements"] = requirements

        yield data
