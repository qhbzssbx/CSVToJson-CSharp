import csv
import os


def GetDate(path):
    path = path
    date = Read(path)
    date = InitDate(date)

    return date


def Read(path):
    files = []
    for item in os.listdir(path):
        if os.path.splitext(item)[1] == ".csv":
            files.append(os.path.join(path, item))

    date = {}
    for item in files:
        with open(item, newline='', encoding="utf-8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='^')
            print(type(spamreader))
            index = 0
            title = []
            arg_types = []
            date_temp = []
            for row in spamreader:
                index += 1
                if index == 1:
                    title = row[0].split(",")

                elif index == 2:
                    arg_types = row[0].split(",")

                elif index == 3:
                    continue
                else:
                    date_temp.append(row[0].split(","))

        file_name = os.path.split(item)[1]
        if title.__len__() == arg_types.__len__():
            date[os.path.splitext(file_name)[0]] = (title, arg_types, date_temp)
        else:
            print("配置表" + file_name + "有字段类型未配置")

    return date


def InitDate(date):
    for item in date:
        key = item
        s = date[key][0]
        t = date[key][1]
        v = date[key][2]
        for vv in v:
            for i in range(0, s.__len__()):
                if s[i] == "\ufeffid":
                    s[i] = s[i].lstrip('\ufeff')

                if t[i] == "int":  # 处理int类型
                    if vv[i] == "":
                        vv[i] = 0
                    else:
                        vv[i] = int(vv[i])
                elif t[i] == "str":  # 处理string类型
                    if vv[i] == '':
                        vv[i] = ""
                    else:
                        vv[i] = str(vv[i])
                elif t[i] == "bool":  # 处理bool类型
                    if vv[i] == '':
                        vv[i] = ""
                    else:
                        # excel会把true, false转为大写, 这里需要转换一下
                        vv[i] = str(vv[i]).lower()
                elif "list" in t[i]:  # 处理list类型
                    if vv[i] != "":
                        vv[i] = vv[i].split(";")
                    if "str" in t[i]:
                        for ii in range(vv[i].__len__()):
                            vv[i][ii] = str(vv[i][ii])
                    elif "int" in t[i]:
                        for ii in range(vv[i].__len__()):
                            vv[i][ii] = str(vv[i][ii])
                    elif "bool" in t[i]:
                        for ii in range(vv[i].__len__()):
                            # excel会把true, false转为大写, 这里需要转换一下
                            vv[i][ii] = str(vv[i][ii]).lower()
    return date

