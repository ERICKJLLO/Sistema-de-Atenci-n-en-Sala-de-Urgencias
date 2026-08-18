# Sistema de Atención en Sala de Urgencias

Este proyecto implementa una simulación de atención de pacientes en una sala de urgencias utilizando listas doblemente enlazadas en Python. La idea principal es gestionar pacientes con diferentes categorías y niveles de prioridad, aplicando operaciones sobre la estructura de datos para ordenar, aislar, depurar e intercambiar elementos según reglas específicas.

## Descripción del proyecto

El sistema trabaja con pacientes representados por la clase `Paciente`, donde cada registro incluye:

- `id_paciente`: identificador del paciente
- `categoria`: categoría del paciente (`tercera_edad`, `adulto`, `pediatria`)
- `nivel_triage`: nivel de prioridad del paciente

La lógica del proyecto se basa en una lista doblemente enlazada (`dlinkedlist`) que permite:

- agregar pacientes al inicio o final,
- buscar por ID,
- eliminar elementos,
- mover pacientes según prioridad,
- aislar un bloque de nodos,
- reordenar elementos según reglas de urgencia,
- intercalar dos listas.

## Estructura de archivos

- `main.py`: contiene la lógica principal del sistema y ejecuta los puntos solicitados.
- `paciente.py`: define la clase `Paciente`.
- `nodo.py`: define la clase `NodeD` para los nodos de la lista.
- `lista_doblemente_enlazada.py`: implementa la lista doblemente enlazada con sus operaciones.
- `README.md`: documentación del proyecto.

## Cómo ejecutar

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta el siguiente comando:

```bash
python main.py
```

3. El programa mostrará en consola la salida de cada punto del ejercicio, mostrando cómo cambia la lista en cada etapa.

## Funcionalidades principales

### 1. Construcción de la lista base
Se crea una lista inicial con pacientes de diferentes categorías y niveles de triage.

### 2. Prioridad para tercera edad
Se mueve al inicio a los pacientes de `tercera_edad` con triage 1.

### 3. Depuración de adultos
Se eliminan los pacientes adultos con nivel de triage mayor a 3.

### 4. Aislamiento de un bloque
Se separa un tramo de la lista comprendido entre dos IDs específicos.

### 5. Inversión condicional
Si la cantidad de pacientes de `pediatria` supera a la de `adulto`, la lista se invierte.

### 6. Reordenamiento por prioridad
La lista se reorganiza según la categoría y el nivel de triage.

### 7. Intercalado de listas
Se toma una lista derivada y se intercalan sus nodos en la lista principal en proporción 2:1.

## Requisitos

- Python 3.x
- No se requieren librerías externas.

## Observaciones

Este proyecto es una práctica de estructuras de datos, especialmente de listas doblemente enlazadas, donde se trabaja con la manipulación de nodos y la lógica de ordenamiento según condiciones específicas.
