from difPy import dif
import os, datetime, shutil

path = r"folder_direct_path"
savepath = os.path.join(path, "Saved Pics")

def list_full_paths(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if directory == directory]
    
list = list_full_paths(path)
search = dif(path)

for i in range(len(search.lower_quality)):
    list.remove(search.lower_quality[i])

listd = dict.fromkeys(list, "")
for i in range(len(list)):
    listd[list[i]] = str(datetime.datetime.fromtimestamp(os.path.getmtime(list[i])))
listd2 = {}

years = []
date = ""
year = ""

for value in listd.keys():
    date = listd[value].split()
    year = date[0].split("-")
    listd2[value] = year[0]
    if year[0] not in years:
        years.append(year[0])
        
os.mkdir(savepath)
for y in years:
    path = os.path.join(savepath, y)
    os.mkdir(path)

for i in range(len(years)):
    value = 0
    for x in listd2.keys():
        if listd2[x] == years[i]:
            shutil.copy(x, os.path.join(savepath, listd2[x], ((listd[x].split())[0] + "-" + str(value) + ".jpg")))
            value += 1