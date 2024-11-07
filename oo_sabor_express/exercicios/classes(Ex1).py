class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = Musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = Musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234

restaurante_praca.categoria = 'Italiana'

nome_do_restaurante = restaurante_praca.nome

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

    categoria = Restaurante.categoria

    restaurante_praca.nome = 'Bistrô'

    restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

restaurante_pizza.ativo = True

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')