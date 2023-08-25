import os
import CSharpTemplate

def BuildCSharp(date, save_path):
    for key in date.keys():
        file_name = key
        cfg = BuildCfgClass(save_path, file_name, date[key])
        item_class = CreateItemClass(date[key], file_name)
        cfg += "\n\n" + item_class
        name1 = file_name.capitalize()
        saveFile(save_path, f"{name1}Cfg", cfg)


def CreateItemClass(date, file_name):
    k = date[0]
    t = date[1]
    item_class = ""
    lines = []
    for i in range(k.__len__()):
        ty = ""
        if t[i] == "str":
            ty = "public readonly string "
        elif t[i] == "int":
            ty = "public readonly int "
        elif t[i] == "float":
            ty = "public readonly float "
        elif t[i] == "bool":
            ty = "public readonly bool "
        elif "list" in t[i]:
            if "int" in t[i]:
                ty = "public readonly List<int> "
            elif "str" in t[i]:
                ty = "public readonly List<string> "

        lines.append(ty + k[i])
    content = ";\n\t".join(lines) + ";"
    excel_name_capitalize = file_name.capitalize()
    # content = f"public struct {name1}CfgItem\n{{\n\t{content}\n}}"
    code_content = CSharpTemplate.GetItemTemplate(file_name, content)
    print(code_content)
    return code_content



def BuildCfgClass(save_path, file_name, date):
    id_type = date[1][0]
    if id_type == "str":
        id_type = "string"
    # name1 = file_name.capitalize()
    # name2 = file_name.lower()
    # aaa = "using System.Collections;\n" \
    #       "using System.Collections.Generic;\n" \
    #       "using UnityEngine;\n\n"
    # cfg = f"public class {name1}Cfg : IEnumerable<{name1}CfgItem>\n{{\n\tprivate static {name1}Cfg instance;\n\tpublic static {name1}Cfg Instance \n\t{{\n\t\tget\n\t\t{{\n\t\t\tif (instance == null)\n\t\t\t{{\n\t\t\t\tinstance = new();\n\t\t\t}}\n\t\t\treturn instance;\n\t\t}}\n\t}}\n\n\t//List<{name1}CfgItem> cfgs;\n\tpublic Dictionary<{id_type}, {name1}CfgItem> cfgs = new();\n\tpublic {name1}CfgItem? GetValueById({id_type} id)\n\t{{\n\t\t{name1}CfgItem {name2}CfgItem;\n\t\tif (cfgs.TryGetValue(id, out {name2}CfgItem))\n\t\t{{\n\t\t\treturn {name2}CfgItem;\n\t\t}}\n\n\t\treturn null;\n\t}}\n\n\tpublic IEnumerator<{name1}CfgItem> GetEnumerator()\n\t{{\n\t\tforeach (var item in cfgs.Values)\n\t\t{{\n\t\t\tyield return item;\n\t\t}}\n\t}}\n\n\tIEnumerator IEnumerable.GetEnumerator()\n\t{{\n\t\treturn GetEnumerator();\n\t}}\n}}"
    # return aaa + cfg

    excel_name_capitalize = file_name.capitalize()
    excel_name_lower = file_name.lower()
    code_content = CSharpTemplate.GetCfgTemplate(file_name, date)
    return code_content




def saveFile(save_path, file_name, s):
    with open(os.path.join(save_path, file_name + ".cs"), "w", encoding="utf-8") as file:
        file.write(s)
