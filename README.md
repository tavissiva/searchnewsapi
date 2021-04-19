# Searchnewsapi

[SearchFlash Website Link](http://searchflash.herokuapp.com/)

This is a Flask based News Search Website. The Search results are fetched from a various website by using GET request of query parameter 'search' in google.

The Search query is written as a API Service using FLASK [News API Service Website Link](http://newsapiservice.herokuapp.com/). 
This API Service filtered all the results of Google from various website and using web scrapping technique to fetch the headline of the news.


From the [SearchFlash](http://searchflash.herokuapp.com/) Website, user can search the query ex.today news and get the top news from all website.  




# News Search API

Searching a keyword in a google using **requests,BeautifulSoup** library in python, it returns the list of URL link. Using one of the link to scrape the web content in a website. After scraping the headline content, Build an api using FLASK-RESTFUL-API which return the responce as a json object contains resource content, content information link further search, source content link,  query all link.


