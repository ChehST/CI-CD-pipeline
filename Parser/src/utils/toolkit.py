import cloudscraper
# Add imports here


# Get plain html text
def get_html(url):
    scraper = cloudscraper.create_scraper()
    try:
        requested_html = scraper.get(url)
        return requested_html.text
    except:
        print(requested_html.status_code)
        return requested_html.status_code

# Ad counter function. It count ads per 1 page PAR-23
def ad_counter(ads):
    pass