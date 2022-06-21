# crypto_bots
Useful crypto bots written in python 

coin_alarm.py : Automatic bot to check TOKEN/COIN prices mainly only listed in Pancakeswap.
The program will send messages to your telegram so you need to set up a bot there too and get its ID in line 8.
(Tutorial to set up telegram bot not included, please search in youtube).
You should add the name of the coin and the pancakeswap identification inside the program in line 22.
You can modify the price change percentage in line 35. (8% by default).
Also it is possible to change:
The frequency to check the price in line 37. (180 seconds by default)
The time zone in line 39.

I would recommend to run the program as:
python3 -u coin_alarm.py > sal_coin.dat 2>stderr_coin.out &

where sal_coin.dat is the log file
and stderr_coin.out an outputs in case that the program crash.