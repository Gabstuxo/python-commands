# =============================================================================
# GUIA COMPLETO DE PYTHON - Todos os comandos, funções, variáveis e constantes
# Baseado na documentação oficial: https://docs.python.org/3/
# =============================================================================


# =============================================================================
# 1. TIPOS DE DADOS PRIMITIVOS
# =============================================================================

# --- Inteiros (int) ---
x = 10                      # inteiro decimal
x_bin = 0b1010              # inteiro em binário (prefixo 0b) → 10
x_oct = 0o12                # inteiro em octal (prefixo 0o) → 10
x_hex = 0xA                 # inteiro em hexadecimal (prefixo 0x) → 10
x_grande = 1_000_000        # underscore como separador visual (PEP 515)
print(type(x))              # <class 'int'> — type() retorna o tipo do objeto

# --- Ponto flutuante (float) ---
pi = 3.14159                # float normal
f_exp = 1.5e3               # notação científica → 1500.0
f_inf = float('inf')        # infinito positivo
f_nan = float('nan')        # NaN (Not a Number)
print(type(pi))             # <class 'float'>

# --- Números complexos (complex) ---
c = 3 + 4j                  # número complexo (parte real + imaginária com j)
print(c.real)               # 3.0 — parte real
print(c.imag)               # 4.0 — parte imaginária
print(abs(c))               # 5.0 — módulo do número complexo

# --- Booleanos (bool) ---
verdadeiro = True           # True e False são instâncias de int (1 e 0)
falso = False
print(isinstance(True, int)) # True — bool é subclasse de int

# --- Strings (str) ---
s1 = 'aspas simples'        # string com aspas simples
s2 = "aspas duplas"         # string com aspas duplas
s3 = '''múltiplas
linhas'''                   # string multilinha com três aspas simples
s4 = """também
multilinha"""               # string multilinha com três aspas duplas
s5 = r"C:\novo\teste"       # raw string — barras invertidas são literais
s6 = b"bytes"               # bytes literal (tipo bytes, não str)
s7 = f"PI vale {pi:.2f}"    # f-string (PEP 498) — interpolação em tempo real
s8 = "Olá" " " "mundo"      # concatenação implícita de literais

# Métodos de string mais importantes:
texto = "  Olá, Mundo!  "
print(texto.strip())        # remove espaços das bordas → "Olá, Mundo!"
print(texto.lstrip())       # remove espaços à esquerda
print(texto.rstrip())       # remove espaços à direita
print(texto.upper())        # tudo maiúsculo → "  OLÁ, MUNDO!  "
print(texto.lower())        # tudo minúsculo
print(texto.title())        # primeira letra de cada palavra maiúscula
print(texto.capitalize())   # primeira letra maiúscula
print(texto.swapcase())     # inverte maiúsculas/minúsculas
print(texto.replace("Mundo", "Python"))  # substitui substring
print(texto.find("Mundo"))  # índice da primeira ocorrência ou -1
print(texto.index("Mundo")) # igual ao find, mas lança ValueError se não achar
print(texto.count("l"))     # conta ocorrências da substring
print(texto.startswith("  Olá"))  # True se começa com o prefixo
print(texto.endswith("!  "))      # True se termina com o sufixo
print(texto.split(","))     # divide a string → ['  Olá', ' Mundo!  ']
print(",".join(["a","b","c"]))    # une lista em string → "a,b,c"
print(texto.center(30, "*"))# centraliza em 30 chars preenchendo com *
print(texto.ljust(30, "-")) # alinha à esquerda
print(texto.rjust(30, "-")) # alinha à direita
print(texto.zfill(30))      # preenche com zeros à esquerda
print("abc".encode("utf-8"))# codifica a string em bytes
print(b"abc".decode("utf-8"))# decodifica bytes em string
print("abc123".isalnum())   # True se todos alfanuméricos
print("abc".isalpha())      # True se todos alfabéticos
print("123".isdigit())      # True se todos dígitos
print("123".isnumeric())    # True se numérico (inclui ², ³, frações unicode)
print("   ".isspace())      # True se só espaços
print("HELLO".isupper())    # True se tudo maiúsculo
print("hello".islower())    # True se tudo minúsculo
print("Hello World".istitle()) # True se formato título
print("{} tem {}".format("Python", 30))   # formatação com .format()
print("{nome}".format(nome="Ana"))         # .format() com nome
print("%s tem %d anos" % ("João", 25))    # formatação estilo C (legado)

# Fatiamento (slicing) de strings:
s = "Python"
print(s[0])                 # 'P' — índice 0
print(s[-1])                # 'n' — último caractere
print(s[1:4])               # 'yth' — slice [início:fim] (fim exclusivo)
print(s[:3])                # 'Pyt' — do início até índice 3 (exclusivo)
print(s[3:])                # 'hon' — do índice 3 até o fim
print(s[::2])               # 'Pto' — passo 2
print(s[::-1])              # 'nohtyP' — string invertida

# --- None ---
nada = None                 # representa ausência de valor
print(nada is None)         # True — use 'is' para comparar com None


# =============================================================================
# 2. OPERADORES
# =============================================================================

