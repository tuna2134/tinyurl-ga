import requests

def create(url):
    r = requests.post("https://tinyurl.ga/api", json = {"url": url})
    return result(r.json())
    
class result:
    def __init__(self, data):
        self.data = data
        
    @property
    def url(self) -> str:
        return self.data["url"]
