from flask import Flask, json, jsonify, render_template, request
import chats
app = Flask('/')


@app.route('/')
def galvenais():
    return render_template('suni.html')


@app.route('/galerija')
def galerija():
    return render_template('pile.html')


@app.route('/veidotaji')
def veidotaji():
    return render_template('veidotaji.html')


@app.route('/parmums')
def parmums():
    return render_template('parmums.html')


@app.route('/about')
def about():
    return render_template('aboutpage.html')

@app.route('/chat')
def index_lapa():
  return render_template('chats.html')


@app.route('/chats/lasi')
def ielasit_chatu():
  return chats.lasi()


@app.route('/chats/suuti', methods=['POST'])
def suutiit_zinju():
  dati = request.json
  
  chats.pieraksti_zinju(dati)

  return chats.lasi()
if __name__ == "__main__":
  app.run(debug=True)
#app.run('0.0.0.0', port=8020)