# Aritméticos:
print(10 + 3)               # 13  — adição
print(10 - 3)               # 7   — subtração
print(10 * 3)               # 30  — multiplicação
print(10 / 3)               # 3.333... — divisão real (sempre retorna float)
print(10 // 3)              # 3   — divisão inteira (floor division)
print(10 % 3)               # 1   — módulo (resto da divisão)
print(10 ** 3)              # 1000 — exponenciação
print(-10 // 3)             # -4  — floor division com negativos (arredonda para baixo)

# Comparação (retornam bool):
print(5 == 5)               # True  — igual
print(5 != 4)               # True  — diferente
print(5 > 4)                # True  — maior
print(5 < 4)                # False — menor
print(5 >= 5)               # True  — maior ou igual
print(5 <= 4)               # False — menor ou igual

# Lógicos:
print(True and False)       # False — E lógico (ambos precisam ser True)
print(True or False)        # True  — OU lógico (pelo menos um True)
print(not True)             # False — NÃO lógico

# Identidade (compara se são o MESMO objeto na memória):
a = [1, 2]
b = a
c = [1, 2]
print(a is b)               # True  — b aponta para o mesmo objeto
print(a is c)               # False — c é objeto diferente com mesmo valor
print(a is not c)           # True

# Pertencimento:
print(3 in [1, 2, 3])       # True  — 3 está na lista
print(4 not in [1, 2, 3])   # True  — 4 não está na lista
print("Py" in "Python")     # True  — substring

# Bitwise (bit a bit):
print(0b1010 & 0b1100)      # 8   (0b1000) — AND bit a bit
print(0b1010 | 0b1100)      # 14  (0b1110) — OR bit a bit
print(0b1010 ^ 0b1100)      # 6   (0b0110) — XOR bit a bit
print(~0b1010)              # -11           — NOT bit a bit (complemento de dois)
print(0b1010 << 2)          # 40  (0b101000)— shift left (multiplica por 2^n)
print(0b1010 >> 1)          # 5   (0b101)  — shift right (divide por 2^n)

# Atribuição composta:
n = 10
n += 5                      # n = n + 5  → 15
n -= 3                      # n = n - 3  → 12
n *= 2                      # n = n * 2  → 24
n /= 4                      # n = n / 4  → 6.0
n //= 2                     # n = n // 2 → 3.0
n **= 3                     # n = n ** 3 → 27.0
n %= 5                      # n = n % 5  → 2.0

# Operador Walrus := (PEP 572 — Python 3.8+)
# Atribui e usa o valor ao mesmo tempo:
import re
if m := re.search(r"\d+", "versão 3.11"):
    print(m.group())        # '3' — capturou e já usou o resultado

# Operador ternário (expressão condicional):
idade = 20
status = "maior" if idade >= 18 else "menor"  # if inline
print(status)               # 'maior'


# =============================================================================
# 3. ESTRUTURAS DE CONTROLE DE FLUXO
# =============================================================================

# --- if / elif / else ---
nota = 75
if nota >= 90:
    conceito = "A"
elif nota >= 80:
    conceito = "B"
elif nota >= 70:
    conceito = "C"
else:
    conceito = "D"
print(conceito)             # 'C'

# --- match / case (Python 3.10+ — pattern matching) ---
comando = "sair"
match comando:
    case "iniciar":
        print("Iniciando...")
    case "parar" | "sair":  # múltiplos padrões com |
        print("Encerrando...")
    case _:                 # wildcard — equivale ao else
        print("Comando desconhecido")

# match com estruturas:
ponto = (1, 0)
match ponto:
    case (0, 0):
        print("Origem")
    case (x, 0):            # captura x
        print(f"Eixo X em {x}")
    case (0, y):            # captura y
        print(f"Eixo Y em {y}")
    case (x, y):
        print(f"Ponto ({x}, {y})")

# --- for ---
for i in range(5):          # range(5) → 0,1,2,3,4
    print(i, end=" ")
print()

for i in range(2, 10, 3):   # range(início, fim, passo) → 2,5,8
    print(i, end=" ")
print()

for letra in "Python":      # itera sobre string
    print(letra, end=" ")
print()

# enumerate — retorna (índice, valor):
frutas = ["maçã", "banana", "uva"]
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

# enumerate com início personalizado:
for i, fruta in enumerate(frutas, start=1):
    print(f"{i}: {fruta}")

# zip — itera em paralelo sobre múltiplos iteráveis:
nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")

# zip_longest (continua até o mais longo):
from itertools import zip_longest
for a, b in zip_longest([1,2,3], ["x","y"], fillvalue=0):
    print(a, b)

# --- while ---
contador = 0
while contador < 5:         # continua enquanto condição for True
    contador += 1
print(contador)             # 5

# --- break, continue, else em loops ---
for i in range(10):
    if i == 3:
        continue            # pula o restante do bloco e vai para próxima iteração
    if i == 6:
        break               # sai do loop imediatamente
    print(i, end=" ")       # 0 1 2 4 5
print()

# else em loop — executado quando loop termina normalmente (sem break):
for i in range(5):
    if i == 10:
        break
else:
    print("Loop terminou sem break")  # imprime isso

# --- pass ---
for _ in range(3):
    pass                    # instrução vazia (placeholder, não faz nada)


# =============================================================================
# 4. FUNÇÕES
# =============================================================================

# Definição básica:
def saudacao(nome):
    """Docstring: Descreve a função. Acessível via help() ou __doc__."""
    return f"Olá, {nome}!"

print(saudacao("Maria"))    # 'Olá, Maria!'
print(saudacao.__doc__)     # exibe a docstring

# Parâmetros com valor padrão:
def potencia(base, expoente=2):     # expoente tem valor padrão 2
    return base ** expoente

print(potencia(3))          # 9   — usa o padrão
print(potencia(3, 3))       # 27  — sobrescreve o padrão

# Parâmetros posicionais e nomeados:
def descricao(nome, cidade, pais="Brasil"):
    return f"{nome} de {cidade}, {pais}"

print(descricao("Ana", "SP"))                    # por posição
print(descricao(cidade="RJ", nome="Bruno"))      # por nome (ordem não importa)

# *args — argumentos posicionais variáveis (recebe como tupla):
def soma(*numeros):
    return sum(numeros)

print(soma(1, 2, 3, 4, 5))  # 15

# **kwargs — argumentos nomeados variáveis (recebe como dicionário):
def exibir(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir(nome="Carla", idade=28, cidade="BH")

# Combinando tudo (ordem obrigatória: pos, *args, nomeados, **kwargs):
def completa(a, b, *args, chave="default", **kwargs):
    print(a, b, args, chave, kwargs)

completa(1, 2, 3, 4, chave="x", extra=True)

# Parâmetros somente posicionais (/ — PEP 570, Python 3.8+):
def somente_pos(a, b, /, c):  # a e b só podem ser passados por posição
    return a + b + c

print(somente_pos(1, 2, c=3)) # OK

# Parâmetros somente nomeados (* — Python 3.0+):
def somente_named(*, nome, idade):  # só podem ser passados por nome
    return f"{nome} tem {idade}"

print(somente_named(nome="Leo", idade=30))

# Lambda (função anônima — expressão única):
dobrar = lambda x: x * 2       # equivale a def dobrar(x): return x * 2
print(dobrar(5))                # 10

quadrado = lambda x, y: x ** y
print(quadrado(3, 2))           # 9

# Funções como objetos (first-class functions):
operacoes = [lambda x: x+1, lambda x: x*2, lambda x: x**2]
for op in operacoes:
    print(op(3))                # 4, 6, 9

# Closure — função que captura variáveis do escopo externo:
def multiplicador(fator):
    def multiplicar(numero):    # captura 'fator' do escopo externo
        return numero * fator
    return multiplicar          # retorna a função

triple = multiplicador(3)
print(triple(5))                # 15

# Decorator — função que envolve outra função:
def meu_decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes da função")
        resultado = func(*args, **kwargs)
        print("Depois da função")
        return resultado
    return wrapper

@meu_decorator                  # sintaxe açúcar para: saudacao2 = meu_decorator(saudacao2)
def saudacao2(nome):
    print(f"Olá, {nome}!")

saudacao2("Diego")

# functools.wraps — preserva metadados da função original:
import functools

def decorator_correto(func):
    @functools.wraps(func)      # copia __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Generators — funções que usam yield (lazy evaluation):
def contagem(inicio, fim):
    while inicio <= fim:
        yield inicio            # pausa e retorna o valor
        inicio += 1             # retoma daqui na próxima chamada

gen = contagem(1, 5)
print(next(gen))                # 1 — avança um passo
print(next(gen))                # 2
print(list(gen))                # [3, 4, 5] — consome o restante

# yield from — delega para outro gerador:
def cadeia(*iteraveis):
    for it in iteraveis:
        yield from it           # equivale a: for item in it: yield item

print(list(cadeia([1,2], [3,4], [5])))  # [1, 2, 3, 4, 5]

# Funções recursivas:
def fatorial(n):
    if n <= 1:                  # caso base
        return 1
    return n * fatorial(n - 1) # chamada recursiva

print(fatorial(6))              # 720

# nonlocal — acessa variável do escopo externo (sem ser global):
def contador():
    count = 0
    def incrementar():
        nonlocal count          # permite modificar 'count' do escopo externo
        count += 1
        return count
    return incrementar

inc = contador()
print(inc(), inc(), inc())      # 1 2 3

# global — acessa/modifica variável global dentro de função:
total = 0
def adicionar(n):
    global total                # declara intenção de modificar variável global
    total += n

adicionar(10)
adicionar(5)
print(total)                    # 15

# Funções internas úteis do Python (built-ins):
print(abs(-5))                  # 5      — valor absoluto
print(round(3.14159, 2))        # 3.14   — arredondamento
print(round(2.5))               # 2      — banker's rounding (para par mais próximo)
print(pow(2, 10))               # 1024   — potência
print(pow(2, 10, 1000))         # 24     — potência com módulo (mais eficiente)
print(divmod(17, 5))            # (3, 2) — retorna (quociente, resto)
print(bin(255))                 # '0b11111111' — inteiro para binário
print(oct(255))                 # '0o377'       — inteiro para octal
print(hex(255))                 # '0xff'        — inteiro para hexadecimal
print(int("ff", 16))            # 255   — string hex para inteiro
print(int("1010", 2))           # 10    — string binária para inteiro
print(chr(65))                  # 'A'   — código Unicode para caractere
print(ord("A"))                 # 65    — caractere para código Unicode
print(repr("olá\n"))            # "'olá\\n'" — representação oficial do objeto
print(len("Python"))            # 6     — comprimento
print(len([1,2,3,4]))           # 4
print(max(3, 1, 4, 1, 5, 9))   # 9     — maior valor
print(min(3, 1, 4, 1, 5, 9))   # 1     — menor valor
print(sum([1, 2, 3, 4, 5]))     # 15    — soma
print(sum(range(1, 101)))       # 5050  — soma de 1 a 100
print(sorted([3,1,4,1,5,9]))    # [1, 1, 3, 4, 5, 9] — retorna nova lista ordenada
print(sorted("python"))         # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted([3,1,2], reverse=True))   # [3, 2, 1] — decrescente
print(sorted(["banana","maçã","uva"], key=len))  # por comprimento
print(list(reversed([1,2,3,4])))# [4,3,2,1] — iterador reverso
print(list(enumerate(["a","b"])))# [(0,'a'),(1,'b')]
print(list(zip([1,2,3],[4,5,6])))# [(1,4),(2,5),(3,6)]
print(list(map(str, [1,2,3])))  # ['1','2','3'] — aplica função a cada elemento
print(list(filter(None, [0,1,False,2,"",3]))) # [1,2,3] — remove falsy
print(list(filter(lambda x: x>2, [1,2,3,4]))) # [3,4]
print(bool(0), bool(""), bool([]))  # False False False — conversão para bool
print(bool(1), bool("a"), bool([1]))# True True True
print(int(3.9))                 # 3    — float para int (trunca, não arredonda)
print(float(3))                 # 3.0  — int para float
print(str(42))                  # '42' — número para string
print(list("abc"))              # ['a','b','c'] — string para lista
print(tuple([1,2,3]))           # (1,2,3) — lista para tupla
print(set([1,2,2,3]))           # {1,2,3} — lista para conjunto
print(dict(a=1, b=2))          # {'a':1,'b':2} — para dicionário
print(frozenset([1,2,3]))       # frozenset({1,2,3}) — conjunto imutável
print(complex(3, 4))            # (3+4j) — cria número complexo
print(bytes(5))                 # b'\x00\x00\x00\x00\x00' — bytes zerados
print(bytes([65,66,67]))        # b'ABC' — bytes de lista de inteiros
print(bytearray([65,66]))       # bytearray(b'AB') — bytes mutável
print(memoryview(b"hello"))     # view sem copiar os dados
print(hash("Python"))           # inteiro hash (varia por execução por segurança)
print(id(x))                    # endereço de memória do objeto
print(type(x))                  # <class 'int'>
print(isinstance(x, int))       # True — verifica se é instância do tipo
print(isinstance(x, (int, float))) # True — aceita tupla de tipos
print(issubclass(bool, int))    # True — verifica herança
print(callable(len))            # True — verifica se pode ser chamado
print(hasattr("hello", "upper"))# True — verifica se objeto tem atributo
print(getattr("hello", "upper"))# <built-in method upper ...> — obtém atributo
setattr_obj = type("Obj", (), {})() # cria objeto dinâmico
setattr(setattr_obj, "valor", 42)   # define atributo dinamicamente
print(getattr(setattr_obj, "valor"))# 42
delattr(setattr_obj, "valor")       # remove atributo
print(dir([]))                  # lista todos os atributos/métodos do objeto
print(vars())                   # dicionário de variáveis do escopo atual
print(globals())                # dicionário de variáveis globais
# locals() — dicionário de variáveis locais (dentro de função)
print(any([False, True, False]))# True  — True se pelo menos um for True
print(all([True, True, True]))  # True  — True se todos forem True
print(any([]))                  # False — any([]) é sempre False
print(all([]))                  # True  — all([]) é sempre True (vacuously true)
print(iter([1,2,3]))            # <list_iterator object>
it = iter([10, 20, 30])
print(next(it))                 # 10
print(next(it, "fim"))          # 20 — next com padrão se StopIteration
print(next(it, "fim"))          # 30
print(next(it, "fim"))          # 'fim' — sem StopIteration

# input e print com argumentos:
# nome = input("Digite seu nome: ")  # lê entrada do usuário (comentado para não pausar)
print("a", "b", "c", sep="-")  # 'a-b-c' — sep define separador
print("linha", end="!\n")       # 'linha!' — end define terminador
print("x", file=__import__("sys").stdout)  # redireciona saída

# open e I/O de arquivos:
# with open("arquivo.txt", "w", encoding="utf-8") as f:
#     f.write("Olá\n")           # escreve no arquivo
#     f.writelines(["linha1\n", "linha2\n"])  # escreve lista de strings
#
# with open("arquivo.txt", "r", encoding="utf-8") as f:
#     conteudo = f.read()        # lê tudo como string
#     linha = f.readline()       # lê uma linha
#     linhas = f.readlines()     # lê todas as linhas como lista
#     for linha in f:            # itera linha por linha (eficiente)
#         print(linha.strip())
#
# Modos de abertura:
# "r"  — leitura (padrão)
# "w"  — escrita (sobrescreve)
# "a"  — append (adiciona ao final)
# "x"  — criação exclusiva (erro se já existe)
# "b"  — modo binário (rb, wb, ab...)
# "+"  — leitura e escrita (r+, w+, a+)

# eval e exec:
resultado = eval("2 + 2 * 3")   # avalia expressão string → 8
print(resultado)
exec("y = 100; print(y)")       # executa código string (cria y=100 e imprime)

# compile — pré-compila código:
codigo = compile("print('compilado')", "<string>", "exec")
exec(codigo)

# __import__ — importa módulo por nome string:
math_mod = __import__("math")
print(math_mod.pi)              # 3.141592...

# staticmethod, classmethod, property — vistos na seção de Classes

# super() — acessa a classe pai — visto na seção de Classes

# object() — instância base de todos os objetos:
obj_base = object()


# =============================================================================
# 5. ESTRUTURAS DE DADOS
# =============================================================================

# --- Lista (list) — mutável, ordenada, heterogênea ---
lista = [1, 2, 3, 4, 5]
lista.append(6)             # adiciona ao final
lista.insert(0, 0)          # insere 0 na posição 0
lista.extend([7, 8])        # adiciona múltiplos elementos
lista += [9]                # também estende
print(lista.pop())          # remove e retorna o último → 9
print(lista.pop(0))         # remove e retorna pelo índice → 0
lista.remove(3)             # remove a primeira ocorrência do valor 3
lista.sort()                # ordena in-place (modifica a lista)
lista.sort(key=lambda x: -x)# ordena por critério customizado
lista.reverse()             # inverte in-place
print(lista.index(5))       # índice da primeira ocorrência de 5
print(lista.count(2))       # quantas vezes 2 aparece
copia = lista.copy()        # cópia rasa (shallow copy)
lista.clear()               # remove todos os elementos

# List comprehension — cria lista de forma concisa:
quadrados = [x**2 for x in range(10)]           # [0,1,4,9,...,81]
pares = [x for x in range(20) if x % 2 == 0]   # filtrando
matriz = [[i*j for j in range(3)] for i in range(3)]  # aninhada
flat = [n for sub in [[1,2],[3,4]] for n in sub]# "flat map" → [1,2,3,4]

# Descompactação (unpacking):
a, b, c = [1, 2, 3]         # atribui cada elemento a uma variável
primeiro, *resto = [1,2,3,4,5]  # * captura o restante como lista
*inicio, ultimo = [1,2,3,4,5]   # * captura os primeiros
a, b = b, a                 # troca de valores (swap elegante)

# --- Tupla (tuple) — imutável, ordenada ---
tupla = (1, 2, 3)
tupla_um = (42,)            # tupla com um elemento precisa da vírgula
tupla_vazia = ()
t = 1, 2, 3                 # parênteses são opcionais
print(tupla[0])             # 1 — acesso por índice
print(tupla.count(1))       # conta ocorrências
print(tupla.index(2))       # índice de valor
a, b, c = tupla             # unpacking
# Tuplas nomeadas (mais legível):
from collections import namedtuple
Ponto = namedtuple("Ponto", ["x", "y"])
p = Ponto(3, 4)
print(p.x, p.y)             # 3 4
print(p._asdict())          # {'x': 3, 'y': 4}

# --- Dicionário (dict) — mutável, chaves únicas, ordenado (Python 3.7+) ---
dicio = {"nome": "Ana", "idade": 25, "ativo": True}
dicio["email"] = "ana@email.com"   # adiciona/atualiza chave
print(dicio["nome"])               # acessa por chave (KeyError se não existir)
print(dicio.get("fone", "N/A"))   # acessa sem KeyError, retorna padrão
print(dicio.keys())                # dict_keys(['nome','idade','ativo','email'])
print(dicio.values())              # dict_values([...])
print(dicio.items())               # dict_items([(chave,valor),...])
del dicio["ativo"]                 # remove chave
removido = dicio.pop("email", None)# remove e retorna; None se não existir
dicio.update({"cidade": "SP", "idade": 26})  # atualiza múltiplos
print(dicio.setdefault("pais", "Brasil"))     # retorna ou cria com padrão
dicio2 = {"a": 1}
merged = {**dicio, **dicio2}       # merge de dicionários (Python 3.5+)
merged2 = dicio | dicio2           # merge com | (Python 3.9+)
dicio |= {"extra": True}           # update in-place com |= (Python 3.9+)
print(dicio.copy())                # cópia rasa
dicio.clear()                      # limpa o dicionário

# Dict comprehension:
quadrados_d = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# defaultdict — valor padrão automático para chaves inexistentes:
from collections import defaultdict
contagem_letras = defaultdict(int)     # padrão: 0
for letra in "abracadabra":
    contagem_letras[letra] += 1        # não precisa verificar se chave existe
print(dict(contagem_letras))

# OrderedDict — mantém ordem de inserção (legado; dict já faz isso no 3.7+):
from collections import OrderedDict
od = OrderedDict([("b", 2), ("a", 1)])
od.move_to_end("b")            # move chave para o final
od.move_to_end("a", last=False)# move para o início

# Counter — conta elementos:
from collections import Counter
c = Counter("abracadabra")
print(c.most_common(3))        # [('a', 5), ('b', 2), ('r', 2)]
print(c["a"])                  # 5 — conta de 'a'

# ChainMap — encadeia múltiplos dicionários:
from collections import ChainMap
cm = ChainMap({"x": 1}, {"y": 2})
print(cm["x"], cm["y"])        # 1 2

# --- Conjunto (set) — mutável, não ordenado, sem duplicatas ---
conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)                # adiciona elemento
conjunto.discard(3)            # remove se existir (sem erro)
conjunto.remove(4)             # remove; KeyError se não existir
conjunto.pop()                 # remove aleatório
a_set = {1, 2, 3}
b_set = {3, 4, 5}
print(a_set | b_set)           # {1,2,3,4,5} — união
print(a_set & b_set)           # {3}          — interseção
print(a_set - b_set)           # {1,2}        — diferença
print(a_set ^ b_set)           # {1,2,4,5}    — diferença simétrica
print(a_set <= {1,2,3,4})      # True — subconjunto
print({1,2,3,4} >= a_set)      # True — superconjunto
print(a_set.isdisjoint({7,8})) # True — sem elementos em comum

# frozenset — conjunto imutável (pode ser usado como chave de dicionário):
fs = frozenset([1, 2, 3])

# Set comprehension:
pares_set = {x for x in range(10) if x % 2 == 0}  # {0,2,4,6,8}

# --- deque — fila duplamente encadeada (eficiente nas duas pontas) ---
from collections import deque
fila = deque([1, 2, 3])
fila.appendleft(0)             # adiciona à esquerda → deque([0,1,2,3])
fila.append(4)                 # adiciona à direita
fila.popleft()                 # remove da esquerda → 0
fila.pop()                     # remove da direita → 4
d = deque(range(5), maxlen=3)  # maxlen — descarta ao ultrapassar limite
print(d)                       # deque([2, 3, 4], maxlen=3)
fila.rotate(2)                 # rotaciona 2 posições à direita


# =============================================================================
# 6. CLASSES E ORIENTAÇÃO A OBJETOS
# =============================================================================

class Animal:
    """Classe base demonstrando OOP em Python."""

    especie_total = 0           # atributo de classe (compartilhado por todas as instâncias)

    def __init__(self, nome, som):      # __init__: inicializador (chamado ao criar instância)
        self.nome = nome        # atributo de instância (privado à instância)
        self.som = som
        self._protegido = "use com cuidado"  # convenção: _ = "protegido"
        self.__privado = "acesso restrito"   # name mangling: __attr → _Classe__attr
        Animal.especie_total += 1

    def __str__(self):          # __str__: representação legível (para print())
        return f"Animal({self.nome})"

    def __repr__(self):         # __repr__: representação oficial (para debug/eval)
        return f"Animal(nome={self.nome!r}, som={self.som!r})"

    def __len__(self):          # __len__: chamado por len()
        return len(self.nome)

    def __eq__(self, outro):    # __eq__: chamado por ==
        return self.nome == outro.nome

    def __lt__(self, outro):    # __lt__: chamado por < (e sorted)
        return self.nome < outro.nome

    def __add__(self, outro):   # __add__: chamado por +
        return Animal(self.nome + outro.nome, self.som)

    def __contains__(self, item):   # __contains__: chamado por 'in'
        return item in self.nome

    def __getitem__(self, key):     # __getitem__: chamado por []
        return self.nome[key]

    def __iter__(self):         # __iter__: torna o objeto iterável
        return iter(self.nome)

    def __call__(self, *args):  # __call__: torna o objeto "chamável" como função
        return f"{self.nome} faz {self.som}"

    def falar(self):            # método de instância (recebe self)
        return f"{self.nome} faz {self.som}"

    @classmethod
    def criar_mudo(cls, nome):  # classmethod: recebe a classe (cls) em vez de self
        return cls(nome, "...")

    @staticmethod
    def e_animal_valido(nome):  # staticmethod: não recebe self nem cls
        return bool(nome and isinstance(nome, str))

    @property
    def nome_maiusculo(self):   # property: acesso como atributo mas executa função
        return self.nome.upper()

    @nome_maiusculo.setter
    def nome_maiusculo(self, valor):  # setter da property
        self.nome = valor.lower()

    @nome_maiusculo.deleter
    def nome_maiusculo(self):   # deleter da property
        del self.nome

    def __del__(self):          # __del__: chamado quando o objeto é destruído (GC)
        Animal.especie_total -= 1


# Herança:
class Cachorro(Animal):         # Cachorro herda de Animal
    def __init__(self, nome, raca):
        super().__init__(nome, "Au")  # chama __init__ do pai
        self.raca = raca

    def falar(self):            # override do método do pai
        base = super().falar()  # chama o método do pai
        return f"{base} (cão da raça {self.raca})"

    def buscar(self):
        return f"{self.nome} busca a bolinha!"


# Herança múltipla e MRO (Method Resolution Order):
class Voador:
    def voar(self):
        return "Estou voando!"

class Nadador:
    def nadar(self):
        return "Estou nadando!"

class Pato(Animal, Voador, Nadador):  # herança múltipla
    def __init__(self, nome):
        super().__init__(nome, "Quack")

print(Pato.__mro__)             # mostra a ordem de resolução de métodos

# Dataclass (Python 3.7+) — gera automaticamente __init__, __repr__, __eq__:
from dataclasses import dataclass, field

@dataclass
class Produto:
    nome: str
    preco: float
    estoque: int = 0                        # com padrão
    tags: list = field(default_factory=list)# padrão mutável usa field

    def desconto(self, percentual: float) -> float:
        return self.preco * (1 - percentual/100)

p1 = Produto("Notebook", 3500.00, estoque=5)
p2 = Produto("Notebook", 3500.00, estoque=5)
print(p1 == p2)                 # True — __eq__ gerado automaticamente
print(repr(p1))                 # Produto(nome='Notebook', ...)

# @dataclass(frozen=True) — cria dataclass imutável
@dataclass(frozen=True)
class PontoImmutavel:
    x: float
    y: float

# Abstract Base Classes (ABC):
from abc import ABC, abstractmethod

class Forma(ABC):               # classe abstrata — não pode ser instanciada
    @abstractmethod
    def area(self) -> float:    # método abstrato — subclasses devem implementar
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

class Circulo(Forma):
    def __init__(self, raio: float):
        self.raio = raio

    def area(self) -> float:
        import math
        return math.pi * self.raio ** 2

    def perimetro(self) -> float:
        import math
        return 2 * math.pi * self.raio

c = Circulo(5)
print(f"Área: {c.area():.2f}")  # Área: 78.54

# Uso das classes criadas:
dog = Cachorro("Rex", "Labrador")
print(dog)                      # Animal(Rex)
print(repr(dog))                # Animal(nome='Rex', som='Au')
print(len(dog))                 # 3
print("R" in dog)               # True
print(dog[0])                   # 'R'
print(dog())                    # 'Rex faz Au'
print(dog.nome_maiusculo)       # 'REX'
dog.nome_maiusculo = "BUDDY"    # chama o setter
print(dog.nome)                 # 'buddy'
print(Animal.criar_mudo("Gato"))# Animal(Gato)
print(Animal.e_animal_valido("Rex"))  # True
print(Animal.especie_total)     # número de animais criados


# =============================================================================
# 7. TRATAMENTO DE EXCEÇÕES
# =============================================================================

# Hierarquia resumida:
# BaseException
#   SystemExit, KeyboardInterrupt, GeneratorExit
#   Exception
#     ArithmeticError: ZeroDivisionError, OverflowError, FloatingPointError
#     AttributeError, LookupError: IndexError, KeyError
#     NameError, TypeError, ValueError, IOError/OSError, RuntimeError
#     StopIteration, NotImplementedError, RecursionError ...

try:
    resultado = 10 / 0          # lança ZeroDivisionError
except ZeroDivisionError as e:  # captura exceção específica
    print(f"Erro: {e}")
except (TypeError, ValueError) as e:  # captura múltiplas exceções
    print(f"Tipo/Valor inválido: {e}")
except Exception as e:          # captura qualquer exceção derivada de Exception
    print(f"Exceção genérica: {e}")
else:
    print("Não houve exceção!")  # executado apenas se não houver exceção
finally:
    print("Sempre executa!")     # executado sempre (com ou sem exceção)

# raise — lança uma exceção manualmente:
def dividir(a, b):
    if b == 0:
        raise ValueError("Divisor não pode ser zero!")
    return a / b

# raise sem argumento — relança a exceção atual:
try:
    dividir(10, 0)
except ValueError:
    raise              # relança o ValueError

# Exceção encadeada (chaining):
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("Falha na conversão") from e  # encadeia

# Criando exceções customizadas:
class SaldoInsuficienteError(ValueError):
    """Exceção para saldo bancário insuficiente."""
    def __init__(self, saldo, valor):
        self.saldo = saldo
        self.valor = valor
        super().__init__(f"Saldo {saldo} insuficiente para saque de {valor}")

try:
    raise SaldoInsuficienteError(100, 200)
except SaldoInsuficienteError as e:
    print(e.saldo, e.valor)     # 100 200

# Context manager com __enter__ e __exit__:
class GerenciadorContexto:
    def __enter__(self):
        print("Entrando no contexto")
        return self             # valor atribuído ao 'as'

    def __exit__(self, tipo_exc, valor_exc, traceback):
        print("Saindo do contexto")
        return False            # False = não suprime a exceção

with GerenciadorContexto() as gc:
    print("Dentro do contexto")

# contextlib.contextmanager — cria context manager com generator:
from contextlib import contextmanager, suppress

@contextmanager
def timer():
    import time
    inicio = time.time()
    try:
        yield                   # aqui ocorre o bloco 'with'
    finally:
        print(f"Tempo: {time.time() - inicio:.4f}s")

with timer():
    sum(range(1_000_000))

# suppress — suprime exceções específicas:
with suppress(FileNotFoundError):
    open("arquivo_inexistente.txt")  # FileNotFoundError é ignorado


# =============================================================================
# 8. MÓDULOS E PACOTES
# =============================================================================

# Importações básicas:
import math                         # importa o módulo inteiro
from math import sqrt, pi           # importa nomes específicos
from math import sqrt as raiz       # importa com alias
import os.path                      # importa submódulo
from os import path                 # outra forma

# Módulos da biblioteca padrão mais importantes:

# --- math ---
import math
print(math.pi)                  # 3.141592653589793
print(math.e)                   # 2.718281828459045
print(math.tau)                 # 6.283... (2*pi)
print(math.inf)                 # inf
print(math.nan)                 # nan
print(math.sqrt(16))            # 4.0
print(math.ceil(3.1))           # 4 — arredonda para cima
print(math.floor(3.9))          # 3 — arredonda para baixo
print(math.trunc(3.9))          # 3 — trunca (remove parte decimal)
print(math.factorial(5))        # 120
print(math.gcd(12, 8))          # 4 — máximo divisor comum
print(math.lcm(4, 6))           # 12 — mínimo múltiplo comum (Python 3.9+)
print(math.log(math.e))         # 1.0 — logaritmo natural
print(math.log(100, 10))        # 2.0 — log base 10
print(math.log2(8))             # 3.0
print(math.log10(1000))         # 3.0
print(math.sin(math.pi/2))      # 1.0
print(math.cos(0))              # 1.0
print(math.tan(math.pi/4))      # 0.999...
print(math.degrees(math.pi))    # 180.0 — radianos para graus
print(math.radians(180))        # 3.14... — graus para radianos
print(math.isnan(float("nan"))) # True
print(math.isinf(float("inf"))) # True
print(math.isfinite(42))        # True
print(math.comb(5, 2))          # 10 — combinações C(n,r)
print(math.perm(5, 2))          # 20 — permutações P(n,r)
print(math.hypot(3, 4))         # 5.0 — hipotenusa (distância euclidiana)
print(math.dist([0,0], [3,4]))  # 5.0 — distância entre dois pontos

# --- random ---
import random
random.seed(42)                  # define semente para reprodutibilidade
print(random.random())           # float uniforme [0.0, 1.0)
print(random.uniform(1, 10))     # float uniforme [a, b]
print(random.randint(1, 10))     # inteiro [a, b] (ambos inclusivos)
print(random.randrange(0, 100, 5))# inteiro [0,100) com passo 5
lst = list(range(10))
random.shuffle(lst)              # embaralha a lista in-place
print(lst)
print(random.choice([1,2,3,4]))  # elemento aleatório da sequência
print(random.choices([1,2,3], weights=[10,1,1], k=5))  # amostragem com peso
print(random.sample(range(100), k=5))  # amostragem sem reposição
print(random.gauss(0, 1))        # distribuição normal (média, desvio padrão)

# --- os ---
import os
print(os.getcwd())               # diretório de trabalho atual
os.chdir("/tmp")                 # muda o diretório atual
print(os.listdir("."))           # lista arquivos/dirs do diretório
print(os.path.join("pasta", "arquivo.txt"))  # une partes de caminho (OS-agnostico)
print(os.path.abspath("./teste"))# caminho absoluto
print(os.path.dirname("/a/b/c")) # '/a/b' — diretório pai
print(os.path.basename("/a/b/c"))# 'c' — nome do arquivo/dir
print(os.path.exists("/tmp"))    # True — verifica se existe
print(os.path.isfile("/tmp"))    # False — é arquivo?
print(os.path.isdir("/tmp"))     # True — é diretório?
print(os.path.splitext("arquivo.txt"))  # ('arquivo', '.txt')
print(os.path.getsize("/tmp"))   # tamanho em bytes
print(os.sep)                    # '/' em Unix, '\\' no Windows
print(os.linesep)                # '\n' em Unix, '\r\n' no Windows
print(os.environ.get("HOME", "N/A"))    # variável de ambiente
os.environ["MINHA_VAR"] = "valor"       # define variável de ambiente
print(os.getenv("MINHA_VAR"))           # outra forma de ler variável de ambiente
# os.makedirs("pasta/sub", exist_ok=True)  # cria diretórios (incluindo intermediários)
# os.remove("arquivo.txt")       # remove arquivo
# os.rmdir("pasta")              # remove diretório vazio
# os.rename("velho", "novo")     # renomeia
# os.stat("arquivo")             # informações do arquivo (tamanho, datas, etc.)

# --- sys ---
import sys
print(sys.version)               # versão do Python
print(sys.platform)              # 'linux', 'darwin', 'win32'
print(sys.argv)                  # argumentos da linha de comando
print(sys.path)                  # caminhos de busca de módulos
sys.path.append("/meu/modulo")   # adiciona ao path
print(sys.maxsize)               # inteiro máximo da plataforma
print(sys.float_info)            # informações sobre floats
print(sys.getrecursionlimit())   # limite de recursão
sys.setrecursionlimit(2000)      # muda o limite
print(sys.getsizeof([1,2,3]))    # tamanho do objeto em bytes
# sys.exit(0)                    # encerra o programa (0 = sucesso)
# sys.stdin, sys.stdout, sys.stderr — streams padrão

# --- pathlib (moderno, orientado a objetos) ---
from pathlib import Path
p = Path("/tmp")
print(p / "subpasta" / "arq.txt")  # concatenação de caminhos com /
print(p.exists())               # True
print(p.is_dir())               # True
print(p.home())                 # diretório home do usuário
print(p.cwd())                  # diretório de trabalho atual
# p.mkdir(parents=True, exist_ok=True)  # cria diretório
# p.write_text("conteúdo")      # escreve texto
# p.read_text()                 # lê texto
# list(p.iterdir())             # lista conteúdo
# list(p.glob("*.py"))          # encontra arquivos com padrão
# list(p.rglob("*.py"))         # recursivo

# --- datetime ---
from datetime import datetime, date, time, timedelta, timezone

hoje = date.today()             # data de hoje
print(hoje)                     # 2024-...
agora = datetime.now()          # data e hora atuais (local)
utc = datetime.now(timezone.utc)# data e hora UTC
print(agora.year, agora.month, agora.day, agora.hour, agora.minute)
delta = timedelta(days=7, hours=3)  # intervalo de tempo
print(agora + delta)            # daqui a 7 dias e 3 horas
print((agora - timedelta(days=30)).strftime("%d/%m/%Y"))  # formato BR
d = datetime.strptime("25/12/2024", "%d/%m/%Y")  # string para datetime
print(d.isoformat())            # "2024-12-25T00:00:00"
print(datetime.fromisoformat("2024-12-25"))  # ISO 8601 para datetime
print(agora.timestamp())        # Unix timestamp (float)
print(datetime.fromtimestamp(0))# epoch Unix → 01/01/1970

# --- re (expressões regulares) ---
import re
padrao = r"\d{3}-\d{4}"        # r"..." raw string para regexes
texto_re = "Ligue: 987-6543 ou 123-4567"
print(re.search(padrao, texto_re))        # primeiro match (ou None)
print(re.findall(padrao, texto_re))       # todos os matches como lista
print(re.finditer(padrao, texto_re))      # iterador de Match objects
print(re.match(r"\w+", "Python 3.11"))   # match apenas no início
print(re.fullmatch(r"\d+", "12345"))     # match da string inteira
print(re.sub(r"\d", "X", "abc123"))      # substitui → "abcXXX"
print(re.subn(r"\d", "X", "abc123"))     # substitui e conta → ("abcXXX", 3)
print(re.split(r"\s+", "a  b   c"))      # divide → ['a','b','c']
compilado = re.compile(r"\d+")           # pré-compila para reutilização
print(compilado.findall("1 e 2 e 3"))    # ['1', '2', '3']

# Grupos de captura:
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Data: 2024-12-25")
if m:
    print(m.group(0))           # match completo: '2024-12-25'
    print(m.group(1))           # 1º grupo: '2024'
    print(m.groups())           # ('2024', '12', '25')
    print(m.start(), m.end())   # posições no texto

# Grupos nomeados:
m2 = re.search(r"(?P<ano>\d{4})-(?P<mes>\d{2})", "2024-12")
if m2:
    print(m2.group("ano"))      # '2024'
    print(m2.groupdict())       # {'ano': '2024', 'mes': '12'}

# Flags:
re.findall(r"python", "Python é PYTHON", re.IGNORECASE)  # ignora maiúsc
re.findall(r"^\w+", "linha1\nlinha2", re.MULTILINE)       # ^ em cada linha

# --- json ---
import json
dados = {"nome": "Ana", "idades": [25, 30], "ativo": True, "extra": None}
json_str = json.dumps(dados, indent=2, ensure_ascii=False)  # Python→JSON string
print(json_str)
de_volta = json.loads(json_str)    # JSON string → Python
# json.dump(dados, arquivo)         # escreve JSON em arquivo
# json.load(arquivo)                # lê JSON de arquivo

# --- collections adicionais ---
from collections import deque   # já vimos acima
from collections import UserDict, UserList, UserString  # classes base para subclasses

# heapq — heap (fila de prioridade):
import heapq
h = [3, 1, 4, 1, 5, 9, 2]
heapq.heapify(h)                # transforma lista em heap in-place (min-heap)
print(heapq.heappop(h))         # 1 — remove e retorna o menor
heapq.heappush(h, 0)            # insere novo elemento
print(heapq.nsmallest(3, h))    # 3 menores sem modificar
print(heapq.nlargest(3, h))     # 3 maiores

# bisect — busca e inserção em lista ordenada (O(log n)):
import bisect
lst_ord = [1, 3, 5, 7, 9]
print(bisect.bisect_left(lst_ord, 5))   # 2 — posição para inserir
print(bisect.bisect_right(lst_ord, 5))  # 3 — posição após elementos iguais
bisect.insort(lst_ord, 6)               # insere mantendo ordem

# --- itertools ---
import itertools
print(list(itertools.count(1, 2)))[:5]  # [1,3,5,7,9,...] (infinito — use next ou islice)
print(list(itertools.cycle([1,2,3])))   # repete infinitamente (use islice)
print(list(itertools.repeat(5, 3)))     # [5,5,5]
print(list(itertools.islice(itertools.count(), 5)))  # [0,1,2,3,4] — limita iterável infinito
print(list(itertools.chain([1,2],[3,4],[5])))         # [1,2,3,4,5]
print(list(itertools.product([1,2],[3,4])))           # produto cartesiano
print(list(itertools.permutations([1,2,3], 2)))       # permutações
print(list(itertools.combinations([1,2,3], 2)))       # combinações sem repetição
print(list(itertools.combinations_with_replacement([1,2,3], 2)))  # com repetição
print(list(itertools.accumulate([1,2,3,4], lambda a,b: a*b)))     # [1,2,6,24]
print(list(itertools.dropwhile(lambda x: x<3, [1,2,3,4,2])))     # [3,4,2]
print(list(itertools.takewhile(lambda x: x<3, [1,2,3,4])))       # [1,2]
print(list(itertools.filterfalse(lambda x: x%2, range(5))))      # [0,2,4]
print(list(itertools.starmap(pow, [(2,10),(3,2)])))               # [1024,9]
print(list(itertools.compress([1,2,3,4,5],[1,0,1,0,1])))         # [1,3,5]
for k, g in itertools.groupby([1,1,2,2,3], lambda x: x):
    print(k, list(g))       # agrupa elementos consecutivos iguais

# --- functools ---
import functools
print(functools.reduce(lambda a,b: a+b, [1,2,3,4,5]))  # 15 — reduz a um valor
print(functools.reduce(lambda a,b: a+b, [1,2,3], 10))  # 16 — com valor inicial

@functools.lru_cache(maxsize=128)   # memoização — cacheia resultados
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(50))                  # rápido graças ao cache
print(fib.cache_info())         # CacheInfo(hits=..., misses=..., ...)
fib.cache_clear()               # limpa o cache

@functools.cache                # lru_cache sem limite (Python 3.9+)
def fib2(n):
    if n < 2: return n
    return fib2(n-1) + fib2(n-2)

parcial = functools.partial(pow, 2)  # "congela" o primeiro argumento
print(parcial(10))              # 1024 — equivale a pow(2, 10)

# total_ordering — gera comparadores a partir de __eq__ e __lt__:
@functools.total_ordering
class Versao:
    def __init__(self, v): self.v = v
    def __eq__(self, o): return self.v == o.v
    def __lt__(self, o): return self.v < o.v
    # Python gera automaticamente >, >=, <=

# --- operator ---
import operator
print(operator.add(3, 4))       # 7 — equivale a 3+4
print(operator.itemgetter(1)([10,20,30]))  # 20 — pega item por índice
print(operator.attrgetter("nome")(dog))    # 'buddy' — pega atributo
print(sorted([(1,"b"),(2,"a")], key=operator.itemgetter(1)))  # por 2º elemento

# --- typing (anotações de tipo) ---
from typing import (List, Dict, Tuple, Set, Optional, Union,
                    Any, Callable, Generator, Iterator, Iterable,
                    TypeVar, Generic, Protocol, Final, ClassVar,
                    overload, get_type_hints)

# Desde Python 3.9, use os tipos nativos (list, dict, etc.) em vez de typing:
def processar(itens: list[int], mapa: dict[str, float]) -> tuple[int, ...]:
    return tuple(itens)

T = TypeVar("T")                # variável de tipo genérico

def primeiro(lst: list[T]) -> T:   # função genérica
    return lst[0]

# Optional[X] equivale a Union[X, None]:
def buscar(nome: str) -> str | None:  # Python 3.10+ usa | em vez de Optional
    return nome if nome else None

# Final — indica que a variável não deve ser reatribuída:
CONSTANTE: Final = 42

# --- time ---
import time
print(time.time())              # timestamp atual (float, segundos desde epoch)
print(time.time_ns())           # timestamp em nanossegundos (Python 3.7+)
print(time.monotonic())         # relógio monotônico (sem ajustes, para medir duração)
print(time.perf_counter())      # contador de alta resolução para benchmarks
print(time.process_time())      # CPU time do processo
time.sleep(0.001)               # dorme por 0.001 segundos
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # formata data/hora atual
print(time.gmtime())            # struct_time UTC
print(time.localtime())         # struct_time local
print(time.mktime(time.localtime()))  # struct_time para timestamp

# --- logging ---
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)
logger.debug("Mensagem de debug (mais detalhado)")
logger.info("Informação geral")
logger.warning("Aviso: algo pode estar errado")
logger.error("Erro recuperável")
logger.critical("Erro crítico, possível crash")

