import CalcPlantao

salario = float(input("Salario:"))
horas_60 = float(input("Qtd. de horas 60%:"))
horas_100 = float(input("Qtd. de horas 100%:"))
adNot = float(input("Qtd. de Adicional Noturno:"))

def calcula_plantao():
    return ((salario / 220) * 0.33) * CalcPlantao.sobAvisoCount

def calcula_he60():
    return ((salario/220)*1.6) * horas_60

def calcula_he100():
    return ((salario/220)*2) * horas_100

def calcula_adNoturno():
    return ((salario/220)*0.2) * adNot

valor_plantao = calcula_plantao()
valor_he60 = calcula_he60()
valor_he100 = calcula_he100()
valor_adNoturno = calcula_adNoturno()

def valorBruto():
    return (valor_plantao+valor_he60+valor_he100+valor_adNoturno+salario)

valor_totais = valorBruto()
descontos = valor_totais*0.235

print("")
print(f"Valor do plantão: R${valor_plantao:.2f}")
print(f"Valor da hora extra 60%: R${valor_he60:.2f}")
print(f"Valor da hora extra 100%: R${valor_he100:.2f}")
print(f"Valor do hora adicional noturno: R${valor_adNoturno:.2f}")
print(f"Valor Bruto: R${valor_totais:.2f}")
print(f"Valor Liq. aproximado: R${(valor_totais-descontos):.2f}")
