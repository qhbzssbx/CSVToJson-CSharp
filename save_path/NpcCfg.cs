
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
        
public class NpcCfg : IEnumerable<NpcCfgItem>
{
    private static NpcCfg instance;
    public static NpcCfg Instance 
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
    
    public NpcCfg()
    {
        cfgs = ConfigLoader.GetDate<string, NpcCfgItem>("npc");
    }
    
    //List<NpcCfgItem> cfgs;
    public Dictionary<string, NpcCfgItem> cfgs = new();
    
    public IEnumerator<NpcCfgItem> GetEnumerator()
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
}


public struct NpcCfgItem
{
    public readonly string id;
	public readonly string name;
}