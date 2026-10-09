Actúa como un Desarrollador Senior y Profesor Experto en Programación Orientada a Objetos (POO) en Python.

Necesito que generes un único archivo de código ejecutable en Python 3 que resuelva de manera completa y estructurada el taller práctico de la asignatura Programación Orientada a Objetos 1 de la CUN (Corporación Unificada Nacional de Educación Superior).

---
### 1. REQUISITOS GENERALES Y LENGUAJE:
- Lenguaje: Python 3 (haciendo uso de typing, super(), name mangling y la librería nativa abc).
- Formato de entrega: Todo el código debe estar unificado en un solo script (.py).
- Estructura visual: Usar separadores claros e imprimibles para delimitar cada sección.
- Interacción: Incluir un menú interactivo mediante consola al final del archivo (if __name__ == "__main__":) que permita al usuario elegir ejecutar el Nivel Técnico, Tecnólogo, Profesional, todos a la vez, o salir.

---
### 2. DATOS DE ENTRADA Y NIVELES A IMPLEMENTAR:

#### NIVEL 1: TÉCNICO - Gestión de Inventario Pyme CUN
- Pilares: Encapsulamiento y Validaciones de Negocio.
- Datos/Estructura:
  - Crear la clase `Producto`.
  - Atributos privados: `_codigo`, `_precio` y `_stock`. Atributo público: `nombre`.
  - Getters y Setters: Implementar métodos para acceder y modificar `precio` y `stock`, validando expresamente que NO se permitan valores negativos.
  - Método de negocio: `vender(cantidad)` que descuente del stock si hay disponibilidad suficiente o lance un mensaje de error en caso contrario.
  - Método de prueba: Incluir una función `probar_nivel_tecnico()` con instanciación de productos y pruebas de caso borde (precios negativos y stock insuficiente).

#### NIVEL 2: TECNÓLOGO - Sistema de Peaje Inteligente
- Pilares: Herencia y Polimorfismo.
- Datos/Estructura:
  - Superclase base `Vehiculo` con atributos `placa` y `marca`, y un método base `calcular_peaje()`.
  - Subclase `Moto`: Hereda de `Vehiculo`. Implementa tarifa fija ($6,500).
  - Subclase `Automovil`: Hereda de `Vehiculo`. Incluye el atributo `es_electrico` y aplica tarifa de $12,000 con un 20% de descuento si es eléctrico.
  - Subclase `Camion`: Hereda de `Vehiculo`. Incluye el atributo `numero_ejes` y calcula la tarifa a $8,500 por cada eje.
  - Método de prueba: Incluir una función `probar_nivel_tecnologo()` que recorra una lista polimórfica de vehículos, calcule los peajes e imprima una tabla con el recaudo total.

#### NIVEL 3: PROFESIONAL - Plataforma de Inscripción Académica
- Pilares: Composición/Agregación y Principio de Responsabilidad Única (SRP).
- Datos/Estructura:
  - Clase `Materia` con `codigo`, `nombre` y `creditos`.
  - Clase `Estudiante` con `identificacion`, `nombre` y `programa`.
  - Clase `Inscripcion` que contenga un `Estudiante` y una lista de objetos `Materia`.
  - Reglas de negocio: Constante `MAX_CREDITOS = 18`. Métodos `inscribir_materia(materia)` (valida que no se duplique ni exceda los 18 créditos) y `cancelar_materia(codigo_materia)` (elimina de forma segura).
  - Método de prueba: Incluir una función `probar_nivel_profesional()` que demuestre la adición de materias hasta sobrepasar el tope, la cancelación de una materia y la reinscripción posterior.

---
### 3. FORMATO Y ESTILO DE CÓDIGO SOLICITADO:
- Comentarios explicativos en el código señalando los conceptos POO aplicados.
- Tipado de datos claro (`-> float`, `-> bool`, `: str`, `: int`).
- Mención explícita a la CUN en el encabezado del archivo.
