# Cortos de Organización y Lenguajes de Compiladores 2

- [Cortos de Organización y Lenguajes de Compiladores 2](#cortos-de-organización-y-lenguajes-de-compiladores-2)
  - [Corto 1](#corto-1)
  - [Corto 2](#corto-2)

## Corto 1

Escriba un esquema de traducción dirigido por la sintaxis posfijo, para un analizador ascendente que reciba como entrada una expresión aritmética (*, +, -, / y paréntesis) y genere para esta el código de tres direcciones equivalente.

Gramática

```
S -> E      { print(E.C3D) }
E -> E + T  { E.TMP = new_temp()
              E.C3D = E1.C3D + T.C3D
              + E.TMP + '=' + E1.TMP + '+' + T.TMP }
E -> E - T  { E.TMP = new_temp()
              E.C3D = E1.C3D + T.C3D
              + E.TMP + '=' + E1.TMP + '-' + T.TMP }
E -> T      { E.TMP = T.TMP
              E.C3D = T.C3D }
T -> T * F  { E.TMP = new_temp()
              E.C3D = E1.C3D + T.C3D
              + E.TMP + '=' + E1.TMP + '*' + T.TMP }
T -> T / F  { E.TMP = new_temp()
              E.C3D = E1.C3D + T.C3D
              + E.TMP + '=' + E1.TMP + '/' + T.TMP }
T -> F      { T.TMP = F.TMP
              T.C3D = F.C3D }
F -> ( E )  { F.TMP = E.TMP
              F.C3D = E.C3D }
F -> id     { F.TMP = id.lex_value
              F.C3D = '' }
```

Pruebas realizadas

Entrada:
```
a+b*c
```

Salida:
```
t1 = b * c
t2 = a + t1
```

---

Entrada:
```
(a+b)*(c-d)
```

Salida:
```
t1 = a + b
t2 = c - d
t3 = t1 * t2
```

---

Entrada:
```
(a+b)*c-d+a
```

Salida:
```
t1 = a + b
t2 = t1 * c
t3 = t2 - d
t4 = t3 + a
```

---

Entrada:
```
a+(b-d)*c
```

Salida:
```
t1 = b - d
t2 = t1 * c
t3 = a + t2
```

---

Entrada:
```
(a+(b-d)*c)*((a+b)*c-d+a)
```

Salida:
```
t1 = b - d
t2 = t1 * c
t3 = a + t2
t4 = a + b
t5 = t4 * c
t6 = t5 - d
t7 = t6 + a
t8 = t3 * t7
```

## Corto 2

Se agregaron expresiones relacionales a la gramática devolviendo su correspondiente en código en 3 direcciones.

Entrada:
```
a > b && c > d
```

Salida:
```
if a > b goto L1
goto L2
L1:
if c > d goto L3
goto L4
Etiquetas verdaderas:
['L3']
Etiquetas falsas:
['L2', 'L4']
```

---

Entrada:
```
a > b || c > d
```

Salida:
```
if a > b goto L1
goto L2
L2:
if c > d goto L3
goto L4
Etiquetas verdaderas:
['L1', 'L3']
Etiquetas falsas:
['L4']
```

---

Entrada:
```
!e > f
```

Salida:
```
if e > f goto L1
goto L2
Etiquetas verdaderas:
['L2']
Etiquetas falsas:
['L1']
```

---