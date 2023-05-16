import os
import subprocess
from config import URL, DATA_PATH, PROJECT_ROOT
from src.fetch_jobids import JobUrlScraper


if __name__ == "__main__":
    id_output_file = os.path.join(DATA_PATH, "job_ids.npy")

    scraper = JobUrlScraper(URL, id_output_file)
    scraper.scrape_job_urls()

    output_file = os.path.join(DATA_PATH, "scraped_jobs.json")
    command = f"scrapy crawl job_ads -a inputfile={id_output_file} -o {output_file} --nolog"
    
    try:
        # Change the current working directory to the Scrapy project directory
        os.chdir(os.path.join(PROJECT_ROOT, "src", "jobads_scrapy"))
        
        # Execute the Scrapy command
        subprocess.run(command, shell=True, check=True)
        print("Scrapy command executed successfully.")
        os.chdir(PROJECT_ROOT)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the Scrapy command: {e}")
        os.chdir(PROJECT_ROOT)