try:
    1/0
except:
    logger.exception("Erro com traceback completo")  # inclui traceback

# --- threading ---
import threading

resultado_thread = []
def tarefa(n):
    resultado_thread.append(n * 2)

threads = [threading.Thread(target=tarefa, args=(i,)) for i in range(5)]
for t in threads:
    t.start()                   # inicia a thread
for t in threads:
    t.join()                    # aguarda a thread terminar
print(sorted(resultado_thread)) # [0, 2, 4, 6, 8]

# Lock para sincronização:
lock = threading.Lock()
def tarefa_segura():
    with lock:                  # garante acesso exclusivo
        pass

# --- multiprocessing ---
# import multiprocessing
# def worker(n): return n**2
# with multiprocessing.Pool(processes=4) as pool:
#     resultados = pool.map(worker, range(10))  # paralelismo real (múltiplos CPUs)

# --- concurrent.futures ---
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(lambda x: x**2, i) for i in range(5)]
    resultados = [f.result() for f in futures]
print(resultados)               # [0, 1, 4, 9, 16]

# executor.map — versão mais simples:
with ThreadPoolExecutor() as ex:
    res = list(ex.map(lambda x: x+1, range(5)))
print(res)                      # [1, 2, 3, 4, 5]

# --- asyncio (programação assíncrona) ---
import asyncio

