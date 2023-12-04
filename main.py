from utils.gerenciadores import Arquivo
from utils.analisadores import Lexica, Sintatica, Semantica

if __name__ == '__main__':
    conteudo_arquivo = Arquivo.processar('expressoes.txt')
    
    tokens = Lexica.analisar(conteudo_arquivo, True)
    
    arvore_sintatica = Sintatica.analisar(tokens, True)
    
    analise_semantica = Semantica.analisar(arvore_sintatica, True)