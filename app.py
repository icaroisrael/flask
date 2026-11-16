from flask import Flask, redirect, render_template, request, url_for
from conexao import conectar

app = Flask("__main__")

turmas = ["1º INF", "2º INF", "3º INF"]
@app.route("/turma", methods=["GET", "POST"])
def turma():
      con = conectar()
      cursor = con.cursor()
      if request.method == "POST":
            
            descricao = request.form["descricao"]
            sql = """
                        INSERT INTO turma
                        (DESCRICAO)
                        VALUES (%s)
                    """
            values = (descricao,)
            
            cursor.execute(sql, values)
            con.commit()
            cursor.close()
      return render_template("turma.html", turma=turmas)




@app.route("/", methods=["GET", "POST"])
def home():    
    return render_template("index.html")

# CADASTRAR ALUNO
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    con = conectar()
    cursor = con.cursor()
    if request.method == "POST":
        matricula = request.form["matricula"]
        nome = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        sexo = request.form["sexo"]
        email = request.form["email"]
        senha = request.form["senha"]
        turma = request.form["turma"]
        sql = """
            INSERT INTO aluno
            (MATRICULA, NOME, SOBRE_NOME, SEXO, EMAIL, SENHA, TURMA)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (matricula, nome, sobrenome, sexo, email, senha, turma)
        cursor.execute(sql, valores)
        con.commit()
        cursor.close()
        con.close()
        return redirect(url_for("cadastrar"))

        

        #CONSULTAR alunos
        cursor.execute("SELECT * FROM aluno")
        alunos = cursor.fetchall()

        cursor.close()
        con.close()

    return render_template("alunos.html", turmas=turmas)

@app.route("/pesquisarAlunos", methods=["GET", "POST"])
def pesquisarAlunos():
    con = conectar()
    cursor = con.cursor()
    # CONSULTAR ALUNOS
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()
    cursor.close()
    con.close()
    return render_template("pesquisarAlunos.html", alunos=alunos)
    

if __name__ == "__main__":
    app.run(debug=True)

