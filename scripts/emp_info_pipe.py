import os
import subprocess
from config import PROJECT_ROOT, DATA_PATH
from src.pdfgen.generate_pdf import JobPdfGenerator


if __name__ == "__main__":
    """
    This script provides functionality to scrape employer information and generate PDFs.

    The script performs the following tasks:
        1. Executes a Scrapy crawl command to scrape employer information from a website.
        The output is saved in a JSON file in the specified DATA_PATH.

        2. Generates PDFs containing employer information based on the scraped data.
        The PDFs are created using a template and saved in the specified output directory.
    """
    print("########### Started scrapy crawl ###########")
    output_file = os.path.join(DATA_PATH, "employer_info.json")
    command = f"scrapy crawl employer-info  -O {output_file} --nolog"    
    try:
        os.chdir(os.path.join(PROJECT_ROOT, "src", "jobads_scrapy"))
        
        subprocess.run(command, shell=True, check=True)
        os.chdir(PROJECT_ROOT)
        print("Scrapy command executed successfully.")
    except subprocess.CalledProcessError as e:
        os.chdir(PROJECT_ROOT)
        print(f"An error occurred while running the Scrapy command: {e}")
    print(f"########### Saved craped employer info in {output_file} ###########")

    print("########### Started generating pdfs ###########")
    template_path = os.path.join(PROJECT_ROOT, "src", "pdfgen", "employer")
    job_data_path = os.path.join(output_file)
    pdf_generator = JobPdfGenerator(template_path, job_data_path)
    pdf_generator.load_job_data()
    pdf_generator.generate_info_pdfs()
    pdf_output = os.path.join(DATA_PATH, "results", "employer_information")
    print(f"########### Saved pdfs in {pdf_output} ###########")