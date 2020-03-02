data=[]
import json
with open("./primessource/primes.txt") as f:
    data=json.loads(f.read())
newData=[]
for i in data:
    newData.append(str(i))
with open("./primessource/primes.txt","w") as f:
    f.write("\n".join(newData))