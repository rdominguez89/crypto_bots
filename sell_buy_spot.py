import warnings
warnings.filterwarnings("ignore")
import importlib
import numpy as np
import time
from datetime import datetime
from pytz import timezone
import pandas as pd
import telegram_send
import numpy as np

from binance.client import Client
import os
import requests
from requests.exceptions import ConnectionError


#credentials
api_key = "" #(str)
api_secret = "" #(str)
client = Client(api_key, api_secret)
TOKEN = #Telegram bot ID

def check_client():
    try:
        check = int(float(client.get_asset_balance(asset='USDT')["free"]))
    except:
        print("Something is wrong with your credentials.")
        exit()
    return
check_client()

def send_telegram_message(message, token=TOKEN):
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

class def_coin():
    trade_on = True #Variable de clase Estática
    price_now=0.0
    price_now_btc=0.0
    price_min=10**6
    price_max=0.0
    price_barrier=0.0
    frac_of_price_buy = 1.0016  
    frac_of_price_sell = 0.995  
    var1=0.0
    var2=0.0
    var3=0.0
    all_notifications=1
    diff_var=0.0
    time_check_max=0
    time_sell_max=0
    times_diff=0.0
    check_decrease_min=0
    check_increase_min=0
    risk_rebuy = 0.900
    t_wait_short=0
    t_wait_normal=0
    t_wait_long=0
    #reload_functions=0
    sell_percentage=1.0
    name=''
    mode_check = True
    mode_buy=False
    mode_sell=False
    pair=''
    presition=''
    sell_now=False
    price_buy=0.0
    price_buy_0 =0.0
    price_buy_mod=False
    price_high=False
    balance=0.0
    balance_min = 10.0
    check_time=0
    check_sell=0
    check_loss=0
    check_profit=0
    balance_coin=0.0
    price_central=0.0
    file_cond = ''
    down = False
    high = False
    price_rised = False
    opt_test = 1
    quantity_free = 0
    dummy = 0
    quantity_original = 0
    price_original = 0.0
    wait_to_buy = "False"
    cancel_buy = False
    price_var_high = 1.058
    mode_waring = 0
    var3_warning = 0.96
    risk_rebuy_warning = 0.700
    btc_min_price = 10000
    def read_global_conditions(self,opt):
        self.file_cond = "conditions_global.dat"
        try:
            data = np.array(pd.read_table(self.file_cond,header=None,sep='\s+'))
            if(opt==0):[self.var1,self.price_var_high,self.var2,self.var3,self.var4,self.all_notifications,self.diff_var
             ,self.time_check_max,self.time_sell_max,self.check_decrease_min
             ,self.check_increase_min,self.times_diff,self.t_wait_short
             ,self.t_wait_normal,self.t_wait_long,self.risk_rebuy
                        ,self.sell_percentage,self.mode_warning,self.var3_warning
                        ,self.risk_rebuy_warning,self.btc_min_price]= [float(data[0][0]),float(data[1][0]),float(data[2][0]),float(data[3][0]),float(data[4][0]),int(data[5][0])
                                             ,float(data[6][0]),int(data[7][0]),int(data[8][0]),int(data[9][0])
                                             ,int(data[10][0]),int(data[11][0]),int(data[12][0]),int(data[13][0]),int(data[14][0]),float(data[15][0])
                                              ,int(data[16][0]),int(data[17][0]),float(data[18][0]),float(data[19][0]),float(data[20][0])]
            if(opt==1):[self.var3,self.all_notifications,self.diff_var
             ,self.time_check_max,self.time_sell_max,self.check_decrease_min
             ,self.check_increase_min,self.times_diff,self.t_wait_short
             ,self.t_wait_normal,self.t_wait_long,self.risk_rebuy
             ,self.sell_percentage,self.mode_warning,self.var3_warning,self.risk_rebuy_warning,self.btc_min_price] = [float(data[4][0]),int(data[5][0])
                                             ,float(data[6][0]),int(data[7][0]),int(data[8][0]),int(data[9][0])
                                             ,int(data[10][0]),int(data[11][0]),int(data[12][0]),int(data[13][0]),int(data[14][0]),float(data[15][0])
                                             ,int(data[16][0]),int(data[17][0]),float(data[18][0]),float(data[19][0]),float(data[20][0])]
            if(self.mode_warning==1):
                self.var3 = self.var3_warning
                self.risk_rebuy = self.risk_rebuy_warning
        except FileNotFoundError:
            print("Conditions global not found, creating example of it")
            self.write_example_file()
            exit()
        except:
            print("Conditions global wrong, creating example of it")
            self.write_example_file()
            exit()

    def write_example_file(self):
        f = open(self.file_cond,"w")
        f.write("1.033  #var1_to_check_increase_shorter_time \n")   #0
        f.write("1.080  #price_var_high \n")                        #1
        f.write("0.97   #var2_to_increase_sell_price \n")           #2
        f.write("0.90   #var3_to_sell_max_loss_without_profit \n")  #3
        f.write("0.965  #var4_to_sell_max_loss_with_profit \n")     #4
        f.write("1      #all_notifications_0:No_1:Yes \n")          #5
        f.write("0.02   #diff_var_to_increase_min_profit \n")       #6
        f.write("30     #n_times_check_var1 \n")                    #7
        f.write("5      #n_times_check_sell \n")                    #8
        f.write("20     #n_times_check_decrease \n")                #9
        f.write("5      #n_times_check_increase \n")                #10
        f.write("1      #factor_for_diff_var \n")                   #11
        f.write("5      #t_wait_short \n")                          #12
        f.write("20     #t_wait_normal \n")                         #13
        f.write("60     #t_wait_long \n")                           #14
        f.write("0.900  #risk_rebuy \n")                            #15
        f.write("1.0    #sell_percentage/100 \n")                   #16
        f.write("0      #mode_warning \n")                          #17
        f.write("0.96   #var3_warning \n")                          #18
        f.write("0.700  #risk_rebuy_warning \n")                    #19
        f.write("10000  #BTC_min_price \n")                         #20                                                                                      
        f.close()
        exit()
    
    def quantityfree(self):
        try:
            quantity = int(float(client.get_asset_balance(asset=self.name)["free"]))
        except:
            print("Try again because of quantity error")
            quantity = self.quantityfree()
            return quantity
        return quantity
    
    def quantityfree_2(self):
        try:
            quantity = int(float(client.get_asset_balance(asset=self.pair)["free"]))
        except:
            print("Try again because of quantity error")
            quantity = self.quantityfree_2()
            return quantity
        return quantity
    
    def cond_to_buy_sell(self,opt):
        file_cond = "conditions_to_buy_"+self.name+".dat"
        self.sell_now = False
        try:
            with open(file_cond) as f:
                f.close()
                if(opt==0):print("Reading min price of %s to buy" %self.name)
                cond_to_buy_now = np.array(pd.read_table(file_cond,header=None,sep='\s+'))
                self.price_central = float(cond_to_buy_now[0])
                self.pair = cond_to_buy_now[1][0]
                self.presition = cond_to_buy_now[2][0]
                order_to_stop = cond_to_buy_now[3][0]
                self.price_original = float(cond_to_buy_now[4][0])
                self.quantity_original = float(cond_to_buy_now[5][0])
                try:
                    self.wait_to_buy = cond_to_buy_now[6][0]
                except:
                    self.wait_to_buy = "False"
                if(opt==0 and order_to_stop == "True"):
                    order_to_stop = "False"
                    f = open(file_cond,"w")
                    f.write("%s \n" %str(self.price_central))
                    f.write("%s \n" %self.pair)
                    f.write("%s \n" %self.presition)
                    f.write("%s \n" %order_to_stop)
                    f.write("%s \n" %str(self.price_original))
                    f.write("%s \n" %str(self.quantity_original))
                    f.write("True \n")
                    f.close()
                if(order_to_stop == "True"):
                    if(self.mode_buy==True):message = "Stopping %s trade because of user"%self.name 
                    if(self.mode_sell==True):
                        message = "Selling %s now because of user"%self.name
                        self.sell_now = True
                    print(message)
                    send_telegram_message(message)
                    if(self.mode_buy==True):exit()
                    return
        except FileNotFoundError:
            print("No conditions to sell. Creating a default.")
            self.__get_presition()
            self.update_price()
            self.price_central = 0.995*self.price_now
            self.price_original = self.price_central
            self.quantity_free = self.quantityfree()
            if((self.quantity_free>0.1 and self.name!="BNB") or (self.quantity_free>0.9 and self.name=="BNB")): #check coin balance
                print("%s was bought aleady"%self.name)
                self.quantity_original = self.quantity_free
                self.wait_to_buy = "False"
            else:
                self.quantity_original = int(500./self.price_now) #500 usd
                if(self.quantity_original<1):self.quantity_original = 1
                self.wait_to_buy = "True"
            f = open(file_cond,"w")
            f.write("%s \n" %str(self.price_central))
            f.write("%s \n" %self.pair)
            f.write("%s \n" %self.presition)
            f.write("False \n")
            f.write("%s \n" %str(self.price_original))
            f.write("%s \n" %str(self.quantity_original))
            if(self.quantity_free>0.1):
                f.write("False \n")
            else:
                f.write("True \n")
            f.close()
            
    def __get_presition(self):
        
        info = client.get_symbol_info(self.name+'BUSD')
        self.pair = "BUSD"
        if(self.name == "VTHO"):info=None #error in binance info
        if(info==None):
            info = client.get_symbol_info(self.name+'USDT')
            self.pair = "USDT"
        if(info==None):
            print("Not information found for %s"%self.name)
            exit()
        min_price = float(info['filters'][0]['minPrice'])
        self.presition = 0
        for i in range(10):
            if(int(min_price)==1):
                self.presition = int(self.presition)
                break
            self.presition += 1
            min_price = 10*min_price
        self.presition = "{:."+str(self.presition)+"f}"
        
    def __price_request(self):
        try:
            self.price_now = float(client.get_symbol_ticker(symbol=self.name+self.pair)["price"])
            self.price_now_btc = float(client.get_symbol_ticker(symbol='BTC'+self.pair)["price"])
        except ConnectionError as e:
            time_to_sleep = 30
            print("Error connection, waiting %i seconds"%time_to_sleep)
            time.sleep(time_to_sleep)
            self.__price_request()
            return
        except:
            print("Asking again, because of error")
            self.__price_request()
            return
        return

    def update_price(self):
        self.__price_request()
        return

                                                                                                                      
    def __price_round(self,price_here):
        priceround = float(self.presition.format(price_here)) 
        return priceround

    def __check_open_order(self,opt,order):
        t_wait_order=0
        t_wait_order_max = 12
        if(opt==1): self.mode_sell = False
        if(opt==2): self.mode_buy = False
        while(len(client.get_open_orders(symbol=self.name+self.pair))!=0):
            t_wait_order+=1
            if(t_wait_order>t_wait_order_max):
                cancel = client.cancel_order(symbol=self.name+self.pair, orderId=order['orderId'])
                if(opt==1):
                    self.mode_sell = True
                    message = "Selling took too long, try again"
                if(opt==2):
                    self.mode_buy = True
                    message = "Buying took too long, maybe try again"
                print(message)
                if(self.all_notifications==1):send_telegram_message(message)
            if(t_wait_order<=t_wait_order_max):    
                if(opt==1):print("Waiting until finish selling","%i/%i"%(t_wait_order,t_wait_order_max))
                if(opt==2):print("Waiting until finish buying","%i/%i"%(t_wait_order,t_wait_order_max))
                time.sleep(5)

    def sell(self):
        self.quantity_free = int(self.sell_percentage*self.quantityfree())
        if(self.quantity_free==0):exit
        self.__price_request()
        self.price_sell = self.price_now
        self.price_sell = self.frac_of_price_sell*self.price_sell
        priceround = self.__price_round(self.price_sell)
        if(self.opt_test==0):
            print("Selling %i %s for %.5f" %(self.quantity_free,self.name,priceround))
            print("testing sell")
            exit()
        
        try:
            sell_order_limit = client.create_order(
                symbol=self.name+self.pair,
                side='SELL',
                type='LIMIT',
                timeInForce='GTC',
                quantity=self.quantity_free,
                price=priceround)
        except:
            print("Try again because of selling error")
            self.sell()
            return 
        message = "Order %i %s %i %s at %.4f %s, now: %s" %(sell_order_limit['orderId'],sell_order_limit['side']
                                                                       ,int(float(sell_order_limit['origQty'])),sell_order_limit['symbol']
                                                                       ,priceround,self.pair,sell_order_limit['status'])
        print(message)
        send_telegram_message(message)  
        self.__check_open_order(1,sell_order_limit)
        if(self.mode_sell):self.sell()
        return

    def buy(self):
        self.cancel_buy = False
        self.__price_request()
        self.price_buy = self.price_now  
        self.price_buy = self.frac_of_price_buy*self.price_buy
        priceround = self.__price_round(self.price_buy)
        #quantity_buy = int(self.quantity_free*self.price_sell/priceround)
        quantity_buy = int(1.0*self.quantity_free)
        if(self.name=="BNB"):quantity_buy=quantity_buy+0.1
        self.balance = self.quantityfree_2()
        
        if(self.balance < quantity_buy*priceround and self.balance < 340.):
            message = "%s can not be bought, balance %i not enough \n"%(self.name,self.balance)
            message = message+"Waiting 1 min and check start again"
            self.cancel_buy = True
            print(message)
            if(self.all_notifications==1):send_telegram_message(message)
            time.sleep(60)
            return
        if(self.balance < quantity_buy*priceround and self.balance >= 340.):
            quantity_buy = int(self.balance/priceround)
        if(self.opt_test==0):
            print("Buying %i %s for %.5f" %(quantity_buy,self.name,priceround))
            print("testing buy")
            exit()
        try:
            buy_order_limit = client.create_order(
                symbol=self.name+self.pair,
                side='BUY',
                type='LIMIT',
                timeInForce='GTC',
                quantity=quantity_buy,
                price=priceround)
        except:
            print("Try again because of buying error")
            self.buy()
            return
        message = "Order %i %s %.1f %s at %.4f %s, now: %s" %(buy_order_limit['orderId'],buy_order_limit['side']
                                                                       ,float(buy_order_limit['origQty']),buy_order_limit['symbol']
                                                                       ,priceround,self.pair,buy_order_limit['status'])
        print(message)
        send_telegram_message(message)   
        self.__check_open_order(2,buy_order_limit)
        if(self.mode_buy):self.buy()
        coin_info.balance_coin = coin_info.quantityfree()
        return 

