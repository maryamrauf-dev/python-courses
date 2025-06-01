class m:
    z=1
    @classmethod  #class decorator
    def show(cls):
        print(f"the value of class atribute z is {cls.z}")
mary=m()
mary.z=65
mary.show()