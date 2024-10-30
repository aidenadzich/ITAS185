class MyClass:
    def __init__(self) -> None:
        self.public_var = 10
        self._protected_var = 20
        self.__private_var = 30

    def get_private_var(self):
        return self.__private_var
        
    def set_private_var(self, value):
        self.__private_var = value