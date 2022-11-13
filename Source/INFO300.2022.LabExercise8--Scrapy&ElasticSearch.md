# Scrapy & ElasticSearch

October 21, 2022

1. Learn the architecture of scrapy
2. Create a project of Scrapy
3. Store the data in the ElasticSearch via pipeline of Scrapy

## The architecture of scrapy

<img src="scrapy_architecture_02.png">

You can learn from:


https://docs.scrapy.org/en/latest/topics/architecture.html


## Create a project of scrapy

### 0. Install Scrapy
To install Scrapy using conda, run:
```
conda install -c conda-forge scrapy
```
or

To install Scrapy using pip, run:
```
pip install Scrapy
```

### 1. Run the following command to create a project of scrapy

```
scrapy startproject helloworld_scrapy
```
This will create a helloworld_scrapy directory with the following contents:

```
helloworld_scrapy/
    scrapy.cfg            # deploy configuration file

    helloworld_scrapy/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file, you will use the file in the ScrapyElasticSearch part

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```

### 2. Create your first Spider

This is the code for our first Spider. Save it in a file named hello_spider.py under the helloworld_scrapy/spiders directory in your project:

```python
import scrapy


class HelloSpider(scrapy.Spider):
    name = "hello"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'hello-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

```
We create a Spider subclasses scrapy.Spider and defines some attributes and methods:

* **name**: identifies the Spider. It must be unique within a project, that is, you can’t set the same name for different Spiders.

* **start_requests()**: must return an iterable of Requests (you can return a list of requests or write a generator function) which the Spider will begin to crawl from. Subsequent requests will be generated successively from these initial requests.

* **parse()**: a method that will be called to handle the response downloaded for each of the requests made. The response parameter is an instance of TextResponse that holds the page content and has further helpful methods to handle it.

### 3. Run your spider

To put our spider to work, go to the project’s top level directory and run:

```
scrapy crawl quotes
```

### 4. A shortcut to the start_requests method

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
```

### 5. Extracting data by CSS (XPath)

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes-data"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
```

### 6. Run your spider

To put our spider to work, go to the project’s top level directory and run:

```
scrapy crawl quotes-data -O quotes_data.json
```

That will generate a quotes_data.json file containing all scraped items, serialized in JSON.

Notes: The **-O** command-line switch overwrites any existing file; use **-o** instead to append new content to any existing file.

### 7. Following links

Instead of just scraping the stuff from the first two pages from https://quotes.toscrape.com, let's quotes from all the pages in the website.

```python

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes-whole-site"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

```

Now, after extracting the data, the parse() method looks for the link to the next page, builds a full absolute URL using the urljoin() method (since the links can be relative) and yields a new request to the next page, registering itself as callback to handle the data extraction for the next page and to keep the crawling going through all the pages.

A shortcut for creating Requests:
```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

```
Unlike **scrapy.Request**, **response.follow** supports relative URLs directly - no need to call urljoin. Note that **response.follow** just returns a Request instance; you still have to yield this Request.

### 8. More examples and patterns

```Python
import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author-all'

    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
```

This spider will start from the main page, it will follow all the links to the authors pages calling the parse_author callback for each of them, and also the pagination links with the parse callback as we saw before.

The parse_author callback defines a function to extract and cleanup the data from a CSS query and yields the Python dict with the author data.

Another interesting thing this spider demonstrates is that, even if there are many quotes from the same author, we don’t need to worry about visiting the same author page multiple times. By default, Scrapy filters out duplicated requests to URLs already visited, avoiding the problem of hitting servers too much because of a programming mistake. This can be configured by the setting DUPEFILTER_CLASS.

## Store scrapy items in Elastic Search

Scrapy pipeline which allows you to store scrapy items in Elastic Search.

### 0. Install scrapy-elasticsearch

Run the following command to install ScrapyElasticSearch:
```
pip install ScrapyElasticSearch
```

### 1. Configure settings.py (the file is in your Scrapy project folder):

```python
ITEM_PIPELINES = {
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 500
}

ELASTICSEARCH_SERVERS = ['121.43.234.160']
ELASTICSEARCH_PORT = 9200 # If port 80 leave blank
ELASTICSEARCH_USERNAME = 'your_username'
ELASTICSEARCH_PASSWORD = 'your_password'
ELASTICSEARCH_INDEX_DATE_FORMAT = '%Y-%m'
ELASTICSEARCH_INDEX = 'suwei_author_scrapy'
ELASTICSEARCH_TYPE = '_doc'

# ELASTICSEARCH_UNIQ_KEY = 'url'  # Custom unique key

# can also accept a list of fields if need a composite key
# ELASTICSEARCH_UNIQ_KEY = ['url', 'id']
```
### 2. Re-run the above scrapy crawler:

```
scrapy crawl author-all
```

### 3. Run the following command in the ElasticSearch:

```json
GET /suwei_author_scrapy/_search
{
  "query": {
    "match_all": {}
  }
}
```
Now you can see author data in the ElasticSearch crawled by scrapy.

## Further work
You can try crawl a whole website, such as LZU, or Douban.

You can learn more scrapy from here:
https://docs.scrapy.org/en/latest/intro/tutorial.html

You can learn more scrapy-elasticsearch from here:
https://github.com/jayzeng/scrapy-elasticsearch
