from flask import Flask, render_template, request
app = Flask('/')


@app.route('/')
def galvenais():
    return render_template('galvenais.html')


@app.route('/viens')
def viens():
    return render_template('viens.html')


@app.route('/divi')
def divi():
    return render_template('divi.html')


@app.route('/galerija')
def galerija():
    return render_template('galerija.html')


@app.route('/veidotaji')
def veidotaji():
    return render_template('veidotaji.html')


@app.route('/parmums')
def parmums():
    return render_template('parmums.html')


if __name__ == "__main__":
  app.run(debug=True)
#app.run('0.0.0.0', port=8020)