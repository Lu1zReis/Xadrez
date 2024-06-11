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
        self.init_peca        = None
        self.end_peca         = None
        self.selected_sprite = None

    def on_draw(self):
        arcade.start_render()
        self.xadrez.mesa.draw()
        self.xadrez.pecas_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        # Evento de clique do mouse
        sprites_hit = arcade.get_sprites_at_point((x, y), self.xadrez.pecas_list)
        
        self.init_peca = self.xadrez.posicao_sprites(x, y) 

        if len(sprites_hit) > 0:
            self.selected_sprite = sprites_hit[0]
    
    def on_mouse_release(self, x, y, button, modifiers):
        # Evento de soltar o mouse
        self.end_peca = self.xadrez.posicao_sprites(x, y)
        posicao_correta = self.xadrez.posicao_tabuleiro(x, y)
        print(self.init_peca, self.end_peca, posicao_correta, [x, y])
        if len(self.init_peca) and len(self.end_peca) and len(posicao_correta):
            self.xadrez.pecas_list[self.end_peca[0]].center_x = posicao_correta[0]
            self.xadrez.pecas_list[self.end_peca[0]].center_y = posicao_correta[1]
        else:
            if self.selected_sprite != None:
                posicao_correta = self.xadrez.posicao_tabuleiro(self.init_peca[1], self.init_peca[2])
                self.xadrez.pecas_list[self.init_peca[0]].center_x = posicao_correta[0]
                self.xadrez.pecas_list[self.init_peca[0]].center_y = posicao_correta[1]

        self.selected_sprite = None

    def on_mouse_motion(self, x, y, dx, dy):
        # Evento de movimento do mouse
        if self.selected_sprite:
            self.selected_sprite.center_x = x
            self.selected_sprite.center_y = y

def main ():
    jogo = MyGame()
    # print(jogo.xadrez.tabuleiro)
    arcade.run()

if __name__ == "__main__":
    main()
