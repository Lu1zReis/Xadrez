# criar uma funçao para arrumar as peças na posição certa na matriz pecas_list()
# já que na parte de posicionar por exemplo peças como a torre, colocamos uma próxima a outra

import arcade
import arcade.color
import arcade.gui
import tabuleiro
import damas

arcade.start_render()

xadrez = tabuleiro.Tabuleiro()

xadrez.cria_tabuleiro()
xadrez.posicionarPeca()
print(xadrez.tabuleiro)

# movimentando uma peça

getPeca = 8
destino = 16 * 2

# escolhemos a peça e pegamos suas coordenadas
mx = xadrez.tabuleiro[getPeca][0] # x da tela
my = xadrez.tabuleiro[getPeca][1] # y da tela

# achamos a poisicao correspondente no array dos sprites (já que lá não esta ordenado) 
p  = xadrez.posicao(mx, my)
sprite = xadrez.pecas_list[p] 

# pegamos a coordenada aonde queremos ir
dx = xadrez.tabuleiro[destino][0]
dy = xadrez.tabuleiro[destino][1]

# mudamos a posicao do sprite que escolhemos
sprite.center_x = dx
sprite.center_y = dy

# colocamos ele na posicao da lista novamente
xadrez.pecas_list[p] = sprite

xadrez.mostrar()

arcade.gui.UIInputText()

"""
dama = damas.Dama(12, xadrez.tabuleiro)
print(dama.possibilidades())
"""

arcade.finish_render()
arcade.run()