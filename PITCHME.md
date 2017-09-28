# Motor de búsqueda v0.1

- Mónica Inés Vela     150251
- Dominic Hermida      151968
- Arturo Loya          150406
- Juan Carlos Ramírez	 152016

---

### Descripción del problema

- Desarrollar un motor de búsqueda utilizando el modelo vectorial como método de peso y el producto punto como método de similitud

---

### Modelo de datos

- Se decidió no utilizar una base de datos y trabajar todo en matrices y arreglos.
- La colección, los documentos y las consultas son cada uno una matriz.
- Precisión, cobertura y RR son arreglos.

---

### Asignación de pesos

- Se utilizó el modelo vectorial como esquema de asignación de pesos
- Se genera un vector donde se guardan todos los términos únicos de la colección
- Se calcula TF para todos los documentos y las consultas

---

Se calcula el IDF con la siguiente fórmula: 
![imagendeidf](https://raw.githubusercontent.com/monicavelaje/BuscadorRI/master/idf.PNG)

Por último se realiza TF * IDF para los documentos y las consultas

---

### Medida de similitud

- Se utilizó el producto punto para calcular la similitud de nuestras consultas. Dicho producto punto se realizaba entre la consulta deseada y toda la colección.

---

##### Función utilizada para generar el vector de términos únicos de nuestra colección

```python
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
  ```  
---
#### Función para separar y guardar documentos y consultas en matrices

```python
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
```
