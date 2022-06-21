import warnings
warnings.filterwarnings("ignore")
from binance.client import Client
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

import time
from datetime import datetime
from pytz import timezone
import telegram


api_key = ""
api_secret = ""
client = Client(api_key, api_secret)
TOKEN = "" #(str)


def send_telegram_message(msg, token=TOKEN):
    try:
        chat_id = #(int)
        bot = telegram.Bot(token=token)
        bot.sendMessage(chat_id=chat_id, text=msg)
    except:
        print("Trying to send message again because of error")
        time.sleep(10)
        send_telegram_message(msg)
        return
    return


# get the candles
[coin,pair] = ['','USDT']


def open_position(n_entry,coin_price_now,size_USDT_entry,size_pos,stop_long):
    if(n_entry==0):
        price_open_position_1 = 1.005*coin_price_now
        priceround = float(presition.format(price_open_position_1))
        size_pos_1 = int(size_USDT_entry[n_entry]/price_open_position_1)
        open_order(coin,pair,priceround,size_pos_1,'OPEN')
        message_1 = "Opening long of %i %s at price %.4f USDT"%(size_pos_1,coin,price_open_position_1)
        message_2 = "Stoploss at %.4f"%(stop_long*price_open_position_1)
        print(message_1)
        print(message_2)
        print("Calling function to buy",n_entry)
        if(send_msgs):send_telegram_message(message_1)
        if(send_msgs):send_telegram_message(message_2)
    if(n_entry>=1):
        price_open_position_2 = 1.005*coin_price_now
        size_pos_2 = int(size_USDT_entry[n_entry]/price_open_position_2)
        priceround = float(presition.format(price_open_position_2))
        open_order(coin,pair,priceround,size_pos_2,'OPEN')
        if(n_entry==1):message_1 = "Opening second long of %i %s at price %.4f USDT"%(size_pos_2,coin,price_open_position_2)
        if(n_entry==2):message_1 = "Opening third long of %i %s at price %.4f USDT"%(size_pos_2,coin,price_open_position_2)
        print(message_1)
        if(send_msgs):send_telegram_message(message_1)
        size_pos_1 = size_pos + size_pos_2
        price_open_position_1 = sum(size_USDT_entry[0:n_entry+1])/(size_pos_1)
        message_2 = "New position of %i %s at price %.3f USDT"%(size_pos_1,coin,price_open_position_1)
        message_3 = "Stoploss at %.4f"%(stop_long*price_open_position_1)
        print(message_2)
        print(message_3)
        if(send_msgs):send_telegram_message(message_2)
        if(send_msgs):send_telegram_message(message_3)
        print("Calling function to buy",n_entry)
        
    open_long = True
    max_price = coin_price_now
    time_wait = 15
    n_count = 0
    n_entry += 1
    
    
    return price_open_position_1,size_pos_1,open_long,max_price,time_wait,n_count,n_entry


def price_request(coin,pair):
    try:
        price = float(client.get_symbol_ticker(symbol=coin+pair)["price"])
    except:
        print("Asking again, because of error",coin+pair)
        time.sleep(10)
        price = price_request(coin+pair)
        return price
    return price

def med(i,med,med_i,candles,med_n):
    med.append(np.average(np.array(candles[i-med_n:i+1], dtype='f')[:,4]))
    #med_i.append(i)
    med_i.append(np.array(candles[i,0], dtype='f'))
    return med,med_i

def plot_candle(i,candlestick):#open,max,min,close 1,2,3,4
    color_candle = 'red'
    if(candlestick[1]<candlestick[4]):color_candle = 'green'
    plt.fill_between([i-0.15,i+0.15],candlestick[4],candlestick[1],color=color_candle)
    plt.plot([i,i],[candlestick[3],candlestick[2]],color=color_candle)
    
    return


