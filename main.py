#nome Gustavo Viana do Nascimento
# Ciencia da computação 4 período noturno PUCPR

"""''''''
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a 
linguagem de programação Python, C++, C, que seja capaz de validar e executar programas escritos na 
linguagem  proposta  a  seguir  emitindo  um  relatório  de  análise  léxica,  a  classificação  como  válida  ou 
invalida para cada declaração da linguagem e o resultado do programa.   
Descrição da linguagem  
Identificadores: compostos apenas de letras minúsculas e números;  
Símbolos especiais: ?, ), (;  
Operações:  soma  (+),  subtração  (-),  multiplicação  (*),  divisão  (/),  seno  (sin),  cosseno  (cos), 
exponenciação (exp), raiz (rot) segundo os seguintes exemplos:  
(3 4 +) representa a soma de 3 e 4 e devolve 7.000;  
  (3.4 2.5 -) representa a subtração entre 3,6 e 2,5 e devolve 1.100;  
(2.5 3 *) representa o produto de 2,5 por 3 e devolve 7.500;   
(2.6 2 /) representa a divisão de 2,6 por 2 e devolve 1.300;  
   (sin 30) representa o seno de 30 graus e devolve 0.500;  
   (cos 30) representa o cosseno de 30 graus e devolve 0.866;  
   (exp 3 2) representa 3 elevado a 2 e devolve 9.000;  
   (rot 81 2) representa a raiz quadrada de 81 e devolve 9.000;  
Observe  que  todos  os  números  são  reais  de  precisão  dupla  e  todos  os  resultados  serão 
truncados na terceira casa depois da vírgula.  
O símbolo especial será usado para passar o resultado de uma linha para a linha seguinte. Assim, 
um arquivo contendo as declarações a seguir:   
(3 4 +)  
(2 ? *)  
Deverá  devolver  como  reposta  14  além da  validação  de todos  os  lexemas  e da  validação  das 
declarações. Para o exemplo acima, a saída deverá ser:   
Linha 1: lexemas: (, 3, 4, +,) todos válidos  
Linha 1: sintaxe: correta  
Linha 2: lexemas: (, 2, ?, ) todos válidos  
Linha 2: sintaxe: correta  
Além  disso,  poderemos  usar  indentificadores  e  ainhamento.  Então  para  criar  uma  variável  e 
armazenar um valor usaremos a sentença:   
 
Frank Coelho de Alcantara   
Exercícios, pesquisas e atividades   
RECUPERAÇÃO   
Página |  3   de  4     
  
(teste (2 3 *))   
Neste exemplo foi criada a variável teste e esta variável irá armazenar o valor 6.000.   
Um programa completo poderia ser escrito como:   
  
(op1 15)  
(op2 2)  
(sin (op1 op2 *) ) 
(3 ? *)  
Neste exemplo o resultado será 1.500.  
Considerações  importantes:  para  testar  seu  programa,  você  deverá  enviar  três  arquivos 
contendo  programas  com  6  ou  mais  declarações  que  usem  todas  as  operações  descritas  com  pelo 
menos dois aninhamento de operações em cada arquivo de testes e com, no mínimo uma variável em 
cada arquivo de testes.   
Os testes devem ser capazes de indicar o comportamento do seu programa caso o código criado 
contenha erros léxicos ou sintáticos.  
Para a realização da validação léxica você deverá simular, em código, uma máquina de estados 
finitos e não poderá utilizar nenhuma expressão regular.   
Para  a  realização  da  validação  sintática  você  pode  usar  um  parser  LL1  ou  criar  o  seu  próprio 
código de validação de declarações.'
''''''"""

import string
import math

contadorListValidar = 0

def validarEsquerdaBarreira(listCountLeftBarreira):
  for m in listCompletaValidar:
    for n in m:
      LeftBarreiraVV = "("
      RIghtBarreiraVV = ")"
      if n == LeftBarreiraVV:
        listCountLeftBarreira = listCountLeftBarreira + 1
  return listCompletaValidar and listCountLeftBarreira

def validarDireitaBarreira(list):
  listRightValidar = 0
  for m in listCompletaValidar:
    for n in m:
      LeftBarreiraVV = "("
      RIghtBarreiraVV = ")"
      if n == RIghtBarreiraVV:
        listRightValidar = listRightValidar + 1
  return listCompletaValidar and listRightValidar
  
def get_file(file):
  return open(file).read()

