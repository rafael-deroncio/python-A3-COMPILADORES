class Arquivo:

    @staticmethod
    def processar(caminho_arquivo: str) -> str:
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                conteudo: str = arquivo.read()
                if not conteudo:
                    raise ValueError(f"Erro: Arquivo '{caminho_arquivo}' está vazio.")
                return conteudo
        except FileNotFoundError:
            raise FileNotFoundError(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
