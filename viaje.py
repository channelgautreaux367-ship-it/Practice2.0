def exchange_money(budget, exchange_rate):
    """
    Fórmula: Moneda Extranjera = Presupuesto / Tasa de Cambio
    Esta función cumple con el ejemplo del mandato: 300 / 0.0075 = 40000
    """
    return budget / exchange_rate

# Sección de pruebas con datos reales
print("--- CALCULADORA DE DIVISAS PARA VIAJEROS ---")

try:
    # Pedimos los datos al usuario
    monto = float(input("Cantidad de dinero en moneda original (budget): "))
    tasa = float(input("Tasa de cambio (valor de 1 unidad extranjera en tu moneda): "))

    # Llamada a la función
    resultado = exchange_money(monto, tasa)

    print("-" * 30)
    print(f"El equivalente es: {resultado:,.2f}")
    print("-" * 30)

except ValueError:
    print("Error: Por favor, ingresa solo números (usa punto para decimales).")
except ZeroDivisionError:
    print("Error: La tasa de cambio no puede ser cero.")

    