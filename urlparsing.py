import urlparse

host = "http://ddn.com/"
api = "api/"
end = "person"

# url = urlparse.urljoin("http://ddn.com", "api", "person")

url = reduce(lambda a, x: urlparse.urljoin(a, x), [host, api, end])

print url