import json
import random
import emoji
import datetime
from difflib import get_close_matches
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route("/", methods=['get'])
def hello():
    return "Hello World!"

@app.route('/bot', methods=['POST'])
def bot():
    quote=json.load(open("quotes.json",encoding='cp1252')) 
    data=json.load(open("data.json",encoding='cp1252'))
    cnv= ['Bye', 'See you later', 'Sayonara', "I'm also leaving", 'Goodbye', 'Farewell']
    hl=['greetings', 'hello', 'hi', 'howdy', 'I am here', 'I have arrived','Okaeri']

    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if "hi" in incoming_msg or "hello" in incoming_msg or "hey" in incoming_msg or "hola" in incoming_msg:
        txt=random.choice(hl)
        em=emoji.emojize(":grinning_face_with_big_eyes:")
        msg.body(txt+" {}".format(em))
        responded = True
    if "bye" in incoming_msg or "good bye" in incoming_msg or "byee" in incoming_msg:
        txt=random.choice(cnv)
        em=emoji.emojize("\N{slightly smiling face}")
        msg.body(txt+" {}".format(em))
        responded = True
    if "made you" in incoming_msg or "creator" in incoming_msg or "madw you" in incoming_msg :
        em=emoji.emojize("\N{smiling face with halo}")
        txt="My creator is 'Vijay Kumar' {}".format(em)
        msg.body(txt)
        responded = True
    if 'Quote' in incoming_msg or 'quotes' in incoming_msg:
        qu=random.choice(quote)
        x = qu.get("quoteText")
        author=qu["quoteAuthor"]
        rq=x+"By-'{}'".format(author)
        msg.body(rq)
        responded = True  
    if 'meaning' in incoming_msg or 'mean' in incoming_msg:
        word=incoming_msg.split("meaning of")[1]
        def translate(w):        
            if w in data:
                msg.body(w+"\n")
                return data[w]
            elif w.title() in data: 
                msg.body(w.title()+"\n")
                return data[w.title()]
            elif w.upper() in data:
                msg.body(w.upper()+"\n")
                return data[w.upper()]
            elif len(get_close_matches(w,data.keys()))>0:
                sm_word=get_close_matches(w,data.keys())[0]
                msg.body(sm_word.title()+":\n")
                return data[get_close_matches(w,data.keys())[0]]
            else:
                msg.body("No such word exits.Please double check it!!")

        output=translate(word.lower())
        if(type(output)==list):
            for items in output:
                rq=items
                msg.body("\n"+rq)
                responded = True
        else:
            rq=output
            msg.body("\n"+rq)
            responded = True 
    if 'nasa' in incoming_msg:
        url="https://api.nasa.gov/planetary/apod?api_key=sbESYWcBiR1n0tggKJfi2nsewtZpcxkQe33NhZjk"
        response = requests.request("GET", url)
        nasa=response.json()
        explanation=nasa.get('explanation')
        img_url=nasa.get('url')
        msg.media(img_url)
        msg.body(explanation)
        responded = True
    if 'photo' in incoming_msg:
        word=incoming_msg.split("photo")[0]
        url="https://source.unsplash.com/1600x900/?{}".format(word)
        print(url)
        msg.media(url)
        responded = True
    if 'covid details' in incoming_msg or 'Covid of' in incoming_msg:
        word=incoming_msg.split("covid details of ")[1]
        def covid(country):
            cn=emoji.emojize("\N{face with medical mask}")
            dt=emoji.emojize("\N{skull and crossbones}")
            rc=emoji.emojize("\N{military medal}")
            url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"
            querystring = {"country":"{}".format(country)}
            headers = {
                'x-rapidapi-key': "0a1a5d8af0msh8ce40a5e61cc781p12ba3bjsnc58b718fa50f"
            }
            response = requests.request("GET", url, headers=headers,params=querystring)
            if response.status_code == 200:
                covid_data=response.json()
                recover=covid_data['data'].get('recovered')
                death=covid_data['data'].get('deaths')
                confirm=covid_data['data'].get('confirmed')
                msg.body(country.title()+"\n"+"\n{}Recovered:{}\n{}Deaths:{}\n{}Confirmed:{}".format(rc,recover,dt,death,cn,confirm))
            elif(response.status_code==201):
                msg.body("Sorry!,I couldn't understand.")
            else:
                text="I could not retrieve the results at this time, sorry."
                msg.body(text)
        covid(word.title())
        responded = True  
    if 'weather' in incoming_msg or 'weather of' in incoming_msg:
        word=incoming_msg.split("weather of ")[1]
        def weather(city):
            url = "https://community-open-weather-map.p.rapidapi.com/weather"
            querystring = {"q":"{}".format(city)}
            headers = {
                'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
                'x-rapidapi-key': "0a1a5d8af0msh8ce40a5e61cc781p12ba3bjsnc58b718fa50f"
            }
            response = requests.request("GET", url,headers=headers, params=querystring)
            if response.status_code == 200:
                weather_data=response.json()
                city_name=city.split(",")[0]
                temp_max=round(weather_data['main'].get('temp_max'))/10
                feels_like=round(weather_data['main'].get('feels_like'))/10
                humidity=weather_data['main'].get('humidity')
                wind=weather_data['wind'].get('speed')
                msg.body("City:{}\nMaximum Temprature:{}\nFeels Like:{}\nHumidity:{}\nWind Speed:{}".format(city_name,temp_max,feels_like,humidity,wind))
            elif(response.status_code==201):
                msg.body("Sorry!,I couldn't understand.")
            else:
                text="I could not retrieve the results at this time, sorry."
                msg.body(text)
        weather(word.title())
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if "current time" in incoming_msg or "What day" in incoming_msg or "date" in incoming_msg or "time" in incoming_msg:
        em1=emoji.emojize("\N{milky way}")
        em=emoji.emojize("\N{sleeping face}")
        x = datetime.datetime.now()
        t=x.strftime("%X").split(":")[0]
        if(t>='12' and t<='17'):
            em_w=emoji.emojize("\N{grimacing face}")
            txt="Good AfterNoon,Time for the work!!"
            time=x.strftime("%c {} {}").format(em_w)
            msg.body(time+"\n"+txt)
            responded = True
        elif(t>='17' and t<='23'):
            em1=emoji.emojize("\N{milky way}")
            em=emoji.emojize("\N{sleeping face}")
            txt="Good Nigth,Time to sleep!!{}{}".format(em1,em)
            time=x.strftime("%c")
            msg.body(time+"\n"+txt)
            responded = True
        else:
            em1=emoji.emojize("\N{hot beverage}")
            em=emoji.emojize("\N{cooking}")
            txt="Good Morning!!{}{}".format(em1,em)
            time=x.strftime("%c")
            msg.body(time+"\n"+txt)
            responded = True
    if "fact" in incoming_msg or "random" in incoming_msg:
        url="https://uselessfacts.jsph.pl//random.json?language=en"
        response = requests.request("GET", url)
        fact=response.json()
        txt=fact["text"]
        msg.body(txt)
        responded=True

    if "help me" in incoming_msg:
        txt="I can \n\n[1] Give you the Covid Details\n[2] Give you Weather Details\n[3]Give you the  Random Quotes\n[4] Be your English dictionary\n[5] Can give you the Nasa pic of the day\n[6] Can search the photo for you\n[7] Can give you the random fact.\n[8] Can be your clock."
        msg.body(txt)
        responded=True
    if "top news" in incoming_msg or "current news" in incoming_msg:
        url="http://newsapi.org/v2/top-headlines?country=in&apiKey=05c523b114d24ae38428e9462f06c3ff"
        response = requests.request("GET", url)
        news=response.json()
        articles=news.get("articles")
        for sources in articles:
            title=sources.get("title")
            new_url=sources.get("url")
        msg.body(title+"\n"+new_url)
        responded=True
    if not responded:
        em=emoji.emojize(":zipper-mouth_face:")
        txt="Sorry, I have no idea what you're talking about {}\n\nType 'help me' to see what i can do.".format(em)
        msg.body(txt)
        responded = True
    return str(resp)
if __name__ == '__main__':
    app.run()