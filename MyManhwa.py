from bs4 import BeautifulSoup
import cloudscraper


class Manhwa():
    def __init__(self, url):
        
        self.domain = url.split("//")[-1].split("/")[0].replace("www.", "")
        sites = {"asurascans.com": self.mangaStream,
                 "void-scans.com": self.mangaStream,
                 "flamescans.org": self.mangaReader,
                 "reaperscans.com": self.reaper
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
            self.image = None
        
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
            self.image = None
        
        infos = soup.findAll("div", class_="imptdt")
        self.status = infos[0].text.strip()
        self.type = infos[1].text.strip().split()[1]
        self.tags = soup.find("span", class_="mgen").text.split()
        
        self.chapters = []
        ch = soup.find("div", class_="eplister").findAll("li")
        for c in ch:
            self.chapters.append(c.find('a')['href'])
 
            
    def reaper(self, url):
        scraper = cloudscraper.create_scraper()
        soup = BeautifulSoup(scraper.get(url).content, "html.parser")
        self.title = soup.find("h1", class_="focus:outline-none font-semibold text-xl text-neutral-700 dark:text-white lg:mt-0 truncate").text.strip()
        self.description = soup.find("p", class_="focus:outline-none prose lg:prose-sm dark:text-neutral-500 mt-3 w-full").text.strip()
        self.rating = None
        self.status = soup.findAll("dd", class_="whitespace-nowrap text-neutral-200")[3].text.strip()
        try:
            self.image = soup.find("div", class_="transition min-h-80 aspect-w-1 aspect-h-1 w-full overflow-hidden rounded lg:aspect-none").find("img")['src']
        except:
            self.image = None
        self.type = None
        self.tags = None
        
        self.chapters = []
        ch = soup.find("ul", role="list").findAll("li")
        for c in ch:
            self.chapters.append(c.find('a')['href'])

class ManhwaChapter():
    def __init__(self, url):
        
        self.domain = url.split("//")[-1].split("/")[0].replace("www.", "")
        sites = {"asurascans.com": self.mangaStream,
                 "void-scans.com": self.mangaStream,
                 "flamescans.org": self.mangaReader,
                 "reaperscans.com": self.reaper
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
        
        self.getNextPrev(url)
              
    def mangaReader(self, url):
        self.mangaStream(url)
        
    
    def reaper(self, url):
        scraper = cloudscraper.create_scraper()
        r = scraper.get(url).content
        
        soup = BeautifulSoup(r, 'html.parser')
        s = soup.findAll("img", class_="max-w-full mx-auto display-block")
        self.pages = self.getLinks(s)
        self.name = soup.find("p", class_="text-2xl font-semibold text-neutral-400 sm:text-3xl lg:text-3xl").text.strip()
        self.manhwa = '/'.join(url.split("/")[:5])
        
        self.getNextPrev(url)
        
        
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
    
    def getNextPrev(self, url):
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
        
        
"""
        scraper = cloudscraper.create_scraper()
        soup = BeautifulSoup(scraper.get(url).content, "html.parser")
        self.title = soup.find("div", class_="overflow-hidden").text.strip()
        self.description = ""
        self.rating = ""
        self.image = ""
        self.status = ""
        self.type = ""
        self.tags = ""
        self.chapters = ""
        
        
        self.pages = ""
        self.name = ""
        self.manhwa = ""
        self.next = ""
        self.prev = ""       
"""