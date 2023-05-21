import os
import json
import re
import jinja2
import pdfkit
from config import PROJECT_ROOT


class JobPdfGenerator:
    def __init__(self, template_path, job_data_path):
        """
        Initialize the JobPdfGenerator class.

        Args:
            template_path (str): The path to the directory containing the HTML template file.
            job_data_path (str): The path to the JSON file containing job data.
        """
        self.template_loader = jinja2.FileSystemLoader(template_path)
        self.template_env = jinja2.Environment(loader=self.template_loader)
        self.job_data_path = job_data_path
        self.job_data = {}

    def load_job_data(self):
        """
        Load job data from the specified JSON file.
        """
        with open(self.job_data_path, 'r') as file:
            self.job_data = json.load(file)

    def generate_pdfs(self):
        """
        Generate PDF files based on the loaded job data and the provided HTML template.

        This method generates PDF files containing job data information based on the provided template and job data.
        The method converts the job data into the required format and renders it using the Jinja2 template engine.
        The resulting HTML is then converted to a PDF using pdfkit.

        Note: The path to the 'wkhtmltopdf' binary is set to '/usr/local/bin/wkhtmltopdf'. Adjust it according to your environment.
        """
        for job in self.job_data:
            context = {
                'title': job['title'],
                'code': job['code'],
                'entry_type': job['entry_type'],
                'location': job['location'],
                'company': job['company'],
                'tasks': '\n'.join(f'<li>{task}</li>' for task in job['tasks']),
                'requirements': '\n'.join(f'<li>{requirement}</li>' for requirement in job['requirements'])
            }

            template = self.template_env.get_template('template.html')
            output_text = template.render(context)

            job_id = re.search(r'\d+', job['code']).group().lstrip('0')

            config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
            filename = f"{job_id}.pdf"
            output_path = os.path.join(PROJECT_ROOT, "results", "generated_pdfs", filename)
            css_path = os.path.join(PROJECT_ROOT, 'src', 'pdfgen', 'style.css')

            pdfkit.from_string(output_text, output_path, configuration=config, css=css_path)

    def generate_info_pdfs(self):
        """
        Generates PDF files containing employer information.

        This method generates PDF files containing employer information based on the provided template and employer data.
        The method converts the job data into the required format and renders it using the Jinja2 template engine.
        The resulting HTML is then converted to a PDF using pdfkit.

        The generated PDF files are saved in the 'results/employer_info' directory with the filename 'employer_info.pdf'.

        Note: The path to the 'wkhtmltopdf' binary is set to '/usr/local/bin/wkhtmltopdf'. Adjust it according to your environment.
        """
        context = self.convert_to_array()

        template = self.template_env.get_template('template.html')
        output_text = template.render(data=context)

        config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

        filename = "employer_info.pdf"
        output_path = os.path.join(PROJECT_ROOT, "results", "employer_info", filename)
        css_path = os.path.join(PROJECT_ROOT, 'src', 'pdfgen', 'employer', 'style.css')

        pdfkit.from_string(output_text, output_path, configuration=config, css=css_path)

    def convert_to_array(self):
        """
        Converts the job data in the context into an array format.

        This method takes the job data stored in the context attribute and converts it into an array format. The job data
        should be a list of dictionaries, where each dictionary represents a job with 'title' and 'text' keys.

        Returns:
            list: A list of dictionaries in the following format: [{'title': title1, 'text': text1},...]
        """
        context = self.job_data

        array = [{'title': title, 'text': text} for title, text in zip(context[0]['title'], context[0]['text'])]

        return array
