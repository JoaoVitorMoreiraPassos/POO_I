import os
class Televisao():
    def __init__(self):
        self._volume = None
        self._canal = None
        self._canais = [7, 11, 13]
        self.sintoniza()
        
    def sintoniza(self):
        self.volume = 0    
        self.canal = self.canais[0]
    
    @property
    def volume(self):
        return self._volume
    @volume.setter
    def volume(self, vol):
        self._volume = vol
    
    @property
    def canal(self):
        return self._canal
    @canal.setter
    def canal(self, cn):
        self._canal = cn
    
    @property
    def canais(self):
        return self._canais
    @canais.setter
    def addCanal(self, num):
        if(num not in self.canais):
            self._canais.append(num)
            self._canais.sort()
        
class Controle():
    def __init__(self):
        pass

    def menu(self,tv):
        print("0 - Escolha um canal\n1 - Aumentar volume\n2 - Diminuir volume\n3 - Aumentar canal\n4 - Diminuir canal\n5 - Consultar volume\n6 - Consultar canal\n7 - Sair")
        escolha = input("Escolha: ")
        
        if(escolha == "0"):
            return self.trocaCanal(tv, int(input("Canal: ")))
        elif(escolha == "1"):
            return self.aumentaVolume(tv)
        elif(escolha == "2"):
            return self.diminuiVolume(tv)
        elif(escolha == "3"):
            return self.aumentaCanal(tv)
        elif(escolha == "4"):
            return self.diminuiCanal(tv)
        elif(escolha == "5"):
            return self.mostraVolume(tv)
        elif(escolha == "6"):
            return self.mostraCanal(tv)
        elif(escolha == "7"):
            return -1
        else:
            return 3 
        
    def aumentaVolume(self, tv):
        if(tv.volume < 100):
            tv.volume += 1
        return 1
        
    def diminuiVolume(self, tv):
        if(tv.volume > 0):
            tv.volume -= 1
        return 1
        
    def aumentaCanal(self, tv):
        if(tv.canal == tv.canais[-1]):
            tv.canal = tv.canais[0]
        else:        
            tv.canal = tv.canais[tv.canais.index(tv.canal)+1]
        return 2

    def diminuiCanal(self, tv):
        if(tv.canal == tv.canais[0]):
            tv.canal = tv.canais[-1]
        else:
            tv.canal = tv.canais[tv.canais.index(tv.canal)-1]
        return 2

    def trocaCanal(self, tv, num):
        tv.addCanal = num
        tv.canal = num
        return 2
        
    def mostraCanal(self, tv):
        return 2
    
    def mostraVolume(self, tv):
        return 1
    

if __name__ == "__main__":
    ctrl = Controle()
    tv = Televisao()

    while True:
        resultado = ctrl.menu(tv)
        os.system('cls' if os.name == 'nt' else 'clear')    
        if(resultado == 1):
            print(f"Volume: {tv.volume}")
        if(resultado == 2):
            print(f"Canal: {tv.canal}")
        if(resultado == 3):
            print("Opção Inválida!")
        if(resultado == -1):
            break
        print("-----------------")
