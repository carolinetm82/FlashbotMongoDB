from scrapy import Request
import scrapy
from pprint import pprint
import pymongo


class FlashbotSpider(scrapy.Spider):
    name = 'flashbot'
    allowed_domains = ['rss.jobsearch.monster.com']

    # Start the crawler at this URLs
    #start_urls = ['file:///home/caroline09/projects/job_search_engine_project/query_big_data.xml']
    start_urls = ['http://rss.jobsearch.monster.com/rssquery.ashx?q={query}']

    thesaurus = ["machine learning", "machine", "learning", "big data", "big", "data",
                 "accountant","actor","architect","barber","banker","carpenter","doctor","economist"]

    #thesaurus=["accountant"]

    LOG_LEVEL = "INFO"

    def parse(self, response):

        # We stat with this url
        url = self.start_urls[0]

        # Build and send a request for each word of the thesaurus
        for query in self.thesaurus:
            target = url.format(query=query)
            print("fetching the URL: %s" % target)
            if target.startswith("file://"):
                r = Request(target, callback=self.scrapit, dont_filter=True)
            else:
                r = Request(target, callback=self.scrapit)
            r.meta['query'] = query
            yield r

    def scrapit(self, response):
        query = response.meta["query"]


        # Scrap the data
        for doc in response.xpath("//item"):
            # Base item with query used to this response
            item = {"query": query}

            item["title"] = doc.xpath("title/text()").extract_first()
            item["description"] = doc.xpath("description/text()").extract_first()
            item["link"] = doc.xpath("link/text()").extract_first()
            item["pubDate"] = doc.xpath("pubDate/text()").extract_first()
            item["guid"] = doc.xpath("guid/text()").extract_first()
            #pprint(item, indent=2)
            #print("item scraped:", item["title"])
            yield item