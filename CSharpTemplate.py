from jinja2 import Template


def GetCfgTemplate(excel_name, date):
    excel_name_capitalize = excel_name.capitalize()
    excel_name_lower = excel_name.lower()
    id_type = date[1][0]
    if id_type == "str":
        id_type = "string"
    template = Template('''
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
        
public class {{ excel_name_capitalize }}Cfg : IEnumerable<{{ excel_name_capitalize }}CfgItem>
{
    private static {{ excel_name_capitalize }}Cfg instance;
    public static {{ excel_name_capitalize }}Cfg Instance 
    {
        get
        {
            if (instance == null)
            {
                instance = new();
            }
            return instance;
        }
    }
    
    public {{ excel_name_capitalize }}Cfg()
    {
        cfgs = ConfigLoader.GetDate<{{id_type}}, {{ excel_name_capitalize }}CfgItem>("{{excel_name_lower}}");
    }
    
    //List<{{ excel_name_capitalize }}CfgItem> cfgs;
    public Dictionary<{{id_type}}, {{ excel_name_capitalize }}CfgItem> cfgs = new();
    
    public IEnumerator<{{ excel_name_capitalize }}CfgItem> GetEnumerator()
    {
        foreach (var item in cfgs.Values)
        {
            yield return item;
        }
    }
    
    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }
}''')

    csharp_code = template.render(excel_name_capitalize=excel_name_capitalize,
                                  excel_name_lower=excel_name_lower,
                                  id_type=id_type)

    return csharp_code


def GetItemTemplate(excel_name, content):
    excel_name_capitalize = excel_name.capitalize()
    template = Template('''
public struct {{ excel_name_capitalize }}CfgItem
{
    {{ content }}
}''')

    return template.render(excel_name_capitalize=excel_name_capitalize, content=content)