async def buscar_dados(id_):    # coroutine — definida com async def
    await asyncio.sleep(0.01)   # await suspende a coroutine (sem bloquear o loop)
    return f"dados do id {id_}"

async def main_async():
    # gather executa coroutines concorrentemente:
    resultados_async = await asyncio.gather(
        buscar_dados(1),
        buscar_dados(2),
        buscar_dados(3)
    )
    print(resultados_async)

asyncio.run(main_async())       # executa a coroutine principal

# Async generator:
async def gerador_async():
    for i in range(3):
        await asyncio.sleep(0)
        yield i

async def consumir():
    async for valor in gerador_async():  # async for
        print(valor)

asyncio.run(consumir())

# Async context manager:
class AsyncCtx:
    async def __aenter__(self):
        return self
    async def __aexit__(self, *args):
        pass

async def usar_ctx():
    async with AsyncCtx() as ctx:       # async with
        pass

# --- subprocess ---
import subprocess
resultado_proc = subprocess.run(
    ["echo", "Olá do shell"],
    capture_output=True,        # captura stdout e stderr
    text=True                   # decodifica bytes para string
)
print(resultado_proc.stdout.strip())   # 'Olá do shell'
print(resultado_proc.returncode)       # 0 — código de retorno

# --- socket ---
# import socket
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect(("httpbin.org", 80))  # conecta TCP

