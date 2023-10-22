import scrapy

class MySpider(scrapy.Spider):
    name = 'example'

    start_urls = ['https://cs50.harvard.edu/python/2022/']

    def parse(self, response):
        headers = response.css('h1, h2, h3, h4')
        data = {}
        current_header = None

        for header in headers:
            if header.xpath('self::h1'):
                current_header = header.xpath('string()').get()
                data[current_header] = ''
            else:
                if current_header:
                    data[current_header] += f"#{header.xpath('string()').get()}\n"

        with open('output.md', 'w') as f:
            for key, value in data.items():
                f.write(f"# {key}\n\n{value}\n\n")

def main():
    my_spider = MySpider()
    my_spider.parse()

if __name__ == "__main__":
    main()
