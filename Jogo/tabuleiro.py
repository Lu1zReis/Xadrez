import arcade

# ---------CONSTANTES----------
resolucao_x = 400
resolucao_y = 400
"""
    CONFIGURAÇÕES
"""
# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(resolucao_x, resolucao_y, "Xadrez")
# fundo
arcade.set_background_color(arcade.color.MOONSTONE_BLUE)
# arcade.start_render()

class Tabuleiro():
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
            arcade.draw_text(f'{self.lateral[texto_acima]}', x-4, y+25, arcade.color.BLACK)
            x += self.espaco-1
        x = self.inicio_x


        for linha in range(8):
            # mudar as cores do quadrado
            aux = 0
            if linha % 2 == 0:
                aux = 0
            else:
                aux = 1
            
            arcade.draw_text(f'{linha}', x-self.espaco-5, y-4, arcade.color.BLACK)
            for coluna in range(8):
                self.tabuleiro.append([x, y, 0])
                # x, y, width, height, color
                if coluna % 2 == aux:
                    arcade.draw_rectangle_filled(x, y, self.largQuadrado, self.compQuadrado, arcade.color.AO)
                else:
                    arcade.draw_rectangle_filled(x, y, self.largQuadrado, self.compQuadrado, arcade.color.YELLOW)

                x += self.espaco
            y -= self.espaco
            x = self.inicio_x


    def pecas(self, caminho, nome, soma, aux, dist = None, numPeca = 0):
        if nome == 'peao':    
            for i in range(8):
                self.sprites['peao'] = arcade.Sprite(f'{caminho}/peao.png', 0.06)
                self.sprites['peao'].center_x = self.tabuleiro[i+soma][0]
                self.sprites['peao'].center_y = self.tabuleiro[i+soma][1]
                self.pecas_list.append(self.sprites['peao'])
                self.tabuleiro[i+soma][2] = numPeca

        elif nome == 'dama' or nome == 'rei':
            tam = 0.055
            self.tabuleiro[soma+aux+dist][2] = numPeca
            if nome == 'dama':
                tam = 0.036
            self.sprites[nome] = arcade.Sprite(f'{caminho}/{nome}.png', tam)
            self.sprites[nome].center_x = self.tabuleiro[soma+aux+dist][0]
            self.sprites[nome].center_y = self.tabuleiro[soma+aux+dist][1] 
            self.pecas_list.append(self.sprites[nome])
        else:
            self.tabuleiro[soma+aux+dist][2] = numPeca
            self.sprites[nome] = arcade.Sprite(f'{caminho}/{nome}.png', 0.06)
            self.sprites[nome].center_x = self.tabuleiro[soma+aux+dist][0]
            self.sprites[nome].center_y = self.tabuleiro[soma+aux+dist][1]
            self.pecas_list.append(self.sprites[nome])
            d = 7 - dist
            self.tabuleiro[soma+aux+d][2] = numPeca
            self.sprites[nome] = arcade.Sprite(f'{caminho}/{nome}.png', 0.06)
            self.sprites[nome].center_x = self.tabuleiro[soma+aux+d][0]
            self.sprites[nome].center_y = self.tabuleiro[soma+aux+d][1]
            self.pecas_list.append(self.sprites[nome])
            

    def posicionar_auxiliar(self, caminho, soma): 
        aux = 8
        if soma == 8:
            aux = -8

        # setando nas posições
        self.pecas(caminho, 'peao', soma, aux, None, 6)
        self.pecas(caminho, 'torre', soma, aux, 0, 5)
        self.pecas(caminho, 'cavalo', soma, aux, 1, 4)
        self.pecas(caminho, 'bispo', soma, aux, 2, 3)
        self.pecas(caminho, 'dama', soma, aux, 3, 2)
        self.pecas(caminho, 'rei', soma, aux, 4, 1)
        

    def posicionarPeca(self):
        # setar 8 ou 48
        self.posicionar_auxiliar('pecas/branco', 48) 
        self.posicionar_auxiliar('pecas/preto', 8)
    

    def mostrar(self):
        self.pecas_list.draw();

"""
xadrez = Tabuleiro()
xadrez.cria_tabuleiro()
xadrez.posicionarPeca()
xadrez.mostrar()
# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
"""
