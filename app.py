from flask import Flask 

app = Flask(__name__)

@app.route('/')

def healthcheck():
  return "ok"

@app.route('/home')
def home():
    return '<h1>we are home</h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 80,debug=True)