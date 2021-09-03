class Soma:

    @staticmethod
    def calcula(array):
        result = 0
        for numero in array:
            result = result + numero
        return result

bytearray = [104, 29, 93]
resultado = Soma.calcula(bytearray)
print(resultado)
