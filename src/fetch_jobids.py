import requests
import os
import numpy as np


class JobUrlScraper:
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file

    def scrape_job_urls(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()

            data = response.json()
            job_ids = []

            for item in data["SearchResult"]["SearchResultItems"]:
                job_ids.append(item["MatchedObjectDescriptor"]["ID"])

            np.save(self.output_file, np.array(job_ids))
            print("Job URLs saved to:", self.output_file)

        except requests.exceptions.RequestException as e:
            print("Error occurred:", e)
    