import os

class Color:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    BG_BLANCO = '\033[48;2;240;240;240m'
    BG_NEGRO = '\033[48;2;50;50;50m'
    
    TEXTO_ROJO = '\033[38;2;230;50;50m'
    TEXTO_BLANCO = '\033[38;2;255;255;255m'
    TEXTO_AMARILLO = '\033[38;2;255;215;0m'
    TEXTO_VERDE = '\033[38;2;46;204;113m'


class TableroDamasColor:
    def __init__(self):
        self.tablero = [
            ['.', '❌', '.', '❌', '.', '❌', '.', '❌'],
            ['❌', '.', '❌', '.', '❌', '.', '❌', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '⬜', '.', '⬜', '.', '⬜', '.', '⬜'],
            ['⬜', '.', '⬜', '.', '⬜', '.', '⬜', '.']
        ]
        self.turno = '⬜'

    def formatear_pieza(self, pieza, es_casilla_negra):
        bg = Color.BG_NEGRO if es_casilla_negra else Color.BG_BLANCO
        
        if pieza == '❌':
            return f"{bg}{Color.TEXTO_ROJO} ❌ {Color.RESET}"
        elif pieza == '⬜':
            return f"{bg}{Color.TEXTO_BLANCO} ⬜ {Color.RESET}"
        elif pieza == 'W':
            return f"{bg}{Color.TEXTO_AMARILLO}{Color.BOLD} W {Color.RESET}"
        elif pieza == 'K':
            return f"{bg}{Color.TEXTO_ROJO}{Color.BOLD} K {Color.RESET}"
        else:
            return f"{bg}   {Color.RESET}"

    def mostrar_tablero(self):
        print("\n     A  B  C  D  E  F  G  H")
        print("   ┌────────────────────────┐")
        
        for i, fila in enumerate(self.tablero):
            num_fila = 8 - i
            linea = f" {num_fila} │"
            
            for j, pieza in enumerate(fila):
                es_casilla_negra = (i + j) % 2 != 0
                linea += self.formatear_pieza(pieza, es_casilla_negra)
            
            linea += f"│ {num_fila}"
            print(linea)
            
        print("   └────────────────────────┘")
        print("     A  B  C  D  E  F  G  H\n")

    def notacion_a_coordenadas(self, notacion):
        if len(notacion) != 2:
            return None
        col_char, fila_char = notacion[0].upper(), notacion[1]
        cols = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        
        if col_char in cols and fila_char.isdigit():
            fila = 8 - int(fila_char)
            col = cols[col_char]
            if 0 <= fila <= 7:
                return fila, col
        return None

    def coordenadas_a_notacion(self, fila, col):
        cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        return f"{cols[col]}{8 - fila}"

    def es_reina(self, pieza):
        return pieza in ['W', 'K']

    def pertenece_a_jugador(self, pieza, jugador):
        if jugador == '⬜':
            return pieza in ['⬜', 'W']
        if jugador == '❌':
            return pieza in ['❌', 'K']
        return False

    def obtener_direcciones(self, pieza):
        if pieza == '⬜':
            return [-1]
        elif pieza == '❌':
            return [1]
        elif self.es_reina(pieza):
            return [-1, 1]
        return []

    def hay_capturas_obligatorias(self, jugador):
        enemigo = '❌' if jugador == '⬜' else '⬜'
        
        for f in range(8):
            for c in range(8):
                pieza = self.tablero[f][c]
                if self.pertenece_a_jugador(pieza, jugador):
                    direcciones = self.obtener_direcciones(pieza)
                    for df in direcciones:
                        for dc in [-1, 1]:
                            f_dest, c_dest = f + (2 * df), c + (2 * dc)
                            f_inter, c_inter = f + df, c + dc
                            if 0 <= f_dest <= 7 and 0 <= c_dest <= 7:
                                if (self.pertenece_a_jugador(self.tablero[f_inter][c_inter], enemigo) and 
                                    self.tablero[f_dest][c_dest] == '.'):
                                    return True
        return False

    def obtener_movimientos_validos(self, f, c):
        pieza = self.tablero[f][c]
        direcciones = self.obtener_direcciones(pieza)
        enemigo = '❌' if self.turno == '⬜' else '⬜'
        hay_obligacion = self.hay_capturas_obligatorias(self.turno)

        movimientos = {}

        for df in direcciones:
            for dc in [-1, 1]:
                dir_h = "Izquierda" if dc == -1 else "Derecha"
                
                es_avance_normal = (df == -1 and self.turno == '⬜') or (df == 1 and self.turno == '❌')
                dir_v = "" if not self.es_reina(pieza) else (" (Adelante)" if es_avance_normal else " (Atrás)")
                
                etiqueta_dir = f"{dir_h}{dir_v}"

                f_dest, c_dest = f + (2 * df), c + (2 * dc)
                f_inter, c_inter = f + df, c + dc
                if 0 <= f_dest <= 7 and 0 <= c_dest <= 7:
                    if (self.pertenece_a_jugador(self.tablero[f_inter][c_inter], enemigo) and 
                        self.tablero[f_dest][c_dest] == '.'):
                        movimientos[(f_dest, c_dest)] = (f"Comer hacia la {etiqueta_dir}", True)

                if not hay_obligacion:
                    f_dest_s, c_dest_s = f + df, c + dc
                    if 0 <= f_dest_s <= 7 and 0 <= c_dest_s <= 7:
                        if self.tablero[f_dest_s][c_dest_s] == '.':
                            movimientos[(f_dest_s, c_dest_s)] = (f"Mover a la {etiqueta_dir}", False)

        return movimientos

    def ejecutar_movimiento(self, f_orig, c_orig, f_dest, c_dest, es_captura):
        pieza = self.tablero[f_orig][c_orig]
        self.tablero[f_dest][c_dest] = pieza
        self.tablero[f_orig][c_orig] = '.'

        if es_captura:
            f_inter = (f_orig + f_dest) // 2
            c_inter = (c_orig + c_dest) // 2
            self.tablero[f_inter][c_inter] = '.'
            print(f"{Color.TEXTO_AMARILLO}Captura realizada en ({self.coordenadas_a_notacion(f_inter, c_inter)})!{Color.RESET}")

        self.verificar_promocion(f_dest, c_dest)
        self.cambiar_turno()

    def verificar_promocion(self, fila, col):
        pieza = self.tablero[fila][col]
        if pieza == '⬜' and fila == 0:
            self.tablero[fila][col] = 'W'
            print(f"{Color.TEXTO_AMARILLO}Una ficha Blanca se ha convertido en Reina (W)!{Color.RESET}")
        elif pieza == '❌' and fila == 7:
            self.tablero[fila][col] = 'K'
            print(f"{Color.TEXTO_AMARILLO}Una ficha Roja se ha convertido en Reina (K)!{Color.RESET}")

    def cambiar_turno(self):
        self.turno = '❌' if self.turno == '⬜' else '⬜'

    def obtener_movimientos_jugador(self, jugador):
        for f in range(8):
            for c in range(8):
                if self.pertenece_a_jugador(self.tablero[f][c], jugador):
                    if len(self.obtener_movimientos_validos(f, c)) > 0:
                        return True
        return False

    def verificar_fin_juego(self):
        piezas_b = sum(fila.count('⬜') + fila.count('W') for fila in self.tablero)
        piezas_r = sum(fila.count('❌') + fila.count('K') for fila in self.tablero)

        if piezas_b == 0:
            return True, "¡Las fichas ROJAS (❌) han ganado! (Blancas sin piezas)"
        if piezas_r == 0:
            return True, "¡Las fichas BLANCAS (⬜) han ganado! (Rojas sin piezas)"

        if not self.obtener_movimientos_jugador(self.turno):
            ganador = "Rojas (❌)" if self.turno == '⬜' else "Blancas (⬜)"
            return True, f"¡Las fichas {ganador} han ganado! (El rival no tiene movimientos)"

        return False, None


