def tratamento_de_entrada(f):
    for i in range(len(f) - 1):
        if f[i].isdigit() and f[i+1].isalpha():
            f = f.replace(f[i] + f[i+1], f[i] + '*' + f[i+1])
    f = f.replace('f(x)=', '')
    f = f.replace('^', '**')
    return f

def calcula_y(f, x):
    y = 0.0
    f = f.replace('x', str(x))
    y = eval(f)
    return y

def bisseccao(f, precisao, a, b):
    listaX=[]
    listFx=[]
    if (b - a) < precisao:
        p = a
    else:
        i = 1
        p = (a + b) / 2
        fp = calcula_y(f, p)
        fa = calcula_y(f, a)
        while b-a >= precisao:
            p = (a + b) / 2
            fp = calcula_y(f, p)
            fa = calcula_y(f, a)
            listaX.append(p)
            listFx.append(fp)
            if fa *fp > 0:
                a = p
            else:
                b = p
            i += 1
        i -= 1         
        print('<x>=', listaX)
        print('<fx>=', listFx)
        print('x=', p)
        print('f(x)=', fp)
        print('errx=', a-b)
        print('iter=', i)

#entradas
f = 'f(x)=x^2-3'
precisao = 0.01
intervalo = [1.0, 2.0]

#tratamento entradas
f = tratamento_de_entrada(f)
a = intervalo[0]
b = intervalo[1]

#chamadas
bisseccao(f, precisao, a, b)