def check_high_increase():
    check_high = True               #keep checking
    check_sell = 0                  #n time to check
    coin_info.price_rised = False   #price central updated
    while check_high:               #checking
        check_sell += 1             ##n time to check + 1
        coin_info.update_price()    ##update price
        var_here = coin_info.price_now/coin_info.price_central ###variation here
        if(var_here > coin_info.var1):                         ###if varitiion > var1
            coin_info.price_central=coin_info.price_now        ###updating price central
            check_sell = 0                                     ###restart n time to check
            coin_info.price_rised = True                       ###info about price rised here
            coin_info_0.price_rised = True                     ###info about price rised original 
            message = "%s high increase detected var: %.3f, increasing price central and keep checking."%(coin_info.name,coin_info.price_now/coin_info_0.price_central)
            if(coin_info.all_notifications==1):send_telegram_message(message)
            print(message)
        if(check_sell>=coin_info.check_increase_min):                ##checking n time  
            current_time = datetime.now(timezone('Europe/Berlin')).strftime("%H:%M:%S")  #time
            coin_info_0.price_rised = True 
            if(coin_info.price_rised == False):message = "%s normal increase detected var: %.3f, increasing price central and keep checking. "%(coin_info.name,coin_info.price_now/coin_info_0.price_central)+current_time 
            if(coin_info.price_rised):message = "%s returning to check with a var: %.3f. "%(coin_info.name,coin_info.price_now/coin_info_0.price_central)+current_time 
            if(coin_info.all_notifications==1):send_telegram_message(message)
            print(message)
            coin_info.mode_sell = False
            coin_info.mode_check = True
            coin_info.high = False
            return   ###return to check
        print("Checking again in case of another increase var: %.3f %i/%i"%(var_here,check_sell,coin_info.check_increase_min))
        time.sleep(coin_info.t_wait_short)                 ##wait short time

