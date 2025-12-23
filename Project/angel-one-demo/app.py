from flask import Flask, jsonify
from SmartApi import SmartConnect
import pyotp
from config import API_KEY, CLIENT_ID, PASSWORD, TOTP_SECRET

# ---------------- LOGIN ----------------
obj = SmartConnect(api_key=API_KEY)

totp = pyotp.TOTP(TOTP_SECRET).now()
login = obj.generateSession(CLIENT_ID, PASSWORD, totp)

if not login["status"]:
    print("❌ Login Failed")
    exit()

print("✅ Angel One Login Successful")

# ---------------- FLASK ----------------
app = Flask(__name__)

# ---------- FUNCTION TO FETCH LTP ----------
def get_nifty_ltp():
    quote = obj.ltpData(
        exchange="NSE",
        tradingsymbol="NIFTY",
        symboltoken="26000"
    )
    return quote["data"]["ltp"]

# ---------- API FOR WEBSITE ----------
@app.route("/prices")
def prices():
    try:
        ltp = get_nifty_ltp()
        return jsonify({
            "symbol": "NIFTY 50",
            "ltp": ltp
        })
    except Exception as e:
        return jsonify({"error": str(e)})

# ---------- BUTTON CLICK API ----------
@app.route("/run-pathu", methods=["POST"])
def run_pathu():
    try:
        ltp = get_nifty_ltp()
        return jsonify({
            "status": "success",
            "ltp": ltp
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)
