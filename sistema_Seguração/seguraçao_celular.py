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
            print("ENTRADA INICIAL")
            print(f'descrição do {self.verificar}')
            self.senha = input("Digite uma Senha: ").upper()
            self.senha2 = input('Confirme a senha: ').upper()

            if self.senha == self.senha2 and self.senha:
                print("Senha salva com sucesso.")

                self.verificar = False
            else:
                print('Senha incorreta ou vazia. Tente novamente.')
        print(f'descrição tipo dois {self.verificar}')
        

        self.executar_acao()
        print("PASSOU AQUI DA EXECUÇÃO")

    def executar_acao(self):
        self.pergunta = input('''Execute a ação:\n
              1 - Bloquear celular
              2 - Desbloquer Celular
              3 - Desligar Celular
              4 - Desligar Dados moveis
            1
              ''')

        if self.pergunta == '1':
            self.bloqueia_celular()
            print("ACESSO BLOQUEIADO")
        elif self.pergunta == '2':
            self.desbloqueia_celular()
            print("DESBLOQUEIADO")
        elif self.pergunta == '3':
            self.desligar_celular()
            print('DESLIGADO CELULAR')
        elif self.pergunta == '4':
            self.desligar_dados_moveis()
            print('DESLIGADO DADOS MOVEIS')
    

    def bloqueia_celular(self):
        if self.status != self.LOCKED:
            self.status = self.LOCKED
            print('Celular bloqueado com sucesso.')
            self.executar_acao()
        else:
            print('Celular já está bloqueado.')
            self.executar_acao()

    def desbloqueia_celular(self):
        if self.status == self.LOCKED:
            SENHA = input('Digite a senha')
            if SENHA == self.senha:
                self.status = self.UNLOCKED
                print("Celular desbloqueado")
                # self.executar_acao()
            else:
                print('Senha incorreta')
                self.executar_acao()
        else:
            print("Celular ja desbloqueiado")
            self.executar_acao()
    

    def desligar_celular(self):
        if self.status == self.LOCKED:
            if self.celular != self.OFF:
                senha = input('Digite a senha ')
                if self.senha == senha:
                    self.celular = self.OFF
                    print("celular desligado")

                else:
                    print("Senha Incorreta")
                    self.executar_acao()
        else:
            print('Celular desligado')
    def desligar_dados_moveis(self):
        if self.status == self.LOCKED:
            if self.dados_moveis != self.OFF:
                senha = input("Digite sua Senha")
                if senha == self.senha:
                    print('Dados moveis Desligado')
                    self.executar_acao()
                else:
                    print('Senha Incorreta')
                    self.executar_acao()
        else:
            print('Dados Moveis Desligados')
            self.executar_acao()

                
            

# Example usage:
seguranca = Segurança()

