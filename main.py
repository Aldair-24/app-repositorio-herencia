from model.Deportivo import Deportivo
from model.Furgoneta import Furgoneta

objDeprotivo=Deportivo("ferrari","488", 2021, 330)
print(objDeprotivo.descripcion())
print(objDeprotivo.tipo())

objFurgoneta=Furgoneta("conbi", "230", "2024", "350lg")
print(objFurgoneta.descripcion())
