from model.model_cp import plantamode1

class plantacontroller:
    def __init__(self):
        self.model = plantamode1()

    def salvar_plantas(self, nome_popular, nome_cientifico, imagem_path):

        if nome_popular and nome_cientifico:
            return self.model.inserir_planta(nome_popular, nome_cientifico, imagem_path)
        return None