def check_high_decrease():
    coin_info.price_min=coin_info.price_now
    check_down = True
    var_min = 1.0
    check_buy = 0
    check_message = -1
    t_wait = coin_info.t_wait_short
    wait_long = False
    if(coin_info.wait_to_buy=="True"):
        coin_info.price_sell = coin_info.price_central
        coin_info.wait_to_buy = "False"
        check_buy = 200
        
    while check_down:
        current_time = datetime.now(timezone('Europe/Berlin')).strftime("%H:%M:%S")  #time
        coin_info.read_global_conditions(0)
        coin_info.update_price()
        #print(coin_info.price_now,coin_info.price_now_btc,coin_info.btc_min_price)
        var_here = coin_info.price_now/coin_info.price_sell
        if(var_here > coin_info.price_var_high):
            check_buy += 100
            message = "Increasing price sell for %s"%(coin_info.name)
            coin_info.price_sell = coin_info.var2*coin_info.price_now
            var_min  = 1.00
            var_here = coin_info.price_now/coin_info.price_sell
            print(message)
            if(coin_info.all_notifications==1):send_telegram_message(message)
        if(var_here < var_min and coin_info.price_now<coin_info.price_sell):
            message = "%s price keeps decreasing var: %.3f , %.4f %s. "%(coin_info.name,coin_info.price_now/coin_info.price_sell,coin_info.price_now,coin_info.pair)+current_time+"\n"
            if(wait_long==True):
                wait_long = False
                t_wait = coin_info.t_wait_short
                check_message = -1
                message = message + "Restarting check."
            coin_info.price_min=coin_info.price_now
            var_min = var_here
            check_buy = 1
            t_wait = coin_info.t_wait_short
            check_message += 1
            if(check_message % 5 == 0 and coin_info.all_notifications==1):send_telegram_message(message)
            print(message)
        if((var_here > (var_min+coin_info.times_diff*coin_info.diff_var) or check_buy >= coin_info.check_decrease_min) and (coin_info.price_now<coin_info.risk_rebuy*coin_info.price_sell or coin_info.price_now_btc<=coin_info.btc_min_price)):
            coin_info.buy()
            if(coin_info.cancel_buy==False):
                coin_info.price_central=coin_info.price_buy
                coin_info_0.price_central=coin_info.price_buy
                message = ""
                if(check_buy >= coin_info.check_decrease_min):message="Check time for checking the decrease done \n"
                message = message+"Rebuying %s with a sell price var: %.3f "%(coin_info.name,coin_info.price_buy/coin_info.price_sell)+current_time
                send_telegram_message(message)
                print(message)
                return
            if(coin_info.cancel_buy==True):
                current_time = datetime.now(timezone('Europe/Berlin')).strftime("%H:%M:%S")  #time
                message="Returning to check %s after lack of balance. "%(coin_info.name)+current_time
                if(coin_info.all_notifications==1):send_telegram_message(message)
                print(message)
        
        if(check_buy > coin_info.check_decrease_min):
            if(wait_long==False):
                check_buy = 1
                if(var_min <= 1.05):t_wait = coin_info.t_wait_long
                if(var_min > 1.05):t_wait = 5*coin_info.t_wait_long
                message= "Trade for %s took too long to find a lower price, waiting %i min. Actual price sell var: %.3f , var_min: %.3f "%(coin_info.name,t_wait/60,var_here,var_min)+current_time
                if(coin_info.all_notifications==1):send_telegram_message(message)
                print(message)
                wait_long = True
        #print("Waiting %i sec to rebuy %i %s ,actual price sell var: %.3f/%.3f ,var_min: %.3f (%.3f), %i/%i "%(t_wait,coin_info.quantity_free,coin_info.name,var_here,coin_info.price_now_btc/coin_info.btc_min_price,var_min,coin_info.risk_rebuy,check_buy,coin_info.check_decrease_min),current_time)
        print("Waiting %i sec to rebuy %i %s ,actual price sell var: %.3f ,var_min: %.3f (%.3f/%.3f), %i/%i "%(t_wait,coin_info.quantity_free,coin_info.name,var_here,var_min,coin_info.risk_rebuy,coin_info.price_now_btc/coin_info.btc_min_price,check_buy,coin_info.check_decrease_min),current_time)
        time.sleep(t_wait)
        check_buy += 1
        if(var_here < coin_info.risk_rebuy):check_buy += 4
        if(wait_long==True):check_buy = 1


