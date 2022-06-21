THIS IS NOT FINANCIAL ADVICE. DO YOUR OWN RESEARCH. YOU CAN USE THESE CODES AS EXAMPLES TO CREATE YOUR OWN. A BAD IMPLEMENTATION CAN LEAD TO THE LOSS OF ALL YOUR ASSETS.<br /><br />

Useful crypto bots written in python <br /><br />

(I) coin_alarm.py : Automatic bot to check TOKEN/COIN prices mainly only listed in Pancakeswap.<br />
The program will send messages to your telegram so you need to set up a bot there too and get its ID in line 8.
(Tutorial to set up telegram bot not included, please search in youtube).<br />
1.-You should add the name of the coin and the pancakeswap identification inside the program in line 22.<br />
2.-You can modify the price change percentage in line 35. (8% by default).<br />

Also it is possible to change:<br />
The frequency to check the price in line 37. (180 seconds by default)<br />
The time zone in line 39.

I would recommend to run the program as:<br />
python3 -u coin_alarm.py > sal_coin.dat 2>stderr_coin.out &

where sal_coin.dat is the log file and stderr_coin.out an outputs in case that the program crash.<br /><br />


(II) sell_buy_spot.py: Automatic binance bot to buy and sell in spot.<br />

IF IT IS NOT THE FIRST TIME RUNNING FOR THE SAME COIN: DELETE "conditions_to_buy_....dat"<br />

1.-Add binance credentials in lines 19 and 20.<br />
2.-Add telegram bot info in lines 22 and 35<br />
3.-Please create a text file and name it "coin.dat" and inside write the coin to trade.<br />
4.-The program will create a file called "conditions_global.dat" and stop.<br />
5.-Modify conditions_global.dat as you wish. The description is inside.<br />
6.-I would recommend to only change the lines 4 y 5 (profit and stop loss conditions) and lines 16 and 21 (re-buy conditions). <br />
7.1-After modifying the conditions you should run the code again. By default (if it is possible) the program will use ALL your BUSD avaiable to buy.
Be aware about this. If you want to use less, modify line 356 (by default 1.0).
7.2-If you want to use USDT instead, stop the program and modify the file "conditions_to_buy_....dat" and re-run.
8.-The program will wait until reaching conditions 16 or 21 and then sell at conditions 4 or 5. 

I would recommend to run the program as:
python3 -u sell_buy_spot.py > sal_coin.dat 2>stderr_coin.out & , but replacing "coin" by the actual coin you are trading


(III) create_longs_beta.py: Automatic futures binance bot to buy longs.<br />

1.-Add binance credentials in lines 15 and 16.<br />
2.-Add telegram bot info in lines 18 and 23.<br />
3.-Add coin and pair in line 35. (pair mostly USDT)<br /><br />

The strategy is based on three periods average 7,25,99 (you can change this in line 134). When 7 reaches 25 in an up trend and the prices are far away form 99, the program open a long with the first size (line 143).
If the price goes lower than the stop_loss (line 133) it will open a second long with the second size, if it is the case, otherwise it will close the position and wait for new entry. You can add and modify the time of new entries as you wish.


I would recommend to run the program as:
python3 -u create_longs_beta.py > sal_long_coin.dat 2>stderr_long_coin.out & , but replacing "coin" by the actual coin you are trading

THIS IS A BETA VERSION, PROCEED WITH CAUTION.