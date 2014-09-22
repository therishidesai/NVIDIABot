data=[12, 133, 1]
dataS=""
for i in range(len(data)):
    if(len(str(data[i]))==2):
        s=",".join(str(data[i]))
        s+=",-1,"
        dataS+=s
    elif(len(str(data[i]))==3):
        s=",".join(str(data[i]))
        s+=","
        dataS+=s
    else:
        dataS+=str(data[i])
        dataS+=","
print dataS
