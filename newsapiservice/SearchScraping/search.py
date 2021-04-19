import requests
import re
from bs4 import BeautifulSoup


def scrapeLink(query):
    query = query.replace(" ","+")
    if "meaning" in query:
        query.replace("meaning", "dictionary")
    url = f"https://google.com/search?q={query}"

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    headers = {"User_Agent": USER_AGENT}
    result_query = requests.get(url, headers=headers)
    result_url_page = str()
    result_url_link = list()
    if result_query.status_code == 200:
        soup = BeautifulSoup(result_query.text, 'html.parser')
        a_soup = soup.find_all('a')
        
        #save all link
        for i in a_soup:
            a_tag = i.get('href')
            # href = re.search("(?P<url>https?://[^\s]+)", a_tag)
            href = a_tag
            if href is not None and "/url?q=" in href:
                word = href.split("/url?q=")[1]
                if "&" in word:
                    word = word.split("&")[0]
                if "%" in word:
                    word = word.split("%")[0]
                result_url_link.append(word)

        #get one best link to scrape
        for i in a_soup:
            href = i.get('href')
            if href is not None and "/url?q=" in href:
                word = href.split("/url?q=")[1]
                if "&" in word:
                    word = word.split("&")[0]
                if "%" in word:
                    word = word.split("%")[0]
                result_url_page = word
                if "wikipedia" in query and "wikipedia" not in result_url_page:
                        continue
                if "meaning" in query and "www.dictionary.com/browse" not in result_url_page:
                        continue
                if "indiatoday" in result_url_page or "business-standard" in result_url_page:
                    continue
                break
                # string = str(m).split(", ")[2][7:-2]
                # print(string)
                #print(m)  
    return result_url_page,result_url_link





'''#savefile.commemt'''
# f = open("query.txt",'w', encoding='utf-8')
# for link in a_soup:
#     f.write(str(link))
#     f.write('\n')
# f.close()
# f2 = open("href.txt", 'w', encoding='utf-8')
# for i in a_soup:
#     a_tag = i.get('href')
#     # href = re.search("(?P<url>https?://[^\s]+)", a_tag)
#     href = a_tag
#     if href is not None and "/url?q=" in href:
#         word = href.split("/url?q=")[1]
#         if "&" in word:
#             word = word.split("&")[0]
#         if "%" in word:
#             word = word.split("%")[0]
#         f2.write(str(word)) 
#         f2.write('\n')
# f2.close()