# --- struct ---
import struct
packed = struct.pack("!I", 12345)   # empacota inteiro em bytes (big-endian)
print(packed)                        # b'\x00\x00\x30\x39'
print(struct.unpack("!I", packed))  # (12345,) — desempacota

# --- io ---
import io
buf = io.StringIO()             # buffer de string em memória
buf.write("Olá\n")
buf.write("Mundo\n")
print(buf.getvalue())           # 'Olá\nMundo\n'
buf.seek(0)                     # volta ao início
print(buf.read())               # lê tudo

bbuf = io.BytesIO(b"\x00\x01\x02")  # buffer de bytes em memória

# --- copy ---
import copy
original = [[1, 2], [3, 4]]
rasa = copy.copy(original)       # shallow copy — listas internas são shared
profunda = copy.deepcopy(original)# deep copy — tudo independente
original[0].append(99)
print(rasa)                      # [[1, 2, 99], [3, 4]] — afetado
print(profunda)                  # [[1, 2], [3, 4]] — não afetado

# --- pprint ---
from pprint import pprint
pprint({"a": [1,2,3], "b": {"c": 4}}, width=40)  # pretty print

# --- enum ---
from enum import Enum, IntEnum, Flag, auto

class Cor(Enum):
    VERMELHO = 1
    VERDE = 2
    AZUL = 3

