#   Erstellen Sie eine Variable pounds = 2.205
#   und konvertieren Sie 200 pounds in Kilogramm (1 Kg ≈ 2,205 pounds).
#   Wiederholen Sie den gleichen Vorgang im interaktiven Modus
#   und im Skriptmodus (mit Spyder).

pounds = 2.205
weight = 200 / pounds

print(weight)

x="Hallo"
print(type(x))

y='3.999'
print(type(y))

y_f=float(y)
# ...

(2*5)**(1+1)
#100

3**2**2
#81

1/(2*5)**(1+1)
#0.01


P=100
t=10
i=0.03
A=P*(1+i)**t
print(A)
#134.39163793441222

P2 = 1
t2=365*24*60
n2=365*24*60
t2 = 1
i2=1
A2 = P2*(1+i2/n2)**n2*t2
print(A2)
#1.0304545330410038

from math import exp
print(exp(1))