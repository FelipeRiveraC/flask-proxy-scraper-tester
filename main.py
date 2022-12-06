from proxy_test import ProxyTest
from proxy_scraper import Scraper
from flask import Flask

app = Flask(__name__)

sources = [
  'https://free-proxy-list.net/',
  'https://www.us-proxy.org/',
  'https://www.socks-proxy.net/',
  'https://www.sslproxies.org/'    
]

@app.route('/all')
def scrape_and_test_proxies(sources=sources):
  scraper = Scraper(sources)
  scraper.scrape_multiple_sources()
  proxy_test = ProxyTest(scraper.proxies, num_threads = 20, timeout = 5)
  checked_proxies = proxy_test.assign_threads()
  return { "data": checked_proxies }

@app.route('/one')
def scrape_and_test_one_proxy():
  scraper = Scraper(sources)
  scraper.scrape_multiple_sources()
  proxy_test = ProxyTest(scraper.proxies, num_threads = 20, timeout = 5)
  return { "data" : proxy_test.return_first_working_proxy()}

if __name__ == '__main__':
  app.run(debug=True)