print(Cor.VERMELHO)             # Cor.VERMELHO
print(Cor.VERMELHO.name)        # 'VERMELHO'
print(Cor.VERMELHO.value)       # 1
print(Cor(2))                   # Cor.VERDE — por valor
print(list(Cor))                # todos os membros

class Permissao(Flag):          # Flag permite combinação bit a bit
    LER = auto()                # auto() gera valor automaticamente
    ESCREVER = auto()
    EXECUTAR = auto()

p = Permissao.LER | Permissao.ESCREVER
print(Permissao.LER in p)       # True

# --- dataclasses extras ---
from dataclasses import asdict, astuple, replace
p_orig = Produto("Mouse", 50.0, 10)
print(asdict(p_orig))           # {'nome': 'Mouse', 'preco': 50.0, 'estoque': 10}
print(astuple(p_orig))          # ('Mouse', 50.0, 10, [])
p_novo = replace(p_orig, preco=45.0)  # cria cópia com campo alterado

# --- contextlib extras ---
from contextlib import ExitStack, asynccontextmanager

# ExitStack — gerencia múltiplos context managers dinamicamente:
with ExitStack() as stack:
    arquivos = [stack.enter_context(open("/dev/null")) for _ in range(3)]

# --- weakref ---
import weakref
class Objeto: pass
obj = Objeto()
ref = weakref.ref(obj)          # referência fraca (não impede GC)
print(ref())                    # <Objeto object> — ainda existe
del obj
print(ref())                    # None — foi coletado pelo GC

# --- gc (garbage collector) ---
import gc
gc.collect()                    # força coleta de lixo
print(gc.get_count())           # (gen0, gen1, gen2) — objetos pendentes
gc.disable()                    # desativa GC automático
gc.enable()                     # reativa

# --- traceback ---
import traceback
try:
    1/0
except:
    traceback.print_exc()       # imprime o traceback atual
    tb = traceback.format_exc() # captura como string

# --- inspect ---
import inspect
print(inspect.isfunction(saudacao))  # True
print(inspect.isclass(Animal))       # True
print(inspect.signature(saudacao))   # (nome)
print(inspect.getsource(saudacao))   # código-fonte da função
print(inspect.getmembers(dog, predicate=inspect.ismethod))  # métodos do objeto

# --- ast (Abstract Syntax Tree) ---
import ast
arvore = ast.parse("x = 1 + 2")# analisa código para árvore sintática
print(ast.dump(arvore))         # representação da árvore
print(compile(arvore, "<string>", "exec"))  # compila a árvore

# --- dis (disassembler) ---
import dis
dis.dis(fatorial)               # mostra bytecode da função

# --- importlib ---
import importlib
mod = importlib.import_module("math")  # importa módulo por string
print(mod.pi)
# importlib.reload(mod)          # recarrega módulo (útil no desenvolvimento)

# --- pkgutil ---
# import pkgutil
# for importer, name, ispkg in pkgutil.iter_modules():
#     print(name)                # lista todos os módulos instalados

# --- platform ---
import platform
print(platform.python_version())  # '3.11.x'
print(platform.system())          # 'Linux', 'Windows', 'Darwin'
print(platform.machine())         # 'x86_64', 'arm64', etc.

# --- locale ---
import locale
locale.setlocale(locale.LC_ALL, "")  # configura locale do sistema
# print(locale.currency(1234.56))  # formata moeda (depende do locale)

# --- decimal (precisão arbitrária) ---
from decimal import Decimal, getcontext
getcontext().prec = 50          # define precisão
print(Decimal("0.1") + Decimal("0.2"))  # 0.3 — sem erro de float!
print(0.1 + 0.2)                # 0.30000000000000004 — erro de float normal

