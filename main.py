"""
Autor: Gabriel Alberto Paz González 221087
Descripción: Implementación interactiva de MTF e IMTF
             
"""
import re, datetime, pathlib, sys
from typing import List, Tuple
from colorama import init, Fore, Style
init(autoreset=True)

GREEN = Fore.GREEN + Style.BRIGHT
CYAN  = Fore.CYAN  + Style.BRIGHT
YELL  = Fore.YELLOW+ Style.BRIGHT
MAG   = Fore.MAGENTA + Style.BRIGHT
RESET = Style.RESET_ALL

# ──────────── UTILIDADES ──────────── #
def marco(titulo: str, ancho: int = 70):
    borde = "=" * ancho
    print(f"\n{MAG}{borde}")
    print(titulo.center(ancho))
    print(f"{borde}{RESET}")

def banner(txt: str):
    print(f"{CYAN}✨ {txt}{RESET}")

def parse_numbers(line: str) -> List[int]:
    nums = re.split(r'[,\s]+', line.strip())
    try:    return [int(n) for n in nums if n]
    except ValueError:  return []

# ──────────── COSTOS Y OPERACIONES ──────────── #
def cost_mtf(pos: int) -> int:
    return 2 * (pos + 1) - 1

def process_request(cfg: List[int], req: int, algo: str,
                    upcoming: List[int] = None) -> Tuple[int, str]:
    if req not in cfg:
        return 0, f"⚠️  {req} no está en la lista, solicitud omitida."
    pos = cfg.index(req)

    if algo == "MTF":
        cost = cost_mtf(pos)
        cfg.pop(pos); cfg.insert(0, req)
        line = f"🔎 {req:<2}| Pos {pos:<2}| Costo {cost:<2}| Mover: sí "
    else:                       
        lookahead = upcoming[:pos] if upcoming else []
        mover = req in lookahead
        if mover:
            cost = cost_mtf(pos)
            cfg.pop(pos); cfg.insert(0, req)
        else:
            cost = pos + 1
        movetxt = "sí" if mover else "no"
        line = f"🔎 {req:<2}| Pos {pos:<2}| Costo {cost:<2}| Mover: {movetxt}"
    return cost, line

# ──────────── CASOS PREDEFINIDOS ──────────── #
PRESETS: dict[int, Tuple[List[int], List[int]]] = {
    1: ([0,1,2,3,4],  [0,1,2,3,4]*4),
    2: ([0,1,2,3,4],  [4,3,2,1,0,1,2,3,4,3,2,1,0,1,2,3,4]),
    3: ([0,1,2,3,4],  [0]*20),          # mejor caso MTF
    4: ([0,1,2,3,4],  [4,3,2,1,0]*4),   # peor caso MTF
    5: ([0,1,2,3,4],  [2]*20),
    6: ([0,1,2,3,4],  [3]*20),
}

# ──────────── EJECUCIÓN DEL ALGORITMO ──────────── #
def run_algorithm(cfg: List[int], seq: List[int], algo: str,
                  log_lines: List[str] | None = None) -> int:
  
    total = 0
    log = log_lines.append if log_lines is not None else (lambda *_: None)

    banner(f"Ejecutando {algo} {'🐙' if algo=='MTF' else '🦄'}")
    for i, req in enumerate(seq):
        # Lista antes
        antes = f"{YELL}Lista antes →{RESET} {cfg}"
        print(antes)
        log(antes.replace(YELL, "").replace(RESET, ""))

        # Procesar solicitud
        upcoming = seq[i+1:]
        cost, linea = process_request(cfg, req, algo, upcoming)
        total += cost
        print(linea)
        log(linea)

        # Lista después
        despues = f"📦 Lista después → {cfg}\n"
        print(despues)
        log(despues.strip())

    resumen = f"{GREEN}Costo total {algo} ≡ {total}{RESET}"
    print(resumen)
    log(resumen.replace(GREEN, "").replace(RESET, ""))
    log("")
    return total

def export_log(lines: List[str], filename: str):
    out_dir = pathlib.Path("resultados")
    out_dir.mkdir(exist_ok=True)
    (out_dir / filename).write_text("\n".join(lines), encoding="utf-8")
    print(f"{CYAN}📝 Log guardado en resultados/{filename}{RESET}")

def elegir_preset() -> Tuple[List[int], List[int]]:
    banner("Casos disponibles 📚")
    for k in sorted(PRESETS):
        print(f"  {k}. Caso {k}")
    while True:
        try:    return [*map(list, PRESETS[int(input('Elige caso → '))])]
        except (ValueError, KeyError):
            print("Número inválido, intenta de nuevo.")

# ──────────── FUNCION MAIN ──────────── #
def main():
    while True:
        marco("🔥  PROYECTO 3 - LISTA AUTORGANIZABLE  🔥")
        print("1️⃣  Usar MTF (Move-To-Front)")
        print("2️⃣  Usar IMTF (Improved MTF)")
        print("3️⃣  Salir\n")

        try: op = int(input("Selecciona opción → "))
        except ValueError:   continue
        if op == 3:
            print("👋 ¡Gracias por usar el sistema!")
            break

        algorithm = "MTF" if op == 1 else "IMTF"

        while True:
            marco("📂  CONFIGURAR PRUEBA")
            print("1️⃣ Inputs personalizados")
            print("2️⃣ Inputs predefinidos")
            print("3️⃣ Regresar\n")
            try:    sub = int(input("Selecciona opción → "))
            except ValueError:   continue
            if sub == 3:   break

            if sub == 1:
                cfg = parse_numbers(input("Lista de configuración → "))
                seq = parse_numbers(input("Secuencia de solicitudes → "))
                if not cfg or not seq:
                    print("❌ Entrada inválida. Intenta de nuevo.")
                    continue
            else:
                cfg, seq = elegir_preset()

            run_algorithm(cfg.copy(), seq, algorithm)
            input(f"\n{CYAN}Presiona Enter para continuar…{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Interrumpido por usuario.")
        sys.exit(0)
