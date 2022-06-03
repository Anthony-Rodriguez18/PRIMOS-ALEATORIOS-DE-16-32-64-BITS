# PRIMOS-ALEATORIOS-DE-16-32-64-BITS

En presente Repositorio se nos pidio crear numeros binarios primos de 16, 32 y 64 bits; donde utilizamos tres algoritmos que nos ayudaran para crear estos números un EXPMOD, COMPUESTO, MILLER_RABIN.

EXPMOD:La exponenciación modular para hallar el residuo de algun número de una gran cantidad de cifras (caso de 16bits a más), donde "y" toma el valor de exponente (donde su valor es p-1), "a" como base y "p" el número que comprobaremos durante el proceso de compuesto o no.

COMPUESTO:Para comprobar si el número es compuesto (valor false) mediante el residuo obtenido en caso que sea 1 o el numero que se comprueba menos 1 entonces descimos que es pseudo primo, luego comprueba si ese número lo divide en n-1 se considera pseudo.

MILLER:Utilizando el compuesto halla la fidelidad si el número es primo o no (teniendo en cuenta a los pseudoprimos) 

FINALIZANDO:
"for _ in iter(int, 1)" --> Es un iterador infinito por lo cual se pone un if y este cuando llegue el contador a 10 termine el bucle con un break.
"b = random.getrandbits(VALUE)" --> para generar numeros binarios de manera aleatoria, donde value toma la cantidad de bits utilizados.
Luego con "if (Miller(b, s))" se comprueba que si es primo con un seguridad dependiendo de S (En nuestro caso utilizamos 10 porque son menos numeros generados y la comprobacion de Miller demora casi el mismo tiempo que con 5). Posteriormente si da true el test ese valor lo imprime y en contador aumenta.
Este proceso se repite para 16, 32 y 64 bits.
