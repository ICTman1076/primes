print("Preparing...")
import time
data=[]
import json
timethen=time.time()
print("Loading in data...")
with open("./primessource/primes.txt") as f:
    data=json.loads(f.read())
newData=[]
print("Converting data...")
for i in data:
    newData.append(str(i))
print("Making a string...")
finalContent="\n".join(newData)
print("...and now writing it in.")
with open("./primessource/primes.txt","w") as f:
    f.write()
print("Done in "+str(int((time.time()-timethen)*10)/10)+"s")