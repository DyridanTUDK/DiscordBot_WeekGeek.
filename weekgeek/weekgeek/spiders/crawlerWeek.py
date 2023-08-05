import scrapy


class CrawlerweekSpider(scrapy.Spider):
    name = "crawlerWeek"
    allowed_domains = ["techcrunch.com"]
    start_urls = ["https://techcrunch.com/"]

    def parse(self, response):
            # title = response.css("article")
            header = response.css(".post-block__title__link::text").extract()
            paragraph = response.css(".post-block__content::text").extract()
            titleLink = response.css(".post-block__title__link::attr(href)").extract()
            top_para = response.css(".fi-main-block__subtitle::text").extract()
            print(titleLink)
            latestHeader = []
            latestParagraph = [top_para]
            latestTitleLink = []
            for head in header:    
                text = head.strip()
                if text != '':
                    if text not in latestHeader:
                        latestHeader.append(text)
            for para in paragraph:
                 text = para.strip()
                 if text !='':
                    if text not in latestParagraph:
                        latestParagraph.append(text)
            for title in titleLink:
                 text = title.strip()
                 if text != '':
                    latestTitleLink.append(text)
            yield {'array':latestHeader,'paragraph':latestParagraph,"titleLink":latestTitleLink}
