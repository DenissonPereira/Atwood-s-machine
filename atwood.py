# Máquina de Atwood

m1 = float(input("Qual o valor da primeira massa? "))
m2 = float(input("Qual o valor da segunda massa? "))
GRAVIDADE = 10

if (m2 > m1) or (m2 < m1):
    a = ((m2 - m1) / (m1 + m2)) * GRAVIDADE
    T = m1*(GRAVIDADE + a)
    print("a = {} m/s²; \nT = {} N.".format(a, T))
else:
    print("As massas permanecerão estáticas.")