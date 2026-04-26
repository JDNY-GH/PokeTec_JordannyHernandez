import tkinter                  #Biblioteca Tkinter
from time import sleep          #Controlar tiempos
from PIL import Image, ImageTk  #Para tener más opciones de edición de imágenes
from random import choice       #Elecciones aleatorias para el bot
from copy import deepcopy       #Para diccionario anidados (pkDefaultStats y gameStats)

import tkinter
#|||Código para la aplicación|||

#Variables globales

IsPlayerTurn = True



pkDefaultStats = {
    "Don Elmer": {
        "HP": 100,
        "ATQ": 50,
        "DEF": 30,
        "DEFEX": 0},
    "Rodrigo Chaves": {
        "HP": 120,
        "ATQ": 40,
        "DEF": 50,
        "DEFEX": 0},
    "BB7": {
        "HP": 80,
        "ATQ": 60,
        "DEF": 20,
        "DEFEX": 0},
    "Diego Garro": {
        "HP": 90,
        "ATQ": 55,
        "DEF": 25,
        "DEFEX": 0},
    "Porcionzón": {
        "HP": 110,
        "ATQ": 45,
        "DEF": 40,
        "DEFEX": 0},
    "Ignacio Santos": {
        "HP": 95,
        "ATQ": 65,
        "DEF": 15,
        "DEFEX": 0},
    "Edgar Silva": {
        "HP": 85,
        "ATQ": 70,
        "DEF": 10,
        "DEFEX": 0},
    "Jerry Alfaro": {
        "HP": 105,
        "ATQ": 35,
        "DEF": 45,
        "DEFEX": 0},
    "Araya Vlogs": {
        "HP": 115,
        "ATQ": 30,
        "DEF": 55,
        "DEFEX": 0},
    "Corney": {
        "HP": 75,
        "ATQ": 80,
        "DEF": 5,
        "DEFEX": 0}
}

listaPokemones = ["Don Elmer", "Rodrigo Chaves", "BB7", "Diego Garro", "Porcionzón", "Ignacio Santos", "Edgar Silva", "Jerry Alfaro", "Araya Vlogs", "Corney"]
gameStats = deepcopy(pkDefaultStats)



def img(path, x, y):
    Imagen = ImageTk.PhotoImage(Image.open(f"Img/{path}").resize((x, y)))
    return Imagen

class registroClasificacion:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje
    
    #Función para leer la clasificación desde el archivo de texto
    def leerClasificacion():
        with open("Data/scoreboard.txt", "r") as file:
            lineas = file.readlines()
            
            return
            clasificacion = []
            for linea in lineas:
                nombre, puntaje = linea.strip().split(",")
                clasificacion.append(registroClasificacion(nombre, int(puntaje)))
            #Ordenar la clasificación de mayor a menor puntaje
            clasificacion.sort(key=lambda x: x.puntaje, reverse=True)
            return clasificacion

class bot:
    def __init__(self, nombre, avatar, equipo):
        self.nombre = nombre
        self.avatar = avatar
        self.pk = equipo
        self.currentPk

    def nombreBot(self):
        #Elegir aleatoriamente el nombre del bot
        nombre = choice(["Alfa", "Beta", "Gamma", "Delta", "Epsilon"])
        nombre = nombre + str(choice(range(1, 100)))  # Agregar un número aleatorio al nombre para hacerlo único
        return nombre
    def avtarBot(self):
        #Cargar la imagen del avatar aleatorio del bot
        avt = choice(["av0", "av1", "av2", "av3", "av4"])
        #avtImage = ImageTk.PhotoImage(Image.open(f"Img/{avt}.png").resize((300, 300), Image.Resampling.LANCZOS))
        return avt
    def equipoBot(self):
        #Elegir aleatoriamente el equipo de pokemones del bot sin repetir
        equipo = []
        for _ in range(3):
            pk = choice(list(pkDefaultStats.keys()))
            while pk in equipo or pk in jugador.pk: #Evalúa si ya tiene un Pokemon igual en su equipo o en el del jugador
                pk = choice(list(pkDefaultStats.keys()))
            equipo.append(pk)
        return equipo

class jugador:
    def __init__(self, nombre, avatar, equipo):
        self.nombre = nombre
        self.avatar = avatar
        self.pk = equipo #Esto es una tupla con los nombres de los pokemones seleccionados por el jugador, se asigna al iniciar la partida
        self.currentPk #Índice del pokemon actual en batalla, se incrementa cada vez que el pokemon actual es derrotado
    

def TESTFUNCTION():
    print("\n\n\n\n\n\n\n\n\n\n-------------PRUEBA-------------\n")
    print(f"Lista de pokemones del JUGADOR: {jugador.pk}")
    print(f"Pokemon en uso de JUGADOR: {jugador.currentPk}\n")
    
    print(f"Pokemon en uso de BOT: {bot.currentPk}")
    print(f"Lista de pokemones del BOT: {bot.pk}")
    
    
    print("DATOS POR DEFECTO-----\n")
    print(f"Estadisticas del Pokemon de JUGADOR por defecto: ATQ({pkDefaultStats[jugador.currentPk]['ATQ']})  DEF({pkDefaultStats[jugador.currentPk]['DEF']})  HP({pkDefaultStats[jugador.currentPk]['HP']})")
    print(f"Estadisticas del Pokemon BOT por defecto: ATQ({pkDefaultStats[bot.currentPk]['ATQ']})  DEF({pkDefaultStats[bot.currentPk]['DEF']})  HP({pkDefaultStats[bot.currentPk]['HP']})")
    print("\nDATOS EN BATALLA------\n")
    print(f"Estadisticas del Pokemon de JUGADOR en turno ATQ({gameStats[jugador.currentPk]['ATQ']})  DEF({gameStats[jugador.currentPk]['DEF']})  HP({gameStats[jugador.currentPk]['HP']})  +DEF({gameStats[jugador.currentPk]['DEFEX']})")
    print(f"Estadisticas del Pokemon de BOT en turno ATQ({gameStats[bot.currentPk]['ATQ']})  DEF({gameStats[bot.currentPk]['DEF']})  HP({gameStats[bot.currentPk]['HP']})  +DEF({gameStats[bot.currentPk]['DEFEX']})")



#Acciones de jugador y bot




    # Ahora puedes acceder a L_AvtCont a través de la instancia
    # Ejemplo: instance.L_AvtCont.config(text="Avatar seleccionado")  # O lo que necesites hacer con él
    
    # Para actualizar el canvas con la imagen (basado en tu línea comentada):
    #image = instance.controller.Img(f"Img/{avt}.png", (300, 300))  # Asumiendo que controller es accesible; ajusta si es necesario
    #instance.C_AvtSeleccionado.create_image(150, 150, anchor="center", image=image)


#Funciones para la batalla

