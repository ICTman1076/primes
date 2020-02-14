# DOCS
# When executed in IDLE, you can use the p variable.
# When imported, you must construct the class. To do this, use
#     <variableName> = primeslib.Primes()
# You can provide an alternative source by passing it as an argument. It must
# be a JSON list of prime numbers.
#
# To get the primes as a list, do <variableName>.primes (when in IDLE, p.primes)
# To refresh the primes, do <variableName>.refresh()

import json
import urllib.request as url
import ssl

class Primes:
    def __init__(self, src="http://ictman1076.eu.pythonanywhere.com/primes.txt"):
        self.src = src
        self.refresh()

    def refresh(self, src="default"):
        if src == "default":
            src = self.src
        # ssl stuff, so it works in areas with ssl interception - it's not like
        # this is secure data so it doesn't matter about the cert.
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        self.request = url.urlopen(src, context=ctx)
        self.rawData = self.request.read()
        self.data = self.rawData.decode()
        self.primes = json.loads(self.data)

if __name__ == "__main__":
    p = Primes()