# --- fractions ---
from fractions import Fraction
print(Fraction(1, 3) + Fraction(1, 6))  # 1/2 — aritmética exata
print(Fraction(0.5))            # 1/2 — float para fração

# --- statistics ---
import statistics
dados_stat = [2, 4, 4, 4, 5, 5, 7, 9]
print(statistics.mean(dados_stat))     # 5.0 — média aritmética
print(statistics.median(dados_stat))   # 4.5 — mediana
print(statistics.mode(dados_stat))     # 4   — moda
print(statistics.stdev(dados_stat))    # desvio padrão amostral
print(statistics.variance(dados_stat)) # variância amostral
print(statistics.pstdev(dados_stat))   # desvio padrão populacional
print(statistics.quantiles(dados_stat, n=4))  # quartis

# --- hashlib ---
import hashlib
h = hashlib.sha256(b"Python")   # hash SHA-256
print(h.hexdigest())            # string hexadecimal do hash
print(hashlib.md5(b"texto").hexdigest())  # MD5 (não usar para segurança)
print(hashlib.algorithms_available)  # todos os algoritmos disponíveis

# --- hmac ---
import hmac
chave = b"chave_secreta"
msg = b"mensagem"
mac = hmac.new(chave, msg, hashlib.sha256)
print(mac.hexdigest())
print(hmac.compare_digest(mac.hexdigest(), mac.hexdigest()))  # True (seguro contra timing attack)

# --- secrets ---
import secrets
print(secrets.token_hex(16))    # 32 chars hex criptograficamente seguro
print(secrets.token_bytes(16))  # 16 bytes aleatórios
print(secrets.token_urlsafe(16))# 22 chars URL-safe
print(secrets.choice("abcdefghij"))  # escolha aleatória segura

# --- base64 ---
import base64
encoded = base64.b64encode(b"Python")
print(encoded)                  # b'UHl0aG9u'
print(base64.b64decode(encoded))# b'Python'
print(base64.urlsafe_b64encode(b"Python"))  # versão URL-safe

# --- urllib ---
from urllib.parse import urlparse, urlencode, quote, unquote
u = urlparse("https://www.example.com:8080/path?q=python&v=3")
print(u.scheme, u.netloc, u.path, u.query)
print(urlencode({"chave": "valor com espaços", "num": 42}))
print(quote("Olá mundo"))       # URL-encode
print(unquote("Ol%C3%A1%20mundo")) # URL-decode

# --- html ---
import html
print(html.escape("<script>alert('xss')</script>"))  # escapa HTML
print(html.unescape("&lt;p&gt;"))  # desescapa HTML

# --- csv ---
import csv
import io

saida_csv = io.StringIO()
writer = csv.writer(saida_csv)
writer.writerow(["nome", "idade", "cidade"])     # escreve cabeçalho
writer.writerows([["Ana", 25, "SP"], ["Bruno", 30, "RJ"]])

saida_csv.seek(0)
reader = csv.reader(saida_csv)
for linha in reader:
    print(linha)

# DictWriter / DictReader:
saida_csv2 = io.StringIO()
campos = ["nome", "nota"]
dw = csv.DictWriter(saida_csv2, fieldnames=campos)
dw.writeheader()
dw.writerow({"nome": "Carla", "nota": 9.5})

# --- sqlite3 ---
import sqlite3
conn = sqlite3.connect(":memory:")   # banco em memória
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
""")
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Ana", 25))
cursor.executemany(
    "INSERT INTO usuarios (nome, idade) VALUES (?, ?)",
    [("Bruno", 30), ("Carla", 22)]
)
conn.commit()
cursor.execute("SELECT * FROM usuarios WHERE idade > ?", (20,))
print(cursor.fetchall())        # [(1,'Ana',25),(2,'Bruno',30),(3,'Carla',22)]
for linha in cursor.execute("SELECT nome FROM usuarios"):
    print(linha[0])
conn.row_factory = sqlite3.Row  # acessa colunas por nome
conn.close()

# --- pickle ---
import pickle
# pickle.dump(objeto, arquivo_binário)  # serializa para arquivo
# objeto = pickle.load(arquivo_binário)  # desserializa de arquivo
bytes_pickle = pickle.dumps({"a": [1,2,3]})  # serializa para bytes
obj_de_volta = pickle.loads(bytes_pickle)    # desserializa de bytes
print(obj_de_volta)             # {'a': [1, 2, 3]}

# --- shelve ---
# import shelve
# with shelve.open("meu_banco") as db:
#     db["chave"] = {"dado": 42}  # persiste objetos Python em arquivo
#     print(db["chave"])

# --- configparser ---
import configparser
config = configparser.ConfigParser()
config["DEFAULT"] = {"servidor": "localhost", "porta": "8080"}
config["banco"] = {"nome": "meubanco", "usuario": "admin"}
cfg_str = io.StringIO()
config.write(cfg_str)
print(cfg_str.getvalue())

# --- argparse ---
import argparse
parser = argparse.ArgumentParser(description="Meu programa")
parser.add_argument("nome", help="Nome do usuário")
parser.add_argument("--idade", type=int, default=18, help="Idade")
parser.add_argument("--verbose", action="store_true", help="Verboso")
# args = parser.parse_args()    # lê de sys.argv (comentado para não pausar)
args = parser.parse_args(["João", "--idade", "25", "--verbose"])
print(args.nome, args.idade, args.verbose)  # João 25 True

# --- shutil ---
import shutil
# shutil.copy("origem.txt", "destino.txt")    # copia arquivo
# shutil.copy2("origem.txt", "destino/")      # copia preservando metadados
# shutil.copytree("dir_orig", "dir_dest")     # copia árvore de diretórios
# shutil.move("origem", "destino")            # move/renomeia
# shutil.rmtree("diretorio")                  # remove árvore
# shutil.make_archive("saida", "zip", "pasta")# cria arquivo zip
print(shutil.which("python3"))  # caminho do executável

# --- tempfile ---
import tempfile
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
    f.write("conteúdo temporário")
    print(f.name)               # caminho do arquivo temporário

with tempfile.TemporaryDirectory() as tmpdir:
    print(tmpdir)               # diretório temporário (removido ao sair)

# --- zipfile / tarfile ---
import zipfile
with zipfile.ZipFile("/tmp/teste.zip", "w") as zf:
    zf.writestr("arquivo.txt", "conteúdo")   # cria zip com conteúdo
with zipfile.ZipFile("/tmp/teste.zip", "r") as zf:
    print(zf.namelist())        # lista arquivos no zip
    # zf.extractall("/tmp/destino")

# import tarfile
# with tarfile.open("arquivo.tar.gz", "w:gz") as tar:
#     tar.add("pasta/")

# --- textwrap ---
import textwrap
texto_longo = "Python é uma linguagem de programação de alto nível, interpretada e de propósito geral."
print(textwrap.fill(texto_longo, width=40))   # quebra em 40 chars
print(textwrap.wrap(texto_longo, width=40))   # retorna lista de linhas
print(textwrap.dedent("""
    linha 1
    linha 2
