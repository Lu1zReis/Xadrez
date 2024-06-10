# criar uma funçao para arrumar as peças na posição certa na matriz pecas_list()
# já que na parte de posicionar por exemplo peças como a torre, colocamos uma próxima a outra

import arcade
import arcade.color
import arcade.gui
import tabuleiro
import damas

# ---------CONSTANTES----------
resolucao_x = 400
resolucao_y = 400


# arcade.start_render()

class MyGame(arcade.Window):
    def __init__(self):
        #    CONFIGURAÇÕES
        # Open the window. Set the window title and dimensions (width and height)
        super().__init__(resolucao_x, resolucao_y, "Xadrez")
        # fundo
        arcade.set_background_color(arcade.color.MOONSTONE_BLUE)
        self.xadrez = tabuleiro.Tabuleiro()
        self.xadrez.cria_tabuleiro()
        self.xadrez.posicionarPeca()
        self.peca_selecionada = None
        self.entrada_texto = ''

    def on_draw(self):
        arcade.start_render()
        self.xadrez.mesa.draw()
        self.xadrez.pecas_list.draw()
        arcade.draw_text(f"Digite as coordenadas (x, y): {self.entrada_texto}", 3, 40, arcade.color.BLACK, 12)

    def on_text(self, text):
        # Evento de digitar texto
        if text.isdigit() or text == ',':
            self.entrada_texto += text

def main ():
    jogo = MyGame()
    print(jogo.xadrez.tabuleiro)
    arcade.run()

if __name__ == "__main__":
    main()

"""
xadrez = tabuleiro.Tabuleiro()

xadrez.cria_tabuleiro()
xadrez.posicionarPeca()
# print(xadrez.tabuleiro)

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

# arcade.gui.UIInputText()
# dama = damas.Dama(12, xadrez.tabuleiro)
# print(dama.possibilidades())
"""