def intercambiarPK(ganador, perdedor):
    perdedor.pk.remove(perdedor.currentPk)      #Remover el Pokemon derrotado del equipo del perdedor
    ganador.pk.append(perdedor.currentPk)       #Añadir el Pokemon derrotado al equipo del ganador

    gameStats[ganador.pk[-1]]["HP"] = pkDefaultStats[ganador.pk[-1]]["HP"]      #Restaurar la vida del Pokemon añadido


    if len(perdedor.pk) == 0:
        #Victoria para el ganador
        return

    perdedor.currentPk = perdedor.currentPk[0]  #Establecer el primer Pokemon del equipo del perdedor como Pokemon en uso
    




def cambiarPk(JB):
    lastIndex = len(JB.pk) -1
    nextPk = JB.pk.index(JB.currentPk)
    nextPk += 1

    if nextPk > lastIndex:
        nextPk = 0

    JB.currentPk = JB.pk[nextPk]
    cambiarPk

def calcularFortaleza(CurrentPk):
    #Todos los pokemones incrementan su defensa en 20% de su defensa base cuando utilizan la habilidad DEFENDER
    global gameStats
    fortaleza = pkDefaultStats[CurrentPk]["DEF"]
    fortaleza = round(fortaleza * 0.2)

    return fortaleza


def calcularDaño(CurrentPk, RivalCurrentPk):
    #Resta el ataque del jugador con la defensa base y extra del rival

    CurrentPkAtq = gameStats[CurrentPk]["ATQ"]
    RivalCurrentPkDef = gameStats[RivalCurrentPk]["DEF"]

    DefExtra = gameStats[RivalCurrentPk]["DEFEX"]
    dañoReal = (CurrentPkAtq - DefExtra) - RivalCurrentPkDef
    DefExtraRestante = DefExtra - CurrentPkAtq

    if dañoReal < 0:
        dañoReal = 0
    
    if DefExtraRestante < 0:
        DefExtraRestante = 0

    gameStats[RivalCurrentPk]["DEFEX"] = DefExtraRestante


    return dañoReal
        

def calcularCura(currentPk):
    vidaMax = pkDefaultStats[currentPk]["HP"]
    cura =  round(vidaMax * 0.2)
    return cura



def turnoBot(controller):
    sleep(2)
    global IsPlayerTurn
    global gameStats

    game_frame = controller.ventanas[game]

    #Elegir entre Defender, Atacar, Curar o Cambiar pokemon actual
    acc = choice(["DEF", "ATQ", "HP", "CH"])

    sleep(2)
    if acc == "CH":
        cambiarPk(bot)
        game_frame.C_PkBot.delete("all")

        game_frame.botPkImg = img(f"pk{listaPokemones.index(bot.currentPk)}.png", 200, 200)
        game_frame.C_PkBot.create_image(0, 0, anchor="nw", image=game_frame.botPkImg)
        game_frame.L_PkBotName.configure(text=f"{bot.nombre}:   {bot.currentPk}")

        Hp = gameStats[bot.currentPk]["HP"]
        Atq = gameStats[bot.currentPk]["ATQ"]
        Def = gameStats[bot.currentPk]["DEF"]
        DefEx = gameStats[bot.currentPk]["DEFEX"]
        game_frame.BcurrentPkHP.set(f"HP: {Hp}")
        game_frame.BcurrentPkATQ.set(f"ATQ: {Atq}")
        game_frame.BcurrentPkDEF.set(f"DEF: {Def}")
        game_frame.BcurrentPkDEFEx.set(f"+DEF: {DefEx}")

        game_frame.L_BotInfo.configure(text=f"{bot.nombre} cambió a {bot.currentPk}!")
        turnoBot(controller)
        return
    
    currentPk = bot.currentPk
    
    
    #Defensa
    if acc == "DEF":
        gameStats[currentPk]["DEFEX"] += calcularFortaleza(currentPk)

        #Cambios gráficos
        DefEx = gameStats[currentPk]["DEFEX"]
        game_frame.PcurrentPkDEFEx.set(f"+DEF: {DefEx}")

        game_frame.L_BotInfo.configure(text=f"{bot.currentPk} ha incrementado su defensa! +{gameStats[bot.currentPk]['DEFEX']} DEF por 1 turno")
    
    #Ataque
    if acc == "ATQ":
        daño = calcularDaño(currentPk, jugador.currentPk)

        if daño == 0:
            game_frame.L_BotInfo.configure(text=f"{bot.currentPk} ha atacado a {jugador.currentPk} pero no le hizo daño!")
            gameStats[jugador.currentPk]["DEFEX"] = 0
            game_frame.PcurrentPkDEFEx.set(f"+DEF: {gameStats[jugador.currentPk]['DEFEX']}")    
            IsPlayerTurn = True
            return
        
        HpRestante = gameStats[jugador.currentPk]["HP"] - daño

        if HpRestante < 0:
            gameStats[jugador.currentPk]["HP"] = 0
            game_frame.L_BotInfo.configure(text=f"{bot.currentPk} ha derrotado a {jugador.currentPk}, {jugador.currentPk} ahora le pertenece a {bot.nombre}!")
            sleep(2)
            #intercambiarPk(jugador, bot)
        
        else:
            gameStats[jugador.currentPk]["HP"] = HpRestante
            game_frame.L_BotInfo.configure(text=f"{bot.currentPk} ha atacado a {jugador.currentPk} causando {daño} de daño!")
        
        game_frame.PcurrentPkHP.set(f"HP: {gameStats[jugador.currentPk]['HP']}")
        game_frame.PcurrentPkDEFEx.set(f"+DEF: {gameStats[jugador.currentPk]['DEFEX']}")
    
    #Cura
    if acc == "HP":
        cura = calcularCura(currentPk)
        vidaActual = gameStats[currentPk]["HP"]
        vidaMax = pkDefaultStats[currentPk]["HP"]

        curacionPk = vidaActual + cura

        if curacionPk > vidaMax:
            gameStats[currentPk]["HP"] = vidaMax
            game_frame.PcurrentPkHP.set(f"HP: {gameStats[currentPk]['HP']}")
            game_frame.L_BotInfo.configure(text=f"{bot.currentPk} se ha curado por completo!")
        else:
            gameStats[currentPk]["HP"] += cura
            game_frame.PcurrentPkHP.set(f"HP: {gameStats[currentPk]['HP']}")
            game_frame.L_BotInfo.configure(text=f"{bot.currentPk} se ha curado por {cura} HP!")
    
    gameStats[jugador.currentPk]["DEFEX"] = 0
    game_frame.PcurrentPkDEFEx.set(f"+DEF: {gameStats[jugador.currentPk]['DEFEX']}")

    IsPlayerTurn = True
        

