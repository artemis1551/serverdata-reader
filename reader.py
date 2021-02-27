#Coded by artemis#1551

import os
from os import system
import requests
import time
from time import sleep

print("server_data.php Reader")
print("Coded by artemis#1551")
ip = input('IP Address > ')
print("Succesfully readed, please wait 5 seconds.....")

post = requests.post(f'http://{ip}/growtopia/server_data.php')
sleep(5)
print('Target server_data.php : ')
print('\n')
print(post.text)
print("\nReaded!")
sleep(10)