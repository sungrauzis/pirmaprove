from flask import Flask, render_template, request
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

if __name__ == "__main__":
  app.run(debug=True)
#app.run('0.0.0.0', port=8020)