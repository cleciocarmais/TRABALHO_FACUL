class Segurança:
    UNLOCKED = 'desbloqueado'
    LOCKED = 'bloqueado'
    ON = 'LIGADO'
    OFF = 'DESLIGADO'
    

    def __init__(self) -> None:
        self.celular = self.ON
        self.status = self.UNLOCKED
        self.dados_moveis = self.ON
        self.verificar_senha()


    def verificar_senha(self):
        self.verificar = True
        while self.verificar:
            self.senha = input("Digite uma Senha: ").upper()
            self.senha2 = input('Confirme a senha: ').upper()

            if self.senha == self.senha2 and self.senha:
                print("Senha salva com sucesso.")
                self.verificar = False
            else:
                print('Senha incorreta ou vazia. Tente novamente.')

        self.executar_acao()

    def executar_acao(self):
        self.pergunta = input('''Execute a ação:\n
              1 - Bloquear celular
              2 - Desbloquer Celular
              3 - Desligar Celular
              4 - Desligar Dados moveis
            
              ''')

        if self.pergunta == '1':
            self.bloqueia_celular()
        elif self.pergunta == '2':
            self.desbloquea()
        elif self.pergunta == '3':
            self.desligar()
    

    def bloqueia_celular(self):
        if self.status != self.LOCKED:
            self.status = self.LOCKED
            print('Celular bloqueado com sucesso.')
            self.executar_acao()
        else:
            print('Celular já está bloqueado.')
            self.executar_acao()

    def desbloquea(self):
        if self.status != self.UNLOCKED:
            SENHA = input('Digite a senha')
            if SENHA == self.senha:
                self.status = self.UNLOCKED
                print("Celular desbloqueado")
                self.executar_acao()
            else:
                print('Senha incorreta')
                self.executar_acao()
        else:
            print("CELULAR DESBLOQUEIDO")
            self.executar_acao()
    

    def desligar(self):
        if self.celular != self.OFF:
            senha = input('Digite a senha ')
            if self.senha == senha:
                self.celular = self.OFF
                print("celular desligado")

            else:
                print("Senha Incorreta")
                self.executar_acao()
       

                
            

# Example usage:
seguranca = Segurança()

        

    
        
  
celular = Segurança()
print(celular.executar_acao)
