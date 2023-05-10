from flask import Flask, render_template, request, url_for, redirect
from models import db,Paciente

app = Flask(__name__, template_folder='templates')
# conexao com o banco
app.config['SQLALCHMY DATABASE_URI'] = 'sqlite:///pacientes.db'

db.init_app(app)
@app.before_first_request
def create_table():
    db.create_all()

@app.route('/')
def index():
    pacientes = Paciente.query.all()
    return render_template('index.html', pacientes=pacientes)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        paciente = Paciente(request.form['nome'], request.form['dtNasc'], request.form['nomeMae'],request.form['nomePai'], request.form['dataIngresso'], request.form['servicoOrigem'], request.form['recebeBeneficio'], request.form['cep'], request.form['rua'], request.form['numero'], request.form['complemento'])



    app.run(host='localhost',port=5000)
