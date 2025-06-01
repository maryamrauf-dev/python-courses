class twoDvector():
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The vector a is {self.i}i + {self.j}j.")

class threeDvector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i, j)
        self.k=k

    def show(self):
        print(f"The vector b is {self.i}i + {self.j}j + {self.k}k.")
a=twoDvector(8,9)
b=threeDvector(5,4,5)
a.show()
b.show()
