from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    # TODO: crie pelo menos 3 autores.
    # TODO: crie pelo menos 6 livros.
    # TODO: inclua livros disponíveis e indisponíveis.
    # TODO: use session.add ou session.add_all e finalize com session.commit().

    if session.query(Autor).first:
        return

    autor1 = Autor(nome='Antoine de Saint', pais='frança')
    autor2= Autor(nome='Fiódor Dostoiévski' , pais='russia')
    autor3= Autor(nome=' Machado de Assis' , pais='brasil')
    autor4= Autor(nome=' Gabriel García ' , pais='colômbia')
    autor5= Autor(nome=' Miguel de Cervantes' , pais='espanha')

    livro1= Livro(titulo='O Pequeno Príncipe ', ano=1943, autor="Antoine de Saint")
    livro2= Livro(titulo='Crime e Castigo ', ano= 1866, autor="Fiódor Dostoiévsk")
    livro3= Livro(titulo='Memórias Póstumas de Brás Cubas ', ano=1881, autor="Machado de Assis")
    livro4= Livro(titulo='Casa Velha  ', ano=1885, autor="Machado de Assis")
    livro5= Livro(titulo='Cem Anos de Solidão ', ano=1967, autor= "Gabriel García")
    livro6= Livro(titulo='Dom Quixote ', ano=1605, autor= "Miguel de Cervantes")

    session.add_all([autor1,autor2,autor3,autor4,autor5,livro1,livro2,livro3,livro4,livro5,livro6])
    session.commit()