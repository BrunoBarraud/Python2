"""
   Final AyED
    08/02/2023
    
    Algoritmo caculador de distancia entre centros de orificios alineados y de díametro variable
    ---
    
    Se quiere confeccionar un guardador de mechas de acero rápido. Las mechas 
    son de diferentes diámetros, que van de 1mm a 13mm. Se las quiere guardar
    de forma lineal y separadas 1cm una de la otra entre sus perímetros. Las 
    presentaciones comerciales vienen cada 0.25mm.
    
    Realizar un algoritmo que calcule la distancia entre centros de mecha tal que
    cumple la distancia entre ellas. Las mechas se guardan ordenadas por diámetro.
    
    Algoritmo debe servir tambien para guardar X cantidad de caños de diferentes
    diámetros.    
    
    1) Diseñar un generardor de todas las mechas. Precios aleatoreos.
    2) Ordenarlas de menor a mayor según precio y mostrar por pantalla.
    3) Implementar una función que haga el cálculo distancia entre centros y 
       la longitud total del contenedor.
    4) Implementar una función para calcular el precio máx, mín y promedio.
"""

import random

class Mecha:
    diametro = 0
    precio = 0
    def __init__(self, d):
        self.diametro = d
        self.precio = 0

    def crear_mechas(self, mechas):
        mechas = []
        for i in range(1, 14):
            mecha = Mecha(i)
            mecha.precio = random.randint(1, 1000)
            mechas.append(mecha)
        return mechas
    
    def mostrar_mechas(self, mechas):
        for mecha in mechas:
            print("Diametro: ", mecha.diametro, "mm", "Precio: $", mecha.precio)

    def ordenar_precio(self, mechas):
        aux = []
        for i in range(len(mechas) - 1):
            for j in range(i + 1, len(mechas)):
                if mechas[i].precio > mechas[j].precio:
                    aux = mechas[i]
                    mechas[i] = mechas[j]
                    mechas[j] = aux
        return mechas
    
    def ordenar_diametro(self, mechas):
        aux = []
        for i in range(len(mechas) - 1):
            for j in range(i + 1, len(mechas)):
                if mechas[i].diametro > mechas[j].diametro:
                    aux = mechas[i]
                    mechas[i] = mechas[j]
                    mechas[j] = aux
        return mechas
    
    def ordenar_diametro_precio(self, mechas):
        aux = []
        for i in range(len(mechas) - 1):
            for j in range(i + 1, len(mechas)):
                if mechas[i].diametro > mechas[j].diametro:
                    aux = mechas[i]
                    mechas[i] = mechas[j]
                    mechas[j] = aux
                elif mechas[i].diametro == mechas[j].diametro:
                    if mechas[i].precio > mechas[j].precio:
                        aux = mechas[i]
                        mechas[i] = mechas[j]
                        mechas[j] = aux
        return mechas
    
    def calcular_distancia(self, mechas):
        distancia = 0
        for mecha in mechas:
            distancia += mecha.diametro
        return distancia
    
    def calcular_precio(self, mechas):
        maximo = 0
        minimo = 1001
        promedio = 0
        suma = 0
        for mecha in mechas:
            if mecha.precio > max:
                maximo = mecha.precio
            if mecha.precio < min:
                minimo = mecha.precio
            suma += mecha.precio
        promedio = suma / len(mechas)
        precio_total = suma
        return max, min, promedio, precio_total        
    
    def menu():
        print("Bienvenido al programa de mechas")
        print("Ingrese la cantidad de mechas que desea crear")
        cantidad = int(input())
        mechas = []
        mecha = mecha(0)
        mechas = mecha.crear_mechas(mechas)
        print("Mechas creadas")
        print("Ingrese la opcion que desea realizar")
        print("1. Mostrar mechas")
        print("2. Ordenar por precio")
        print("3. Ordenar por diametro")
        print("4. Ordenar por diametro y precio")
        print("5. Calcular distancia")
        print("6. Calcular precio")
        print("Cualquier otra opcion para salir")
        opcion = int(input())
        if opcion == 1:
            mecha.mostrar_mechas(mechas)
        elif opcion == 2:
            mecha.ordenar_precio(mechas)
            mecha.mostrar_mechas(mechas)
        elif opcion == 3:
            mecha.ordenar_diametro(mechas)
            mecha.mostrar_mechas(mechas)
        elif opcion == 4:
            mecha.ordenar_diametro_precio(mechas)
            mecha.mostrar_mechas(mechas)
        elif opcion == 5:
            distancia = mecha.calcular_distancia(mechas)
            print("La distancia total es: ", distancia)
        elif opcion == 6:
            maximo, minimo, promedio, precio_total = mecha.calcular_precio(mechas)
            print("El precio maximo es: ", maximo)
            print("El precio minimo es: ", minimo)
            print("El precio promedio es: ", promedio)
            print("El precio total es: ", precio_total)
        else:
            print("Gracias por usar el programa")

    menu()

