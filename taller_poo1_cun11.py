#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TALLER PRÁCTICO DE PROGRAMACIÓN ORIENTADA A OBJETOS 1
CUN - Corporación Unificada Nacional de Educación Superior

Niveles incluidos:
1. Técnico: Gestión de Inventario Pyme CUN (encapsulamiento y validaciones).
2. Tecnólogo: Sistema de Peaje Inteligente (herencia y polimorfismo).
3. Profesional: Plataforma de Inscripción Académica (composición/agregación y SRP).

Requisitos: Python 3. Sin dependencias externas.
"""

from abc import ABC, abstractmethod
from typing import List


# ============================================================================
# NIVEL 1: TÉCNICO — GESTIÓN DE INVENTARIO PYME CUN
# Conceptos POO: encapsulamiento, propiedades de acceso y validación de negocio.
# ============================================================================

class Producto:
    """Representa un producto con precio y stock sujetos a validación."""

    def __init__(self, codigo: str, nombre: str, precio: float, stock: int) -> None:
        self._codigo: str = codigo
        self.nombre: str = nombre  # Atributo público solicitado.
        self._precio: float = 0.0
        self._stock: int = 0
        self.precio = precio
        self.stock = stock

    @staticmethod
    def __validar_no_negativo(valor: float, nombre_campo: str) -> None:
        """
        Método privado con name mangling: Python transforma su nombre interno
        para reducir el riesgo de acceso accidental desde fuera de la clase.
        """
        if valor < 0:
            raise ValueError(f"El valor de {nombre_campo} no puede ser negativo.")

    @property
    def codigo(self) -> str:
        """Permite consultar el código sin exponerlo como atributo público."""
        return self._codigo

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio: float) -> None:
        self.__validar_no_negativo(nuevo_precio, "precio")
        self._precio = float(nuevo_precio)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock: int) -> None:
        if isinstance(nuevo_stock, bool) or not isinstance(nuevo_stock, int):
            raise TypeError("El stock debe ser un número entero.")
        self.__validar_no_negativo(nuevo_stock, "stock")
        self._stock = nuevo_stock

    def vender(self, cantidad: int) -> bool:
        """Vende unidades si hay stock suficiente; si no, informa el error."""
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("La cantidad a vender debe ser un número entero.")
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero.")
        if cantidad > self._stock:
            raise ValueError(
                f"Stock insuficiente para '{self.nombre}'. "
                f"Disponible: {self._stock}; solicitado: {cantidad}."
            )
        self._stock -= cantidad
        return True

    def __str__(self) -> str:
        return (
            f"Código: {self._codigo} | Nombre: {self.nombre} | "
            f"Precio: ${self._precio:,.2f} | Stock: {self._stock}"
        )


def probar_nivel_tecnico() -> None:
    """Ejecuta pruebas de funcionamiento y casos borde del nivel Técnico."""
    print("\n" + "=" * 76)
    print("NIVEL 1 — TÉCNICO: GESTIÓN DE INVENTARIO PYME CUN")
    print("=" * 76)

    producto = Producto("P-001", "Teclado", 75000, 10)
    print("Producto creado:")
    print(producto)

    print("\n[Prueba] Venta válida de 3 unidades:")
    producto.vender(3)
    print(f"Venta realizada. Stock restante: {producto.stock}")

    print("\n[Prueba de borde] Intentar asignar precio negativo:")
    try:
        producto.precio = -5000
    except ValueError as error:
        print(f"Validación correcta: {error}")

    print("\n[Prueba de borde] Intentar asignar stock negativo:")
    try:
        producto.stock = -2
    except ValueError as error:
        print(f"Validación correcta: {error}")

    print("\n[Prueba de borde] Intentar vender más unidades que las disponibles:")
    try:
        producto.vender(20)
    except ValueError as error:
        print(f"Validación correcta: {error}")

    print("\nEstado final del producto:")
    print(producto)


# ============================================================================
# NIVEL 2: TECNÓLOGO — SISTEMA DE PEAJE INTELIGENTE
# Conceptos POO: herencia, abstracción y polimorfismo.
# ============================================================================

class Vehiculo(ABC):
    """Clase base abstracta: define la interfaz común de los vehículos."""

    def __init__(self, placa: str, marca: str) -> None:
        self.placa: str = placa
        self.marca: str = marca

    @abstractmethod
    def calcular_peaje(self) -> float:
        """Cada tipo concreto de vehículo define su propia tarifa."""
        raise NotImplementedError("Las subclases deben calcular su peaje.")


class Moto(Vehiculo):
    TARIFA: float = 6500.0

    def calcular_peaje(self) -> float:
        return self.TARIFA


class Automovil(Vehiculo):
    TARIFA: float = 12000.0
    DESCUENTO_ELECTRICO: float = 0.20

    def __init__(self, placa: str, marca: str, es_electrico: bool) -> None:
        super().__init__(placa, marca)  # Reutilización del constructor padre.
        self.es_electrico: bool = es_electrico

    def calcular_peaje(self) -> float:
        if self.es_electrico:
            return self.TARIFA * (1 - self.DESCUENTO_ELECTRICO)
        return self.TARIFA


class Camion(Vehiculo):
    TARIFA_POR_EJE: float = 8500.0

    def __init__(self, placa: str, marca: str, numero_ejes: int) -> None:
        super().__init__(placa, marca)
        if isinstance(numero_ejes, bool) or not isinstance(numero_ejes, int):
            raise TypeError("El número de ejes debe ser un entero.")
        if numero_ejes <= 0:
            raise ValueError("El camión debe tener al menos un eje.")
        self.numero_ejes: int = numero_ejes

    def calcular_peaje(self) -> float:
        return self.TARIFA_POR_EJE * self.numero_ejes


def probar_nivel_tecnologo() -> None:
    """Demuestra el polimorfismo y presenta el recaudo total."""
    print("\n" + "=" * 76)
    print("NIVEL 2 — TECNÓLOGO: SISTEMA DE PEAJE INTELIGENTE")
    print("=" * 76)

    # Una sola lista contiene objetos de subclases diferentes.
    # La llamada calcular_peaje() se comporta según el tipo real del objeto.
    vehiculos: List[Vehiculo] = [
        Moto("ABC12D", "Yamaha"),
        Automovil("KLM234", "Renault", False),
        Automovil("ELC789", "BYD", True),
        Camion("TRK456", "International", 4),
        Moto("XYZ98A", "Honda"),
        Camion("PQR321", "Kenworth", 3),
    ]

    print(f"{'PLACA':<12} {'MARCA':<20} {'TIPO':<14} {'PEAJE':>14}")
    print("-" * 64)
    recaudo_total: float = 0.0

    for vehiculo in vehiculos:
        peaje: float = vehiculo.calcular_peaje()
        recaudo_total += peaje
        if isinstance(vehiculo, Moto):
            tipo = "Moto"
        elif isinstance(vehiculo, Automovil):
            tipo = "Automóvil eléctrico" if vehiculo.es_electrico else "Automóvil"
        elif isinstance(vehiculo, Camion):
            tipo = f"Camión ({vehiculo.numero_ejes} ejes)"
        else:
            tipo = "Vehículo"
        print(f"{vehiculo.placa:<12} {vehiculo.marca:<20} {tipo:<14} ${peaje:>12,.0f}")

    print("-" * 64)
    print(f"{'RECAUDO TOTAL':<48} ${recaudo_total:>12,.0f}")
    print("\nTarifas aplicadas:")
    print("- Moto: $6.500")
    print("- Automóvil: $12.000; eléctrico: 20 % de descuento ($9.600)")
    print("- Camión: $8.500 por cada eje")


# ============================================================================
# NIVEL 3: PROFESIONAL — PLATAFORMA DE INSCRIPCIÓN ACADÉMICA
# Conceptos POO: composición/agregación, encapsulamiento y responsabilidad
# única (SRP: cada clase tiene una responsabilidad principal).
# ============================================================================

class Materia:
    """Contiene los datos académicos de una materia."""

    def __init__(self, codigo: str, nombre: str, creditos: int) -> None:
        if not codigo.strip():
            raise ValueError("El código de la materia no puede estar vacío.")
        if not nombre.strip():
            raise ValueError("El nombre de la materia no puede estar vacío.")
        if isinstance(creditos, bool) or not isinstance(creditos, int):
            raise TypeError("Los créditos deben ser un número entero.")
        if creditos <= 0:
            raise ValueError("Una materia debe tener al menos un crédito.")
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.creditos: int = creditos

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.creditos} créditos)"


class Estudiante:
    """Contiene únicamente la información básica del estudiante."""

    def __init__(self, identificacion: str, nombre: str, programa: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.programa: str = programa


class Inscripcion:
    """Administra las materias asociadas a un estudiante."""

    MAX_CREDITOS: int = 18

    def __init__(self, estudiante: Estudiante) -> None:
        self.estudiante: Estudiante = estudiante
        # La inscripción mantiene referencias a objetos Materia (agregación).
        self._materias: List[Materia] = []

    @property
    def materias(self) -> List[Materia]:
        """Devuelve una copia para evitar cambios externos a la lista interna."""
        return self._materias.copy()

    @property
    def total_creditos(self) -> int:
        return sum(materia.creditos for materia in self._materias)

    def inscribir_materia(self, materia: Materia) -> bool:
        """Agrega una materia si no está duplicada ni excede el límite."""
        if not isinstance(materia, Materia):
            raise TypeError("Solo se pueden inscribir objetos de tipo Materia.")

        if any(actual.codigo == materia.codigo for actual in self._materias):
            raise ValueError(
                f"La materia '{materia.codigo}' ya está inscrita."
            )

        nuevo_total: int = self.total_creditos + materia.creditos
        if nuevo_total > self.MAX_CREDITOS:
            raise ValueError(
                f"No se puede inscribir '{materia.nombre}': el total sería "
                f"{nuevo_total} créditos y el máximo permitido es "
                f"{self.MAX_CREDITOS}."
            )

        self._materias.append(materia)
        return True

    def cancelar_materia(self, codigo_materia: str) -> bool:
        """Cancela una materia por código; devuelve False si no existe."""
        for indice, materia in enumerate(self._materias):
            if materia.codigo == codigo_materia:
                del self._materias[indice]
                return True
        return False

    def mostrar_resumen(self) -> None:
        print(f"Estudiante: {self.estudiante.nombre}")
        print(f"Identificación: {self.estudiante.identificacion}")
        print(f"Programa: {self.estudiante.programa}")
        print("Materias inscritas:")
        if not self._materias:
            print("  (No hay materias inscritas)")
        else:
            for materia in self._materias:
                print(f"  - {materia}")
        print(f"Total de créditos: {self.total_creditos}/{self.MAX_CREDITOS}")


def probar_nivel_profesional() -> None:
    """Prueba inscripción, límite de créditos, cancelación y reinscripción."""
    print("\n" + "=" * 76)
    print("NIVEL 3 — PROFESIONAL: PLATAFORMA DE INSCRIPCIÓN ACADÉMICA")
    print("=" * 76)

    estudiante = Estudiante("1020304050", "Laura Gómez", "Ingeniería de Sistemas")
    inscripcion = Inscripcion(estudiante)

    materias: List[Materia] = [
        Materia("POO101", "Programación Orientada a Objetos", 4),
        Materia("BD102", "Bases de Datos", 4),
        Materia("MAT103", "Matemáticas Discretas", 3),
        Materia("ING104", "Inglés Técnico", 3),
        Materia("RED105", "Redes de Computadores", 4),
        Materia("ETI106", "Ética Profesional", 2),
    ]

    print("\n[Prueba] Inscribir materias hasta intentar superar el máximo:")
    for materia in materias:
        try:
            inscripcion.inscribir_materia(materia)
            print(f"Inscrita: {materia.nombre}. "
                  f"Total: {inscripcion.total_creditos} créditos.")
        except ValueError as error:
            print(f"Inscripción rechazada: {error}")

    print("\nEstado después del intento de superar el límite:")
    inscripcion.mostrar_resumen()

    print("\n[Prueba] Cancelar la materia BD102:")
    if inscripcion.cancelar_materia("BD102"):
        print("Materia BD102 cancelada correctamente.")
    else:
        print("No se encontró la materia BD102.")

    print(f"Créditos después de cancelar: {inscripcion.total_creditos}")

    print("\n[Prueba] Reinscribir la materia que se canceló:")
    materia_bd = next(m for m in materias if m.codigo == "BD102")
    try:
        inscripcion.inscribir_materia(materia_bd)
        print("Materia BD102 reinscrita correctamente.")
    except ValueError as error:
        print(f"No fue posible reinscribir: {error}")

    print("\nResumen final de inscripción:")
    inscripcion.mostrar_resumen()

    print("\n[Prueba adicional] Cancelar una materia inexistente:")
    resultado: bool = inscripcion.cancelar_materia("NO-EXISTE")
    print(f"¿Se canceló alguna materia?: {resultado}")


# ============================================================================
# MENÚ PRINCIPAL
# ============================================================================

def mostrar_menu() -> None:
    """Presenta el menú de ejecución del taller."""
    while True:
        print("\n" + "=" * 76)
        print("TALLER POO 1 — CUN")
        print("Corporación Unificada Nacional de Educación Superior")
        print("=" * 76)
        print("1. Ejecutar Nivel Técnico")
        print("2. Ejecutar Nivel Tecnólogo")
        print("3. Ejecutar Nivel Profesional")
        print("4. Ejecutar todos los niveles")
        print("0. Salir")
        opcion: str = input("Seleccione una opción: ").strip()

        if opcion == "1":
            probar_nivel_tecnico()
        elif opcion == "2":
            probar_nivel_tecnologo()
        elif opcion == "3":
            probar_nivel_profesional()
        elif opcion == "4":
            probar_nivel_tecnico()
            probar_nivel_tecnologo()
            probar_nivel_profesional()
        elif opcion == "0":
            print("Gracias por utilizar el taller POO 1 de la CUN. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Ingrese 1, 2, 3, 4 o 0.")


if __name__ == "__main__":
    mostrar_menu()
