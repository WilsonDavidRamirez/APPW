from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return;

@app.route('/enviar')
def enviar():
    return;

@app.route('/borrar')
def borrar():
    return;

if __name__ == '__main__':
    app.run(debug=True, port=5000)


    