def turnoJugador(acc, controller):
    global IsPlayerTurn
    global gameStats
    global PlayerExtraDEF
    
    game_frame = controller.ventanas[game]
    

    if not IsPlayerTurn:
        return
    
    if acc == "CH":
        cambiarPk(jugador)
        game_frame.C_PkJugador.delete("all")
        
        #Cambios gráficos
        game_frame.jugadorPkImg = img(f"pk{listaPokemones.index(jugador.currentPk)}.png", 200, 200)
        game_frame.C_PkJugador.create_image(0, 0, anchor="nw", image=game_frame.jugadorPkImg)
        game_frame.L_PkPlayerName.configure(text=f"{jugador.nombre}:   {jugador.currentPk}")


        Hp = gameStats[jugador.currentPk]["HP"]
        Atq = gameStats[jugador.currentPk]["ATQ"]
        Def = gameStats[jugador.currentPk]["DEF"]
        DefEx = gameStats[jugador.currentPk]["DEFEX"]
        game_frame.PcurrentPkHP.set(f"HP: {Hp}")
        game_frame.PcurrentPkATQ.set(f"ATQ: {Atq}")
        game_frame.PcurrentPkDEF.set(f"DEF: {Def}")
        game_frame.PcurrentPkDEFEx.set(f"+DEF: {DefEx}")

        game_frame.L_PlayerInfo.configure(text=f"{jugador.nombre} cambió a {jugador.currentPk}!")

        #game_frame
        return

    IsPlayerTurn = False
    currentPk = jugador.currentPk
    



    #Defensa
    if acc == "DEF":
        gameStats[currentPk]["DEFEX"] = calcularFortaleza(currentPk)

        #Cambios gráficos
        DefEx = gameStats[currentPk]["DEFEX"]

        game_frame.PcurrentPkDEFEx.set(f"+DEF: {DefEx}")

        game_frame.L_PlayerInfo.configure(text=f"{jugador.currentPk} ha incrementado su defensa! +{gameStats[jugador.currentPk]['DEFEX']} DEF por 1 turno")

    
    #Ataque
    if acc == "ATQ":
        daño = calcularDaño(currentPk, bot.currentPk)
        
        if daño == 0:
            game_frame.L_PlayerInfo.configure(text=f"{jugador.currentPk} ha atacado a {bot.currentPk} pero no le hizo daño!")
            gameStats[bot.currentPk]["DEFEX"] = 0
            game_frame.BcurrentPkDEFEx.set(f"+DEF: {gameStats[bot.currentPk]['DEFEX']}")
            sleep(2)
            return turnoBot(controller)

        HpRestante = gameStats[bot.currentPk]["HP"] - daño

        if HpRestante < 0:
            gameStats[bot.currentPk]["HP"] = 0
            game_frame.L_PlayerInfo.configure(text=f"{jugador.currentPk} ha derrotado a {bot.currentPk}, {bot.currentPk} ahora le pertenece a {jugador.nombre}!")
            sleep(2)
            #intercambiarPK(jugador, bot)                                       #Si la vida del bot llega a 0, pasarlo al jugador
            game_frame.C_PkJugador.delete("all")
            game_frame.jugadorPkImg = img(f"pk{listaPokemones.index(bot.currentPk)}.png", 200, 200)
            game_frame.C_PkJugador.create_image(0, 0, anchor="nw", image=game_frame.jugadorPkImg)

            game_frame.L_PkPlayerName.configure(text=f"{jugador.nombre}:   {bot.currentPk}")
            game_frame.PcurrentPkHP.set(f"HP: {gameStats[currentPk]['HP']}")
            game_frame.PcurrentPkATQ.set(f"ATQ: {gameStats[currentPk]['ATQ']}")
            game_frame.PcurrentPkDEF.set(f"DEF: {gameStats[currentPk]['DEF']}")
            game_frame.PcurrentPkDEFEx.set(f"+DEF: {gameStats[currentPk]['DEFEX']}")
        else:
            gameStats[bot.currentPk]["HP"] = HpRestante
            game_frame.L_PlayerInfo.configure(text=f"{jugador.currentPk} ha atacado a {bot.currentPk} causando {daño} de daño!")
        

       
    
    #Cura
    if acc == "HP":
        cura = calcularCura(currentPk)
        vidaActual = gameStats[currentPk]["HP"]
        vidaMax = pkDefaultStats[currentPk]["HP"]

        curacionPk = vidaActual + cura

        if curacionPk > vidaMax :
            gameStats[currentPk]["HP"] = vidaMax
            game_frame.PcurrentPkHP.set(f"HP: {gameStats[currentPk]['HP']}")
            game_frame.L_PlayerInfo.configure(text=f"{jugador.currentPk} se ha curado por completo!")
        else:
            gameStats[currentPk]["HP"] += cura
            game_frame.L_PlayerInfo.configure(text=f"{jugador.currentPk} se ha curado por {cura} HP!")

    gameStats[bot.currentPk]["DEFEX"] = 0
    game_frame.BcurrentPkDEFEx.set(f"+DEF: {gameStats[bot.currentPk]['DEFEX']}")


    game_frame.BcurrentPkHP.set(f"HP: {gameStats[bot.currentPk]['HP']}")
    game_frame.BcurrentPkDEFEx.set(f"+DEF: {gameStats[bot.currentPk]['DEFEX']}")
    
    
    turnoBot(controller)
    

    


























#|||Estructura de la aplicación|||

#Cargar Imagen



