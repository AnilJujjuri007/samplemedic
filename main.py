from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "Satwika is a API Developer"

if __name__ =="__main__":
    app.run()