coin_info = def_coin()
coin_info_0 = def_coin()
coin_info.name = pd.read_table("coin.dat",header=None,sep='\s+')[0][0]

coin_info.balance_coin = coin_info.quantityfree()    
coin_info_0.name = coin_info.name
coin_info.read_global_conditions(0)
coin_info_0.read_global_conditions(0)
coin_info.cond_to_buy_sell(0)
coin_info_0.cond_to_buy_sell(0)

if(coin_info.wait_to_buy=="True"):
    print("Setting options to wait to buy %s"%(coin_info.name))
    coin_info.quantity_free = coin_info.quantity_original
    coin_info.mode_check= False
    coin_info.mode_buy = True


n_sell_loss = 0
message = "Starting trade for %s"%coin_info.name
send_telegram_message(message)
print(message)
while coin_info.trade_on:
    t_check = 0
    coin_info.down = False
    coin_info.high = False
    while coin_info.mode_check:                                                  #checking mode
        t_check += 1
        if(t_check>99):t_check = 50
        coin_info.read_global_conditions(0)
        current_time = datetime.now(timezone('Europe/Berlin')).strftime("%H:%M:%S")  #time
        coin_info.update_price() #update_price
        if(t_check>coin_info.time_check_max/2 and coin_info.price_now>coin_info.price_central):
            message = "The price for %s has stayed in this range too long, updating price, var: %.3f (%.4f %s)"%(coin_info.name,coin_info.price_now/coin_info.price_central,coin_info.price_now,coin_info.pair)+current_time
            #send_telegram_message(message)
            print(message)
            coin_info.price_central = coin_info.price_now
            t_check = 0
        var_here = coin_info.price_now/coin_info.price_central                   #price variation
        
        if((var_here<coin_info.var3 and coin_info.price_now<coin_info_0.price_central/coin_info.var4) or (var_here<coin_info.var4 and coin_info.price_now>=coin_info_0.price_central/coin_info.var4)):##check if price decreases
            coin_info.mode_sell = True                                           ###activate the sell
            coin_info.down = True                                                ###because of the decrease
            coin_info.mode_check = False                                         ###finish check
        if(var_here>coin_info.var1):                                             ##check if price increases
            coin_info.mode_sell = True                                           ###activate the sell
            coin_info.high = True                                                ###because of the increase
            coin_info.mode_check = False                                         ###finish check
        if(coin_info.mode_check==False):break
        if(coin_info.price_now<coin_info_0.price_central/coin_info.var4):var_min_here = coin_info.var3
        if(coin_info.price_now>=coin_info_0.price_central/coin_info.var4):var_min_here = coin_info.var4
        print("Waiting %i sec to check %s .Original var: %.3f ,min/actual var: %.3f/%.3f %i/%i. (%ix%.4f/%.4f:%.4f/%ix%.4f %s)"%(coin_info.t_wait_normal,coin_info.name,coin_info.price_now/coin_info_0.price_central,var_min_here,coin_info.price_now/coin_info.price_central,t_check,coin_info.time_check_max/2,coin_info.quantity_original,coin_info.price_original,coin_info.price_central,coin_info.price_now,coin_info.balance_coin,coin_info_0.price_central,coin_info.pair),current_time)
        time.sleep(coin_info.t_wait_normal)
    
    while coin_info.mode_sell:                                                   #selling mode
        if coin_info.down:                                                       ##selling because of decrease
            coin_info.sell()                                                     ###sell order
            coin_info.mode_buy = True                                            ###activate the buy
            if(coin_info.price_sell/coin_info_0.price_central<=1):message = "Selling %s with loss %.3f. "%(coin_info.name,coin_info.price_sell/coin_info_0.price_central)+current_time ####selling with loss
            if(coin_info.price_sell/coin_info_0.price_central>1):
                n_sell_loss = 0
                message = "Selling %s with profit %.3f. "%(coin_info.name,coin_info.price_sell/coin_info_0.price_central)+current_time  ####selling with profit
            send_telegram_message(message)
            print(message)
            if(coin_info.quantity_free*coin_info.price_sell<coin_info.var3*coin_info.quantity_original*coin_info.price_original):
                n_sell_loss+=1
                if(n_sell_loss>2 and (coin_info.quantity_free*coin_info.price_sell-coin_info.quantity_original*coin_info.price_original)<-20):
                    message ="Stopping trade for %s because of multiple lost %i %s "%(coin_info.name,coin_info.quantity_free*coin_info.price_sell-coin_info.quantity_original*coin_info.price_original,coin_info.pair)+current_time
                    send_telegram_message(message)
                    print(message)
                    exit()
        if coin_info.high:                                                       ##high variation detected
            check_high_increase()                                                ###check high increase
        break

    while coin_info.mode_buy:
        check_high_decrease()
        coin_info.mode_check = True
        coin_info.mode_buy = False
        break



    