class root(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title("TicoMon")
        self.state("zoomed")
        self.configure(bg="blue")
    


        #Contenedor dentro de root para mostrar las ventanas
        self.contenedor = tkinter.Frame(self, background="black")
        self.contenedor.pack(expand=True, fill="both")

        #Diccionario para almacenar las ventanas
        self.ventanas = {}

        #Bucle para crear las ventanas y almacenarlas en el diccionario
        for F in (main, selecAvt, selecPk, game, result, clasif):
            ventana = F(self.contenedor, self)
            self.ventanas[F] = ventana
            ventana.grid(row=0, column=0, sticky="nsew")
        
        # Configurar pesos para que el frame ocupe todo el espacio
        self.contenedor.grid_rowconfigure(0, weight=1)
        self.contenedor.grid_columnconfigure(0, weight=1)
        
        #Mostrar la ventana inicial
        self.mostrar_ventana(main)

    #Función para mostrar la primera ventana
    def mostrar_ventana(self, ventana):
        registroClasificacion.leerClasificacion()
        ventana = self.ventanas[ventana]
        ventana.tkraise()

#imagenes = {
#    "MainTitle.png": ImageTk.PhotoImage(Image.open("Img/MainTitle.png").resize((800,300)))
#}



#---------------------------------------------------------------------------------------

#                   VENTANA DE SELECCIÓN DE POKEMON

#---------------------------------------------------------------------------------------




class main(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        #Imagenes utilizadas en el frame
        self.MainTitle = img("MainTitle.png", 800, 330)


        self.mainCont = tkinter.Label(self, bg="#C4EAFF", borderwidth=0)
        self.mainCont.pack(expand=True, fill="both") 
        self.mainCont.columnconfigure(0, weight=1)
        self.mainCont.rowconfigure(0, weight=1)
        self.mainCont.rowconfigure(1, weight=1)
        self.mainCont.rowconfigure(2, weight=1)
        self.mainCont.rowconfigure(3, minsize=100)

        self.C_Titulo = tkinter.Canvas(self.mainCont, bg="#C4EAFF", width=800, height=330, highlightthickness=0)
        self.C_Titulo.create_image(0, 0, anchor="nw", image=self.MainTitle)
        self.C_Titulo.grid(column=0, row=0, sticky="ns")

        self.B_BotonJugar = tkinter.Button(self.mainCont, text="¡Adelante!", bg="#54C3FF", fg="white", relief="flat", height=1, width=10, font=("", 50), padx=10, pady=10, cursor="hand2", command=lambda: controller.mostrar_ventana(selecAvt))
        self.B_BotonJugar.grid(column=0, row=1)

        self.B_BotonClasificacion = tkinter.Button(self.mainCont, text="Clasificación",  bg="#54C3FF", fg="white", relief="flat", height=1, width=10, font=("", 50), padx=10, pady=10, cursor="hand2", command=lambda: controller.mostrar_ventana(clasif))
        self.B_BotonClasificacion.grid(column=0, row=2)

        #Label inferior de la ventana principal
        self.L_LabelInferior = tkinter.Label(self.mainCont, bg="#fcef7d", borderwidth=0)
        self.L_LabelInferior.columnconfigure(0, weight=1)
        self.L_LabelInferior.columnconfigure(1, weight=1)
        self.L_LabelInferior.rowconfigure(0, weight=1)
        self.L_LabelInferior.grid(column=0, row=3, sticky="nswe")

        #Widgets dentro del label inferior
        self.L_Creditos = tkinter.Label(self.L_LabelInferior, text="Por: Jordanny Hernández", fg="white", font=("", 20), bg="#0059ff")
        self.L_Creditos.grid(column=0, row=0, sticky="nsw")



#---------------------------------------------------------------------------------------

#                   VENTANA DE SELECCIÓN DE AVATAR

#---------------------------------------------------------------------------------------

def obtenerNombreJugador(event, controller):
    if jugador.avatar == "":
        return  # No hacer nada si no se ha seleccionado un avatar
    if event.get() == "":
        return  # No hacer nada si el campo de texto está vacío
    jugador.nombre = event.get()
    controller.mostrar_ventana(selecPk)  # Cambia a la ventana de selección de Pokémon
    

prevImgSelec = ""

class selecAvt(tkinter.Frame):

    

    def __init__(self, parent, controller):
        super().__init__(parent)

        #Imagenes utilizadas en el frame
        self.av0_Img = img("av0.png", 300, 300)
        self.av1_Img = img("av1.png", 300, 300)
        self.av2_Img = img("av2.png", 300, 300)
        self.av3_Img = img("av3.png", 300, 300)
        self.av4_Img = img("av4.png", 300, 300)

        self.mainCont = tkinter.Label(self, background="yellow", borderwidth=0)
        self.mainCont.pack(expand=True, fill="both")
        self.mainCont.columnconfigure(0, weight=1)
        self.mainCont.rowconfigure(0, minsize=100)
        self.mainCont.rowconfigure(1, weight=1)
        self.L_AvtCont = tkinter.Label(self.mainCont, bg="#8BC6FE", borderwidth=0)
        #self.L_AvtCont.pack_propagate(False)
        self.L_AvtCont.grid(column=0, row=0, sticky="nswe")

        #Botones de avatares
        self.B_Avt0 = tkinter.Button(self.L_AvtCont, text="AV0", bg="#fff79b", relief="flat", image=self.av0_Img, cursor="hand2", command=lambda: avatarSeleccionado("av0", self.av0_Img))
        self.B_Avt0.pack(side="left", fill="both", expand=True)
        self.B_Avt1 = tkinter.Button(self.L_AvtCont, text="AV1", bg="#75f5fe", relief="flat", image=self.av1_Img, cursor="hand2", command=lambda: avatarSeleccionado("av1", self.av1_Img))
        self.B_Avt1.pack(side="left", fill="both", expand=True)
        self.B_Avt2 = tkinter.Button(self.L_AvtCont, text="AV2", bg="#fccd81", relief="flat", image=self.av2_Img, cursor="hand2", command=lambda: avatarSeleccionado("av2", self.av2_Img))
        self.B_Avt2.pack(side="left", fill="both", expand=True)
        self.B_Avt3 = tkinter.Button(self.L_AvtCont, text="AV3", bg="#6efec0", relief="flat", image=self.av3_Img, cursor="hand2", command=lambda: avatarSeleccionado("av3", self.av3_Img))
        self.B_Avt3.pack(side="left", fill="both", expand=True)
        self.B_Avt4 = tkinter.Button(self.L_AvtCont, text="AV4", bg="#3e948f", relief="flat", image=self.av4_Img, cursor="hand2", command=lambda: avatarSeleccionado("av4", self.av4_Img))
        self.B_Avt4.pack(side="left", fill="both", expand=True)

        self.L_r1Cont = tkinter.Label(self.mainCont, bg="#554CFF", borderwidth=0)
        self.L_r1Cont.grid(column=0, row=1, sticky="nswe")

        self.C_AvtSeleccionado = tkinter.Canvas(self.L_r1Cont, width=300, height=300, bg="lightblue")
        self.C_AvtSeleccionado.pack(side="left", padx=20)

        self.L_NombreTitulo = tkinter.Label(self.L_r1Cont, text="Nombre del jugador", font=("", 20), fg="white", bg="#39BAFF")
        self.L_NombreTitulo.pack(anchor="center", side="left", padx=10, ipadx=10)

        self.E_NombreJugador = tkinter.Entry(self.L_r1Cont, width=20, font=("", 20))
        self.E_NombreJugador.pack(anchor= "center", side="left", padx=10)

        self.B_Volver = tkinter.Button(self.mainCont, text="Volver", font=("", 30), fg="white", bg="red", relief="flat", width=7, cursor="hand2", command=lambda: controller.mostrar_ventana(main))
        self.B_Volver.place(anchor="sw", rely=1, x=0, y=0)

        self.B_Siguiente = tkinter.Button(self.mainCont, text="Siguiente", font=("", 30), fg="white", bg="green", relief="flat", width=7, cursor="hand2", command=lambda: obtenerNombreJugador(self.E_NombreJugador, controller))
        self.B_Siguiente.place(anchor="se", relx=1, rely=1, x=0, y=0)

        
        
        #Funcion para definir el avatar y cambiar la imagen del avatar seleccionado en el canvas
        def avatarSeleccionado(avt, img):
            jugador.avatar = avt
            self.C_AvtSeleccionado.delete("all")
            self.C_AvtSeleccionado.create_image(0, 0, anchor="nw", image= img)



#---------------------------------------------------------------------------------------

#                   VENTANA DE SELECCIÓN DE POKEMON

#---------------------------------------------------------------------------------------



class selecPk(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        #Las imagenes utilizadas se cargan al seleccionar el pokemon


        self.mainCont = tkinter.Label(self, background="#554CFF", borderwidth=0)
        self.mainCont.pack(expand=True, fill="both")

        #Contenedor para el equipo de pokemones
        self.L_ContPk0 = tkinter.Label(self.mainCont, bg="#ff7979", borderwidth=0, height=40)
        self.L_ContPk0.pack(side="left", fill="x", expand=True)
        self.L_ContPk0.pack_propagate(False)
        self.L_ContPk1 = tkinter.Label(self.mainCont, bg="#92ffaf", borderwidth=0, height=40)
        self.L_ContPk1.pack(side="left", fill="x", expand=True)
        self.L_ContPk1.pack_propagate(False)
        self.L_ContPk2 = tkinter.Label(self.mainCont, bg="#91fff9", borderwidth=0, height=40)
        self.L_ContPk2.pack(side="left", fill="x", expand=True)
        self.L_ContPk2.pack_propagate(False)
        

        self.C_Pk0 = tkinter.Canvas(self.L_ContPk0, width=300, height=300, bg="lightblue")
        self.C_Pk0.pack(side="top", pady=20)
        self.LB_Pk0 = tkinter.Listbox(self.L_ContPk0, height=5, listvariable=tkinter.StringVar(value=listaPokemones))
        self.LB_Pk0.bind("<<ListboxSelect>>", lambda event: self.pkSeleccionado(event, 0))
        self.LB_Pk0.pack(side="top", fill="x", padx=20)

        self.C_Pk1 = tkinter.Canvas(self.L_ContPk1, width=300, height=300, bg="lightblue")
        self.C_Pk1.pack(side="top", pady=20)
        self.LB_Pk1 = tkinter.Listbox(self.L_ContPk1, height=5, listvariable=tkinter.StringVar(value=listaPokemones))
        self.LB_Pk1.bind("<<ListboxSelect>>", lambda event: self.pkSeleccionado(event, 1))
        self.LB_Pk1.pack(side="top", fill="x", padx=20)

        self.C_Pk2 = tkinter.Canvas(self.L_ContPk2, width=300, height=300, bg="lightblue")
        self.C_Pk2.pack(side="top", pady=20)
        self.LB_Pk2 = tkinter.Listbox(self.L_ContPk2, height=5, listvariable=tkinter.StringVar(value=listaPokemones))
        self.LB_Pk2.bind("<<ListboxSelect>>", lambda event: self.pkSeleccionado(event, 2))
        self.LB_Pk2.pack(side="top", fill="x", padx=20)

        #Nombre del Pokemon seleccionado y sus stats

        self.L_ContNombreStatsPk0 = tkinter.Label(self.L_ContPk0, bg="red", borderwidth=0, height=8)
        self.L_ContNombreStatsPk0.pack(side="bottom", fill="x")
        self.L_ContNombreStatsPk0.pack_propagate(False)

        self.L_NombrePk0 = tkinter.Label(self.L_ContNombreStatsPk0, text="NOMBRE DE POKEMON", font=("", 15), height=2, bg="#f6ff47")
        self.L_NombrePk0.pack(side="top", fill="x")

        self.L_ContStatsPk0 = tkinter.Label(self.L_ContNombreStatsPk0, bg="lightgray", borderwidth=0)
        self.L_ContStatsPk0.pack(side="top", fill="both", expand=True)
        self.L_HPPk0 = tkinter.Label(self.L_ContStatsPk0, text="HP:0", font=("", 12), bg="lightblue")
        self.L_HPPk0.pack(side="left", expand=True)
        self.L_AttPk0 = tkinter.Label(self.L_ContStatsPk0, text="ATQ: 0", font=("", 12), bg="lightblue")
        self.L_AttPk0.pack(side="left", expand=True)
        self.L_DefPk0 = tkinter.Label(self.L_ContStatsPk0, text="DEF: 0", font=("", 12), bg="lightblue")
        self.L_DefPk0.pack(side="left", expand=True)



        self.L_ContNombreStatsPk1 = tkinter.Label(self.L_ContPk1, bg="red", borderwidth=0, height=8)
        self.L_ContNombreStatsPk1.pack(side="bottom", fill="x")
        self.L_ContNombreStatsPk1.pack_propagate(False)

        self.L_NombrePk1 = tkinter.Label(self.L_ContNombreStatsPk1, text="NOMBRE DE POKEMON", font=("", 15), height=2, bg="#f6ff47")
        self.L_NombrePk1.pack(side="top", fill="x")

        self.L_ContStatsPk1 = tkinter.Label(self.L_ContNombreStatsPk1, bg="lightgray", borderwidth=0)
        self.L_ContStatsPk1.pack(side="top", fill="both", expand=True)
        self.L_HPPk1 = tkinter.Label(self.L_ContStatsPk1, text="HP: 0", font=("", 12), bg="lightblue")
        self.L_HPPk1.pack(side="left", expand=True)
        self.L_AttPk1 = tkinter.Label(self.L_ContStatsPk1, text="ATQ: 0", font=("", 12), bg="lightblue")
        self.L_AttPk1.pack(side="left", expand=True)
        self.L_DefPk1 = tkinter.Label(self.L_ContStatsPk1, text="DEF: 0", font=("", 12), bg="lightblue")
        self.L_DefPk1.pack(side="left", expand=True)



        self.L_ContNombreStatsPk2 = tkinter.Label(self.L_ContPk2, bg="red", borderwidth=0, height=8)
        self.L_ContNombreStatsPk2.pack(side="bottom", fill="x")
        self.L_ContNombreStatsPk2.pack_propagate(False)

        self.L_NombrePk2 = tkinter.Label(self.L_ContNombreStatsPk2, text="NOMBRE DE POKEMON", font=("", 15), height=2, bg="#f6ff47")
        self.L_NombrePk2.pack(side="top", fill="x")

        self.L_ContStatsPk2 = tkinter.Label(self.L_ContNombreStatsPk2, bg="lightgray", borderwidth=0)
        self.L_ContStatsPk2.pack(side="top", fill="both", expand=True)
        self.L_HPPk2 = tkinter.Label(self.L_ContStatsPk2, text="HP: 100", font=("", 12), bg="lightblue")
        self.L_HPPk2.pack(side="left", expand=True)
        self.L_AttPk2 = tkinter.Label(self.L_ContStatsPk2, text="ATQ: 50", font=("", 12), bg="lightblue")
        self.L_AttPk2.pack(side="left", expand=True)
        self.L_DefPk2 = tkinter.Label(self.L_ContStatsPk2, text="DEF: 30", font=("", 12), bg="lightblue")
        self.L_DefPk2.pack(side="left", expand=True)



        self.B_Volver = tkinter.Button(self.mainCont, text="Volver", font=("", 30), fg="white", bg="red", relief="flat", width=7, cursor="hand2", command=lambda: controller.mostrar_ventana(selecAvt))
        self.B_Volver.place(anchor="sw", rely=1, x=0, y=0)

        self.B_Siguiente = tkinter.Button(self.mainCont, text="Siguiente", font=("", 30), fg="white", bg="green", relief="flat", width=7, cursor="hand2", command=lambda: self.iniciarPartida(controller))
        self.B_Siguiente.place(anchor="se", relx=1, rely=1, x=0, y=0)
    
    def pkSeleccionado(self, event, pkIndex):
        seleccion = event.widget.get(event.widget.curselection())
        imagen = img(f"pk{listaPokemones.index(seleccion)}.png", 300, 300)
        
        if pkIndex == 0:
            self.L_NombrePk0.config(text=seleccion)
            self.L_HPPk0.config(text=f"HP: {pkDefaultStats[seleccion]['HP']}")
            self.L_AttPk0.config(text=f"ATQ: {pkDefaultStats[seleccion]['ATQ']}")
            self.L_DefPk0.config(text=f"DEF: {pkDefaultStats[seleccion]['DEF']}")
            
            self.img0 = imagen  # Mantener referencia persistente
            self.C_Pk0.delete("all")
            self.C_Pk0.create_image(0, 0, anchor="nw", image=self.img0)
        elif pkIndex == 1:
            self.L_NombrePk1.config(text=seleccion)
            self.L_HPPk1.config(text=f"HP: {pkDefaultStats[seleccion]['HP']}")
            self.L_AttPk1.config(text=f"ATQ: {pkDefaultStats[seleccion]['ATQ']}")
            self.L_DefPk1.config(text=f"DEF: {pkDefaultStats[seleccion]['DEF']}")
            
            self.img1 = imagen  # Mantener referencia persistente
            self.C_Pk1.delete("all")
            self.C_Pk1.create_image(0, 0, anchor="nw", image=self.img1)
        elif pkIndex == 2:
            self.L_NombrePk2.config(text=seleccion)
            self.L_HPPk2.config(text=f"HP: {pkDefaultStats[seleccion]['HP']}")
            self.L_AttPk2.config(text=f"ATQ: {pkDefaultStats[seleccion]['ATQ']}")
            self.L_DefPk2.config(text=f"DEF: {pkDefaultStats[seleccion]['DEF']}")
            
            self.img2 = imagen  # Mantener referencia persistente
            self.C_Pk2.delete("all")
            self.C_Pk2.create_image(0, 0, anchor="nw", image=self.img2)
    

    def iniciarPartida(self, controller):

        # No iniciar la partida si no se han seleccionado los pokemones
        if (self.L_NombrePk0.cget("text") == "NOMBRE DE POKEMON" or
            self.L_NombrePk1.cget("text") == "NOMBRE DE POKEMON" or
            self.L_NombrePk2.cget("text") == "NOMBRE DE POKEMON"):
            return 
        
        # No iniciar la partida si se han seleccionado pokemones repetidos
        if (self.L_NombrePk0.cget("text") == self.L_NombrePk1.cget("text") or
            self.L_NombrePk0.cget("text") == self.L_NombrePk2.cget("text") or
            self.L_NombrePk1.cget("text") == self.L_NombrePk2.cget("text")):
            return  
        
        #Asignar el equipo seleccionado al jugador
        jugador.pk = [self.L_NombrePk0.cget("text"), self.L_NombrePk1.cget("text"), self.L_NombrePk2.cget("text")]
        jugador.currentPk = jugador.pk[0]
        #Asignar el equipo del bot aleatoriamente

        bot.nombre = bot.nombreBot(bot)
        bot.avatar = bot.avtarBot(bot)
        bot.pk = bot.equipoBot(bot)
        bot.currentPk = bot.pk[0]

        #Cambios gráficos para game
        

        game_frame = controller.ventanas[game]
        
        game_frame.C_PkJugador.delete("all")

        self.jugadorAvtImg = img(f"{jugador.avatar}.png", 375, 375)
        game_frame.C_AvtJugador.create_image(0, 0, anchor="nw", image=self.jugadorAvtImg)

        self.jugadorPkImg = img(f"pk{listaPokemones.index(jugador.currentPk)}.png", 200, 200)
        game_frame.C_PkJugador.create_image(0, 0, anchor="nw", image=self.jugadorPkImg)

        self.botAvtImg = img(f"{bot.avatar}.png", 375, 375)
        game_frame.C_Bot.create_image(0, 0, anchor="nw", image=self.botAvtImg)

        self.botPkImg = img(f"pk{listaPokemones.index(bot.currentPk)}.png", 200, 200)
        game_frame.C_PkBot.create_image(0, 0, anchor="nw", image=self.botPkImg)

        game_frame.L_PkPlayerName.configure(text=f"{jugador.nombre}:   {jugador.currentPk}")
        game_frame.L_PkBotName.configure(text=f"{bot.nombre}:   {bot.currentPk}")

        #Stats del jugador
        game_frame.PcurrentPkHP.set(f"HP: {gameStats[jugador.currentPk]['HP']}")
        game_frame.PcurrentPkATQ.set(f"ATQ: {gameStats[jugador.currentPk]['ATQ']}")
        game_frame.PcurrentPkDEF.set(f"DEF: {gameStats[jugador.currentPk]['DEF']}")
        #Stats del bot
        game_frame.BcurrentPkHP.set(f"HP: {gameStats[bot.currentPk]['HP']}")
        game_frame.BcurrentPkATQ.set(f"ATQ: {gameStats[bot.currentPk]['ATQ']}")
        game_frame.BcurrentPkDEF.set(f"DEF: {gameStats[bot.currentPk]['DEF']}")
        TESTFUNCTION()
        controller.mostrar_ventana(game)


            
        



#---------------------------------------------------------------------------------------

#                   VENTANA DE BATALLA

#---------------------------------------------------------------------------------------



class game(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.PcurrentPkHP = tkinter.StringVar()
        self.PcurrentPkDEF = tkinter.StringVar()
        self.PcurrentPkATQ = tkinter.StringVar()
        self.PcurrentPkDEFEx = tkinter.StringVar()
        self.PcurrentPkHP.set("HP: 0")
        self.PcurrentPkDEF.set("DEF: 0")
        self.PcurrentPkATQ.set("ATQ: 0")
        self.PcurrentPkDEFEx.set("+DEF: 0")

        self.BcurrentPkHP = tkinter.StringVar()
        self.BcurrentPkDEF = tkinter.StringVar()
        self.BcurrentPkATQ = tkinter.StringVar()
        self.BcurrentPkDEFEx = tkinter.StringVar()
        self.BcurrentPkHP.set("HP: 0")
        self.BcurrentPkDEF.set("DEF: 0")
        self.BcurrentPkATQ.set("ATQ: 0")
        self.BcurrentPkDEFEx.set("+DEF: 0")

        self.mainCont = tkinter.Label(self, background="#554CFF", borderwidth=0)
        self.mainCont.pack(expand=True, fill="both")

        #Información de ambos jugadores
        self.L_InfoBot = tkinter.Label(self.mainCont, width=80, bg="red", height=15, borderwidth=0)
        self.L_InfoBot.place(x=20, y=10)
        self.L_InfoBot.pack_propagate(False)

        self.L_InfoPlayer = tkinter.Label(self.mainCont, width=80, bg="green", height=15, borderwidth=0)
        self.L_InfoPlayer.place(anchor="se", relx=1, rely=1, x=-10, y=-20)
        self.L_InfoPlayer.pack_propagate(False)

        self.L_PkPlayerName = tkinter.Label(self.L_InfoPlayer, text="nombre", font=("", 15), height=2, bg="lightgray")
        self.L_PkPlayerName.pack(side="top", anchor="nw", fill="x")

        self.L_PkPlayerDescCont = tkinter.Label(self.L_InfoPlayer, bg="gray")
        self.L_PkPlayerDescCont.pack(side="bottom", anchor="nw", expand=True, fill="both")
        
        #Contenedor para stats actuales del jugador
        
        self.L_PkStatsCont = tkinter.Label(self.L_PkPlayerDescCont)
        self.L_PkStatsCont.pack(side="top", fill="x")

        #Labels de stats para el jugador
        self.L_PkPlayerHP = tkinter.Label(self.L_PkStatsCont, textvariable=self.PcurrentPkHP, font=("", 12), bg="lightblue")
        self.L_PkPlayerHP.pack(side="left", padx=5, expand=True)
        self.L_PkPlayerATQ = tkinter.Label(self.L_PkStatsCont, textvariable=self.PcurrentPkATQ, font=("", 12), bg="lightblue")
        self.L_PkPlayerATQ.pack(side="left", padx=5, expand=True)
        self.L_PkPlayerDEF = tkinter.Label(self.L_PkStatsCont, textvariable=self.PcurrentPkDEF, font=("", 12), bg="lightblue")
        self.L_PkPlayerDEF.pack(side="left", padx=5, expand=True)
        self.L_PkPlayerDEFEx = tkinter.Label(self.L_PkStatsCont, textvariable=self.PcurrentPkDEFEx, font=("", 12), bg="lightblue")
        self.L_PkPlayerDEFEx.pack(side="left", padx=5, expand=True)

        #Informacion de accion
        self.L_PlayerInfo = tkinter.Label(self.L_PkPlayerDescCont, bg="black", fg="white", font=("", 12))
        self.L_PlayerInfo.pack(side="top", fill="both", expand=True)

        self.L_PkBotName = tkinter.Label(self.L_InfoBot, text="nombre", font=("", 15), height=2, bg="lightgray")
        self.L_PkBotName.pack(side="top", fill="x")

        self.L_PkBotDescCont = tkinter.Label(self.L_InfoBot, bg="gray")
        self.L_PkBotDescCont.pack(side="top", expand=True, fill="both")

        #Contenedor para stats actuales del bot
        self.L_PkBotStatsCont = tkinter.Label(self.L_PkBotDescCont)
        self.L_PkBotStatsCont.pack(side="top", fill="x")

        #Labels de stats para el bot
        self.L_PkBotHP = tkinter.Label(self.L_PkBotStatsCont, textvariable=self.BcurrentPkHP, font=("", 12), bg="lightblue")
        self.L_PkBotHP.pack(side="left", padx=5, expand=True)
        self.L_PkBotATQ = tkinter.Label(self.L_PkBotStatsCont, textvariable=self.BcurrentPkATQ, font=("", 12), bg="lightblue")
        self.L_PkBotATQ.pack(side="left", padx=5, expand=True)
        self.L_PkBotDEF = tkinter.Label(self.L_PkBotStatsCont, textvariable=self.BcurrentPkDEF, font=("", 12), bg="lightblue")
        self.L_PkBotDEF.pack(side="left", padx=5, expand=True)
        self.L_PkBotDEFEx = tkinter.Label(self.L_PkBotStatsCont, textvariable=self.BcurrentPkDEFEx, font=("", 12), bg="lightblue")
        self.L_PkBotDEFEx.pack(side="left", padx=5, expand=True)

        #Informacion de accion
        self.L_BotInfo = tkinter.Label(self.L_PkBotDescCont, bg="black", fg="white", font=("", 12))
        self.L_BotInfo.pack(side="top", fill="both", expand=True)

        #Opciones del jugador
        self.L_ContOpciones = tkinter.Label(self.mainCont, width=100, bg="yellow", height=4)
        self.L_ContOpciones.place(anchor="sw", rely=1, x=0, y=0)
        self.L_ContOpciones.pack_propagate(False)

        self.B_Salir = tkinter.Button(self.L_ContOpciones, text="Salir", bg="red", width=8, font=("", 15), cursor="hand2", command=lambda: controller.mostrar_ventana(main))
        self.B_Salir.pack(side="right", fill="y")

        self.B_Cambiar = tkinter.Button(self.L_ContOpciones, text="Cambiar Ticomon", bg="#ffcb46",cursor="hand2", command=lambda: turnoJugador("CH", controller))
        self.B_Cambiar.pack(side="right", expand=True, fill="both")

        self.B_Atacar = tkinter.Button(self.L_ContOpciones, text="ATACAR", bg="#ff4e4e", cursor="hand2", command=lambda: turnoJugador("ATQ", controller))
        self.B_Atacar.pack(side="right", expand=True, fill="both")

        self.B_Defender = tkinter.Button(self.L_ContOpciones, text="DEFENDER", bg="#97fff3", cursor="hand2", command=lambda: turnoJugador("DEF", controller))
        self.B_Defender.pack(side="right", expand=True, fill="both")

        self.B_Curar = tkinter.Button(self.L_ContOpciones, text="CURAR", bg="#77ff87", cursor="hand2", command=lambda: turnoJugador("HP", controller))
        self.B_Curar.pack(side="right", expand=True, fill="both")

        self.L_PuntosJugador = tkinter.Label(self.L_ContOpciones, text="Puntos: 10")
        self.L_PuntosJugador.pack(side="left", expand=True, fill="both")

        #Sprites de avatares y pokemones
        self.L_ContJugador = tkinter.Label(self.mainCont, width=105, height=25)
        self.L_ContJugador.place(anchor="sw", rely=1, x=10, y=-80)
        self.L_ContJugador.pack_propagate(False)

        self.L_ContBot = tkinter.Label(self.mainCont, width=105, height=25)
        self.L_ContBot.place(anchor="ne", relx=1, x=-10, y=80)
        self.L_ContBot.pack_propagate(False)

        self.C_AvtJugador = tkinter.Canvas(self.L_ContJugador, width=375, bg="blue")
        self.C_AvtJugador.pack(side="left", fill="y")

        self.C_PkJugador = tkinter.Canvas(self.L_ContJugador, width=200, height= 200, bg="lightblue")
        self.C_PkJugador.pack(side="bottom")

        self.C_Bot = tkinter.Canvas(self.L_ContBot, width=375, bg="blue")
        self.C_Bot.pack(side="right", fill="y")

        self.C_PkBot = tkinter.Canvas(self.L_ContBot, width=200, height=200, bg="lightblue")
        self.C_PkBot.pack(side="bottom")



#---------------------------------------------------------------------------------------

#                   VENTANA DE RESULTADOS

#---------------------------------------------------------------------------------------



class result(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.mainCont = tkinter.Label(self, background="yellow", borderwidth=0)
        self.mainCont.pack(expand=True, fill="both")

        self.mainCont.columnconfigure(0, weight=1)
        self.mainCont.rowconfigure(0, weight=1)
        self.mainCont.rowconfigure(1, minsize=100)

        #Tabla de resultados de la partida
        self.L_TablaResultados = tkinter.Label(self.mainCont, bg="lightgreen", width=150, borderwidth=0)
        self.L_TablaResultados.grid(column=0, row=0, sticky="ns", pady=15)
        self.L_TablaResultados.pack_propagate(False)

        self.L_TituloTabla = tkinter.Label(self.L_TablaResultados, text="Resultados", font=("", 20),)
        self.L_TituloTabla.pack(side="top", fill="x")

        self.L_TablaJugador = tkinter.Label(self.L_TablaResultados, bg="green", borderwidth=0)
        self.L_TablaJugador.pack(side="left", fill="both", expand=True)
        self.L_TablaJugador.pack_propagate(False)
        self.L_TablaJugadorTitulo = tkinter.Label(self.L_TablaJugador, text="Jugador", font=("", 15))
        self.L_TablaJugadorTitulo.pack(side="top", pady=15, fill="x")
        self.L_PuntajeJugador = tkinter.Label(self.L_TablaJugador, bg="orange", text="10", font=("", 100))
        self.L_PuntajeJugador.place(relx=0.5, rely=0.5, anchor="center")

        self.L_TablaBot = tkinter.Label(self.L_TablaResultados, bg="blue", borderwidth=0)
        self.L_TablaBot.pack(side="left", fill="both", expand=True)
        self.L_TablaBot.pack_propagate(False)
        self.L_TablaBotTitulo = tkinter.Label(self.L_TablaBot, text="Bot", font=("", 15))
        self.L_TablaBotTitulo.pack(side="top", pady=15, fill="x")
        self.L_PuntajeBot = tkinter.Label(self.L_TablaBot, bg="orange", text="10", font=("", 100))
        self.L_PuntajeBot.place(relx=0.5, rely=0.5, anchor="center")


        #Label inferior de la ventana

        self.L_LabelInferior = tkinter.Label(self.mainCont, bg="lightgray", borderwidth=0)
        self.L_LabelInferior.grid(column=0, row=1, sticky="nswe")

        self.L_LabelInferior.columnconfigure(0, weight=1)
        self.L_LabelInferior.columnconfigure(1, weight=1)
        self.L_LabelInferior.rowconfigure(0, weight=1)
        self.L_LabelInferior.grid_propagate(False)


        self.B_Volver = tkinter.Button(self.L_LabelInferior, bg="red", text="Volver al menú principal", font=("", 30), relief="flat", command=lambda: controller.mostrar_ventana(main))
        self.B_Volver.grid(column=0, row=0, sticky="nswe")
        self.B_Clasificacion = tkinter.Button(self.L_LabelInferior, bg="green", text="Ir al top puntaje", font=("", 30), relief="flat", command=lambda: controller.mostrar_ventana(clasif))
        self.B_Clasificacion.grid(column=1, row=0, sticky="nswe")

class clasif(tkinter.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.mainCont = tkinter.Label(self, background="lightgreen", borderwidth=0)
        self.mainCont.pack(expand=True, fill="both")

        #Tabla de clasificaciones
        self.L_TablaClasificacion = tkinter.Label(self.mainCont, width=100, height=35, bg="green")
        self.L_TablaClasificacion.place(relx=0.5, rely=0.5, anchor="center")
        self.L_TablaClasificacion.pack_propagate(False)

        self.L_Titulo = tkinter.Label(self.L_TablaClasificacion, text="Top 10 Mejores", font=("", 20))
        self.L_Titulo.pack(side="top", fill="x", pady=(0, 10))

        self.L_P0 = tkinter.Label(self.L_TablaClasificacion, anchor="w", text="1", font=("", 20), justify="left", padx=20, bg="yellow")
        self.L_P0.pack(side="top", expand=True, fill="both")
        self.L_P1 = tkinter.Label(self.L_TablaClasificacion, anchor="w", text="2", font=("", 20), justify="left", padx=20, bg="blue")
        self.L_P1.pack(side="top", expand=True, fill="both")
        self.L_P2 = tkinter.Label(self.L_TablaClasificacion, anchor="w", text="3", font=("", 20), justify="left", padx=20, bg="yellow")
        self.L_P2.pack(side="top", expand=True, fill="both")
        self.L_P3 = tkinter.Label(self.L_TablaClasificacion, anchor="w", text="4", font=("", 20), justify="left", padx=20, bg="blue")
        self.L_P3.pack(side="top", expand=True, fill="both")
        self.L_P4 = tkinter.Label(self.L_TablaClasificacion, anchor="w", text="5", font=("", 20), justify="left", padx=20, bg="yellow")
        self.L_P4.pack(side="top", expand=True, fill="both")
        self.L_P5 = tkinter.Label(self.L_TablaClasificacion, anchor="w", text="6", font=("", 20), justify="left", padx=20, bg="blue")
        self.L_P5.pack(side="top", expand=True, fill="both")
        self.L_P6 = tkinter.Label(self.L_TablaClasificacion, anchor="w", text="7", font=("", 20), justify="left", padx=20, bg="yellow")
        self.L_P6.pack(side="top", expand=True, fill="both")
        self.L_P7 = tkinter.Label(self.L_TablaClasificacion, anchor="w", text="8", font=("", 20), justify="left", padx=20, bg="blue")
        self.L_P7.pack(side="top", expand=True, fill="both")
        self.L_P8 = tkinter.Label(self.L_TablaClasificacion, anchor="w", text="9", font=("", 20), justify="left", padx=20, bg="yellow")
        self.L_P8.pack(side="top", expand=True, fill="both")
        self.L_P9 = tkinter.Label(self.L_TablaClasificacion, anchor="w", text="10", font=("", 20), justify="left", padx=20, bg="blue")
        self.L_P9.pack(side="top", expand=True, fill="both")


        self.B_Volver = tkinter.Button(self.mainCont, text="Volver", font=("", 30), bg="red", width=7, height=2, relief="flat", cursor="hand2", command=lambda: controller.mostrar_ventana(main))
        self.B_Volver.place(anchor="sw",rely=1, x=0, y=0)

#Ejecutar la aplicación
if __name__ == "__main__":
    root().mainloop()

