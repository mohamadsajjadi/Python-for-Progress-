import re

s = "Twitter:www.twiter.com/alaviii Instagram:www.instagram.com/aalavi Degree:Master imdb:www.imdb.com/alavi"
s = s.split()
for item in s:
    print(re.findall(r"^[A-Z][a-z]+:www\.[a-z0-9\.]+\/[a-z0-9\_]+", item))
    item=item.split("/")[1]
    print(item)
