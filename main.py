arquivo = open('/home/samuel/Documents/ufmt/zeroFuncao/entrada.txt').read()
entrada = arquivo.split()

#entradas
f = entrada[0]
precisao = entrada[1]
intervaloString = entrada[2]
intervaloString = intervaloString.replace('interval=', '')
intervalo = intervaloString.split(',')

