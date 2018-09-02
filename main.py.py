import urllib2
import urllib
from bs4 import BeautifulSoup

def currentWeather(zipcode):
    url = 'https://forecast.weather.gov/zipcity.php'
    data = urllib.urlencode({'inputstring': str(zipcode)})

    req = urllib2.Request(url=url, data=data)
    resp = urllib2.urlopen(req)
    content = resp.read()
    soup = BeautifulSoup(content, "lxml")
    forcast = soup.find(id="current_conditions-summary")
    for item in forcast.find_all("p"):
        print item.text



