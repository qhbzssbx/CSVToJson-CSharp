
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
        
public class GrowableCfg : IEnumerable<GrowableCfgItem>
{
    private static GrowableCfg instance;
    public static GrowableCfg Instance 
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
    
    public GrowableCfg()
    {
        cfgs = ConfigLoader.GetDate<string, GrowableCfgItem>("growable");
    }
    
    //List<GrowableCfgItem> cfgs;
    public Dictionary<string, GrowableCfgItem> cfgs = new();
    
    public IEnumerator<GrowableCfgItem> GetEnumerator()
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


public struct GrowableCfgItem
{
    public readonly string id;
	public readonly string name;
	public readonly int phaseNum;
	public readonly List<int> phaseCycle;
	public readonly List<string> phaseColor;
	public readonly string res;
}