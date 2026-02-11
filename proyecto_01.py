## Obtener Datos
project = input("Escriba el nombre del proyecto: ")
estimated_hours = input("Escriba las horas que va a dedicar al proyecto: ")
time_value = input("¿Cual es el valor de la hora trabajada?: ")
estimated_term = (input("¿Cual es el plazo estimado para el proyecto?: "))

print(project,"\n", estimated_hours,"\n",time_value ,"\n", estimated_term)

## Calcular Valor Total del Trabajo
total_value = int(estimated_hours) * int(time_value)

## Importar Libreria
from fpdf import FPDF

pdf = FPDF()

## Añadir pagina y definir fuente
pdf.add_page()
pdf.set_font("Arial")

## Imagen de Fondo
pdf.image("Template.png", 0, 0)

## Recopilamos y mostramos los datos obtenidos
pdf.text(115, 145, project)
pdf.text(115, 160, estimated_hours)
pdf.text(115, 175, time_value)
pdf.text(115, 190, estimated_term)
pdf.text(115, 205, str(total_value))

## Guardamos el PDF
pdf.output("Presupuesto.pdf")
