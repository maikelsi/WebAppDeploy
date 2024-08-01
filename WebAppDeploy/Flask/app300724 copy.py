from flask import Flask, render_template

app = Flask(__name__)

@app.route('/curriculo')
def curriculo():
    curriculo = ['Pastor da Rebelião', 'O Atoa e o Pra Nada', 'Chefe Cuzão']
    return render_template('curriculo.html', titulo='CURRICULUM VITAE - SENAI', lista_de_curriculos = curriculo)

app.run()