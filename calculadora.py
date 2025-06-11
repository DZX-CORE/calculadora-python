#!/usr/bin/env python3
"""
Calculadora Python - Criada pelo DZX-CORE
Calculadora simples com operações básicas
"""

class Calculadora:
    """Calculadora com operações matemáticas básicas"""
    
    def somar(self, a, b):
        """Somar dois números"""
        return a + b
    
    def subtrair(self, a, b):
        """Subtrair dois números"""
        return a - b
    
    def multiplicar(self, a, b):
        """Multiplicar dois números"""
        return a * b
    
    def dividir(self, a, b):
        """Dividir dois números"""
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b

def main():
    """Função principal da calculadora"""
    calc = Calculadora()
    
    print("=== Calculadora Python ===")
    print("Operações disponíveis:")
    print("1. Somar (+)")
    print("2. Subtrair (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("5. Sair")
    
    while True:
        try:
            opcao = input("\nEscolha uma operação (1-5): ")
            
            if opcao == '5':
                print("Obrigado por usar a calculadora!")
                break
            
            if opcao not in ['1', '2', '3', '4']:
                print("Opção inválida!")
                continue
            
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            
            if opcao == '1':
                resultado = calc.somar(a, b)
                print(f"Resultado: {a} + {b} = {resultado}")
            elif opcao == '2':
                resultado = calc.subtrair(a, b)
                print(f"Resultado: {a} - {b} = {resultado}")
            elif opcao == '3':
                resultado = calc.multiplicar(a, b)
                print(f"Resultado: {a} * {b} = {resultado}")
            elif opcao == '4':
                resultado = calc.dividir(a, b)
                print(f"Resultado: {a} / {b} = {resultado}")
                
        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
