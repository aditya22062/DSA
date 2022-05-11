arr = []

with open("nyc_weather.csv","r") as f:
    for i in f:
        tokens=i.split(',')
        day=tokens[0]
        try:
            temperatur=int[tokens[1]]
            arr.append[i]
        except:
             False
print(sum(arr[0:7])/len(arr[0:7]))

