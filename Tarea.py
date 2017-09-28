import math as math
import sys, os

def vector(path):
    F = open(path, "r")
    print("PARSEANDO DOCUMENTO")
    myset = set()
    largo = 0
    for document in F:
        document = document.replace(".I", " ")
        document = document.replace(".", " ")
        document = document.replace(";", " ")
        document = document.replace(",", " ")
        document = document.replace(":", " ")
        document = document.replace("(", " ")
        document = document.replace(")", " ")
        lista = document.split()
        largo = len(lista)
        for i in range(largo):
            myset.add(lista[i])
    lista = list(myset)
    lista.sort()

    return lista

def separar_docs(path):
    F = open(path, "r")
    print("SEPARANDO DOCUMENTOS")
    archivo = F.read()
    documents = archivo.split(".I ")
    largo = 0
    con = []
    terminos = []
    
    for document in documents:
        document = document.replace(".", " ")
        document = document.replace(";", " ")
        document = document.replace(",", " ")
        document = document.replace(":", " ")
        document = document.replace("(", " ")
        document = document.replace(")", " ")
       
        wordsInDocument = document.split()
        documentSize = len(wordsInDocument)      
       
        for i in range(documentSize):
            terminos.append(wordsInDocument[i])
        con.append(terminos)
        terminos = []

    del con[0]

    return con


#esta es la funcion que calcula tf
def tf(diferentTerms, documents):
    print("CALCULANDO TF")
    matrixTf = [[0 for x in range(len(diferentTerms))] for y in range(len(documents))]
    counter = 0
    for terms,j in zip(diferentTerms, range(0, len(diferentTerms))):
        
        for document,i in zip(documents, range(0,len(documents))):

            for word in document:

                if terms == word:
                    counter += 1
                    matrixTf[i][j] = counter

            counter = 0

    return matrixTf       


#funcion para saber la posicion de la palabra x en el vector de terminos diferentes
def wordPosition(diferentTerms, word):
    for terms,i in zip(diferentTerms, range(0, len(diferentTerms))):
        if terms == word:
            return i

# en cuantos documentos aparece el termino X
def numOcurrences(diferentTerms, documents, matrixTf):
    print ("CALCULANDO IDF")
    counter = 0
    matrixNumOcurrences = [[0 for x in range(len(diferentTerms))] for y in (0,1)]

    for terms,j in zip(diferentTerms, range(0, len(diferentTerms))):
        
        for document,i in zip(documents, range(0,len(documents))):


                if matrixTf[i][j] > 0:
                    counter += 1

        matrixNumOcurrences[0][j] = counter
        d = float(len(documents))
        df = float(matrixNumOcurrences[0][j])
        matrixNumOcurrences[1][j] = math.log10(d/df)
        counter = 0


    return matrixNumOcurrences 

def tfIdf(matrixTf,matrixNumOcurrences):
    print ("CALCULANDO TF * IDF")
    matrixtfIdf = [[0 for x in range(len(diferentTerms))] for y in range(len(matrixTf))]

    for terms,i in zip(matrixTf, range(0, len(matrixTf))):
        
        for doc,j in zip(terms, range(0,len(terms))):
            
            matrixtfIdf[i][j] = matrixNumOcurrences[1][j] * matrixTf[i][j]

    return matrixtfIdf

def calcularPrecision(rr):
    precision = []
    for term, i in zip(rr, range(1, len(rr))):
        precision.append(term/i)
    return precision

def calcularRecall(rr,totalRelevantes):
    recall = []
    for term, i in zip(rr, range(0, len(rr))):
        recall.append(term / totalRelevantes)
        if(term/totalRelevantes < 1):
            totalRecall = i
    print("Recall = 100% a partir del documento ", totalRecall+1)
    return recall
    

def calcularRR(mostrados,relevantes):
    cont = 0
    rr = []
    for term in mostrados:
        for word in relevantes:
            if(int(term) == int(word)):
                cont = cont + 1
        rr.append(cont)
    return rr

def listaResultado(lista):
    counter = 0
    union = []
    for word in lista:
        for term in word.split():
            if counter == 2:
                union.append(term)
                counter = 0
            else:
                counter = counter + 1
    return union


