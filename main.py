import bisseccao
import posicaoFalsa
import pontoFixo
import newtonRaphson
import secante

arquivo = open('/home/samuel/Documents/ufmt/zeroFuncao/entrada.txt').read()
entrada = arquivo.split()

#entradas
f = entrada[0]
precisao = entrada[1]
intervaloString = entrada[2]

#tratamento entradas
precisao = precisao.replace('precision=', '')
intervaloString = intervaloString.replace('interval=', '')
intervalo = []
for i in intervaloString.split(','):intervalo.append(float(i))

#chamadas
bisseccao.bisseccao(f, precisao, intervalo)
posicaoFalsa.posicao_falsa(f, precisao, intervalo)
pontoFixo.ponto_fixo(f, precisao, intervalo)
newtonRaphson.newton_raphson(f, precisao, intervalo)
secante.secante(f, precisao, intervalo)