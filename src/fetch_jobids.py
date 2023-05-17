import requests
import numpy as np


class JobUrlScraper:
    def __init__(self, url, output_file):
        """
        Initializes the JobUrlScraper class.

        Args:
            url (str): The URL of the job search API.
            output_file (str): The path to the output file where job URLs will be saved.
        """
        self.url = url
        self.output_file = output_file

    def scrape_job_urls(self):
        """
        Scrape job URLs from the specified API and save them to the output file.
        """
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
    