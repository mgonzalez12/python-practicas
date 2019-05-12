class Usuario:
    def __init__(self,username,password,email, *args, **kwargs):
        self.username = username
        self.__password = self.__generar_password(password)
        self.email = email

    def __generar_password(self, password):
        return password.upper()

    def get_password(self):
        return self.__password
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,valor):
        self.__password = self.__generar_password(valor)    

marc = Usuario('marcos','marcos123','marc@mail.com')
print(marc.password)
marc.password = 'Nuevo pass'
print(marc.password)