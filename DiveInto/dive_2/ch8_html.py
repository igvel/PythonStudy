__author__ = 'ielkin'

from sgmllib import SGMLParser


class URLLister(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):
        href = [v for k, v in attrs if k == 'href']
        if href:
            self.urls.extend(href)

# Dictionary based formatting
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print "%(pwd)s" % params

if __name__ == '__main__':
    import urllib

    proxies = {'http': 'http://172.20.64.254:8080'}
    url = 'http://microsoft.com'
    sock = urllib.urlopen(url, proxies=proxies)
    htmlSource = sock.read()
    sock.close()

    parser = URLLister()
    parser.feed(htmlSource)
    parser.close()
    for url in parser.urls: print url
