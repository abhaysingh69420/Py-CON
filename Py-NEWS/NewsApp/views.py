from django.shortcuts import render
from newsapi import NewsApiClient


def index(request):
    newsapi = NewsApiClient(api_key="60d945c8c0de4130b0f1e04ee6441c92")
    topheadlines = newsapi.get_top_headlines(sources='TechRadar,techcrunch,wired,engadget,the-next-web,the-verge')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'index.html', context={"mylist":mylist})



def TechRadar(request):
    newsapi = NewsApiClient(api_key="60d945c8c0de4130b0f1e04ee6441c92")
    topheadlines = newsapi.get_top_headlines(sources='TechRadar')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'TechRadar.html', context={"mylist":mylist})



def techcrunch(request):
    newsapi = NewsApiClient(api_key="60d945c8c0de4130b0f1e04ee6441c92")
    topheadlines = newsapi.get_top_headlines(sources='techcrunch')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'techcrunch.html', context={"mylist":mylist})
#google-news,engadget,business-insider,wired,the-times-of-india,techcrunch,the-verge,the-next-web

def wired(request):
    newsapi = NewsApiClient(api_key="60d945c8c0de4130b0f1e04ee6441c92")
    topheadlines = newsapi.get_top_headlines(sources='wired')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'wired.html', context={"mylist":mylist})

def theverge(request):
    newsapi = NewsApiClient(api_key="60d945c8c0de4130b0f1e04ee6441c92")
    topheadlines = newsapi.get_top_headlines(sources='the-verge')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'theverge.html', context={"mylist":mylist})

def thenextweb(request):
    newsapi = NewsApiClient(api_key="60d945c8c0de4130b0f1e04ee6441c92")
    topheadlines = newsapi.get_top_headlines(sources='the-next-web')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'thenextweb.html', context={"mylist":mylist})


def engadget(request):
    newsapi = NewsApiClient(api_key="60d945c8c0de4130b0f1e04ee6441c92")
    topheadlines = newsapi.get_top_headlines(sources='engadget')


    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    ur = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        ur.append(myarticles['url'])


    mylist = zip(news, desc, img, ur)


    return render(request, 'engadget.html', context={"mylist":mylist})
