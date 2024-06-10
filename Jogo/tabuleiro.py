import arcade
"""
# ---------CONSTANTES----------
resolucao_x = 400
resolucao_y = 400


#    CONFIGURAÇÕES

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(resolucao_x, resolucao_y, "Xadrez")
# fundo
arcade.set_background_color(arcade.color.MOONSTONE_BLUE)
# arcade.start_render()
"""

class Tabuleiro(arcade.Window):
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
        self.mesa = arcade.Sprite()
        # arcade.start_render()

        self.entrada_texto = ''

    def cria_tabuleiro(self):
        self.mesa = arcade.Sprite('pecas/tabuleiro/mesa.png', 0.73)
        x = self.inicio_x
        y = self.inicio_y
        self.mesa.center_x = x + 90
        self.mesa.center_y = y - 120
        for linha in range(8):
            for coluna in range(8):
                self.tabuleiro.append([x, y, 0, -1])
                x += self.espaco
            y -= self.espaco
            x = self.inicio_x

    def pecas(self, caminho, nome, soma, aux, dist = None, numPeca = 0, cor = 1):
        if nome == 'peao':    
            for i in range(8):
                self.sprites['peao'] = arcade.Sprite(f'{caminho}/peao.png', 0.06)
                self.sprites['peao'].center_x = self.tabuleiro[i+soma][0]
                self.sprites['peao'].center_y = self.tabuleiro[i+soma][1]
                self.pecas_list.append(self.sprites['peao'])
                self.tabuleiro[i+soma][2] = numPeca # setando o valor da para identificar qual é a peça
                self.tabuleiro[i+soma][3] = cor # mostrando se aquela peça é preta ou branca

        elif nome == 'dama' or nome == 'rei':
            tam = 0.055
            self.tabuleiro[soma+aux+dist][2] = numPeca # setando o valor da para identificar qual é a peça
            self.tabuleiro[soma+aux+dist][3] = cor # mostrando se aquela peça é preta ou branca
            if nome == 'dama':
                tam = 0.036
            self.sprites[nome] = arcade.Sprite(f'{caminho}/{nome}.png', tam)
            self.sprites[nome].center_x = self.tabuleiro[soma+aux+dist][0]
            self.sprites[nome].center_y = self.tabuleiro[soma+aux+dist][1] 
            self.pecas_list.append(self.sprites[nome])
        else:
            self.tabuleiro[soma+aux+dist][2] = numPeca # setando o valor da para identificar qual é a peça
            self.tabuleiro[soma+aux+dist][3] = cor # mostrando se aquela peça é preta ou branca
            self.sprites[nome] = arcade.Sprite(f'{caminho}/{nome}.png', 0.06)
            self.sprites[nome].center_x = self.tabuleiro[soma+aux+dist][0]
            self.sprites[nome].center_y = self.tabuleiro[soma+aux+dist][1]
            self.pecas_list.append(self.sprites[nome])
            d = 7 - dist
            self.tabuleiro[soma+aux+d][2] = numPeca
            self.tabuleiro[soma+aux+d][3] = cor
            self.sprites[nome] = arcade.Sprite(f'{caminho}/{nome}.png', 0.06)
            self.sprites[nome].center_x = self.tabuleiro[soma+aux+d][0]
            self.sprites[nome].center_y = self.tabuleiro[soma+aux+d][1]
            self.pecas_list.append(self.sprites[nome])
            

    def posicionar_auxiliar(self, caminho, soma, cor): 
        aux = 8
        if soma == 8:
            aux = -8

        # setando nas posições
        """
            * cada peça terá um peso (que é passada no 6 parametro) pra calculo posterior na conta do minimax()
            * variavel soma serve como uma variavel auxiliar para posicionar as peças pra cima ou baixo
        """
        self.pecas(caminho, 'peao', soma, aux, None, 50, cor)
        self.pecas(caminho, 'torre', soma, aux, 0, 100, cor)
        self.pecas(caminho, 'cavalo', soma, aux, 1, 200, cor)
        self.pecas(caminho, 'bispo', soma, aux, 2, 130, cor)
        self.pecas(caminho, 'dama', soma, aux, 3, 500, cor)
        self.pecas(caminho, 'rei', soma, aux, 4, 1000, cor)
        

    def posicionarPeca(self):
        # setar 8 ou 48
        self.posicionar_auxiliar('pecas/branco', 8, 0) 
        self.posicionar_auxiliar('pecas/preto', 48, 1)
    
    
    def mostrar(self):
        arcade.start_render()
        self.pecas_list.draw();
        self.mesa.draw()
  

    def posicao(self, x, y):
        for i in range(0, len(self.pecas_list)):
            if self.pecas_list[i].center_x == x and self.pecas_list[i].center_y == y:
                return i


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