def jugar():
    os.system('')
    juego = TableroDamasColor()
    print(f"{Color.BOLD}=== TABLERO DE DAMAS (CON CAPTURA OBLIGATORIA) ==={Color.RESET}")
    print("Simbología: ⬜ = Blanca | ❌ = Roja | W = Reina Blanca | K = Reina Roja")
    
    while True:
        juego.mostrar_tablero()

        terminado, mensaje = juego.verificar_fin_juego()
        if terminado:
            print("===================================")
            print(f"{Color.TEXTO_AMARILLO}{Color.BOLD}{mensaje}{Color.RESET}")
            print("===================================")
            break

        print(f"Turno de las fichas: {'Blancas (⬜)' if juego.turno == '⬜' else 'Rojas (❌)'}")
        
        hay_que_comer = juego.hay_capturas_obligatorias(juego.turno)
        if hay_que_comer:
            print(f"{Color.TEXTO_AMARILLO}OBLIGATORIO COMER: Tienes una ficha en posición para capturar.{Color.RESET}")

        entrada_origen = input("Selecciona la ficha que deseas mover (ej. B2) o 'salir': ").strip().upper()
        
        if entrada_origen == 'SALIR':
            print("¡Gracias por jugar!")
            break

        coor_origen = juego.notacion_a_coordenadas(entrada_origen)
        if not coor_origen:
            print(f"{Color.TEXTO_ROJO}Casilla inválida. Ingresa un formato como 'B2'.{Color.RESET}")
            continue

        f_orig, c_orig = coor_origen
        pieza = juego.tablero[f_orig][c_orig]

        if not juego.pertenece_a_jugador(pieza, juego.turno):
            print(f"{Color.TEXTO_ROJO}Esa casilla no contiene una ficha tuya ('{juego.turno}').{Color.RESET}")
            continue

        movs_validos = juego.obtener_movimientos_validos(f_orig, c_orig)

        if not movs_validos:
            if hay_que_comer:
                print(f"{Color.TEXTO_ROJO}Esta ficha no puede comer. Debes seleccionar una ficha con la que PUEDAS COMER.{Color.RESET}")
            else:
                print(f"{Color.TEXTO_ROJO}Esta ficha no tiene movimientos disponibles.{Color.RESET}")
            continue

        print(f"\n{Color.TEXTO_VERDE}Posibles movimientos para {entrada_origen}:{Color.RESET}")
        for dest, (desc, _) in movs_validos.items():
            notacion_dest = juego.coordenadas_a_notacion(dest[0], dest[1])
            print(f"  • Casilla {notacion_dest} --> {desc}")

        entrada_destino = input(f"\nSelecciona la casilla destino para {entrada_origen} (o 'cancelar'): ").strip().upper()
        
        if entrada_destino == 'CANCELAR':
            print("Selección cancelada.")
            continue

        coor_destino = juego.notacion_a_coordenadas(entrada_destino)
        
        if coor_destino in movs_validos:
            desc, es_captura = movs_validos[coor_destino]
            f_dest, c_dest = coor_destino
            juego.ejecutar_movimiento(f_orig, c_orig, f_dest, c_dest, es_captura)
        else:
            print(f"{Color.TEXTO_ROJO}Movimiento no permitido. Elige una de las casillas sugeridas.{Color.RESET}")


if __name__ == "__main__":
    jugar()
