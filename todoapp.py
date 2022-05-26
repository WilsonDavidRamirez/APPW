from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return  render_template('mostrar.html');

@app.route('/enviar')
def enviar():
    return  render_template('enviar.html');

@app.route('/borrar')
def borrar():
    return  render_template('borrar.html');

if __name__ == '__main__':
    app.run(debug=True, port=5000)

   
def listToString(lista): 
    
    str1 = " " 
    
    # return string  
    return (str1.join(lista))
        
        
# Driver code    
miLista = [ "HolaMundo", "HolaMundo2"] 
print(listToString(miLista))