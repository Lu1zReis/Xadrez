"""
import arcade
import tabuleiro as t

arcade.start_render()
"""
class Dama:
    def __init__(self, pos, tab):
        self.posicao   = pos
        self.tabuleiro = tab

    def movimento(self, passo, fim):
        pos = self.posicao + passo
        posicoes = []
        if passo > 0:
            while pos < fim and self.tabuleiro[pos][2] == 0:
                posicoes.append(pos)
                pos += passo
            if pos < fim and self.tabuleiro[pos][3] != self.tabuleiro[self.posicao][3]:
                posicoes.append(pos)
        else:
            while pos >= fim and self.tabuleiro[pos][2] == 0:
                posicoes.append(pos)
                pos += passo
            if pos >= fim and self.tabuleiro[pos][3] != self.tabuleiro[self.posicao][3]:
                posicoes.append(pos)
        return posicoes

    def possibilidades(self):
        movimentos = []
        direita  = self.movimento(1, 64)
        esquerda = self.movimento(-1, 0)
        baixo    = self.movimento(8, 64)
        cima     = self.movimento(-8, 0)
        diag_dir_cima  = self.movimento(-7, 0)
        diag_esq_cima  = self.movimento(-9, 0)
        diag_esq_baixo = self.movimento(7, 64)
        diag_dir_baixo = self.movimento(9, 64)
        x = [direita, esquerda, baixo, cima, diag_dir_cima, diag_dir_baixo, diag_esq_baixo, diag_esq_cima]
        for l in x:
            for v in l:
                movimentos.append(v)
        movimentos.sort()

        return movimentos


"""
xadrez = t.Tabuleiro()

xadrez.cria_tabuleiro()
xadrez.posicionarPeca()
xadrez.mostrar()

pos = 8

dama = Dama(pos, xadrez.tabuleiro)
print(xadrez.tabuleiro[pos])
print(dama.possibilidades()) 

# print(xadrez.tabuleiro)


arcade.finish_render()
arcade.run()
"""
