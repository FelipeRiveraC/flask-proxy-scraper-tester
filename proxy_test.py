import requests
import threading

class ProxyTest:
  def __init__(self, proxies, num_threads = 10, timeout = 5):
    self.proxies = proxies
    self.checked_proxies = []
    self.num_threads = num_threads
    self.timeout = timeout
    self.threads = []
  
  def return_first_working_proxy(self):
    for proxy in self.proxies:
      if self.test_proxy(proxy):
        return proxy
    return None

  def test_proxy(self, proxy):
    print("Testing proxy: " + proxy)
    try:
      response = requests.get("https://api.ipify.org?format=json", proxies = { "http"  : proxy}, timeout = self.timeout)
      if response.status_code == 200:
        self.checked_proxies.append(proxy)
        print("Proxy " + proxy + " checked and working!")
        return True
    except:
      print("Proxy " + proxy + " not working!")
      return False

  def test_proxies(self, proxies):
    for proxy in proxies:
      self.test_proxy(proxy)
  
  def assign_threads(self):
    chunks = [self.proxies[i:i + self.num_threads] for i in range(0, len(self.proxies), self.num_threads)]
    for chunk in chunks:
      thread = threading.Thread(target=self.test_proxies, args=(chunk,))
      self.threads.append(thread)
      thread.start()
    
    for thread in self.threads:
      thread.join()

    return self.checked_proxies



    
      

  

    
    

