def ponto_fixo(f, precisao, intervalo):
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

    def gera_gx(f):
        i = 0
        digito = ''
        aux = len(f)
        while len(f) == aux:
            if f[i].isdigit() and f[i+1].isalpha():
                digito += f[i] 
                f = f.replace(f[i-1] + f[i] + f[i+1],'')
            i += 1
        f = f.replace('f(x)=', '')
        f = '(' +  f + ')' + '/' + digito
        return f        

    def resolver(f, gx, tolerancia, p0): 
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
            p1 = calcula_y(gx, p0)
            fp1 = calcula_y(f, p1)
            listaX.append(p1)
            listFx.append(fp1)
            if ((fp1 ** 2) ** (1/2)) < tolerancia or (((p1 - p0) ** 2) ** (1/2)) < tolerancia:
                xBarra = p1
                break
            p0 = p1
            i += 1
        print('Método do Ponto Fixo:')
        print('<x>=', listaX)
        print('<fx>=', listFx)
        print('x=', xBarra)
        print('f(x)=', fp1)
        print('errx=', p1-p0)
        print('iter=', i)
        print()

    #tratamento entradas
    tolerancia = tratamento_de_tolerancia(precisao)
    gx = gera_gx(f)
    gx = tratamento_de_funcao(gx)
    f = tratamento_de_funcao(f)
    a = intervalo[0]
    b = intervalo[1]
    p0 = a+b/2

    #chamadas
    resolver(f, gx, tolerancia, p0)