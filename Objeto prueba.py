import random
class Mascota: 
    comidas=["Pizza","Sushi","Pan","Huevo","Tomate","Pepino","Manzana","Platano","Arroz"]
    bebidas=["Agua","Pisco","Jugo","Café","Gaseosa"]
    
    def __init__(self,nombre: str,color: str,):
        global comidas
        global bebidas
        comidas_p=[]+comidas
        bebidas_p=[]+bebidas
        self.nombre=nombre
        self.color=color
        self.edad=0
        self.salud=100
        self.sed=100
        self.hambre=100
        self.felicidad=50
        self.energia=100
        self.tamaño=[2,3]
        self.suciedad=0
        
        a=[]
        for i in range(3):
            b=random.choice(comidas)
            comidas_p.remove(b)
            a.append(random.choice(comidas))
        
                
        self.comidas_favoritas=a

        a=[]
        for i in range(3):
            b=random.choice(comidas)
            comidas_p.remove(b)
            a.append(random.choice(comidas))

        self.comidas_malas=
    
    def comer(self):
        global comidas
        print(f"Elige uno de los siguientes alimentos para darle a (self.nombre):")
        for i in range(1en(comidas)):
        print(f"i+1"). (comidas[i])
           

a=Mascota("Satoru Gojo","blanco")      

