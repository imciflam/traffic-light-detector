import os
os.getcwd()
collection = "C:/Users/Vitalia/Documents/GitHub/traffic-light-detector/green"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("C:/Users/Vitalia/Documents/GitHub/traffic-light-detector/green/" + filename,
              "C:/Users/Vitalia/Documents/GitHub/traffic-light-detector/green/" + "img_" + str(i) + ".jpg")
