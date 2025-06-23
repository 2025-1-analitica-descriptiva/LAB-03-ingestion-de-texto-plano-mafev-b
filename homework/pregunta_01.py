"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt") as file:
      lineas = file.readlines()
      
      linea1 = re.sub(r'\s{2,}', '\t', lineas[0].strip().lower()).replace(' ', '_').split('\t')
      linea2 = re.sub(r'\s{2,}', '\t', lineas[1].replace('\n', '').lower()).replace(' ', '_').split('\t')

      headers = []
      for i in range(len(linea1)):
        if i < len(linea2) and linea2[i] != '':
          headers.append(linea1[i] + "_" + linea2[i])
        else:
          headers.append(linea1[i])
      
      lineas = lineas[4:]
      clusters = []
      cantidades = []
      porcentajes = []
      principales = []
      filas = []
      line = []
      
      for linea in lineas:
        aux = re.sub(r'\s{1,}', ' ', linea.strip()).replace('.', '').split()
        if len(aux) != 0:
          line += aux
        else:
          line.remove("%")
          filas.append(line)
          line = []
      for fila in filas:
        clusters.append(int(fila[0]))
        cantidades.append(int(fila[1]))
        porcentajes.append(float(fila[2].replace(',', '.')))
        principales.append(" ".join(fila[3:]))

      data = dict(zip(headers, [clusters, cantidades, porcentajes, principales]))
      df = pd.DataFrame(data)
      return df
