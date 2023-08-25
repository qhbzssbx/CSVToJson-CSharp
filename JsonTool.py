import os.path


def Start(date, save_path):
    for key in date.keys():
        file_name = key
        s = BuildjsonDate(date[key])
        with open(os.path.join(save_path, file_name+".json"), "w", encoding="utf-8") as file:
            file.write(s)

def BuildjsonDate(date):
    k = date[0]
    t = date[1]
    v = date[2]

    result = []

    for item in v:
        main_key = 0
        tp = []
        for i in range(0, k.__len__()):
            key = k[i]
            value = item[i]
            if key == "id":
                main_key = item[i]
            if t[i] == "str":
                ss = f"\"{key}\" : \"{value}\""
            elif t[i] == "int":
                ss = f"\"{key}\" : {value}"
            elif "bool" == t[i]:
                ss = f"\"{key}\" : {value}"
            elif "list" in t[i]:
                content = ""
                if "str" in t[i]:
                    content = "\",\"".join(value)
                    content = "[\"" + content + "\"]"

                elif "int" in t[i]:
                    content = ",".join(value)
                    content = "[" + content + "]"
                elif "bool" in t[i]:
                    content = ",".join(value)
                    content = "[" + content + "]"

                ss = f"\"{key}\" : {content}"

            tp.append(ss)

        ss = ",\n\t\t".join(tp)
        s = "\"%s\" : {\n\t\t%s\n\t}" % (str(main_key), ss)
        result.append(s)

    r = "{\n\t%s\n}" % (",\n\t".join(result))

    return r
