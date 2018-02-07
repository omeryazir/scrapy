<img src="https://www.22nds.com/wp-content/uploads/2017/07/scrapy-e1501276846765.png">
<article class="markdown-body entry-content" itemprop="text"><h1><a href="#scrapy" aria-hidden="true" class="anchor" id="user-content-scrapy"></a>README Scrapy</h1>
<p>This project was created to learn <b>Scrapy</b></p>


<h2><a href="#table-of-contents" aria-hidden="true" class="anchor" id="user-content-table-of-contents"></a>Table of Contents</h2>

<ul>
<li><a href="#what">What is Scrapy ?</a></li>
<li><a href="#alternatives">Alternatives to Scrapy</a></li>
<li><a href="#commands">Scrapy Commands</a></li>
<li><a href="#howtoinstall">How to install Scrapy ?</a></li>
<li><a href="#quickstart">Quick Start Demo</a></li>
</ul>

<h2><a href="#what" aria-hidden="true" class="anchor" id="user-content-what"></a>What is Scrapy ?</h2>
<q>An open source and collaborative framework for extracting the data you need from websites.Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival</q>


<h2><a href="#alternatives" aria-hidden="true" class="anchor" id="user-content-alternatives"></a>Alternatives to Scrapy</h2>
  <li><a href="http://lxml.de/"> LXML</a></li>
  <li><a href="http://www.seleniumhq.org/">  Selenium</a></li>
  <li><a href="http://docs.python-requests.org/en/master/">  Request</a></li>
  <li><a href="https://pypi.python.org/pypi/mechanize/">   Mechanize</a></li>
  <li><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">   Beautiful Soup 4</a></li>


<h2></h2>
<h2><a href="#commands" aria-hidden="true" class="anchor" id="user-content-commands"></a>Scrapy commands</h2>
  <b>Global commands:</b>
  <pre>
  $ scrapy startproject myproject  </pre>
  <pre>
  $ scrapy genspider example example.com
  Created spider 'example' using template 'basic'  </pre>
  <pre>
  $ scrapy settings --get BOT_NAME
  scrapybot  </pre>
  <pre>
  scrapy runspider myspider.py
  [ ... spider starts crawling ... ]  </pre>
  <pre>
  $ scrapy fetch --nolog http://www.example.com/some/page.html
  [ ... html content here ... ]  </pre>
  <pre>
  $ scrapy view http://www.example.com/some/page.html
  [ ... browser starts ... ]  </pre>
  <pre>
  $ scrapy version [-v]  </pre>


  <b>Project-only commands:</b>
  <pre>
  $ scrapy crawl myspider
  [ ... myspider starts crawling ... ]  </pre>
  <pre>
  $ scrapy check -l  </pre>
  <pre>
  $ scrapy list  </pre>
  <pre>
  $ scrapy edit spider1  </pre>
  <pre>
  $ scrapy bench  </pre>
  <pre>
  $ scrapy shell http://www.example.com/some/page.html
  [ ... scrapy shell starts ... ]  </pre>
  <pre>
  $ scrapy parse http://www.example.com/ -c parse_item
  [ ... scrapy log lines crawling example.com spider ... ]  </pre>

<h2><a href="#howtoinstall" aria-hidden="true" class="anchor" id="user-content-howtoinstall"></a>How to install Scrapy ?</h2>
<p>Install the latest version of Scrapy</p>

<pre>$ pip install scrapy</pre>
If you want work to virtual enviroment.
<pre>
$ python3 -m venv env_name
$ cd env_name
$ pip install scrapy
</pre>


<h2><a href="#quickstart" aria-hidden="true" class="anchor" id="user-content-quickstart"></a>Quick Start Demo</h2>

My spiders do crawls on the https://stackoverflow.com/ in this project.
<pre>
$ scrapy startproject scrapy_example
New Scrapy project 'scrapy_example', using template directory '/your_directory/scrapy_example/lib/python3.5/site-packages/scrapy/templates/project', created in:
    /your_directory/scrapy_example/scrapy_example

You can start your first spider with:
    cd scrapy_example
    scrapy genspider example example.com
</pre>


<pre>
├── scrapy.cfg            # deploy configuration file
└── scrapy_example        # project's Python module, you'll import your code from here
    ├── __init__.py       
    ├── items.py          # project items definition file
    ├── middlewares.py    # project middlewares file
    ├── pipelines.py      # project pipelines file
    ├── __pycache__
    ├── settings.py       # project settings file
    └── spiders           # a directory where you'll later put your spiders
        ├── __init__.py
        └── __pycache__
</pre>


Create myspider
<pre>
$ scrapy genspider stackoverflow  https://stackoverflow.com
Created spider 'stackoverflow' using template 'basic' in module:
  scrapy_example.spiders.stackoverflow
</pre>

Now, let's work on scrapy shell
<pre>
$ scrapy shell https://stackoverflow.com/

[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x7f6a64ad72e8>
[s]   item       {}
[s]   request    <GET https://stackoverflow.com/>
[s]   response   <200 https://stackoverflow.com/>
[s]   settings   <scrapy.settings.Settings object at 0x7f6a5e8239e8>
[s]   spider     <DefaultSpider 'default' at 0x7f6a5dc1a630>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser</pre>


<img src="http://i68.tinypic.com/t0ohlx.png" >

<pre>
$ response.css('.question-summary')
$ question = response.css('.question-summary')
$ q = question[0]
$ q.css('.question-hyperlink').extract_first()
$ q.css('.question-hyperlink::text').extract_first()
</pre>

<br>
<b>spiders/stackoverflow.py</b>
<pre>
import scrapy
from ..items import ScrapyExampleItem

class StackoverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    allowed_domains = ['https://stackoverflow.com']
    start_urls = ['https://stackoverflow.com']

    def parse(self, response):
        question = response.css('.question-summary')
        for q in question:
            title = q.css('.question-hyperlink::text').extract_first()
            item = ScrapyExampleItem()
            item ['title'] = title
            yield item

</pre>
<br>
<b>items.py</b>
<pre>
import scrapy
class ScrapyExampleItem(scrapy.Item):
&nbsp;&nbsp;&nbsp;title = scrapy.Field()
</pre>

<br>
<br>Result to crawl on stackoverflow
<pre>
$ scrapy crawl stackoverflow</pre>

Save results to questions.jl
<pre>
$ scrapy crawl stackoverflow --set FEED_URI=questions.jl</pre>
Or
Save results to result.json
<pre>
$ scrapy crawl stackoverflow -o result.json</pre>
</article>
