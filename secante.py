def secante(f, precisao, intervalo):

    def tratamento_de_funcao(f):
        for i in range(len(f) - 1):
            if f[i].isdigit() and f[i+1].isalpha():
                f = f.replace(f[i] + f[i+1], f[i] + '*' + f[i+1])
        f = f.replace('f(x)=', '')
        f = f.replace('^', '**')
        return f

    def tratamento_de_tolerancia(precisao):
        tolerancia = '10**-' + precisao
        return eval(tolerancia)

    def calcula_y(f, x):
        f = f.replace('x', str(x))
        return eval(f)

    def resolver(f, p0, p1, tolerancia):
        aux = True
        xBarra = 0.0
        listaX=[]
        listFx=[]
        fp0 = calcula_y(f, p0)
        fp1 = calcula_y(f, p1)
        if ((fp0 ** 2) ** (1/2)) < tolerancia:
            xBarra = p0
            aux = False
        if ((fp1 ** 2) ** (1/2)) < tolerancia or (((p1-p0) ** 2) ** (1/2)) < tolerancia:
            xBarra = p1
            aux = False
        i = 1
        while aux:
            fp1 = calcula_y(f, p1)
            fp0 = calcula_y(f, p0)
            p2 = p1 - (((fp1) / ((fp1) - (fp0))) * (p1 -p0))
            fp2 = calcula_y(f, p2)
            listaX.append(p2)
            listFx.append(fp2)
            if ((fp2 ** 2) ** (1/2)) < tolerancia or (((p2 - p1) ** 2) ** (1/2) < tolerancia):
                xBarra = p2
                break
            p0 = p1
            p1 = p2
            i += 1
        print('Método de Newton Raphson:')
        print('<x>=', listaX)
        print('<fx>=', listFx)
        print('x=', xBarra)
        print('f(x)=', fp2)
        print('errx=', p2-p1)
        print('iter=', i)
        print()
            
    #tratamento entradas
    tolerancia = tratamento_de_tolerancia(precisao)
    f = tratamento_de_funcao(f)
    p0 = intervalo[0]
    p1 = intervalo[1]

    resolver(f, p0, p1, tolerancia)