import arcade

# ---------CONSTANTES----------
resolucao_x = 400
resolucao_y = 400

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(resolucao_x, resolucao_y, "Xadrez")
# fundo
arcade.set_background_color(arcade.color.MOONSTONE_BLUE)

arcade.start_render()

"""

##


"""

class Xadrez():
    def __init__(self):
        self.largQuadrado = 30
        self.compQuadrado = 30
        self.espaco = self.compQuadrado 
        self.tabuleiro = []
        self.lateral = ['A','B','C','D','E','F','G','H']
        self.inicio_x = 100
        self.inicio_y = 320
        self.sprites = {'rei': None, 'dama': None, 'bispo': None, 'cavalo': None, 'torre': None, 'peao': None}
        self.pecas_list = arcade.SpriteList()

    def cria_tabuleiro(self):
        
        x = self.inicio_x
        y = self.inicio_y

        # colocar os numeros em cima do tabuleiro (1 a 8)
        for texto_acima in range(8):
            arcade.draw_text(f'{texto_acima}', x, y+25, arcade.color.BLACK)
            x += self.espaco-1
        x = self.inicio_x


        for linha in range(8):
            # mudar as cores do quadrado
            aux = 0
            if linha % 2 == 0:
                aux = 0
            else:
                aux = 1
            
            arcade.draw_text(f'{self.lateral[linha]}', x-self.espaco-5, y-4, arcade.color.BLACK)
            for coluna in range(8):
                self.tabuleiro.append([x, y])
                # x, y, width, height, color
                if coluna % 2 == aux:
                    arcade.draw_rectangle_filled(x, y, self.largQuadrado, self.compQuadrado, arcade.color.AO)
                else:
                    arcade.draw_rectangle_filled(x, y, self.largQuadrado, self.compQuadrado, arcade.color.YELLOW)

                x += self.espaco
            y -= self.espaco
            x = self.inicio_x

    def posicionarPeca(self):
        self.sprites['cavalo'] = arcade.Sprite('pecas/cavalo_preto.png', 0.05)
        self.sprites['cavalo'].center_x = self.tabuleiro[1][0]
        self.sprites['cavalo'].center_y = self.tabuleiro[1][1]
        
        self.pecas_list.append(self.sprites['cavalo'])
        
        self.sprites['cavalo'] = arcade.Sprite('pecas/cavalo_preto.png', 0.05)
        self.sprites['cavalo'].center_x = self.tabuleiro[6][0]
        self.sprites['cavalo'].center_y = self.tabuleiro[6][1]

        self.pecas_list.append(self.sprites['cavalo'])
        self.pecas_list.draw()


xadrez = Xadrez()
xadrez.cria_tabuleiro()
xadrez.posicionarPeca()

# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

