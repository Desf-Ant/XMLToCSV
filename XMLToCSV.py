from xml.etree import ElementTree
import csv
import os

PATH = "./partitions/XML"
CSV_NAME = "untitled.csv"
CSV_HEADER = ["filename", "x1","y1","x2","y2","label"]


allFiles = os.listdir(PATH)
files = []
csvData = []


for f in allFiles :
    if f.endswith("xml") : files.append(f)

for file in files :
    xml = ElementTree.parse(PATH+"/{}".format(file))

    for obj in xml.findall("object") :
        if obj :
            name = obj.find("name").text
            bndbox = obj.find("bndbox")
            x1 = int(bndbox.find("xmin").text)
            y1 = int(bndbox.find("ymin").text)
            x2 = int(bndbox.find("xmax").text)
            y2 = int(bndbox.find("ymax").text)
            csvData.append([file,x1,y1,x2,y2,name])

with open(CSV_NAME,mode="w") as f :
    writer = csv.writer(f)
    
    writer.writerow(CSV_HEADER)
    writer.writerows(csvData)