import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("notas_1u.csv")

def filtrarPorExamen(df,  tipo_exam):
    notas_exam=[]
    for _, fila in df.iterrows():
        if fila['Tipo_Examen'] == tipo_exam:
            notas_exam.append(fila['Nota'])
    return notas_exam

# Metodo para crear los gráficos
def crearGraficos(df,d):
    # Creamos un layout de 2 filas, 2 columnas para hacer más espacio
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))  # 2 filas, 2 columnas

    # Histograma (ocupando la primera posición: 0,0)
    axes[0, 0].hist(df['Nota'], bins=10, edgecolor='black')
    axes[0, 0].set_title('Distribución de Notas')
    axes[0, 0].set_xlabel('Notas')
    axes[0, 0].set_ylabel('Frecuencia')

    # Gráfico de barras (ocupando la segunda posición: 0,1)
    grupo_promedios = df.groupby('Tipo_Examen')['Nota'].mean()
    grupo_promedios.plot(kind='bar', ax=axes[0, 1])  # Usamos el segundo eje
    axes[0, 1].set_title('Promedio por Tipo de Examen')
    axes[0, 1].set_ylabel('Promedio de Notas')

    # Sección de Datos Derivados (ocupando la posición 1,0 y 1,1)
    axes[1, 0].axis('off')  # Oculta el gráfico
    axes[1, 1].axis('off')  # Oculta el gráfico

    # Convertimos a lista de listas (filas)
    filas = [[d['etiqueta'], round(d['valor'], 2)] for d in datos_utilidad]

    # Añadimos la tabla a un subplot adicional
    tabla = axes[1, 0].table(
        cellText=filas,
        colLabels=['Descripción', 'Valor'],
        cellLoc='left',
        loc='center'
    )
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(9)
    tabla.scale(1, 1.5)
    axes[1, 0].axis('off') 

    # Ajustamos la disposición para que todo se vea bien y no se sobreponga
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    # Mostrar todo
    plt.show()


notas_examen_a = filtrarPorExamen(df,"A")
notas_examen_b = filtrarPorExamen(df,"B")
notas_examen_c = filtrarPorExamen(df,"C")

# Medias de las notas
media_total = df['Nota'].mean()
media_exam_a = round(np.mean(notas_examen_a),2)
media_exam_b = round(np.mean(notas_examen_b),2)
media_exam_c = round(np.mean(notas_examen_c),2)

# Desviación estandar
desviacion_est_total = round(df['Nota'].std(),2)
desviacion_est_a =  round(np.std(notas_examen_a, ddof=1),2)
desviacion_est_b =  round(np.std(notas_examen_b, ddof=1),2)
desviacion_est_c =  round(np.std(notas_examen_c, ddof=1),2)

# Nota máxima
nota_maxima_total = df['Nota'].max()
nota_maxima_a = np.max(notas_examen_a)
nota_maxima_b = np.max(notas_examen_b)
nota_maxima_c = np.max(notas_examen_c)

# Nota minima
nota_minima_total = df['Nota'].min()
nota_minima_a = np.min(notas_examen_a)
nota_minima_b = np.min(notas_examen_b)
nota_minima_c = np.min(notas_examen_c)

datos_utilidad = [
    {'etiqueta': "Media del total de alumnos", 'valor': media_total},
    {'etiqueta': "Media del grupo A", 'valor': media_exam_a},
    {'etiqueta': "Media del grupo B", 'valor': media_exam_b},
    {'etiqueta': "Media del grupo C", 'valor': media_exam_c},

    {'etiqueta': "Desviación estándar del total de alumnos", 'valor': desviacion_est_total},
    {'etiqueta': "Desviación estándar del grupo A", 'valor': desviacion_est_a},
    {'etiqueta': "Desviación estándar del grupo B", 'valor': desviacion_est_b},
    {'etiqueta': "Desviación estándar del grupo C", 'valor': desviacion_est_c},

    {'etiqueta': "Nota máxima del total de alumnos", 'valor': nota_maxima_total},
    {'etiqueta': "Nota máxima del grupo A", 'valor': nota_maxima_a},
    {'etiqueta': "Nota máxima del grupo B", 'valor': nota_maxima_b},
    {'etiqueta': "Nota máxima del grupo C", 'valor': nota_maxima_c},

    {'etiqueta': "Nota mínima del total de alumnos", 'valor': nota_minima_total},
    {'etiqueta': "Nota mínima del grupo A", 'valor': nota_minima_a},
    {'etiqueta': "Nota mínima del grupo B", 'valor': nota_minima_b},
    {'etiqueta': "Nota mínima del grupo C", 'valor': nota_minima_c},
]


crearGraficos(df, datos_utilidad)



