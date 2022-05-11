n = int(input())
m = int(input())

def get_maze_paths(sr, sc, dr, dc):
    #Write your code here
    if sr==dr and sc==dc:
        bres=[]
        bres.append("")
        return bres
    path=[]
    for hms in range(1,dc-sc+1):
        hpath=get_maze_paths(sr,sc+hms,dr,dc)
        for i in hpath:
            path.append("h"+str(hms)+str(i))
    for vms in range(1,dr-sr+1):
        vpath=get_maze_paths(sr+vms,sc,dr,dc)
        for i in vpath:
            path.append("v"+str(vms)+str(i))
    dms=1
    while dms<=dr-sr and dms<=dc-sc:
        dpath=get_maze_paths(sr+dms,sc+dms,dr,dc)
        for i in dpath:
            path.append("d"+str(dms)+str(i))
        dms+=1
    return path

ans = get_maze_paths(1, 1, n, m)
print("["+', '.join(ans) + "]")