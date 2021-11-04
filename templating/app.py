from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ben')
def ben():
    return render_template('ben.html')


@app.route('/harry')
def ben():
    return render_template('harry.html')


@app.route('/bob')
def ben():
    return render_template('bob.html')


@app.route('/jay')
def ben():
    return render_template('jay.html')


@app.route('/matt')
def ben():
    return render_template('matt.html')


@app.route('/bill')
def ben():
    return render_template('bill.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')