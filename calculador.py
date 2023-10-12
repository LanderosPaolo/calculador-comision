# Crear programa para calcular las comisiones de los trabajadores
    # La comision es del 13%

nombre = input('Ingresar nombre del trabajador: ')
venta = int(input('¿Cuanto vendio este mes?: '))
comision = round(venta * 0.13, 2)
total = venta + comision

print(f"El señor: {nombre}\nVendio: ${venta}\nSu comision es: ${comision}\nTotal a pagar: ${total}")