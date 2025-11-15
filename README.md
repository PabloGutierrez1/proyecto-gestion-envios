# Proyecto: Sistema de Gestión de Envíos y Logística

Este es un proyecto universitario desarrollado en Python para simular la gestión de una empresa de envíos instantáneos.

## Descripción

El programa permite administrar dos entidades principales: Repartidores y Envíos. El sistema puede registrar nuevos repartidores y nuevos envíos, asignando un repartidor disponible a cada envío.

Una funcionalidad clave es el cálculo dinámico del costo de envío, que se basa en el peso del paquete y aplica un descuento progresivo. Además, permite modificar el estado de un envío (En tránsito, Entregado, No entregado) y listar todos los envíos registrados.

## Funcionalidades Principales

* Registro y gestión de Repartidores.
* Registro de Envíos con datos de remitente y receptor.
* Asignación de repartidores a envíos.
* Función de cálculo de costos (`calc_cost`) con lógica de descuentos.
* Modificación de estado de los envíos.
* Listado de todos los envíos registrados.

## Tecnologías Utilizadas

* **Python:**
    * Funciones (para modularizar el código).
    * Estructuras de datos (Listas de Diccionarios) para almacenar la información.
    * Manejo de lógica de negocio compleja.
