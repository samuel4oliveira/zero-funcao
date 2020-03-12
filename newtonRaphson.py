def newton_raphson(f, precisao, intervalo):

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

    def calcula_derivada(f):
        from sympy import diff, Symbol
        from sympy.parsing.sympy_parser import parse_expr
        my_symbols = {'x': Symbol('x', real=True)}
        my_func = parse_expr(f, my_symbols)
        fLinha = diff(my_func, my_symbols['x'])
        return fLinha

    def calcula_yFlinha(fLinha, x):
        f = str(fLinha)
        f = f.replace('x', str(x))
        return eval(f)

    def resolver(f, fLinha, tolerancia, p0):
        aux = True
        xBarra = 0.0
        listaX=[]
        listFx=[]
        i = 1
        fp0 = calcula_y(f, p0)
        if ((fp0 ** 2) ** (1/2)) < tolerancia:
            xBarra = p0
            aux = False
        while aux:
            fp0 = calcula_y(f, p0)
            fLinhap0 = calcula_yFlinha(fLinha, p0)
            p1 = p0 - ((fp0) / (fLinhap0))
            fp1 = calcula_y(f, p1)
            listaX.append(p1)
            listFx.append(fp1)
            if ((fp1 ** 2) ** (1/2)) < tolerancia or (((p1 - p0) ** 2) ** (1/2) < tolerancia):
                xBarra = p1
                break
            p0 = p1
            i += 1
        print('Método de Newton Raphson:')
        print('<x>=', listaX)
        print('<fx>=', listFx)
        print('x=', xBarra)
        print('f(x)=', fp1)
        print('errx=', p1-p0)
        print('iter=', i)
        print()
            
    #tratamento entradas
    tolerancia = tratamento_de_tolerancia(precisao)
    f = tratamento_de_funcao(f)
    a = intervalo[0]
    b = intervalo[1]
    p0 = a+b/2
    fLinha = calcula_derivada(f)

    resolver(f, fLinha, tolerancia, p0)