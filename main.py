from datetime import datetime

class Persona:
    def __init__(self, nombre, edad,):
        self.nombre = nombre
        self.edad = edad
        self.respuestas = []
        self.puntaje_final = 0
        self.salida_json = {}

    def guardar_datos(self):
        self.salida_json["Nombre"] = self.nombre
        self.salida_json["Edad"] = self.edad
        self.salida_json["Puntaje final"] = self.puntaje_final

        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archivo = f"{self.nombre}_{fecha}.json" 

        with open(archivo, "w") as f:
            f.write(str(self.salida_json))

    def mostrar_datos(self):
        print("Datos personales: " , self.salida_json)


class TestOrientacionVocacional:
    def __init__(self):
        self.preguntas = [
             "1. ¿Qué tipo de actividades te gustaría realizar en tu trabajo?\n"
            + "\tA) Trabajar con números y datos\n"
            + "\tB) Trabajar con personas y ayudarlas\n"
            + "\tC) Trabajar con tecnología y dispositivos.\n",
            "2. ¿Qué habilidades crees que tienes?\n"
            +"\tA) Habilidad para analizar y resolver problemas\n"
            +"\tB) Habilidad para comunicarte y persuadir a otros\n"
            +"\tC) Habilidad para comunicarte y persuadir a otros.\n",
            "3. ¿Qué materias te gustan más?\n"
            +"\tA) Matemáticas y ciencias\n"
            +"\tB) Lenguaje y literatura\n"
            +"\tC) Artes y humanidades.\n",
            "4. ¿Cómo te gustaría trabajar?\n"
            +"\tA) Trabajando en equipo\n"
            +"\tB) Trabajando de manera individual\n"
            +"\tC) No tengo preferencia.\n",
            "5. ¿Qué ambiente de trabajo prefieres?\n"
            +"\tA) Ambiente de oficina\n"
            +"\tB) Ambiente al aire libre\n"
            +"\tC) No tengo preferencia.\n",
            "6. ¿Qué carrera te llama más la atención?\n"
            +"\tA) Ciencias y tecnología\n"
            +"\tB) Ciencias sociales y humanidades\n"
            +"\tC) Ciencias de la salud\n",
            "7. ¿Qué habilidades manuales tienes?\n"
            +"\tA) Habilidad para construir y reparar cosas\n"
            +"\tB) Habilidad para cocinar y preparar alimentos\n"
            +"\tC) No tengo habilidades manuales\n",
            "8. ¿Cómo te gustaría ayudar a la sociedad?\n"
            +"\tA) Ayudando a solucionar problemas sociales\n"
            +"\tB) Contribuyendo al desarrollo de la tecnología\n"
            +"\tC) A través de la educación y la enseñanza\n",
            "9. ¿Qué te gustaría lograr en tu carrera profesional?\n"
            +"\tA) Un buen salario y estabilidad laboral\n"
            +"\tB) Contribuir a la sociedad y hacer una diferencia\n"
            +"\tC) Desarrollar habilidades y talentos propios\n",
            "10. ¿Qué tan importante es para ti el equilibrio entre el trabajo y la vida personal?\n"
            +"\tA) Muy importante\n"
            +"\tB) Importante\n"
            +"\tC) No es tan importante\n"
        ]

        self.puntaje_respuestas =  {
            'A': [2,3,3,3,3,2,3,3,3,2],
            'B': [3,2,2,2,3,2,2,2,3,3],
            'C': [4,4,4,1,1,4,1,4,4,2]
        }

        self.respuestas = []


    def ingresar_respuestas(self):
        for pregunta in self.preguntas:
            print(pregunta)
            respuesta = input("Ingresa la letra de tu respuesta: ")

            if self.verificar_respuesta(respuesta):
                self.respuestas.append(respuesta.upper())
            
    def verificar_respuesta(self, respuesta):
        if respuesta.upper() in ['A', 'B', 'C']:
            return True
        raise Exception("Has ingresado una respuesta inválida") 
    
    def calcular_puntaje(self):
        puntaje_total = 0
        for i, resp in enumerate(self.respuestas):
            puntaje_total += self.puntaje_respuestas[resp][i]

        return puntaje_total
    
    def mostrar_puntaje(self):
        print(self.calcular_puntaje)


class Recomendador:
    def __init__(self, puntaje):
        self.puntaje = puntaje
        self.recomendacion = self.crear_recomendacion(self.puntaje)

    def crear_recomendacion(self, puntaje):
        if puntaje < 20:
            return "Te recomendamos considerar carreras relacionadas con las ciencias y tecnología."
        elif puntaje < 30:
            return "Te recomendamos considerar carreras relacionadas con las ciencias sociales y humanidades."
        elif puntaje < 40:
            return "Te recomendamos considerar carreras relacionadas con las ciencias de la salud y biología."
        elif puntaje < 50:
            return "Te recomendamos considerar carreras relacionadas con los negocios y la administración."
        elif puntaje < 60:
            return "Te recomendamos considerar carreras relacionadas con el arte y el diseño."
        else:
            return "Te recomendamos considerar carreras relacionadas con la educación o alguna otra carrera de tu elección."
        
    def mostrar_recomendacion(self):
        print(self.recomendacion)

def main():
    print("Bienvenido a la aplicación de orientación vocacional")
    print("Por favor, responda las siguientes preguntas")
    nombre = input("Ingresa tu nombre completo: ")
    edad = input("Ingresa tu edad: ")
    persona = Persona(nombre, edad)
    test = TestOrientacionVocacional()
    test.ingresar_respuestas()
    persona.puntaje_final = test.calcular_puntaje()
    recomendador = Recomendador(persona.puntaje_final)
    recomendador.mostrar_recomendacion()
    persona.guardar_datos()
    persona.mostrar_datos()


main()

