print("PyPy's done with compiling, now I'll read in the file...")
import math
import json
from time import time
cnt = 0
content = []
with open("optimusPrime.txt","r") as f:
    content = json.loads(f.read())
    cnt = content[-1]


print("Awesome! I'll carry on where I left off, @ "+str(cnt))
lastSave = time()
while True:
    try:
        cnt += 1
        prime = True
        maxNum = math.sqrt(cnt)
        for thing in content:
            if cnt%thing == 0:
                prime = False
                break
            if thing>maxNum:
                break
        if prime:
            content.append(cnt)
        elif cnt%10000 == 0:
            if time()-lastSave > 20:
                print("Saving @ "+str(cnt)+"...",end=" ")
                with open("optimusPrime.txt","w") as f:
                    f.write(json.dumps(content))
                print("All done.")
                lastSave = time()
    except KeyboardInterrupt:
        print("You killed me! With my dying breath, I save @ "+str(cnt)+"...", end=" ")
        with open("optimusPrime.txt","w") as f:
            f.write(json.dumps(content))
        print("All done.")
        raise KeyboardInterrupt
    except Exception as e:
        print("Exception! Panicking and saving @ "+str(cnt)+"...", end=" ")
        with open("optimusPrime.txt","w") as f:
            f.write(json.dumps(content))
        print("All done.")
        raise e