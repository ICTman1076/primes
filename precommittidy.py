data=[]
import json
with open("./primessource/primes.txt") as f:
    data=json.loads(f.read())
with open("./primessource/primes.txt","w") as f:
    f.write("\n".join(data))