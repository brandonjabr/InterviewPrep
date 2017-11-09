# Design a basic URL shortener
from urlparse import urlparse
def jabrURL(url):
    parse_url = urlparse(url)

    url_hash = hash(parse_url.netloc)
    if not url_hash:
        url_hash = hash(parse_url.path)

    print "Hash of URL is: ",url_hash

    new_url = "http://ja.br/" + str(abs(url_hash))[0:8]
    return new_url