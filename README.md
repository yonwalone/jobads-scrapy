<h1 align="center">
  <br>
  <a href="https://jobs.porsche.com/index.php?ac=search_result"><img src="/Users/sok1ush/Development/jobads_scrapy/github/spider.png" width="200"></a>
  <br>
  jobads-scrapy
  <br>
</h1>

<h4 align="center">A minimal webscraper for scraping porsche job ads from <a href="https://jobs.porsche.com/index.php?ac=search_result" target="_blank">jobs.porsche.com</a>.</h4>
<p align="center">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/yonwalone/jobads-scrapy">
<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/yonwalone/jobads-scrapy">
      <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/yonwalone/jobads-scrapy">
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

![PDF example](github/jobad_example.png)

## Key Feature

* Get URLs of Porsche job ads
  - Get URLs of the currently available jobs using Porsches API with variable filters.
* Get information of job ads from defined URLs
  - Run the scrapy spider to get the information from defined URLS
* Auto generate a PDF File based on HTML and css and scraped information

## How To Use

Clone the repository and nivagate into repo.
```bash
# Clone this repository
$ git clone https://github.com/yonwalone/jobads-scrapy.git

# Go into the repository
$ cd jobads-scrapy
```

It's recommended to use conda as package manager and virtual env:
* Create a conda venv with the environment.yml file
* Activate the environment
```bash
conda env create --file=environments.yml
conda activate py310-jobads-scrapy
```

Pip install additional packages that could not be installed using conda.
```bash
pip install jinja2
pip install pdfkit
```

> **Note**
> If you are using a different OS with different architecture some pip packages may be available via conda.

## Credits

This software uses the following open source packages:

- [NumPy](https://numpy.org/)
- [Scrapy](https://scrapy.org/)
- [PDFKit](https://pdfkit.org/)
- [Jinja2](https://jinja.palletsprojects.com/en/2.10.x/)

---
> GitHub [@yonwalone](https://github.com/yonwalone)


