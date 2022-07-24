# Write a function that when given a URL as a string, parses out
# just the domain name and returns it as a string. For example:
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"

import urllib.parse


def domain_name(url):
    if 'http' in url or 'https' in url:
        return urllib.parse.urlparse(url).netloc.split('.')[0]
    return urllib.parse.urlparse(url).path.split('.')[1]


print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))