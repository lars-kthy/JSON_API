# ____        _____   __________   _________ 
#|    |      /  _  \  \______   \ /   _____/
#|    |     /  /_\  \  |       _/ \_____  \ 
#|    |___ /    |    \ |    |   \ /        \
#|_______ \____|__  / |____|_  //_______  /
#        \/        \/         \/         \/ 

# BRONNENLIJST 03-04-2025:
# 1. Copilot in Visual Studio Code by GitHub - 03-04-2025
# 2. Flask Documentation - https://flask.palletsprojects.com/ - 03-04-2025
# 3. My Json Server documentation - https://my-json-server.typicode.com/ - 03-04-2025
# 4. Jinja2 Documentation - https://jinja.palletsprojects.com/ - 03-04-2025
# 5 Jinja2 For Loops voor - https://jinja.palletsprojects.com/en/stable/templates/#for - 03-04-2025
# 6. Jinja2 If Statements - https://jinja.palletsprojects.com/en/stable/templates/#if - 03-04-2025

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://my-json-server.typicode.com/lars-kthy/JSON_API/klassieke_autos"

@app.route("/")
def index():
    response = requests.get(API_URL)
    autos = response.json() if response.status_code == 200 else []

    return render_template("index.html", autos=autos)

@app.route("/auto")
def auto_detail():
    auto_id = request.args.get("id")
    response = requests.get(API_URL)
    autos = response.json() if response.status_code == 200 else []

    auto = next((a for a in autos if str(a['ID']) == auto_id), None)
    
    return render_template("detail.html", auto=auto)

if __name__ == "__main__":
    app.run(debug=True)