"""))                                          # remove indentação comum
print(textwrap.indent("linha1\nlinha2", ">>> ")) # adiciona prefixo

# --- difflib ---
import difflib
antes = ["linha1\n", "linha2\n", "linha3\n"]
depois = ["linha1\n", "linha2 editada\n", "linha3\n", "linha4\n"]
diff = list(difflib.unified_diff(antes, depois, fromfile="antes", tofile="depois"))
print("".join(diff))

# --- pdb (debugger) ---
# import pdb
# pdb.set_trace()  # ponto de interrupção (breakpoint)
# breakpoint()     # Python 3.7+ — equivale a pdb.set_trace()

# --- unittest ---
import unittest

class TestMatematica(unittest.TestCase):
    def setUp(self):            # executado antes de cada teste
        self.a = 10
        self.b = 5

    def tearDown(self):         # executado após cada teste
        pass

    def test_soma(self):
        self.assertEqual(self.a + self.b, 15)   # verifica igualdade

    def test_divisao(self):
        self.assertAlmostEqual(1/3, 0.333, places=2)  # float com tolerância

    def test_excecao(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def test_verdadeiro(self):
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertIsNone(None)
        self.assertIsNotNone(42)
        self.assertIn(1, [1,2,3])
        self.assertNotIn(4, [1,2,3])
        self.assertIsInstance(42, int)
        self.assertGreater(5, 3)
        self.assertLessEqual(3, 3)

# Executa os testes:
suite = unittest.TestLoader().loadTestsFromTestCase(TestMatematica)
runner = unittest.TextTestRunner(verbosity=0)
runner.run(suite)

# --- Doctest ---
def somar(a, b):
    """
    Soma dois números.

    >>> somar(2, 3)
    5
    >>> somar(-1, 1)
    0
    """
    return a + b

import doctest
doctest.testmod(verbose=False)  # executa exemplos no docstring


# =============================================================================
# 9. RECURSOS AVANÇADOS DA LINGUAGEM
# =============================================================================

# Descriptor Protocol:
class Validado:
    """Descriptor que valida que o valor é positivo."""
    def __set_name__(self, owner, name):    # chamado quando a classe é criada
        self.name = name

    def __get__(self, obj, objtype=None):  # acessar o atributo
        if obj is None: return self         # acesso via classe
        return getattr(obj, f"_{self.name}", None)

    def __set__(self, obj, value):          # atribuir ao atributo
        if value < 0:
            raise ValueError(f"{self.name} deve ser positivo")
        setattr(obj, f"_{self.name}", value)

class Conta:
    saldo = Validado()          # saldo é um descriptor
    def __init__(self, saldo):
        self.saldo = saldo

c_banco = Conta(100)
print(c_banco.saldo)            # 100

# Metaclasses:
class MetaRegistro(type):
    registro = {}
    def __new__(mcs, nome, bases, namespace):
        cls = super().__new__(mcs, nome, bases, namespace)
        mcs.registro[nome] = cls  # registra a classe
        return cls

class Base(metaclass=MetaRegistro):
    pass

class Filho(Base):
    pass

print(MetaRegistro.registro)    # {'Base': <class 'Base'>, 'Filho': <class 'Filho'>}

# Slots — economiza memória, impede criação de atributos arbitrários:
class PontoSlot:
    __slots__ = ["x", "y"]     # apenas x e y são permitidos
    def __init__(self, x, y):
        self.x, self.y = x, y

ps = PontoSlot(3, 4)
# ps.z = 5                      # AttributeError — z não está nos slots

# Protocol (duck typing estrutural — Python 3.8+):
from typing import Protocol

class Desenhavel(Protocol):
    def desenhar(self) -> None: ...  # define a "interface"

class Circulo2:
    def desenhar(self): print("Desenhando círculo")

def renderizar(forma: Desenhavel) -> None:
    forma.desenhar()

renderizar(Circulo2())          # OK — Circulo2 implementa o protocolo sem herdar

# Annotated (metadados em tipos — Python 3.9+):
from typing import Annotated
IdadeValida = Annotated[int, "deve ser entre 0 e 150"]

# ParamSpec e Concatenate (Python 3.10+):
from typing import ParamSpec, Concatenate
P = ParamSpec("P")

def adicionar_log(func: Callable[P, T]) -> Callable[P, T]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"Chamando {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# TypeAlias (Python 3.10+):
from typing import TypeAlias
Vetor: TypeAlias = list[float]

# Variáveis de tipo com bounds (TypeVar com bound):
Numerico = TypeVar("Numerico", bound=int | float)

def soma_generica(a: Numerico, b: Numerico) -> Numerico:
    return a + b

# __init_subclass__ — hook para personalizar herança:
class Plugin:
    subclasses = []
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.subclasses.append(cls)  # registra automaticamente

class PluginA(Plugin): pass
class PluginB(Plugin): pass
print(Plugin.subclasses)        # [PluginA, PluginB]

# __class_getitem__ — suporte a generics customizados:
class MinhaLista:
    def __class_getitem__(cls, item):
        return f"MinhaLista[{item}]"

print(MinhaLista[int])          # "MinhaLista[<class 'int'>]"

# Positional-only e keyword-only combinados:
def avancada(pos_only, /, normal, *, kw_only):
    return pos_only + normal + kw_only

print(avancada(1, 2, kw_only=3))   # 6

# Walrus em comprehensions:
resultados_wal = [y := f(x), y**2, y**3]  # y é reutilizado


# =============================================================================
# 10. DUNDER METHODS (MÉTODOS MÁGICOS) — REFERÊNCIA COMPLETA
# =============================================================================

class DunderDemo:
    """Demonstra os principais dunder methods."""

    # Criação e inicialização:
    def __new__(cls, *args, **kwargs):      # cria a instância (antes de __init__)
        print("__new__ chamado")
        return super().__new__(cls)

    def __init__(self, valor):              # inicializa a instância
        self.valor = valor

    def __del__(self):                      # destrutor (GC)
        pass

    # Representação:
    def __str__(self):   return f"DD({self.valor})"      # str(obj)
    def __repr__(self):  return f"DunderDemo({self.valor!r})"  # repr(obj)
    def __bytes__(self): return str(self.valor).encode() # bytes(obj)
    def __format__(self, spec): return format(self.valor, spec)  # format(obj, spec)

    # Operadores de comparação:
    def __lt__(self, o): return self.valor < o.valor     # <
    def __le__(self, o): return self.valor <= o.valor    # <=
    def __eq__(self, o): return self.valor == o.valor    # ==
    def __ne__(self, o): return self.valor != o.valor    # !=
    def __gt__(self, o): return self.valor > o.valor     # >
    def __ge__(self, o): return self.valor >= o.valor    # >=

    # Operadores aritméticos (self OP other):
    def __add__(self, o):      return DunderDemo(self.valor + o.valor)   # +
    def __sub__(self, o):      return DunderDemo(self.valor - o.valor)   # -
    def __mul__(self, o):      return DunderDemo(self.valor * o.valor)   # *
    def __truediv__(self, o):  return DunderDemo(self.valor / o.valor)   # /
    def __floordiv__(self, o): return DunderDemo(self.valor // o.valor)  # //
    def __mod__(self, o):      return DunderDemo(self.valor % o.valor)   # %
    def __pow__(self, o):      return DunderDemo(self.valor ** o.valor)  # **
    def __matmul__(self, o):   return NotImplemented                     # @

    # Operadores aritméticos refletidos (other OP self):
    def __radd__(self, o): return DunderDemo(o + self.valor)   # o + self
    def __rsub__(self, o): return DunderDemo(o - self.valor)
    def __rmul__(self, o): return DunderDemo(o * self.valor)

    # Operadores de atribuição composta:
    def __iadd__(self, o): self.valor += o.valor; return self   # +=
    def __isub__(self, o): self.valor -= o.valor; return self   # -=

    # Operadores unários:
    def __neg__(self):  return DunderDemo(-self.valor)  # -obj
    def __pos__(self):  return DunderDemo(+self.valor)  # +obj
    def __abs__(self):  return DunderDemo(abs(self.valor))  # abs(obj)
    def __invert__(self): return DunderDemo(~self.valor)    # ~obj

    # Conversões de tipo:
    def __bool__(self):  return bool(self.valor)   # bool(obj) / if obj
    def __int__(self):   return int(self.valor)    # int(obj)
    def __float__(self): return float(self.valor)  # float(obj)
    def __complex__(self): return complex(self.valor)  # complex(obj)
    def __index__(self): return int(self.valor)    # necessário para slice e bin/oct/hex

    # Container protocol:
    def __len__(self):          return self.valor       # len(obj)
    def __getitem__(self, key): return key              # obj[key]
    def __setitem__(self, key, val): pass               # obj[key] = val
    def __delitem__(self, key): pass                    # del obj[key]
    def __contains__(self, item): return item == self.valor  # item in obj
    def __iter__(self): return iter([self.valor])       # iter(obj) / for in obj
    def __next__(self): raise StopIteration             # next(obj)
    def __reversed__(self): return iter([self.valor])  # reversed(obj)

    # Atributos:
    def __getattr__(self, name): return f"attr_{name}"       # obj.attr (fallback)
    def __setattr__(self, name, val): object.__setattr__(self, name, val)  # obj.attr = val
    def __delattr__(self, name): object.__delattr__(self, name)  # del obj.attr
    def __getattribute__(self, name): return object.__getattribute__(self, name)  # toda acesso

    # Callable:
    def __call__(self, *args): return f"chamado({args})"  # obj()

    # Context manager:
    def __enter__(self): return self        # with obj as x
    def __exit__(self, *args): return False  # saída do bloco with

    # Hash e pickling:
    def __hash__(self):  return hash(self.valor)  # hash(obj), para dicionários
    def __sizeof__(self): return object.__sizeof__(self)  # sys.getsizeof(obj)

    # Classificação (para isinstance, issubclass):
    @classmethod
    def __class_getitem__(cls, item): return cls  # MyClass[int]
    def __instancecheck__(self, instance): return True  # isinstance(x, obj)


# =============================================================================
# 11. VARIÁVEIS ESPECIAIS E CONSTANTES DA LINGUAGEM
# =============================================================================

print(__name__)         # '__main__' se executado diretamente, ou nome do módulo
print(__file__)         # caminho do arquivo atual
print(__doc__)          # docstring do módulo
# __package__           # nome do pacote do módulo
# __spec__              # especificação do módulo (ModuleSpec)
# __loader__            # loader que carregou o módulo
# __builtins__          # módulo builtins ou dicionário de builtins

# Constantes do builtins:
print(True, False)      # booleanos
print(None)             # ausência de valor
print(NotImplemented)   # retornado por operadores quando operação não suportada
print(Ellipsis)         # ...  — placeholder em type hints e slices de numpy
print(...)              # igual a Ellipsis

# __all__ — controla o que é exportado com "from modulo import *":
__all__ = ["saudacao", "Animal"]  # apenas esses serão exportados

# __slots__ — já visto acima

# Atributos de função:
def exemplo_fn(a, b=2): pass
print(exemplo_fn.__name__)      # 'exemplo_fn'
print(exemplo_fn.__qualname__)  # 'exemplo_fn' (qualificado: 'Classe.metodo')
print(exemplo_fn.__defaults__)  # (2,) — valores padrão dos parâmetros
print(exemplo_fn.__code__)      # objeto de código
print(exemplo_fn.__globals__)   # dicionário global do módulo
print(exemplo_fn.__module__)    # '__main__'
print(exemplo_fn.__annotations__)  # {} — anotações de tipo
print(exemplo_fn.__dict__)      # {} — atributos customizados

# Atributos de classe:
print(Animal.__name__)          # 'Animal'
print(Animal.__bases__)         # (<class 'object'>,)
print(Animal.__mro__)           # ordem de resolução de métodos
print(Animal.__dict__)          # namespace da classe
print(Animal.__module__)        # '__main__'
print(Animal.__doc__)           # docstring

# Atributos de instância:
print(dog.__class__)            # <class '__main__.Cachorro'>
print(dog.__dict__)             # {'_protegido': ..., '_Animal__privado': ...}


# =============================================================================
# FIM DO GUIA
# =============================================================================
print("\n✅ Guia completo de Python executado com sucesso!")
print(f"Python {__import__('sys').version}")
