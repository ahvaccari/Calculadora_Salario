from datetime import datetime,timedelta

startDate = datetime.strptime(input("Digite a data inicial do plantão (DD/MM/AAAA): "),"%d/%m/%Y")
endDate = datetime.strptime(input("Digite a data final do plantão (DD/MM/AAAA): "),"%d/%m/%Y")
sobAvisoCount = 0

while startDate < endDate:
    if startDate.weekday() in [0, 1, 2, 3, 4]:
        sobAvisoCount += 14.5
    elif startDate.weekday() in [5, 6]:
        sobAvisoCount += 24

    startDate += timedelta(days=1)
print(f"Horas - Plantão: {sobAvisoCount}")