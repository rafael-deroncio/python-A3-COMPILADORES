import re
from typing import List, Tuple, Union
from utils.matriz_tokens import MATRIZ_TOKENS

class Lexica:
    """
    A classe Lexica é responsável pela análise léxica de expressões matemáticas simples.
    """

    @staticmethod
    def analisar(texto_entrada: str, exibir_resultados: bool) -> List[Tuple[str, str]]:
        """
        Realiza a análise léxica do texto de entrada e retorna uma lista de tokens.

        Args:
            texto_entrada (str): A expressão matemática de entrada.
            exibir_resultados (bool): Indica se os resultados da análise devem ser exibidos.

        Returns:
            List[Tuple[str, str]]: Lista de tokens representados como tuplas (tipo_token, valor).
        """
        tokens: List[Tuple[str, str]] = Lexica.tokenizar(texto_entrada)
        if exibir_resultados:
            Lexica.__exibir_resultados(tokens)
        
        return tokens

    @classmethod
    def tokenizar(cls, texto_entrada: str) -> List[Tuple[str, str]]:
        """
        Divide o texto de entrada em expressões individuais e chama analisar_expressao
        para obter os tokens de cada expressão.

        Args:
            texto_entrada (str): A expressão matemática de entrada.

        Returns:
            List[Tuple[str, str]]: Lista de tokens representados como tuplas (tipo_token, valor).
        """
        tokens = []
        for expressao in texto_entrada.split(';'):
            expressao = expressao.strip()
            if expressao:
                tokens.append(cls.analisar_expressao(expressao))
        return tokens

    @classmethod
    def analisar_expressao(cls, expressao: str) -> List[Tuple[str, str]]:
        """
        Analisa uma expressão individual e retorna uma lista de tokens.

        Args:
            expressao (str): A expressão matemática individual.

        Returns:
            List[Tuple[str, str]]: Lista de tokens representados como tuplas (tipo_token, valor).

        Raises:
            ValueError: Se um caractere inválido for encontrado na expressão.
        """
        tokens = []
        while expressao:
            for padrao, tipo_token in MATRIZ_TOKENS:
                correspondencia = re.match(padrao, expressao)
                if correspondencia:
                    valor = correspondencia.group(0)
                    tokens.append((tipo_token, valor))
                    expressao = expressao[len(valor):].lstrip()
                    break
            else:
                raise ValueError('Caractere inválido: ' + expressao[0])
        return tokens
    
    @staticmethod
    def __exibir_resultados(analise_tokens: List[Tuple[str, str]]) -> None:
        """
        Exibe os resultados da análise léxica.

        Args:
            analise_tokens (List[Tuple[str, str]]): Lista de tokens.

        Returns:
            None
        """
        print("Resultados da análise Léxica: ")
        for resultado in analise_tokens:
            print(f'Tokens válidos: ', ', '.join([f'{r[0]}' for r in resultado]))
        print("\n")


class Sintatica:
    @staticmethod
    def analisar(tokens: List[Tuple[str, str]], exibir_resultados: bool) -> List[str]:
        """
        Realiza a análise sintática da lista de tokens.

        Args:
            tokens (List[Tuple[str, str]]): Lista de tokens.
            exibir_resultados (bool): Indica se os resultados da análise devem ser exibidos.

        Raises:
            ValueError: Se a análise sintática encontrar um erro na expressão.

        Returns:
            None
        """
        tokens_tipo_valor = Sintatica.__separar_tipo_valor_toen(tokens)
        
        if exibir_resultados:
                print('Resultados da análise Sintática:')
        
        for i, token in enumerate(tokens_tipo_valor):
            expressao = Sintatica.__obter_expressao(token[1])
                        
            if not Sintatica.__validar_parenteses_expressao(expressao):
                if exibir_resultados:
                    print(f'Expressão inválida: {expressao}')
                    
                raise ValueError(f'Expressão inválida: {expressao} - parêntese aberto ou número negativo sem correspondência.')
            
            if exibir_resultados:
                print(f'Expressão válida: {expressao}')
            
        return [valores[1] for valores in tokens_tipo_valor]

    @staticmethod
    def __separar_tipo_valor_toen(tokens: List[Tuple[str, str]]) -> List[Tuple[List[str], List[str]]]:
        """
        Separa os tipos e valores dos tokens.

        Args:
            tokens (List[Tuple[str, str]]): Lista de tokens.

        Returns:
            List[Tuple[List[str], List[str]]]: Lista de tuplas contendo listas de tipos e valores.
        """
        return [([t[0] for t in token], [t[1] for t in token]) for token in tokens]

    @staticmethod
    def __obter_expressao(expressao: List[str]) -> str:
        """
        Obtém a expressão completa a partir da lista de valores.

        Args:
            expressao (List[str]): Lista de valores.

        Returns:
            str: Expressão obtida concatenando os valores da lista.
        """
        return ''.join([expr for expr in expressao])

    @staticmethod
    def __validar_parenteses_expressao(expressao: str) -> bool:
        """
        Valida a correspondência de parênteses em uma expressão.

        Args:
            expressao (str): Expressão a ser validada.

        Returns:
            bool: True se a correspondência de parênteses for válida, False caso contrário.
        """
        pilha = []
        
        for simb in expressao:
            if simb == '(':
                pilha.append('(')
            elif simb == ')':
                if len(pilha) > 0:
                    pilha.pop()
                else:
                    pilha.append(')')
                    break
        return len(pilha) == 0


from typing import List, Tuple

class Semantica:
    @staticmethod
    def analisar(expressoes: str, exibir_resultados: bool) -> float:
        resultados: List[Tuple[str, int]] = []
        expr: str = ''
        resl: str = 0
        
        for expressao in expressoes:
            expr = ''.join(expressao)
            try:
                resl = eval(expr)
                resultados.append((expr, resl))

            except SyntaxError as se:
                resultados.append((expr, "Erro de sintaxe"))

            except ZeroDivisionError as ze:
                resultados.append((expr, "Erro Divisão por zero"))
    
            except Exception as e:
                resultados.append((expr, f"Erro inesperado: {e}"))
        
        if exibir_resultados:
            print("\nResultados da análise Semântica: ")
            for resultado in resultados:
                if not isinstance(resultado[1], str):
                    print(f'Expressão válida: {resultado[0]}', end='')
                else:
                    print(f'Expressão inválida: {resultado[0]}', end='')
                
                print(' = ', resultado[1])
        
        return resultados