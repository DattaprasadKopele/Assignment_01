city = ["pune", "mumbai", "nanded", "nashik", "nanded", "kolhapur", "nanded"]

word = "nanded"
n=2

count=0

for i in range(0, len(city)-1):  #len will give no.of element but inndex started from 0 so take -1

    if(city[i] == word):

        count=count+1

        if(count==n):
            del city[i]

print("Updated city name=", city)