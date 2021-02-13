# Python-Bot
## Created a simple information giving what's app bot that can give you the information like:
<ol>
  <li>Covid details of any country.</li>
<li>Top news(For India Only).</li>
<li>It can give you the meaning of any english word.</li>
<li>Current waether of any city.</li>
<li>Can send you a random quote.</li>
<li>Can tell you a random fact.</li>
<li>Can send the NASA pic of the day.</li>
<li>Can search any category wise photo.</li>
<li>Can tell the current time(for India Only) and dynamicaly can send you the greetings.</ol>


# What did I use to make this bot.

<p>For the Quote and English word ,I simply used a json file and from that json file simply fetching the data and passing to the server.
For the rest of the features ,I used REST API(free version only) and passing the information to your what's app I used Twilio.</p>

# What I learned most from this bot.
<p>To be honest ,I learn most from this bot like Fetching the information from API and storing into the json file and fetching
the information from complex nested list or dictionary.</p>

# How to use this bot
<p>This bot is not a AI based bot it is simply information giving bot so Yes there are certain condition to use this bot-></p>
<or>
<li>For the covid details-> Your message should contain the word 'covid details of country name'
  EX- covid details of India.</li>

<li>For the top news->Simply type 'top news'</li>
<li>To saerch the meaning of any english word Your message should contain 'meaning of word'.Ex- meaning of friend.</li>
<li>For the current weather details of any city your messha eshould contain 'waether of city name,country name'
Ex- what's the current weather of London,uk.</li>

<li>For a quote-Message should contain 'quote' or 'quotes'.Ex- Send me a quote.</li>
<li>For the random fact message should conatin 'random fact' or 'fact'.Ex- tell me a random fact.</li>
<li>For the nasa pic of the day message should contain 'nasa' or 'nasa pic'.Ex- send the nasa pic of the day.</li>
<li>For searching category wised photo simply type 'category name photo'.Ex- nature photo.</li>
<li>for the current time simply type 'time' or 'current time'.</li>
</ol>
<h4> Note: To get the current time according to your locality or country, you have to change the latitude and longitude in the time api.
To change the top news a according to your locality or country , you have to change the country name in the api.</h4>
