from flask import Flask, render_template

app = Flask(__name__)

# Dados dos projetos
projects = [
    {
        "title": "Sistema de Gerenciamento de Estoque",
        "description": "Um sistema para gerenciar produtos de estoque com CRUD completo.",
        "technologies": "Python, Flask, MySQL",
        "link": "https://github.com/seu-perfil/estoque-projeto",
        "image": "estoque.jpg"
    },
    {
        "title": "Sistema de Gestão Acadêmica",
        "description": "Gerencia estudantes, cursos e notas com relatórios dinâmicos.",
        "technologies": "Java, PostgreSQL, JavaFX",
        "link": "https://github.com/seu-perfil/gestao-academica",
        "image": "gestao_academica.png"
    },
    {
        "title": "Dashboard de Análise de Dados",
        "description": "Painel interativo para visualizar dados financeiros.",
        "technologies": "Python, Dash, Plotly",
        "link": "https://github.com/seu-perfil/dashboard-analise",
        "image": "dashboard.png"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
