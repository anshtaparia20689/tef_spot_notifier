import os
from flask import Flask
from tef_notifier import check_tef_page
import threading

app = Flask(__name__)

@app.route("/run")
def run():
    thread = threading.Thread(target=check_tef_page)
    thread.start()
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)