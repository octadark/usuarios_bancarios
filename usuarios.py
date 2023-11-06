class cuentabancaria:
    cuentas = []
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        cuentabancaria.cuentas.append(self)
    
    def deposito(self, amount):
        self.balance += amount
        return self
    
    def retiro(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5 fee")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
            return f"{self.balance}"
    
    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.cuentas:
            account.mostrar_info_cuenta()




class usuario:
    def __init__(self, name):
        self.name = name
        self.account = {
            "checkings" : cuentabancaria(.02,1000),
            "Savings" : cuentabancaria(.05,3000)
        }

    def display_user_balance(self):
        print(f"usuario: {self.name}, Checking Balance: {self.account['checkings'].mostrar_info_cuenta()}")
        print(f"usuario: {self.name}, Savings Balance: {self.account['Savings'].mostrar_info_cuenta()}")
        return self
    
    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

octavio = usuario("Octavio")

octavio.account["checkings"].deposito(100)
octavio.display_user_balance()