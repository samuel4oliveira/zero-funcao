def tratamento_de_funcao(f):
    for i in range(len(f) - 1):
        if f[i].isdigit() and f[i+1].isalpha():
            f = f.replace(f[i] + f[i+1], f[i] + '*' + f[i+1])
    f = f.replace('f(x)=', '')
    f = f.replace('^', '**')
    return f

def tratamento_de_tolerancia(precisao):
    precisao = precisao.replace('precision=', '')
    print(precisao)
    tolerancia = '10**-' + precisao
    return eval(tolerancia)

def calcula_y(f, x):
    f = f.replace('x', str(x))
    return eval(f)

def posicao_falsa(f, tolerancia, a, b):
    listaX=[]
    listFx=[]
    if (b - a) < tolerancia:
        p = a
    else:
        i = 1
        while True:
            fa = calcula_y(f, a)
            fb = calcula_y(f, b)
            p = (a*fb - b*fa) / (fb - fa)
            fp = calcula_y(f, p)
            listaX.append(p)
            listFx.append(fp)
            if ((fp ** 2) ** (1/2)) < tolerancia:
                break
            if fa *fp > 0:
                a = p
            else:
                b = p
            if b-a <= tolerancia:
                break
            i += 1
        print('<x>=', listaX)
        print('<fx>=', listFx)
        print('x=', p)
        print('f(x)=', fp)
        print('errx=', a-b)
        print('iter=', i)

#entradas
f = 'f(x)=x^3-9x+3'
precisao = 'precision=4'
intervalo = [0.0, 1.0]

#tratamento entradas
tolerancia = tratamento_de_tolerancia(precisao)
f = tratamento_de_funcao(f)
a = intervalo[0]
b = intervalo[1]

posicao_falsa(f, tolerancia, a, b)