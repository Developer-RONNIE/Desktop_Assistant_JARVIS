import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    # make sure to use your own api keys 
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=465642fe2fcd4965bf386973a82c21bd",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=https://newsapi.org/v2/everything?q=tesla&from=2023-11-17&sortBy=publishedAt&apiKey=465642fe2fcd4965bf386973a82c21bd",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=465642fe2fcd4965bf386973a82c21bd",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=https://newsapi.org/v2/top-headlines?country=in&apiKey=465642fe2fcd4965bf386973a82c21bd",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=465642fe2fcd4965bf386973a82c21bd",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=465642fe2fcd4965bf386973a82c21bd"
    }

    content = None
    url = None 

    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
        speak("thats all")