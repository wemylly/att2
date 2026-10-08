# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?
Para filtrar , de forma que se o livro estiver como "disponivel" será
possível realizar determinadas funções presentes no código . 

2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
para mandar a mudança para o banco com as informações do livro alteradas , de forma que por exemplo 
se um livro for emprestado o commit manda essa mudança para o banco e agora quando um usuário quiser fazer determinadas 
funções com o livro , só acontece se ele estiver disponível . 

3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?
em listar livros com autor e listar livros de x autores .
