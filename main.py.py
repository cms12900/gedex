
import random

# --- MÓDULO DE APRENDIZAJE ---
preguntas_aprendizaje = [
    {"pregunta": "¿Cuál es la velocidad de detonación del TNT?", "opciones": ["6900 m/s", "3000 m/s", "8400 m/s"], "respuesta": "6900 m/s"},
    {"pregunta": "¿Qué explosivo tiene la sigla RDX?", "opciones": ["Ciclotrimetilenotrinitramina", "Trinitrotolueno", "Pentrita"], "respuesta": "Ciclotrimetilenotrinitramina"},
    {"pregunta": "¿Qué elemento es fundamental para iniciar un circuito eléctrico?", "opciones": ["Interruptor", "Batería", "Resistencia"], "respuesta": "Batería"},
    {"pregunta": "¿Qué significa C-4?", "opciones": ["Composición 4", "Carga Cuádruple", "Compuesto 4"], "respuesta": "Composición 4"},
    {"pregunta": "¿Qué medida de seguridad se aplica ante un artefacto con temporizador visible?", "opciones": ["Evacuación y robot", "Corte de energía", "Disparo controlado"], "respuesta": "Evacuación y robot"},
    {"pregunta": "¿Cuál es la función del detonador?", "opciones": ["Activar el explosivo", "Medir la onda expansiva", "Contener el explosivo"], "respuesta": "Activar el explosivo"},
    {"pregunta": "¿Qué tipo de explosivo se usa frecuentemente en minería?", "opciones": ["ANFO", "TNT", "PETN"], "respuesta": "ANFO"},
    {"pregunta": "¿Qué es el cordón detonante?", "opciones": ["Un tubo de gas", "Una mecha lenta", "Un explosivo lineal"], "respuesta": "Un explosivo lineal"},
    {"pregunta": "¿Cuál es el rango de seguridad mínimo ante una amenaza de artefacto?", "opciones": ["100 m", "300 m", "500 m"], "respuesta": "300 m"},
    {"pregunta": "¿Qué debe hacerse si hay un teléfono móvil en un artefacto sospechoso?", "opciones": ["Usar jammer", "Llamarlo", "Cortarlo"], "respuesta": "Usar jammer"},
]

def aprendizaje():
    score = 0
    seleccion = random.sample(preguntas_aprendizaje, 10)
    for i, p in enumerate(seleccion, 1):
        opciones = p['opciones'][:]
        random.shuffle(opciones)
        print(f"\nPregunta {i}: {p['pregunta']}")
        for idx, opcion in enumerate(opciones):
            print(f"  {idx + 1}. {opcion}")
        while True:
            try:
                eleccion = int(input("Elegí la opción correcta (1-3): "))
                if 1 <= eleccion <= len(opciones):
                    break
            except:
                continue
        if opciones[eleccion - 1] == p['respuesta']:
            print("✅ ¡Correcto!")
            score += 1
        else:
            print(f"❌ Incorrecto. La respuesta era: {p['respuesta']}")
    print(f"\nPuntaje final: {score}/10")


# --- MÓDULO DE RECONOCIMIENTO ---
objetos = [
    {
        "descripcion": "Cilindro metálico con espoleta roscada y número de serie grabado. Utilizado habitualmente por fuerzas armadas.",
        "opciones": ["Granada FMK-2", "AEI con caño PVC", "Mortero artesanal"],
        "respuesta": "Granada FMK-2"
    },
    {
        "descripcion": "Recipiente de plástico con cables pelados, teléfono móvil incrustado y cinta aislante negra. Sin marcas visibles.",
        "opciones": ["AEI activado por celular", "Granada ofensiva", "Carga hueca militar"],
        "respuesta": "AEI activado por celular"
    },
    {
        "descripcion": "Cartucho cilíndrico color beige con espoleta en nariz, comúnmente usado como carga para demolición.",
        "opciones": ["TNT militar", "AEI con clavos", "Pirotecnia improvisada"],
        "respuesta": "TNT militar"
    },
    {
        "descripcion": "Termo metálico adaptado con doble fondo, temporizador digital visible y baterías conectadas en serie.",
        "opciones": ["AEI con temporizador", "Granada fragmentaria", "Carga de demolición tradicional"],
        "respuesta": "AEI con temporizador"
    }
]

