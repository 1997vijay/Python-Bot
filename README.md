# Python-Bot
Created a simple information giving what's app bot that can give you the information like:
1-Covid details of any country.
2-Top news(For India Only).
3-It can give you the meaning of any english word.
4-Current waether of any city.
5-Can send you a random quote.
6-Can tell you a random fact.
7-Can send the NASA pic of the day.
8-Can search any category wise photo.
9-Can tell the current time(for India Only) and dynamicaly can send you the greetings.


#What did I use to make this bot.

For the Quote and English word ,I simply used a json file and from that json file simply fetching the data and passing to the server.
For the rest of the features ,I used REST API(free version only) and passing the information to your what's app I used Twilio.

#What I learned most from this bot.
To be honest ,I learn most from this bot like Fetching the information from API and storing into the json file and fetching
the information from complex nested list or dictionary.

#How to use this bot
This bot is not a AI based bot it is simply information giving bot so Yes there are certain condition to use this bot->
1-For the covid details-> Your message should contain the word 'covid details of country name'
EX- covid details of India.

2-For the top news->Simply type 'top news'
3-To saerch the meaning of any english word Your message should contain 'meaning of word'.Ex- meaning of friend.
4-For the current weather details of any city your messha eshould contain 'waether of city name,country name'
Ex- what's the current weather of London,uk.

5-For a quote-Message should contain 'quote' or 'quotes'.Ex- Send me a quote
6-For the random fact message should conatin 'random fact' or 'fact'.Ex- tell me a random fact
7-For the nasa pic of the day message should contain 'nasa' or 'nasa pic'.Ex- send the nasa pic of the day
8-For searching category wised photo simply type 'category name photo'.Ex- nature photo
9-for the current time simply type 'time' or 'current time'.

To get the current time according to your locality or country, you have to change the latitude and longitude in the time api.
To change the top news a according to your locality or country , you have to change the country name in the api.
