from django.shortcuts import render

# Create your views here.
def index(request):
    import requests
    import json
    news_api_request = requests.get("http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=9949d1b189cf4788a231de7cbdf26df0")
    api= json.loads(news_api_request.content)
    return render(request, 'newsapp/newsapp.html', {'api': api})




#9949d1b189cf4788a231de7cbdf26df0 api key