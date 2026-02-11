# Mi Primer Proyecto en Python:

# Generador de Presupuesto de Consultoría

## Descripción del Proyecto

**Presupuesto de Consultoria** es una aplicación en Python que permite generar presupuestos profesionales en formato PDF de manera rapida y sencilla. La herramienta solicita información sobre el proyecto y genera un documento PDF formateado con los datos ingresados.

## Requisitos

Antes de ejecutar el proyecto, asegurate de tener instalados:

- **Python 3.x**
- **Librería FPDF**

Para instalar las dependencias, ejecuta:

```bash
pip install fpdf
```

## Archivos Necesarios

- `proyecto_01.py` - Script principal
- `Template.png` - Imagen de fondo/plantilla para el PDF

## Cómo Usar

1. **Ejecutar el script:**

```bash
python proyecto_01.py
```

2. **Proporcionar la información solicitada:**
   - Nombre del proyecto
   - Horas estimadas de dedicación
   - Valor de la hora trabajada (en USD)
   - Plazo estimado para el proyecto

3. **Resultado:**
   Se generará automáticamente un archivo `Presupuesto.pdf` con toda la información ingresada.

## Ejemplo de Usos

```
Escriba el nombre del proyecto: Sistema de Inventario
Escriba las horas que va a dedicar al proyecto: 40
¿Cual es el valor de la hora trabajada?: 50
¿Cual es el plazo estimado para el proyecto?: 2 semanas
```

**Resultado:** Se crea un PDF con un presupuesto total de **USD $2,000** (40 horas × $50/hora)

## Tecnologías Utilizadas

- **Python 3**
- **FPDF** - Librería para crear documentos PDF

## Notas importantes

- Asegúrate de tener el archivo `Template.png` en el mismo directorio que el script
- Los valores deben ser numéricos para que el cálculo funcione correctamente
- El archivo PDF se sobrescribe cada vez que ejecutas el script
