import os
import subprocess
from config import URL, DATA_PATH, PROJECT_ROOT
from src.fetch_jobids import JobUrlScraper
from src.pdfgen.generate_pdf import JobPdfGenerator


if __name__ == "__main__":
    print("########### Started fetching jobids ###########")
    id_output_file = os.path.join(DATA_PATH, "job_ids.npy")
    scraper = JobUrlScraper(URL, id_output_file)
    scraper.scrape_job_urls()
    print(f"########### Finished saving jobids in {id_output_file} ###########")

    print("########### Started scrapy crawl ###########")
    output_file = os.path.join(DATA_PATH, "scraped_jobs.json")
    command = f"scrapy crawl job_ads -a inputfile={id_output_file} -o {output_file} --nolog"    
    try:
        os.chdir(os.path.join(PROJECT_ROOT, "src", "jobads_scrapy"))
        
        subprocess.run(command, shell=True, check=True)
        os.chdir(PROJECT_ROOT)
        print("Scrapy command executed successfully.")
    except subprocess.CalledProcessError as e:
        os.chdir(PROJECT_ROOT)
        print(f"An error occurred while running the Scrapy command: {e}")
    print(f"########### Saved scraped urls in {output_file} ###########")

    print("########### Started generating pdfs ###########")
    template_path = os.path.join(PROJECT_ROOT, "src", "pdfgen")
    job_data_path = os.path.join(output_file)
    pdf_generator = JobPdfGenerator(template_path, job_data_path)
    pdf_generator.load_job_data()
    pdf_generator.generate_pdfs()
    pdf_output = os.path.join(DATA_PATH, "results", "generated_pdfs")
    print(f"########### Saved pdfs in {pdf_output} ###########")
