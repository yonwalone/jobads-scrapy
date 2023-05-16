import os
import json
import re
import jinja2
import pdfkit
from config import PROJECT_ROOT


class JobPdfGenerator:
    def __init__(self, template_path, job_data_path):
        self.template_loader = jinja2.FileSystemLoader(template_path)
        self.template_env = jinja2.Environment(loader=self.template_loader)
        self.job_data_path = job_data_path
        self.job_data = {}

    def load_job_data(self):
        with open(self.job_data_path, 'r') as file:
            self.job_data = json.load(file)

    def generate_pdfs(self):
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



# template_loader = jinja2.FileSystemLoader(os.path.join(PROJECT_ROOT, 'src', 'pdfgen'))
# template_env = jinja2.Environment(loader=template_loader)

# job_data_path = "/Users/sok1ush/Development/jobads_scrapy/data/scraped_jobs.json"

# with open(job_data_path, 'r') as file:
#     job_data = json.load(file)

# for job in job_data:
#     context = {
#             'title': job['title'],
#             'code': job['code'],
#             'entry_type': job['entry_type'],
#             'location': job['location'],
#             'company': job['company'],
#             'tasks': '\n'.join(f'<li>{task}</li>' for task in job['tasks']),
#             'requirements': '\n'.join(f'<li>{requirement}</li>' for requirement in job['requirements'])
#     }

#     # os.path.join(PROJECT_ROOT, 'src', 'pdfgen','template.html')
#     template = template_env.get_template('template.html')
#     output_text = template.render(context)

#     job_id = re.search(r'\d+', job['code']).group().lstrip('0')
    
#     config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
#     filename = f"{job_id}.pdf"
#     output_path = os.path.join(PROJECT_ROOT, "results", "generated_pdfs", filename)
#     pdfkit.from_string(
#         output_text, 
#         output_path, 
#         configuration=config, 
#         css=os.path.join(PROJECT_ROOT, 'src', 'pdfgen', 'style.css')
#     )


