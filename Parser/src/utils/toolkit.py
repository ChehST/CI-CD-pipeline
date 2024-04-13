import cloudscraper
# Add imports here


# returns requests Response object. It is able to bypass CFP
def get_response_bypassed(url):
    scraper = cloudscraper.create_scraper()
    try:
        requested_html = scraper.get(url)
        return requested_html
    except:
        print(requested_html.status_code)
        return requested_html.status_code

# Ad counter function. It count ads per 1 page PAR-23
def ad_counter(ads):
    pass

# function that return html code from file
def get_html_f(file):
    with open(file,'r',encoding="utf-8") as html:
        html_plain = html.read()
    return html_plain
