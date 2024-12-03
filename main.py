from cliente import Cliente
from carro import Carro
from moto import Moto


cliente1 = Cliente("Marco")
cliente2 = Cliente("Antonio")


carro1 = Carro("ABC123", 100)
carro2 = Carro("XYZ789", 80)
moto1 = Moto("DEF456", 50)
moto2 = Moto("GHI789", 40)


print(carro1.alugar(cliente1, 5))
print(carro2.alugar(cliente2, 15))
print(moto1.alugar(cliente1, 40))
print(moto2.alugar(cliente2, 8))


print(carro1.alugar(cliente2, 3))


print(carro1.devolver())
print(carro2.devolver())


print(carro1.listar_historico())
print(moto1.listar_historico())
