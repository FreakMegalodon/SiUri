"""
A Só Birutas Celulares, uma renomada empresa do ramo de telefonia móvel, promove um campeonato de mensagens de texto todos os anos. 
Neste campeonato, ganha quem digitar uma dada mensagem mais rápido. O aparelho oficial da competicão, de uso obrigatório, tem um 
teclado muito simples, similar ao celular que você provavelmente teria no bolso se aparelhos eletrônicos não fossem proibidos 
durante a Maratona de Programacão. O teclado tem o seguinte layout:​

Como só é permitido o uso dos polegares para pressionar as teclas, todas elas foram feitas quadradas, com 1 centímetro de lado, 
sem espaço entre duas teclas adjacentes. As teclas de 2 a 9 são usadas para digitar as letras de 'a' a 'z', e funcionam como em 
qualquer celular: se quisermos obter uma das letras associadas a uma das teclas, precisamos pressioná-la um número de vezes igual 
à posição da letra desejada. Por exemplo, pressionando a tecla 3 uma vez obtemos 'd'. Se pressionarmos novamente, obteremos 'e' e 
depois 'f'. Se continuarmos pressionando-a obteremos o número '3' e depois reiniciamos em 'd'. A tecla 0 é utilizada para inserir 
espaços na mensagem; as teclas 1 e * não são utilizadas nesta competição.

No caso de termos duas letras consecutivas na mensagem que são formadas pela mesma tecla será necessário fazer uso da tecla #. A 
função desta tecla é separar as sequências de pressionamentos de duas letras na mesma tecla. Por exemplo, para digitar a palavra 
"casa", a sequência de teclas pressionadas seria a seguinte: 2, 2, 2, #, 2, 7, 7, 7, 7, 2.

Para tornar as coisas mais interessantes, a organizaçãao decidiu que este ano as mensagens devem ser digitadas em queda livre: os 
competidores pulam de um avião com o celular em mãos e digitam a mensagem; um sofisticado sistema computadorizado abrirá o 
paraquedas automaticamente quando a mensagem tiver sido digitada sem erros. Entretanto, essa modificação das regras introduziu uma 
dificuldade a mais: para evitar que o celular se perca durante a queda, é necessário utilizar um polegar para segurar o aparelho 
enquanto o outro pressiona uma tecla ou é movido; ou seja, um dos polegares está sempre fixo.

Para satisfazer a curiosidade da platéia, você foi contratado para fazer um programa de computador que, dada uma mensagem de até 
140 caracteres, responde o tempo mínimo necessário para um competidor ideal digitá-la no celular. Suponha que um competidor ideal 
consegue mover seus polegares à incrível velocidade de 30 centímetros por segundo, leva apenas 2 décimos de segundo para pressionar 
uma tecla, inicia a queda livre com o polegar esquerdo sobre a tecla 4, o polegar direito sobre a tecla 6 e sempre pressiona as 
teclas perfeitamente em seus centros.

Entrada
A entrada contém diversos casos de teste. Cada caso de teste é composto por uma mensagem, que é uma string que contém de 1 a 140 
caracteres ('a'-'z' ou ' '), inclusive. Nenhuma mensagem começa ou termina com espaços e tampouco contém acentos ou dois espaços 
consecutivos. O final da entrada é indicado por final de arquivo (EOF).

Saída

Para cada caso de teste imprima uma linha contendo o tempo, em segundos, que nosso competidor ideal levaria para digitar a 
mensagem dada. Utilize duas casas decimais para exibir a resposta.

"""
# constantes
TECLAS          = ["", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz", "", " "]
NUMEROS         = ["x123", "x456", "x789", "x*0#"]
TEMPO_POR_TECLA =   0.2
# subs
def calcularTeclas(palavra):
    palavraCalculada = posicaoDaTecla(palavra[0])
    for i in range(1, len(palavra)):
        palavraCalcTmp = posicaoDaTecla(palavra[i])
        if palavraCalcTmp[0] == palavraCalculada[-1]:
            palavraCalculada += "#"
        palavraCalculada += palavraCalcTmp        
    return palavraCalculada

def posicaoDaTecla(letra):
    for i in range(len(TECLAS)):
        if letra in TECLAS[i]:
            if TECLAS[i] == " ":
                return str(0)
            else:
                return str(i + 1) * (TECLAS[i].index(letra) + 1)

def calcularTempo(teclas):
    tempo = 0
    primeira = teclas[0]
    if primeira ==  teclas[1]:
        tempo += TEMPO_POR_TECLA
    for i in range(, len(teclas))
    return teclas
# entradas
palavra = input()

# processos 
while palavra != "":
    print("{}".format(calcularTempo(calcularTeclas(palavra))))
    palavra = input()
# saidas
