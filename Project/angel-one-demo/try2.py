from SmartApi import SmartConnect
import pyotp
import time
api_key = "fAkzzV4V"
client_id = "AAAE708429"
password = "1811"
totp_secret = "KI4UVM3L5QOQZN3O2BGQWAHNDI"

# Generate TOTP
totp = pyotp.TOTP(totp_secret).now()

# Login
obj = SmartConnect(api_key)
login = obj.generateSession(client_id, password, totp)

if login['status']:
    print("Login successful ✅")
else:
    print("Login failed ❌")
    exit()

# Correct symbol format for NIFTY
symbol = 'NIFTY 50'  # or 'NIFTY50-INDEX' depending on API
exchange = 'NSE'

# Fetch live price
try:
    def pathu():
        while(True):
            time.sleep(3)
            quote = obj.ltpData(exchange, symbol,3045)
            print("Live Quote:", quote)
            return quote

except TypeError as e:
    print("TypeError:", e)
    print("Check symbol and exchange format. Must be string exactly as API expects.")