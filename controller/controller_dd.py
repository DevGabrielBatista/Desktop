from model.model_dd import Plantamode2

class PlantaController:
    def __init__(self):
        self.model = Plantamode2()

    
    def salvar_dados(self, umidade, luminosidade, temperatura):

        if umidade and luminosidade and temperatura:
            return self.model.inserir_dados(umidade, luminosidade, temperatura)
        return None