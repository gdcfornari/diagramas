class Soma:

    @staticmethod
    def calcula(array):
        result = 0
        for numero in array:
            result = result + numero
        return result

bytearray = [5, 4, 93]
resultado = Soma.calcula(bytearray)
print(resultado)
