class Herramientas:
    def __init__(self, lista_numeros):
        self.lista_numeros=lista_numeros
    def verifica_primo(self):
        for i in self.lista_numeros:
            if (self.__verifica_primo(i)):
                print ('el elemento', i, 'Sí es primo')
            else:
                print('el elemento', i, 'NO es primo')

    def __verifica_primo(self,nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo
    
    def factorial (self):
        for i in self.lista_numeros:
            print ('el factorial de', i, 'es', self.__factorial(i))
    def __factorial(self,numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero
    

    def valor_modal(self, menor):
        '''
        Esta función devuelve el valor modal y recibe de parámetros dos valores:
        1-Una lista de números
        2-Verdadero (por defecto) por si se requiere el mínimo de los más repetidos, o Falso si se requiere el máximo
        '''
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista_numeros) == 0:
            return None
        if (menor):
            self.lista_numeros.sort()
        else:
            self.lista_numeros.sort(reverse=True)
        for elemento in self.lista_numeros:
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
    
    def convrsion_grados(self,origen,destino):
        for i in self.lista_numeros:
            print(i,'grados',origen,'son', self.__conversion_grados(i,origen,destino),'grados',destino)
    
    def __conversion_grados(self, valor, origen, destino):
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
    
  
