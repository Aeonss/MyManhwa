from bs4 import BeautifulSoup
import cloudscraper


class Manhwa():
    def __init__(self, url):
        
        self.domain = url.split("//")[-1].split("/")[0].replace("www.", "")
        sites = {"asuratoon.com": self.mangaStream,
                 "void-scans.com": self.mangaStream,
                 "flamecomics.com": self.mangaReader,
                 "reaperscans.com": self.reaper,
                 "toonily.com": self.toonily,
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


    def toonily(self, url):
        scraper = cloudscraper.create_scraper()
        soup = BeautifulSoup(scraper.get(url).content, "html.parser")
        self.title = soup.find("div", class_="post-title").text.strip()
        self.description = soup.find("div", class_="summary__content").text.strip()
        self.rating = soup.find("span", class_="score font-meta total_votes").text.strip()
        try:
            self.image = soup.find("div", class_="summary_image").find("img")['src']
        except:
            self.image = None
        self.status = soup.findAll("div", class_="summary-content")[5].text.strip()
        self.type = None
        self.tags = soup.find("div", class_="genres-content").text.strip().split(", ")
        
        self.chapters = []
        ch = soup.findAll("li", class_="wp-manga-chapter")
        for c in ch:
            self.chapters.append(c.find('a')['href'])
    
    



class ManhwaChapter():
    def __init__(self, url):
        
        self.domain = url.split("//")[-1].split("/")[0].replace("www.", "")
        sites = {"asuratoon.com": self.mangaStream,
                 "void-scans.com": self.mangaStream,
                 "flamecomics.com": self.mangaStream,
                 "reaperscans.com": self.reaper,
                 "toonily.com": self.toonily,
                 }
        if self.domain in sites:
            sites[self.domain](url)
        else:
            raise ValueError(f"The website is not supported: {self.domain}")
        
        self.getNextPrev(url)

              
    def mangaStream(self, url):
        scraper = cloudscraper.create_scraper()
        r = scraper.get(url).content
        
        soup = BeautifulSoup(r, 'html.parser')
        s = soup.find("div", "rdminimal").findAll("img")
        self.pages = [img['src'] for img in s]
        self.name = soup.find("div", class_="allc").find("a").text.strip()
        self.manhwa = soup.find("div", class_="allc").find("a")['href']
        
    
    def reaper(self, url):
        scraper = cloudscraper.create_scraper()
        r = scraper.get(url).content
        
        soup = BeautifulSoup(r, 'html.parser')
        s = soup.find("div", class_="mx-auto max-w-2xl mt-8 lg:max-w-7xl").findAll("img")
        self.pages = [img['src'] for img in s]
        self.name = soup.find("p", class_="text-2xl font-semibold text-neutral-400 sm:text-3xl lg:text-3xl").text.strip()
        self.manhwa = '/'.join(url.split("/")[:5])

    
    def toonily(self, url):
        scraper = cloudscraper.create_scraper()
        r = scraper.get(url).content
        
        soup = BeautifulSoup(r, 'html.parser')
        s = soup.findAll("img", class_="wp-manga-chapter-img img-responsive lazyload effect-fade")
        
        self.pages = [img.get('data-src') for img in s]
        self.pages = [page.strip() for page in self.pages if page is not None]

        self.name = soup.find("div", class_="main-col col-md-12 col-sm-12").findAll("a")[1].text.strip()
        self.manhwa = '/'.join(url.split("/")[:5])
        
    
    def getNextPrev(self, url):
        if "void-scans" in url:
            url = url.replace("/1/", "/")
            
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