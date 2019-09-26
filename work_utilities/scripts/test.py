import json

dic = {'software version':'00.02.01', 'hardware version':'0.0.9', 'part number':'701000106AA'}

# with open('a.json', 'w', encoding='utf-8') as f:
#     json.dump(dic, f)
a={}
with open('../midwares/icmbasicinfo.json', 'r', encoding='utf-8') as f:
    a = json.load(f)

print(a["software version"], type(a["software version"]))
print(a["hardware version"])
print(a["part number"])