import webbrowser
import time

url = input("Enetr URL : ")
duration = input("Enetr duration: ")

for i in range(10):
   webbrowser.open_new(url)
   time.sleep(int(duration))
