from bs4 import BeautifulSoup
import cloudscraper


class Manhwa():
    
    def __init__(self, url):
        
        self.domain = url.split("//")[-1].split("/")[0].replace("www.", "")
        sites = {"asurascans.com": self.mangaStream,
                 "void-scans.com": self.mangaStream,
                 "flamescans.org": self.mangaReader
                 }
        if self.domain in sites:
            sites[self.domain](url)
        else:
            raise ValueError(f"The website is not supported: {self.domain}")



    def mangaStream(self, url):
        scraper = cloudscraper.create_scraper()
        soup = BeautifulSoup(scraper.get(url).content, "html.parser")

        self.title = soup.find("h1", class_="entry-title").text.strip()
        self.description = soup.find(itemprop="description").text.strip()
        self.rating = soup.find("div", class_="num").text.strip()
        
        try:
            self.image = soup.find("div", class_="thumb").find("img")['src']
        except:
            pass
        
        infos = soup.findAll("div", class_="imptdt")
        self.status = infos[0].text.strip().split()[1]
        self.type = infos[1].text.split(" ")[1].strip()
        
        self.tags = soup.find("span", class_="mgen").text.split()

        self.chapters = []
        ch = soup.findAll("div", class_="eph-num")
        for c in ch:
            self.chapters.append(c.find('a')['href'])
    
    def mangaReader(self, url):
        scraper = cloudscraper.create_scraper()
        soup = BeautifulSoup(scraper.get(url).content, "html.parser")
        self.title = soup.find("h1", class_="entry-title").text.strip()
        self.description = soup.find(itemprop="description").text.strip()
        self.rating = soup.find("div", class_="numscore").text.strip()
        
        try:
            self.image = soup.find("div", class_="thumb").find("img")['src']
        except:
            pass
        
        infos = soup.findAll("div", class_="imptdt")
        self.status = infos[0].text.strip()
        self.type = infos[1].text.strip().split()[1]
        self.tags = soup.find("span", class_="mgen").text.split()
        
        self.chapters = []
        ch = soup.find("div", class_="eplister").findAll("li")
        for c in ch:
            self.chapters.append(c.find('a')['href'])

class ManhwaChapter():
    def __init__(self, url):
        
        self.domain = url.split("//")[-1].split("/")[0].replace("www.", "")
        sites = {"asurascans.com": self.mangaStream,
                 "void-scans.com": self.mangaStream,
                 "flamescans.org": self.mangaReader
                 }
        if self.domain in sites:
            sites[self.domain](url)
        else:
            raise ValueError(f"The website is not supported: {self.domain}")
            
    
    
    def mangaStream(self, url):
        scraper = cloudscraper.create_scraper()
        r = scraper.get(url).content
        
        soup = BeautifulSoup(r, 'html.parser')
        s = soup.find("div", "rdminimal").findAll("img", loading="lazy")
        
        self.pages = self.getLinks(s)
        self.name = soup.find("div", class_="allc").find("a").text.strip()
        self.manhwa = soup.find("div", class_="allc").find("a")['href']
        
        chapter_links = Manhwa(self.manhwa).chapters
        curr = chapter_links.index(url)
        
        if curr - 1 < 0:
            self.next = None
        else:
            self.next = chapter_links[curr - 1]
        
        if curr + 1 >= len(chapter_links):
            self.prev = None
        else:
            self.prev = chapter_links[curr  + 1]
    
    def getLinks(self, html):
        links = []
        for h in html:
            try:
                links.append(h['src'])
            except:
                pass
        
        if links == None:
            getLinks(html)
        else:
            return links
        
        
    def mangaReader(self, url):
        self.mangaStream(url)