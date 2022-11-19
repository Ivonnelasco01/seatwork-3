#import
import urllib.request as request
#paste ip in variable
url = "http://192.168.0.102:8080/shot.jpg"

while True:
    #open img
    img = request.urlopen(url)