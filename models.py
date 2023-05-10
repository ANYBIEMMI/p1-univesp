from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Paciente(db.Model):
    __tablename__ = "pacientes"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    idade = db.Column(db.Integer)
    dtNasc = db.Column(db.Date)
    nomeMae = db.Column(db.String(150))
    nomePai = db.Column(db.String(150))
    dataIngresso = db.Column(db.Date)
    servicoOrigem = db.Column(db.String(150))
    recebeBeneficio = db.Column(db.String(150))
    cep = db.Column(db.String(150))
    rua = db.Column(db.String(150))
    numero = db.Column(db.String(150))
    complemento = db.Column(db.String(150))

    def __init__(self, nome, dtNasc, nomeMae, nomePai, dataIngresso, servicoOrigem, recebeBeneficio, cep, rua,
                 numero, complemento):
        self.nome = nome
        self.dtNasc = dtNasc
        self.nomeMae = nomeMae
        self.nomePai = nomePai
        self.dataIngresso = dataIngresso
        self.servicoOrigem = servicoOrigem
        self.recebeBeneficio = recebeBeneficio
        self.cep = cep
        self.rua = numero
        self.complemento = complemento