def open_order(coin,pair,price,quantity,action):
    if(action=='OPEN'):side='BUY'
    if(action=='CLOSE'):side='SELL'    
    open_long_order = client.futures_create_order(
        symbol=coin+pair,
        type='LIMIT',
        timeInForce='GTC',  # Can be changed - see link to API doc below
        price=price,  # The price at which you wish to buy/sell, float
        side=side,  # Direction ('BUY' / 'SELL'), string
        quantity=quantity  # Number of coins you wish to buy / sell, float
    )
    return

def request_candles(open_long,n_candles_now):
    try:
        candles_30m = client.get_klines(symbol=coin+pair,interval=client.KLINE_INTERVAL_30MINUTE,limit=n_candles_now)
    except:
        if(open_long): time_wait_h = 15
        if(not open_long): time_wait_h = 60
        print("Trying to request candles again because of error, waiting %i seconds"%time_wait_h)
        time.sleep(time_wait_h)
        candles_30m = request_candles(open_long,n_candles_now)
        return candles_30m
    return candles_30m

# create lists to hold our different data elements
print(coin)
stop_long = 0.96
[med_1_n,med_2_n,med_3_n] = [7,25,99]
n_candles = 3
[open_long,open_short,close_now] = [False,False,False]
[med_cross_long,med_cross_short] = [False,False]
sum_profit = 0
time_wait = 300
first_med_request=False
size_USDT_entry = [5,10,30]
n_entry = 0
max_n_entry = 3
size_pos = 0
n_count = 0
ploting_n_count = False
first_candles_request=True
test = False #True
presition= '{:.4f}'
[pos_long_open,pos_long_open_i] = [[],[]]
[pos_long_close,pos_long_close_i] = [[],[]]
plot_figures = False #True
send_msgs = True
while True:
    current_time = datetime.now(timezone('Europe/Berlin')).strftime("%H:%M:%S")  #time
    if(first_med_request==True and open_long==False):time_wait = 300
    if(open_long==False or n_count>=20):
        if(n_count>=20):ploting_n_count = True
        n_count = 0
        print("Requesting candles",first_candles_request)
        n_candles_now=200
        candles_30m = request_candles(open_long,n_candles_now)
        candles = np.array(candles_30m, dtype='f')
        if(test):candles = candles[0:180,:]
        [med_1,med_2,med_3,med_1_i,med_2_i,med_3_i] = [[],[],[],[],[],[]]
        if(plot_figures):fig, ax = plt.subplots()
        for ii in range(len(candles[:,0])-50,len(candles[:,0])):    
            if(ii<100):continue
            if(ii>med_1_n):med_1,med_1_i=med(ii,med_1,med_1_i,candles,med_1_n)
            if(ii>med_2_n):med_2,med_2_i=med(ii,med_2,med_2_i,candles,med_2_n)
            if(ii>med_3_n):med_3,med_3_i=med(ii,med_3,med_3_i,candles,med_3_n)   
            if(plot_figures):plot_candle(candles[ii,0],candles[ii,:])
        if(plot_figures):        
            plt.plot(med_1_i,med_1,'-',color='orange',label='7')
            plt.plot(med_2_i,med_2,'-',color='purple',label='25')
            plt.plot(med_3_i,med_3,'-',color='cyan',label='99')
    

    if(med_cross_long and med_1[-1]<med_2[-1]):med_cross_long  = False
    coin_price_now = 0.9999*price_request(coin,pair)
    
    if(test):coin_price_now=0.99*candles[-1,4]
        
    if(open_long):
        n_count += 1
        if(coin_price_now>max_price):max_price=coin_price_now
        if(coin_price_now/price_open_position>1.0): #max/min candle --> in profit 
            if(max_price>med_3[-1]):
                if(coin_price_now<0.98*max_price):
                    close_now=True
                else:
                    pass
                if(max_price>1.05*med_3[-1] and coin_price_now<0.98*max_price  
                and close_now==False):close_now=True #close NOW with high profit
            else:
                if(coin_price_now<0.99*max_price and coin_price_now>1.02*price_open_position or
                coin_price_now<stop_long*price_open_position):
                    close_now=True
                else:
                    pass
        else: # --> not in profit
            if(coin_price_now>stop_long*price_open_position): #> stop lost to close position
                pass
            else:
                if(n_entry==max_n_entry):
                    close_now=True
                    pass
                if(n_entry<max_n_entry):
                    price_open_position,size_pos,open_long,max_price,time_wait,n_count,n_entry = open_position(n_entry,coin_price_now,size_USDT_entry,size_pos,stop_long)
                    pos_long_open_i.append(med_1_i[-1])
                    pos_long_open.append(coin_price_now)  
                    print("Possible profit %.4f"%(med_3[-1]/coin_price_now))

        if(close_now==True):
            price_close_position = 0.995*coin_price_now
            priceround = float(presition.format(price_close_position))
            open_order(coin,pair,priceround,size_pos,'CLOSE')
            message_1 = "Closing positon with profit %.3f at %.4f USDT"%(coin_price_now/price_open_position,coin_price_now)
            if(coin_price_now<price_open_position):message_1 = "Closing positon with loss %.3f at %.4f USDT"%(coin_price_now/price_open_position,coin_price_now)
            if(coin_price_now>price_open_position):message_1 = "Closing positon with profit %.3f at %.4f USDT"%(coin_price_now/price_open_position,coin_price_now)
            print(message_1)
            if(send_msgs):send_telegram_message(message_1)
            sum_profit += (coin_price_now-price_open_position)*size_pos
            pos_long_close_i.append(med_1_i[-1])
            pos_long_close.append(coin_price_now)  
            open_long = False
            close_now = False
            time_wait = 300
            n_count = 20
            n_entry = 0
            continue
        
    if(not open_long):
        candles_slope = (candles[-1,4]-candles[-1-n_candles,4])/n_candles
        dif_med = med_3[-1]/med_2[-1]
        if(test):
            candles_slope = abs(candles_slope) 
            dif_med = 1.03
        if(med_1[-1]>med_2[-1] and dif_med>1.025 and med_cross_long==False and candles_slope>0 and coin_price_now<0.99*med_3[-1] and coin_price_now<1.02*med_2[-1]):
            med_cross_long = True
            pos_long_open_i.append(med_1_i[-1])
            pos_long_open.append(candles[-1,4])            
            price_open_position,size_pos,open_long,max_price,time_wait,n_count,n_entry = open_position(n_entry,coin_price_now,size_USDT_entry,size_pos,stop_long)
            print("Possible profit %.4f"%(med_3[-1]/coin_price_now))
            print("Log: dif med",dif_med,"slope",candles_slope,"price_now",coin_price_now,"0.99 med 99",0.99*med_3[-1])
            if(test):max_price=0.027
            test = False
    if(not open_long or ploting_n_count == True or first_candles_request):
        if(plot_figures):
            plt.scatter(pos_long_open_i,pos_long_open, s=150, facecolors='none', edgecolors='g')
            plt.scatter(pos_long_close_i,pos_long_close, s=100, facecolors='none', edgecolors='r')
            plt.xlim(candles[-50,0],candles[-1,0]+4e6)
            fig.canvas.draw()
            labels = [item.get_text() for item in ax.get_xticklabels()]
            labels[:] = list(np.arange(0,51,10))
            ax.set_xticklabels(labels)
            plt.legend()
            plt.show()
        if(first_candles_request):n_count = 20
        first_candles_request = False
        ploting_n_count = False

    if(not open_long):
        if(sum_profit!=0):print("profit %.2f USDT"%(sum_profit))
        print("Waiting %i seconds. %s"%(time_wait,current_time),n_count)
    else:
        print("Waiting %i seconds. Variation %.4f at %s"%(time_wait,coin_price_now/price_open_position,current_time),n_count)
    if(med_3[-1]<med_2[-1] and not open_long):time_wait=600
    time.sleep(time_wait)



