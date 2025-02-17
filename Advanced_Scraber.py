from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import validators

Visited_urls = set() # to put uniq links

def scrab(url , keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Failed To Connect With Your Target {url}")
        return
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        #print(soup)

        items = [] # to put links and non links then validate them.

        a_tag = soup.find_all("a")
        link_tag = soup.find_all("link")
        for tag in link_tag:
            href = tag.get("href")
            if href is not None and href != '':
                items.append(href)
        for tag in a_tag:
            href2 = tag.get("href")
            if href2 is not None and href2 != '':
                items.append(href2)
        valid_links = [item for item in items if validators.url(item)]
        #print(valid_links)

        for urls2 in valid_links:
            if urls2 not in Visited_urls:
                Visited_urls.add(urls2)
                #print(urls2)
                if keyword in urls2:
                    print(urls2)
                    scrab(urls2,keyword) # We call function again to deep recursive pages
            else:
                pass



url = input("Enter Your Target: ").strip()
keyword = input("Enter Your Keyword: ").strip()
scrab(url,keyword)
