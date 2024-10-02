try:
     open('config.txt')
except FileNotFoundError:
     print("Couldn't find the config.txt file!")