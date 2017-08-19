from bs4 import BeautifulSoup
import urllib.request
import urllib



webpage=urllib.request.urlopen('https://www.youtube.com/playlist?list=PLm5ipifE5Hn5WyXlGVmspI7zlV5o8dZIy').read()
soup= BeautifulSoup(webpage,"html.parser")

playlist = soup.find_all('a',{'class':'pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link '})
i=1
for song in playlist:
    print(i,". ",song.text)
    i+=1