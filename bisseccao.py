def tratamento_de_entrada(fx):
    for i in range(len(fx) - 1):
        if fx[i].isdigit() and fx[i+1].isalpha():
            fx = fx.replace(fx[i] + fx[i+1], fx[i] + '*' + fx[i+1])
    fx = fx.replace('f(x)=', '')
    fx = fx.replace('^', '**')
    return fx

def calcula_y(fx, x, y):
    fx = fx.replace('x', str(x))
    fx = 'y = '+ fx
    exec(fx)
    return y

#entradas
intervalo = (5.1, 5.7)
fx = 'f(x)=x^2-6x+4'
fx = tratamento_de_entrada(fx)

#inicio bisseccao
y = 0.0
pontoMedio = (intervalo[0] + intervalo[1]) / 2
y = calcula_y(fx, pontoMedio, y)
if y == 0:
    print('A raiz que zera a função é: ', pontoMedio)
else:
    y = calcula_y(fx, intervalo[0], y)
    print(y)
    y = calcula_y(fx, intervalo[1], y)
    print(y)