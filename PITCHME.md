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
