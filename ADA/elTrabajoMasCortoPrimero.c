#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <stdbool.h>

#define NUM_TRANSACCIONES 4

// Datos de las transacciones
int t_ids[NUM_TRANSACCIONES] = {1, 2, 3, 4};//Es el numero de cada transicion su id
char* t_nombres[NUM_TRANSACCIONES] = {"Deposito", "Retiro", "Transferencia", "Consulta"};
int t_duracion[NUM_TRANSACCIONES] = {3, 5, 2, 1}; // Duracion en segundos
int t_llegada[NUM_TRANSACCIONES] = {0, 1, 2, 3};  // Tiempos de llegada corregidos
int t_finalizacion[NUM_TRANSACCIONES]; // Para registrar cuando termina cada transacción

// Variables de estado
int t_restante[NUM_TRANSACCIONES];// Tiempo que falta por ejecutar
bool t_completada[NUM_TRANSACCIONES];// Si ya terminó
bool t_lista[NUM_TRANSACCIONES];// Si ya llegó al sistema

// Sincronizacion
int tiempo_global = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;

// Inicializar transacciones
void init_transacciones() {
    for(int i = 0; i < NUM_TRANSACCIONES; i++) {
        t_restante[i] = t_duracion[i];
        t_completada[i] = false;
        t_lista[i] = false;
    }
}

// Mostrar estado actual
void mostrar_estado() {
    printf("\n[t=%d] Estado actual:\n", tiempo_global);
    printf("--------------------------------\n");
    printf("Transaccion\tEstado\t\tTiempo Restante\n");
    printf("--------------------------------\n");
    
    for(int i = 0; i < NUM_TRANSACCIONES; i++) {
        if(t_llegada[i] <= tiempo_global) {
            printf("%s %d\t\t%s\t\t%d\n", 
                   t_nombres[i], t_ids[i],
                   t_completada[i] ? "Completada" : 
                   t_lista[i] ? "Lista" : "Esperando", 
                   t_restante[i]);
        }
    }
    printf("--------------------------------\n");
}

// Hilo de transacci髇 (CORREGIDO)
void* transaccion_thread(void* arg) {
    int id = *(int*)arg;
    int idx = id - 1;
    
    pthread_mutex_lock(&mutex);
    // Esperar hasta el tiempo de llegada exacto
    while(tiempo_global < t_llegada[idx]) {
        pthread_cond_wait(&cond, &mutex);
    }
    
    t_lista[idx] = true;
    printf("[t=%d] %s %d ha llegado al sistema\n", tiempo_global, t_nombres[idx], id);
    pthread_cond_broadcast(&cond);
    
    // Esperar a ser completada
    while(!t_completada[idx]) {
        pthread_cond_wait(&cond, &mutex);
    }
    
    pthread_mutex_unlock(&mutex);
    return NULL;
}

// Algoritmo SJF (Shortest Job First) - Versi髇 corregida
void sjf_bancario() {
    printf("\n=== SISTEMA BANCARIO CON SJF ===\n");
    printf("=== (Shortest Job First) ===\n\n");
    init_transacciones();
    
    pthread_t threads[NUM_TRANSACCIONES];
    int ids[NUM_TRANSACCIONES];
    
    // Crear hilos para cada transaccion
    for(int i = 0; i < NUM_TRANSACCIONES; i++) {
        ids[i] = t_ids[i];
        pthread_create(&threads[i], NULL, transaccion_thread, &ids[i]);
    }
    
    int completadas = 0;
    
    while(completadas < NUM_TRANSACCIONES) {
        pthread_mutex_lock(&mutex);
        mostrar_estado();
        
        // Buscar transaccion mas corta lista

        //aqui se evalúa cada segundo entre todos los procesos que ya han llegado (t_lista[i]) y selecciona el más corto disponible

        int seleccionada = -1;
        int menor_duracion = 999;
        
        for(int i = 0; i < NUM_TRANSACCIONES; i++) {
            if(!t_completada[i] && t_lista[i] && t_restante[i] < menor_duracion) {
                seleccionada = i;
                menor_duracion = t_restante[i];
            }
        }
        
        if(seleccionada != -1) {
            printf(">> EJECUTANDO: %s %d (%d segundos restantes)\n", 
                   t_nombres[seleccionada], t_ids[seleccionada], 
                   t_restante[seleccionada]);
            
            // Restar 1 segundo al tiempo restante
            t_restante[seleccionada]--;
            
            if(t_restante[seleccionada] == 0) {
                t_completada[seleccionada] = true;
                t_finalizacion[seleccionada] = tiempo_global + 1; // <- ESTA LÍNEA ES NUEVA
                completadas++;
                printf(">> COMPLETADO: %s %d en t=%d\n", 
                       t_nombres[seleccionada], t_ids[seleccionada], 
                       tiempo_global + 1);
            }
        }
        
        tiempo_global++;
        pthread_cond_broadcast(&cond);
        pthread_mutex_unlock(&mutex);
        sleep(1); // Simular 1 segundo de ejecuci髇
    }
    
    // Esperar a que terminen todos los hilos
    for(int i = 0; i < NUM_TRANSACCIONES; i++) {
        pthread_join(threads[i], NULL);
    }

    // Calcular y mostrar el tiempo promedio de respuesta
    calcular_tiempo_promedio();
}

// Calcular tiempo promedio de respuesta
void calcular_tiempo_promedio() {
    // 1. Crear copia del arreglo original
    int duraciones_ordenadas[NUM_TRANSACCIONES];
    for(int i = 0; i < NUM_TRANSACCIONES; i++) {
        duraciones_ordenadas[i] = t_duracion[i];
    }

    // 2. Ordenar la copia con algoritmo burbuja
    for(int i = 0; i < NUM_TRANSACCIONES-1; i++) {
        for(int j = 0; j < NUM_TRANSACCIONES-i-1; j++) {
            if(duraciones_ordenadas[j] > duraciones_ordenadas[j+1]) {
                // Intercambiar elementos
                int temp = duraciones_ordenadas[j];
                duraciones_ordenadas[j] = duraciones_ordenadas[j+1];
                duraciones_ordenadas[j+1] = temp;
            }
        }
    }

    // 3. Mostrar los tiempos ordenados
    printf("\nTiempos de ejecucion ordenados: ");
    for(int i = 0; i < NUM_TRANSACCIONES; i++) {
        printf("%d ", duraciones_ordenadas[i]);
    }
    printf("\n");

    // 4. Aplicar la fórmula exacta (4a + 3b + 2c + d)/4
    double promedio = (4*duraciones_ordenadas[0] + 
                       3*duraciones_ordenadas[1] + 
                       2*duraciones_ordenadas[2] + 
                       1*duraciones_ordenadas[3]) / 4.0;

    printf("Tiempo promedio ponderado: %.2f\n", promedio);
    printf("(Formula: (4*%d + 3*%d + 2*%d + 1*%d)/4)\n",
           duraciones_ordenadas[0], duraciones_ordenadas[1],
           duraciones_ordenadas[2], duraciones_ordenadas[3]);
}

void ordenar_burbuja(int arr[], int n) {
    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < n-i-1; j++) {
            if(arr[j] > arr[j+1]) {
                // Intercambiar elementos
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    printf("==== SIMULADOR DE SISTEMA BANCARIO ====\n");
    printf("Algoritmo de planificaci髇: SJF (Shortest Job First)\n\n");
    
    sjf_bancario();
    
    printf("\n=== TODAS LAS TRANSACCIONES COMPLETADAS ===\n");
    return 0;
}
