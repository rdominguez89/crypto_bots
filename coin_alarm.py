import pandas as pd
import time
import telegram
from datetime import datetime
from pytz import timezone
import requests

TOKEN = "" #telegram bot token from pancakeswap (str)

def send_telegram_message(msg, token=TOKEN):
    try:
        chat_id =   #add chat id to send messages (int, can be negative)
        bot = telegram.Bot(token=token)
        bot.sendMessage(chat_id=chat_id,text=msg)
    except ConnectionError as e:
        print("Error in connection, trying to send message again.")
        time.sleep(30)
        send_telegram_message(message)
        return
    return


def price_request_coin():
    try:
        data = requests.get('https://api.pancakeswap.info/api/v2/tokens/....').json() #add token/coin adress in pancakeswap
        df = pd.DataFrame(data)
    except:
        print("Error connection, waiting 1 min")
        time.sleep(60)
        price = price_request_coin()
        return price
    return float(df['data']['price'])

coin = "" #Name of token/coin
price_now = price_request_coin()
price_min_max = [0.92*price_now,1.08*price_now] #percentages to change. In this case ~8%

time_to_sleep = 180 # 3 minutes
while True:
    current_time = datetime.now(timezone('Europe/Berlin')).strftime("%H:%M:%S")  #time
    price = price_request_coin()
    if(price > price_min_max[1]):
        change = 100*(price/price_now - 1)
        message = "The price of %s increased %.1f %s until %.3f"%(coin,change,"%",price)
        price_min_max = [0.92*price,1.08*price]
        price_now = price
        send_telegram_message(message)
    if(price < price_min_max[0]):
        change = 100*(price_now/price -1)
        message = "The price of %s decreased %.1f %s until %.3f"%(coin,change,"%",price)
        price_min_max = [0.92*price,1.08*price]
        price_now = price
        send_telegram_message(message)
    print("Sleeping %i sec with a %s price of %.3f USDT"%(time_to_sleep,coin,price),current_time)
    time.sleep(time_to_sleep)