while contadorListValidar < 3:
  validarCaracterString = string.ascii_lowercase
  listValidSen = []
  listContaPronta = []
  contadorListValidar = contadorListValidar + 1
  CountListelements = []
  file = get_file(f"arquivoDeTeste{contadorListValidar}.txt").split("\n")
  validarParenteses = False
  listaContador = []
  
  for i in file:
    listaContador.append("1")
    listCompletaValidar = i.split(" ")
    new = []
    listCountLeftBarreira = 0
    listCountLeftBarreira = validarEsquerdaBarreira(listCountLeftBarreira)
    listRightValidar = 0
    validarNUmerolist = False

    for l in listCompletaValidar:
      for t in l:
        for o in t:
          if o == '1' or o == '2' or o == '3' or o == '4' or o == '5' or o == '6' or o == '7' or o == '8' or o == '9':
            validarNUmerolist = True
    
    listRightValidar = validarDireitaBarreira(listRightValidar)
    
    if listRightValidar == listCountLeftBarreira:
      print(" ")
    else:
      print(" ")
      validarParenteses = True
      
    for LeftBarreiraVV in listCompletaValidar:
      validarItem = LeftBarreiraVV
      for y in ['\n', '\t', '(', ')']:
        validarItem = validarItem.replace(y, "")
      new.append(validarItem)
    listCompletaValidar = new
    removerInterrog = False
    for interrog in listCompletaValidar:
      if interrog == '?':
        removerInterrog = True
    listContaProntaB = []

    validarSenoAndCos = False
    if listCompletaValidar.count('sin') == 1 and listCompletaValidar.count('op1') == 1:
      validarSenoAndCos = True
      listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != 'sin' ]
      seno = math.sin(math.radians(int(CountListelements[0]) * int(CountListelements[1])))
      print("seno de {} é {}".format(int(CountListelements[0]) * int(CountListelements[1]), seno))
    listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != '?' ]
    
    bufferopContagem = False
    boolenValidated = False
    
    for q in listCompletaValidar:
      if q == 'op1' or q == 'op2':
        boolenValidated = True
        CountListelements.append(listCompletaValidar[1])
        CountListelements = [ LeftBarreiraVV for LeftBarreiraVV in CountListelements if LeftBarreiraVV != 'op1' ]
        CountListelements = [ LeftBarreiraVV for LeftBarreiraVV in CountListelements if LeftBarreiraVV != 'op2' ]
        bufferopContagem = True
        if len(CountListelements) == 4:
          CountListelements.pop(0)
          CountListelements.pop(0)
          
    buffer = 0
    if boolenValidated == True:
      for j in listCompletaValidar:
        if j == '*' or j == '+' or j == '-' or j == '+':
          buffer = j
      if buffer == '*':
        firstTermInList = float(CountListelements[0])
        secondTermInList = float(CountListelements[1])
        stringCountValidated = firstTermInList * secondTermInList

        if listCompletaValidar.count('op1') == 0:

          print(
            '{} * {} ='.format(float(CountListelements[0]), float(CountListelements[1])),
            ' %.3f' % stringCountValidated)
        elif buffer == '*':
          listContaPronta.append(stringCountValidated)

      if buffer == '+':
        firstTermInList = float(CountListelements[0])
        secondTermInList = float(CountListelements[1])
        stringCountValidated = firstTermInList + secondTermInList

        if listCompletaValidar.count('op1') == 0:
          print(
            '{} + {} ='.format(float(CountListelements[0]), float(CountListelements[1])),
            ' %.3f' % stringCountValidated)
        elif buffer == '+':
          listContaPronta.append(stringCountValidated)
   

      if buffer == '-':
        firstTermInList = float(CountListelements[0])
        secondTermInList = float(CountListelements[1])
        stringCountValidated = firstTermInList - secondTermInList

        if listCompletaValidar.count('op1') == 0:
          print(
            '{} - {} ='.format(float(CountListelements[0]), float(CountListelements[1])),
            ' %.3f' % stringCountValidated)
        elif buffer == '-':
          listContaPronta.append(stringCountValidated)
          

      if buffer == '/':
        firstTermInList = float(CountListelements[0])
        secondTermInList = float(CountListelements[1])
        stringCountValidated = firstTermInList / secondTermInList
        if listCompletaValidar.count('op1') == 0:
          print(
            '{} / {} ='.format(float(CountListelements[0]), float(CountListelements[1])),
            ' %.3f' % stringCountValidated)
        elif buffer == '/':
          listContaPronta.append(stringCountValidated)
    print("linha {}".format(len(listaContador)), "lexemas: ", f" {i} ")
    
    validdd = True
    if removerInterrog == True and validarSenoAndCos == False:
      for interrog in listCompletaValidar:
        if interrog == '*' and validdd == False:

          listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != '?' ]
          listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != '*' ]
          firsttermo = int(listCompletaValidar[0])

          second = int(listContaPronta[0])
          
          seno = math.sin(math.radians(int(CountListelements[0]) * int(CountListelements[1])))
          resultado = (seno * int(listCompletaValidar[0]))
          print("resultado é ", ' %.3f' % resultado)

        if interrog == '-':
          listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != '?' ]
          listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != '-' ]
          firsttermo = int(listCompletaValidar[0])
          second = int(listContaPronta[0])
          seno = math.sin(math.radians(int(CountListelements[0]) - int(CountListelements[1])))
          resultado = (seno - int(listCompletaValidar[0]))
          print("resultado é ", ' %.3f' % resultado)
        if interrog == '+':
          listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != '?' ]
          listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != '+' ]
          firsttermo = int(listCompletaValidar[0])
          second = int(listContaPronta[0])
          seno = math.sin(math.radians(int(CountListelements[0]) + int(CountListelements[1])))
          resultado = (seno + int(listCompletaValidar[0]))

          print("resultado é ", ' %.3f' % resultado)
        if interrog == '/':
          listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != '?' ]
          listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != '/' ]
          firsttermo = int(listCompletaValidar[0])
          second = int(listContaPronta[0])
          seno = math.sin(math.radians(int(CountListelements[0]) / int(CountListelements[1])))
          resultado = (seno / int(listCompletaValidar[0]))
          print("resultado é ", ' %.3f' % resultado)


    if bufferopContagem == True:

      listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != 'op1' ]
      listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != 'op2' ]
      listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != '' ]
      buffer = listCompletaValidar[0]
      if buffer == '*':

        firstTermInList = float(CountListelements[0])
        secondTermInList = float(CountListelements[1])
        stringCountValidated = firstTermInList * secondTermInList
        
        print(
          '{} * {} ='.format(float(CountListelements[0]), float(CountListelements[1])),
          ' %.3f' % stringCountValidated)
      if buffer == '+':
        firstTermInList = float(CountListelements[0])
        secondTermInList = float(CountListelements[1])
        stringCountValidated = firstTermInList + secondTermInList
        print(
          '{} + {} ='.format(float(CountListelements[0]), float(CountListelements[1])),
          ' %.3f' % stringCountValidated)
      if buffer == '-':
        firstTermInList = float(CountListelements[0])
        secondTermInList = float(CountListelements[1])
        stringCountValidated = firstTermInList - secondTermInList
        print(
          '{} - {} ='.format(float(CountListelements[0]), float(CountListelements[1])),
          ' %.3f' % stringCountValidated)
      if buffer == '/':

        firstTermInList = float(CountListelements[0])
        secondTermInList = float(CountListelements[1])
        stringCountValidated = (firstTermInList / secondTermInList)
        print(
          '{} / {} ='.format(float(CountListelements[0]), float(CountListelements[1])),
          ' %.3f' % stringCountValidated)

      if buffer == '+':
        firstTermInList = float(CountListelements[0])
        secondTermInList = float(CountListelements[1])
        stringCountValidated = firstTermInList + secondTermInList
        print(
          '{} + {} ='.format(float(CountListelements[0]), float(CountListelements[1])),
          ' %.3f' % stringCountValidated)
      if buffer == '-':
        firstTermInList = float(CountListelements[0])
        secondTermInList = float(CountListelements[1])
        stringCountValidated = firstTermInList - secondTermInList
        print(
          '{} - {} ='.format(float(CountListelements[0]), float(CountListelements[1])),
          ' %.3f' % stringCountValidated)
      if buffer == '/':

        firstTermInList = float(CountListelements[0])
        secondTermInList = float(CountListelements[1])
        stringCountValidated = (firstTermInList / secondTermInList)
        print(
          '{} / {} ='.format(float(CountListelements[0]), float(CountListelements[1])),
          ' %.3f' % stringCountValidated)

    exponencialValidar = False
    for exponencialValidar in listCompletaValidar:
      if exponencialValidar == 'exp':
        exponencialValidar = True
        print(int(listCompletaValidar[1]) ** (2))
        listCompletaValidar = [ LeftBarreiraVV for LeftBarreiraVV in listCompletaValidar if LeftBarreiraVV != 'exp' ]
      
    if len(listCompletaValidar) == 2 and listCompletaValidar[0] == 'sin':
      angulo = int(listCompletaValidar[1])
      seno = math.sin(math.radians(angulo))
      print("seno de {} é {}".format(angulo, seno))
      print("linha {}".format(len(listaContador)), "sintaxe: valido ")


      
    elif len(listCompletaValidar) == 2 and listCompletaValidar[0] == 'cos':
      angulo = int(listCompletaValidar[1])
      seno = math.cos(math.radians(angulo))
      print("cosseno de {} é {}".format(angulo, seno))
    elif len(listCompletaValidar) == 3 and listCompletaValidar[0] == 'exp':
      denominador = int(listCompletaValidar[1])
      elevador = int(listCompletaValidar[2])
      print(listCompletaValidar[1], "elevado listCompletaValidar", listCompletaValidar[2], "é", denominador**elevador)
    elif len(listCompletaValidar) == 3 and listCompletaValidar[0] == 'rot':
      raiz = math.sqrt(int(listCompletaValidar[1]))
      print("listCompletaValidar raiz quadrada é", raiz)


      
    elif len(listCompletaValidar) > 3 and boolenValidated == False and validarNUmerolist == True and validdd == False:


      listNovo = []
      for g in listCompletaValidar:
        elemento = g
        listCompletaValidar = list(string.ascii_lowercase)
        for p in listCompletaValidar:
          elemento = elemento.replace(p, "")
        listNovo.append(elemento)
    
      for LeftBarreiraVV in listNovo.copy():
          if LeftBarreiraVV == '':
              listNovo.remove(LeftBarreiraVV)
      validarParenteses = False
      listContagem = []
      for i in listNovo:
        listContagem.append(i)
      if listContagem[2] == '+':
        firstTermInList = float(listContagem[0])
        secondTermInList = float(listContagem[1])
        print(
          '{} + {} ='.format(float(listContagem[0]), float(listContagem[1])),
          ' %.3f' % (firstTermInList + secondTermInList))
    
      if listContagem[2] == '-':
        firstTermInList = float(listContagem[0])
        secondTermInList = float(listContagem[1])
        print(
          '{} - {} ='.format(float(listContagem[0]), float(listContagem[1])),
          ' %.3f' % (firstTermInList - secondTermInList))
      if listContagem[2] == '*':
        
        firstTermInList = float(listContagem[0])
        secondTermInList = float(listContagem[1])

        print(
          '{} * {} ='.format(float(listContagem[0]), float(listContagem[1])),
          ' %.3f' % (firstTermInList * secondTermInList))
      if listContagem[2] == '/':
        
        firstTermInList = float(listContagem[0])
        secondTermInList = float(listContagem[1])
        print(
          '{} / {} ='.format(float(listContagem[0]), float(listContagem[1])),
          ' %.3f' % (firstTermInList / secondTermInList))
        
  
    if len(listCompletaValidar) > 2 and boolenValidated == False:

      
      listContagem = []
      for i in listCompletaValidar:
        listContagem.append(i)
      if listContagem[2] == '+':
        firstTermInList = float(listContagem[0])
        secondTermInList = float(listContagem[1])
        print(
          '{} + {} ='.format(float(listContagem[0]), float(listContagem[1])),
          ' %.3f' % (firstTermInList + secondTermInList))
    
      if listContagem[2] == '-':
        firstTermInList = float(listContagem[0])
        secondTermInList = float(listContagem[1])
        print(
          '{} - {} ='.format(float(listContagem[0]), float(listContagem[1])),
          ' %.3f' % (firstTermInList - secondTermInList))
      if listContagem[2] == '*':
        firstTermInList = float(listContagem[0])
        secondTermInList = float(listContagem[1])

        print(
          '{} * {} ='.format(float(listContagem[0]), float(listContagem[1])),
          ' %.3f' % (firstTermInList * secondTermInList))
      if listContagem[2] == '/':
    
        firstTermInList = float(listContagem[0])
        secondTermInList = float(listContagem[1])
        print(
          '{} / {} ='.format(float(listContagem[0]), float(listContagem[1])),
          ' %.3f' % (firstTermInList / secondTermInList))
    if validarParenteses == True:
      print("linha {}".format(len(listaContador)), "sintaxe: invalido")
      validarParenteses = False
    else:
      if validarNUmerolist == True:
        print("linha {}".format(len(listaContador)), "sintaxe: valido")
    if validarNUmerolist == False:
      print("linha {}".format(len(listaContador)), "sintaxe: invalido")