import requests
from bs4 import BeautifulSoup
#new_storylising_contentwrap

def findTextContent(soup, class_content=None):
    result = list()
    result_href = list()
    # f = open("resource_query.txt","w", encoding='utf-8')
    for i in class_content:
        div_tag = soup.find_all('div', class_=class_content)
        for tag in div_tag:
            a_tag = tag.find_all('a')
            for atag in a_tag:
                value = str(atag.get_text()).strip()
                value_href = atag.get('href')
                if value is not "" and value_href is not None:
                    result.append(value)
                    result_href.append(value_href)
                    # f.write(value)
                    # f.write("\n")
                    # f.write(str(value_href))
                    # f.write("\n")
                if len(result)>10:
                    return result,result_href
    #             f.write('\n')
    # f.close()
    return result,result_href
def findTextContentMeaning(soup, class_content=None):
    result = list()
    result_href = list()
    for i in class_content:
        div_tag = soup.find_all('div', class_=class_content)
        for tag in div_tag:
            s_tag = tag.find_all('span')
            for stag in s_tag:
                if stag is not None:
                        result.append(stag.text)
                        a_tag = (stag.find('a'))
                        if a_tag is not None:
                            result_href.append(a_tag.text)
    if result is not None and result_href is not None:
        return result[:7],result_href
    else:
        return None,None

def findTextContentWiki(soup, class_content=None):
    result = []
    # f = open("resource_query.txt","w", encoding='utf-8')
    for i in class_content:
        div_tag = soup.find_all('div', class_=class_content)
        for tag in div_tag:
            a_tag = tag.find_all('p')
            for atag in a_tag:
                value = str(atag.get_text()).strip()
                if value is not "":
                    result.append(value)
                    # f.write(value)
                # if len(result)>100:
                #     return result,None
                # f.write('\n')
    # f.close()
    res = []
    if result:
        res.append(result[0])
    return res,None


def scrapeResource(link):
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    headers = {"User_Agent": USER_AGENT}
    r = requests.get(link, headers=headers)
    resource_result = list()
    resource_url = []
    if r.status_code==200:
        soup = BeautifulSoup(r.content, 'html.parser')
        #print(soup.prettify())
        if "ndtv" in link:
            class_content = ["nstory_header"]
            resource_result, resource_url = findTextContent(soup, class_content)
        elif "hindustantimes" in link:
            #class_content = ["col-lg-7 col-md-7 col-sm-12","row row-10","media-body top-news-text"]
            class_content = ["media-heading","mb-30 top-news-design"]
            resource_result, resource_url = findTextContent(soup, class_content)
        elif "timesofindia" in link:
            class_content = ["main-content"]
            resource_result, resource_url = findTextContent(soup, class_content)
            for k in range(len(resource_url)):
                    st = "https://timesofindia.com"+resource_url[k]
                    resource_url[k] = st
        elif "wikipedia.org" in link:
            #"mw-body-content","mw-parser-output","mw-content-ltr"
            class_content = ["mw-body-content"]
            resource_result, resource_url = findTextContentWiki(soup, class_content)
        elif "dictionary.com" in link:
            #"css-1urpfgu e16867sm0","default-content", "one-click-content css-1p89gle e1q3nk1v4"
            class_content = ["default-content"]
            resource_result, resource_url = findTextContentMeaning(soup, class_content)
        # else:
        #     resource_result, resource_url = findTextContentAll(soup)

    return resource_result,resource_url
    

    