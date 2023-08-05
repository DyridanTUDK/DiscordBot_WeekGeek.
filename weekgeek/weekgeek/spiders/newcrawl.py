import scrapy


class NewcrawlSpider(scrapy.Spider):
    name = "newcrawl"
    allowed_domains = ["techcrunch.com"]
    start_urls = ["https://techcrunch.com/"]
    def parse(self, response):
        # All selectors important selectors
        # Selecting the Title, Paragraph and Links
        containerDiv = response.css('.post-block--image')
        titles = containerDiv.css('.post-block__title__link::text').extract()
        paragraphs = containerDiv.css('.post-block__content::text').extract()
        links = containerDiv.css('.post-block__title__link::attr("href")').extract()
        # Arrays to contain + Check for repetative data
        all_Titles = []
        all_Paragraphs = []
        all_links = []
        # Filtrate data
        filtration(titles,all_Titles)
        filtration(paragraphs,all_Paragraphs)
        filtration(links,all_links)
        # yield extracts the value
        yield {'Title':all_Titles,"paragraph":all_Paragraphs, "links":all_links}

def filtration(inputArr, outputArr):
    # this function is reponsible for collecting the unfiltered texts with special characters such as \n or \t and filtrating it and filtering empty strings
    for input in inputArr:
        # .strip() gets rid of special characters.
        text = input.strip()
        if text != '':
            # check for empty strings.
            if text not in outputArr:
                # appends to output Array
                outputArr.append(text)