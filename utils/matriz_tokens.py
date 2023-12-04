from typing import List, Tuple

MATRIZ_TOKENS: List[Tuple[str, str]] = [
    (r'\d+', 'NUMERO'),
    (r'\+', 'MAIS'),
    (r'-', 'MENOS'),
    (r'\*', 'VEZES'),
    (r'/', 'DIVIDIDO'),
    (r'\(', 'PARENTESES_ABERTO'),
    (r'\)', 'PARENTESES_FECHADO'),
]