# $mechas = [];

# function crearMechas(){
#     global $mechas;
#     for ($i=1; $i<=13; $i++){
#         $mecha = new Mecha($i);
#         $mecha->precio = rand(1, 1000);
#         $mechas[] = $mecha;
#     }
# }

# function mostrarMechas(){
#     global $mechas;
#     foreach($mechas as $mecha){
#         echo "Diametro: " . $mecha->diametro . "mm " . "Precio: $" . $mecha->precio . "\n"; 
#     }
# }
    


# function ordenarPrecio(){
#     global $mechas;
#     $aux = [];
#     for($i=0; $i<count($mechas)-1; $i++){
#         for($j=$i+1; $j<count($mechas); $j++){
#             if($mechas[$i]->precio > $mechas[$j]->precio){
#                 $aux = $mechas[$i];
#                 $mechas[$i] = $mechas[$j];
#                 $mechas[$j] = $aux;
#             }
#         }
#     }
# }

# function ordenarDiametro(){
#     global $mechas;
#     $aux = [];
#     for($i=0; $i<count($mechas)-1; $i++){
#         for($j=$i+1; $j<count($mechas); $j++){
#             if($mechas[$i]->diametro > $mechas[$j]->diametro){
#                 $aux = $mechas[$i];
#                 $mechas[$i] = $mechas[$j];
#                 $mechas[$j] = $aux;
#             }
#         }
#     }
#     echo "\n";
#     echo "Ordenado por diametro: \n";
#     echo "\n";
#     mostrarMechas();


# }

# function calcularDistancia(){
#     global $mechas;
#     $distancia = 0;
#     foreach ($mechas as $mecha){
#         $distancia += $mecha->diametro;
#     }
#     echo "\n";
#     echo "Distancia entre centros: " . $distancia . "mm" . "\n";
# }


# function calcularPrecio(){
#     global $mechas;
#     $max = 0;
#     $min = 1001;
#     $promedio = 0;
#     $suma = 0;
#     foreach($mechas as $mecha){
#         if($mecha->precio > $max){
#             $max = $mecha->precio;
#         }
#         if($mecha->precio < $min){
#             $min = $mecha->precio;
#         }
#         $suma += $mecha->precio;
#     }

#     $promedio = $suma / count($mechas);
#     $precioTotal = $suma;

#     echo "\n";
#     echo "Precio máximo: $" . $max . "\n";
#     echo "\n";
#     echo "Precio mínimo: $" . $min . "\n";
#     echo "\n";
#     echo "Precio promedio: $" . round($promedio, 2) . "\n";
#     echo "\n";
#     echo "Precio total: $" . $precioTotal . "\n";
# }


# crearMechas();
# echo "\n";
# ordenarPrecio();
# mostrarMechas();
# echo "\n";
# ordenarDiametro();
# calcularPrecio();
# echo "\n";
# calcularDistancia();