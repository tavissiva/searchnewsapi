from .search import scrapeLink
from .resource import scrapeResource


def scrapeSearch(query):
    result_url_page, result_url_link = scrapeLink(query) 
    resource_result, resource_url = scrapeResource(result_url_page)  
    return resource_result, resource_url, result_url_page, result_url_link