def similitud(doctfidf,queriestfidf):
    print ("CALCULANDO LA SIMILITUD")
    arrayAux = []
    for document, i  in zip (doctfidf, range(0 ,len(doctfidf))):
        string = sum(map(lambda x, y: x * y , queriestfidf, document))
        temp = str(string)
        documento1 = str (i + 1)

        if(string < 10):
            temp = "0" + temp
        if(string < 100):
            temp = "0" + temp
        
        arrayAux.append( temp + " Documento: " + documento1 )

    return arrayAux

def main_menu():
    os.system('cls')
    
    print ("Bienvenidos al Super Buscador!")
    print ("Deseas realizar una consulta?")
    print ("1. SI")
    print ("2. NO")
    print ("\n0. Salir")
    opcn = input(" >>  ")
    correr_menu(opcn)
 
    return

def correr_menu(opcn):
    os.system('cls')
    opcn = str(opcn)
    ch = opcn
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Error, por favor intentalo otra vez.\n")
            menu_actions['main_menu']()

    return
# Lista de opciones del menu
def menu1():
    print ("Que numero de consulta deseas realizar?\n")
    return
   
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': main_menu,
    '0': exit,
}


def doc_relevantes(path):
    resultados = open(path, "r")
    archivo = resultados.read()
    archivo = archivo.replace("0.000000", " ")

    lista = archivo.split()
    eliminar = []

    for terms,i in zip(lista, range(0, len(lista))):
        if(terms == "0"):
            eliminar.append(i)

    for terms in reversed(eliminar):
        del lista[terms]

    pos = 0
    aux = []
    union = []

    for word,i in zip(lista, range(0, len(lista))):
        if(i % 2 == 0):
            if(pos == (int(word)-1)):
                aux.append(int(lista[i+1]))
            else:
                union.append(aux)
                pos = (int(word)-1)
                aux = []
                aux.append(int(lista[i+1]))

    return union



# Menu para realizar consultas nuevas de palabras
 
global varl
# Menu para realizar consultas predeterminadas
    
# Salir del programa
def exit():
    sys.exit()
    
# 

#-------MAIN-------
main_menu()
varl = int(input())
valorF = varl - 1

#base de datos
diferentTerms = vector("C:\\Users\\mones\\Desktop\\H4\\MED_ALL.txt") #vector que contiene todas las palabras diferentes en el doc
documents = separar_docs("C:\\Users\\mones\\Desktop\\H4\\MED_ALL.txt") 

#queries
queries = separar_docs("C:\\Users\\mones\\Desktop\\H4\\MED_QRY.txt") 

relevantes = doc_relevantes("C:\\Users\\mones\\Desktop\\H4\\MED_REL_OLD.txt")

#La querie que se esta buscando
print("LA QUERIE ES:")
print(queries[valorF])

#tf de queries y de documentos

queriesTf = tf(diferentTerms,queries)
matrixTf = tf(diferentTerms,documents)

#idf de documentos y queries
vectorNum = numOcurrences(diferentTerms, documents, matrixTf)


#tfidf de documentos y queries
doctfidf = tfIdf(matrixTf,vectorNum)
queriestfidf = tfIdf(queriesTf,vectorNum)

#similitud
arrayAux = similitud(doctfidf, queriestfidf[valorF])


arrayAux.sort()
reversed(arrayAux)
print("LARGO ARRAY AUX", len(arrayAux))

for i in range(1,len(arrayAux)+ 1):
    print (arrayAux[len(arrayAux) - i])

print("PRUEBA!!!!!!!!!!!!!!!!!!!!!!!! arrayaux[0]")
temp = arrayAux[len(arrayAux) - 2].split()
print("TEMP VALE ", temp, " LARGO AUX VALE ", len(arrayAux))
print(documents[int(temp[len(temp)- 1])])


'''print("LARGOOOOO-----------------", len(relevantes[valorF]))
result = listaResultado(reversed(arrayAux))
#print(result)
print("RR ---------------------------")
rr = calcularRR(result, relevantes[valorF])
print(rr)
print("RECALL ---------------------------")
recall = calcularRecall(rr, len(relevantes[valorF]))
print(recall)
print("PRECISION ---------------------------")
precision = calcularPrecision(rr)
print(precision)
'''
