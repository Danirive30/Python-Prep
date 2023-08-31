class Herramientas:
    def __init__(self, lista_numeros):
        if type(lista_numeros) != list:
            self.lista = [] 
            raise ValueError('Se ha creado una lista vacia. Se esperaba el ingreso de una lista de numeros enteros')
        else:
            self.lista = lista_numeros
        
    def es_primo(self):
        lista_primos = []
        for i in self.lista:
            if (self.__es_primo(i)):
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos
                
    def conversion_grados(self, origen, destino):
        parametros_esperados = ['Celsius','Farenheit','Kelvin']
        lista_conversion = []
        if str(origen) not in parametros_esperados:
            print(f'Los parametros de origen esperados son: {parametros_esperados}')
            return lista_conversion
        if str(destino) not in parametros_esperados:
            print(f'Los parametros de destino esperados son: {parametros_esperados}')
            return lista_conversion
        for i in self.lista:
            lista_conversion.append(self.__conversion_grados(i, origen, destino))
        return lista_conversion
            
    def factorial(self):
        lista_factorial = []
        for i in self.lista:
            lista_factorial.append(self.__factorial(i))
        return lista_factorial
    
    def __es_primo(self, valor):
        if valor == 1:
            return False
        for i in range(2, valor):
            if valor % i == 0:
                return False
        return True
    
    def valor_modal(self, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
    
    def __conversion_grados(self,valor,origen,destino):
        if origen == 'Celsius':
            if destino == 'Celsius':
                valor_destino = valor
            elif destino == 'Farenheit':
                valor_destino = (valor * 9/5) + 32
            elif destino == 'Kelvin':
                valor_destino = (valor + 273.15)
            else:
                print('Parametro de destino incorrecto')
        
        if origen == 'Farenheit':
            if destino == 'Farenheit':
                valor_destino = valor
            elif destino == 'Kelvin':
                valor_destino = ((valor - 32) * 5/9) + 273.15
            elif destino == 'Celsius':
                valor_destino = ((valor - 32) * 5/9)
            else:
                print('Parametro de destino incorrecto')
                
        if origen == 'Kelvin':
            if destino == 'Kelvin':
                valor_destino = valor
            elif destino == 'Celsius':
                valor_destino = valor - 273.15
            elif destino == 'Farenheit':
                valor_destino = ((valor - 273.15) * 9/5) + 32
            else:
                print('Parametro de destino incorrecto')
    
        return valor_destino
    
    def __factorial(self, numero):
        if type(numero) != int:
            return 'El numero ingresado debe ser entero'
        if numero <= 0:
            return 'El numero debe ser entero > 0'
        if numero <= 1:
            return 1
        else:
            return numero * self.__factorial(numero - 1)
        return numero