def reconocimiento():
    print("\n=== MÓDULO DE RECONOCIMIENTO DE OBJETOS ===")
    seleccion = random.sample(objetos, min(10, len(objetos)))
    score = 0
    for i, obj in enumerate(seleccion, 1):
        opciones = obj["opciones"][:]
        random.shuffle(opciones)
        print(f"\nObjeto {i}: {obj['descripcion']}")
        for idx, opcion in enumerate(opciones):
            print(f"  {idx+1}) {opcion}")
        while True:
            try:
                eleccion = int(input("Identificá el artefacto (1-3): "))
                if 1 <= eleccion <= 3:
                    break
            except:
                continue
        if opciones[eleccion - 1] == obj["respuesta"]:
            print("✅ ¡Correcto!")
            score += 1
        else:
            print(f"❌ Incorrecto. La respuesta era: {obj['respuesta']}")
    print(f"\nPuntaje final: {score}/{len(seleccion)}")


# --- MÓDULO DE SIMULACIÓN ---
circuitos = [
    {
        "circuito": "Batería — cable rojo — interruptor — detonador",
        "opciones": ["Cortar cable entre batería e interruptor", "Desconectar el detonador", "Unir cable rojo y negro"],
        "respuesta": "Cortar cable entre batería e interruptor"
    },
    {
        "circuito": "Celda — sensor de movimiento — relay — carga explosiva",
        "opciones": ["Eliminar relay", "Cortar conexión entre sensor y relay", "Tapar el sensor"],
        "respuesta": "Cortar conexión entre sensor y relay"
    },
    {
        "circuito": "Temporizador digital — transistor — carga — tierra",
        "opciones": ["Desconectar transistor", "Cortar cable a tierra", "Apagar el temporizador"],
        "respuesta": "Desconectar transistor"
    },
    {
        "circuito": "Teléfono móvil — placa — relé activador — detonador eléctrico",
        "opciones": ["Cortar conexión al relé", "Apagar el móvil", "Agregar resistencia a la placa"],
        "respuesta": "Cortar conexión al relé"
    }
]

def desactivacion():
    print("\n=== MÓDULO DE SIMULACIÓN DE DESACTIVACIÓN ===")
    seleccion = random.sample(circuitos, 3)
    score = 0
    for i, c in enumerate(seleccion, 1):
        opciones = c["opciones"][:]
        random.shuffle(opciones)
        print(f"\nCircuito {i}: {c['circuito']}")
        for j, opc in enumerate(opciones):
            print(f"  {j+1}) {opc}")
        while True:
            try:
                eleccion = int(input("Elegí cómo desactivar (1-3): "))
                if 1 <= eleccion <= 3:
                    break
            except:
                continue
        if opciones[eleccion - 1] == c["respuesta"]:
            print("✅ Acción correcta")
            score += 1
        else:
            print(f"❌ Incorrecta. La respuesta era: {c['respuesta']}")
    print(f"\nResultado final: {score}/3")


# --- MENÚ PRINCIPAL ---
def menu():
    while True:
        print("\n=== ENTRENAMIENTO INTERACTIVO GEDEX ===")
        print("1. Módulo de Aprendizaje")
        print("2. Reconocimiento de Objetos")
        print("3. Simulación de Desactivación")
        print("4. Salir")
        opcion = input("Seleccioná una opción: ")
        if opcion == "1":
            aprendizaje()
        elif opcion == "2":
            reconocimiento()
        elif opcion == "3":
            desactivacion()
        elif opcion == "4":
            print("¡Hasta la próxima!")
            break
        else:
            print("❗ Opción inválida.")

menu()
