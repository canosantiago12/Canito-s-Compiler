# BTSPL - BangtanSonyeondan Progamming Language

<img
  src="./extra/jiminGIF.gif"
  alt="Alt text"
  title="Optional title"
  style="display: flex; margin: 0 auto; min-width: 600px; max-width: 700px">
<br />

***

## Manual de usuario

### Archivo de entrada

Los archivos de entrada de este lenguaje tienen la extensión **.bts**, comencemos por crear un
archivo **prueba.bts** para poder comenzar a programar.

### Estructura general

Para comenzar a programar es necesario que definamos un nombre del programa que vamos a crear. Para
esto podemos hacer uso de la palabra reservada <span style="color: #ff6b01; font-weight: bold">BTSProgram</span> seguido del nombre que deseamos utilizar
para este programa.

Además de esto es importante agregar la función principal con la palabra reservada <span style="color: #ff6b01; font-weight: bold">mainStage</span> y esta se encargará de guiar nuestro programa por completo.
```
BTSProgram ejemplo;

mainStage() {
    print("안녕하세요");
}
```

### Declaración de variables

***

Si eres nuevo en la programación es importante que aprendas que existen las variables en este y muchos otros lenguajes de programación.
En nuestro caso podemos definir variables de tipo <span style="color: #aa00e9; font-weight: bold">int</span>, <span style="color: #aa00e9; font-weight: bold">float</span>, <span style="color: #aa00e9; font-weight: bold">bool</span>, <span style="color: #aa00e9; font-weight: bold">string</span>.

Toda variable que desees agregar debe estar acompañada de la palabra reserbada <span style="color: #ff6b01; font-weight: bold">var</span>. ¡No lo olvides!

Estas variables pueden tener un valor asignado, pero es importante que le asignes dicho valor después de haberlas declarado con anterioridad:

```
BTSProgram ejemplo;

mainStage() {
    var string saludo;
    saludo = "안녕하세요";

    print(saludo);
}
```

### Arreglos

Puedes declarar arreglos globales y locales para trabajar y acceder las distintas posiciones del mismo de la siguiente manera:
```
BTSProgram ejemplo;

var float arr[5];

mainStage() {
    var float x;

    arr[2] = 2.5;
    x = 10 - arr[2];
}
```

### Uso de operadores

***

#### Operadores and y or (&& y ||)

BTSPL tiene la capacidad de aceptar operaciones de tipo and(<span style="color: #01c6bf; font-weight: bold">&&</span>) y or(<span style="color: #01c6bf; font-weight: bold">||</span>). Sientete con la libertad
de usarlos frecuentemente, solo recuerda usar el operador correcto.

#### Operadores <, <=, >, >=, ==, !=

BTSPL también soporta operaciones de tipo relacional como: <span style="color: #01c6bf; font-weight: bold"><</span>, <span style="color: #01c6bf; font-weight: bold"><=</span>, <span style="color: #01c6bf; font-weight: bold">></span>, <span style="color: #01c6bf; font-weight: bold">>=</span>, <span style="color: #01c6bf; font-weight: bold">==</span> y <span style="color: #01c6bf; font-weight: bold">!=</span>.

```
BTSProgram ejemplo;

mainStage() {
    var bool res;
    res = 2 < 5;

    print(res);
    # true
}
```

#### Operadores aritméticos

Como cualquier otro lenguaje básico de programción, puedes utilziar BTSPL para realizar todas las operaciones aritméticas básicas que conozcas:

- ( <span style="color: #01c6bf; font-weight: bold">+</span> ) Suma
- ( <span style="color: #01c6bf; font-weight: bold">-</span> ) Resta
- ( <span style="color: #01c6bf; font-weight: bold">*</span> ) Multiplicación
- ( <span style="color: #01c6bf; font-weight: bold">/</span> ) División
- ( <span style="color: #01c6bf; font-weight: bold">%</span> ) Módulo
- ( <span style="color: #01c6bf; font-weight: bold">^</span> ) Exponencial
    
### Estatutos condicionales

***

Una vez que identificaste estos operadores, debes recordar que son tus mejores aliados al momento de correr un estatuto condicional (<span style="color: #ff6b01; font-weight: bold">if</span>, <span style="color: #ff6b01; font-weight: bold">else if</span>, <span style="color: #ff6b01; font-weight: bold">else</span>) como se muestra en el ejemplo:

```
BTSProgram ejemplo;

mainStage() {
    var int x, y;
    x = 2;
    y = 7;
    if(x > y) {
        print("안녕");
    } else {
        print("안녕하세요");
    }
}
```

### Ciclos

***

También puedes hacer uso de ciclos de tipo <span style="color: #ff6b01; font-weight: bold">while</span> para realizar muchas cosas diferentes y expandir las capacidades de tus programas.

```
BTSProgram ejemplo;

mainStage() {
    var int i;
    i = 0;
    
    while(i < 10) {
        print("사랑해");
        i = i + 1;
    }
}
```

### Declaración y llamada de variables

***

Si te das cuenta que hay una sección de código que se repite demasiado, puedes probar crear una función que te ayude a ahorrate tiempo para no tener que repetir el mismo código en distintas partes del programa.

```
BTSProgram ejemplo;

func imprimeJunto(string x, string y) {
    print(x, y);
}

mainStage() {
    var string nombre, apellido;

    listen(nombre, apellido);
    imprimeJunto(nombre, apellido);
}
```

Solo recuerda que es importante que tengas en cuenta el tipo de variable que estás creando y si necesita regresar o no un valor.

### Ejecución del programa
***

Para ejecutar nuestro programa solo debemos correr la siguiente línea de código en la consola:
```
python parser.py archivo.bts
```

***
<img
  src="./extra/vGIF.gif"
  alt="Alt text"
  title="Optional title"
  style="display: flex; margin: 0 auto; min-width: 400px; max-width: 500px">