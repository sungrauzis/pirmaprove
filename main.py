from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('chuska.html')

@app.route('/viens')
def viens():
  return render_template('viens.html')


app.run(host='0.0.0.0', port=8020)