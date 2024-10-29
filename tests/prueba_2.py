
def __init__(self):
        self.saldo = 0
        self.transacciones = []
def comprobar_importe(self, importe):
        return importe > 0
def comprobar_comando(self, comando):
        return comando in ['compra', 'venta', 'saldo', 'resetear', 'recuperar', 'salir']

def mostrar_mensaje_error(self, mensaje):
        print(f"Error: {mensaje}")

def procesar_compra(self, importe):
        if self.comprobar_importe(importe):
            self.saldo -= importe
            self.transacciones.append(-importe)
            print(f"Compra procesada: -{importe}. Saldo actual: {self.saldo}")
        else:
            self.mostrar_mensaje_error("El importe de la compra debe ser mayor que cero.")

def procesar_venta(self, importe):
        if self.comprobar_importe(importe):
            self.saldo += importe
            self.transacciones.append(importe)
            print(f"Venta procesada: +{importe}. Saldo actual: {self.saldo}")
        else:
            self.mostrar_mensaje_error("El importe de la venta debe ser mayor que cero.")

def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

def resetear_saldo(self):
        self.saldo = 0
        self.transacciones = []
        print("Saldo y transacciones han sido reiniciados.")

def recuperar_saldo(self):
        print(f"Saldo recuperado: {self.saldo}")

def ejecutar(self):
        while True:
            comando = input("Ingrese un comando (compra, venta, saldo, resetear, recuperar, salir): ").strip().lower()
            if comando == 'salir':
                print("Saliendo del programa.")
                break
            elif comando == 'compra':
                importe = float(input("Ingrese el importe de la compra: "))
                self.procesar_compra(importe)
            elif comando == 'venta':
                importe = float(input("Ingrese el importe de la venta: "))
                self.procesar_venta(importe)
            elif comando == 'saldo':
                self.mostrar_saldo()
            elif comando == 'resetear':
                self.resetear_saldo()
           

    
