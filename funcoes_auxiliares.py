import pygame
import random

class ImageLoader:
    img_set = {}

    def load_image():
        for numero in range(1, 11):
            for naipe in ['C', 'O', 'P', 'E']:
                nome_arquivo = f'assets/images/{numero}{naipe}.png'
                ImageLoader.img_set[f'{numero}{naipe}'] = pygame.image.load(nome_arquivo)

ImageLoader.load_image()

def sorteia_carta():
    """
    Sorteia uma carta aleatória do baralho.

    Recebe um dicionário com as imagens do baralho.

    Retorna uma tupla com o número e naipe da carta sorteada.
    """
    numero = random.randint(1, 10)
    naipe = random.choice(['C', 'O', 'P', 'E'])
    np = 'Copas' if naipe == 'C' else 'Ouros' if naipe == 'O' else 'Paus' if naipe == 'P' else 'Espadas'
    retorno = {
        "numero": numero,
        "naipe": np,
        "imagem": ImageLoader.img_set[f'{numero}{naipe}']
    }
    return retorno