class Mere:
    def methode(self):
        print("dans mere methode 1")

    def methode2(self):
        print("dans mere methode 2")


class Fille(Mere):
    def methode(self):
        print("dans fille methode 1")
        super().methode2()

    def methode2(self):
        print("dans fille methode 2")


f = Fille()
print(type(f))
print(isinstance(f, Fille), isinstance(f, Mere))

m = Mere()
print(type(m))
print(isinstance(m, Fille), isinstance(m, Mere))
