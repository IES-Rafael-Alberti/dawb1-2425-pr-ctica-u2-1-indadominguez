#Prueba programación

def comprobar_importe(valor: str) -> bool:
    
  if valor.isdigit():
         valor = valor.replace(',', '.')

            
    
  

    

    
        
    



def comprobar_comando(comando: str) -> bool:

    if comando.isdigit():
        comando = comando.replace(',', '.')





def mostrar_mensaje_error():
    
    while True:

    






def procesar_compra(saldo: float, importe: float) -> float:
    saldo = saldo - importe
    return saldo


def procesar_venta(saldo: float, importe: float) -> float:
    saldo = saldo + importe
    return saldo





def mostrar_saldo(capsys, saldo: float, cont_compras: int, cont_ventas: int):
    captured = capsys.redoutter()






def resetear_saldo(saldo: float, cont_compras: int, cont_ventas: int) -> tuple[float, int, int]:

saldo = 0
ventas = 0
cost_ventas = 0




def recuperar_comando_e_importe(linea: str) -> tuple[str, str]:







def main():
    encuentra_fin = False
    cont_compras = 0
    cont_ventas = 0
    saldo = 0






if __name__ == "__main__":
    main()