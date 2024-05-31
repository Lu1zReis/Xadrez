import arcade
import tabuleiro as t

arcade.start_render()

xadrez = t.Tabuleiro()
xadrez.cria_tabuleiro()
xadrez.posicionarPeca()
xadrez.mostrar()

print(xadrez.tabuleiro)


return []


arcade.finish_render()
arcade.run()
