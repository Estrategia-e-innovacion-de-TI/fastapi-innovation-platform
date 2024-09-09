import pandas as pd
import numpy as np
import json


def get_results(data):
    excel_file = 'app/lista_innovacion.xlsx'  # Replace with your Excel file path
    df_lista_innovacion = pd.read_excel(excel_file, skiprows=1)  # Read Excel file into a DataFrame

    choosen_purposes = list(data['proposito_iniciativa'])
    
    # Function to check if any of the purposes is in the row's purposes list
    def contains_any_purpose(row):
        row_purposes = row['Propósito'].split(', ')
        return any(purpose in row_purposes for purpose in choosen_purposes)

    df_lista_innovacion_filter = df_lista_innovacion[df_lista_innovacion['En artefacto'] == 'Si']
    df_lista_innovacion_filter = df_lista_innovacion_filter[df_lista_innovacion_filter.apply(contains_any_purpose, axis=1)]
    print("Paso 1:")
    results = calc_top_methodologies_and_techniques(data, df_innovation_filter=df_lista_innovacion_filter)

    results_clean = clean_invalid_values(results)
    try:
        json.dumps(results_clean)  # Check if data can be converted to JSON
    except (ValueError, TypeError) as e:
        print("Error in JSON conversion:", e)

    
    cleaned_results = clean_data(results_clean)
    print(cleaned_results)
    return cleaned_results

def get_dict(list_result, phase=None, df_notes=None):
    result = []
    if isinstance(list_result, str):     
        return [{'nombre': list_result, 'puntuacion': '','url': ''}]
    else:
        for item in list_result:
            if item[1] <= 60:
                result.append({'nombre': 'No tenemos sugerencias para ti', 'puntuacion': '', 'url': ''})
                break
            else:
                if df_notes is not None and phase is None:
                    note = df_notes[df_notes['Nombre'] == item[0]]['Descripción'].values
                    if len(note) > 0:
                        result.append({'nombre': item[0], 'puntuacion': str(item[1])+'%', 'url': item[2], 'comentario': note[0]})
                    else:
                        result.append({'nombre': item[0], 'puntuacion': str(item[1])+'%', 'url': item[2]})
                elif df_notes is not None:
                    note = df_notes[df_notes['Nombre'] == item[0]][phase].values
                    if len(note) > 0:
                        result.append({'nombre': item[0], 'puntuacion': str(item[1])+'%', 'url': item[2], 'comentario': note[0]})
                    else:
                        result.append({'nombre': item[0], 'puntuacion': str(item[1])+'%', 'url': item[2]})
                else:
                    result.append({'nombre': item[0], 'puntuacion': str(item[1])+'%', 'url': item[2]})
        return result

def clean_invalid_values(data):
    if isinstance(data, pd.DataFrame):
        # Reemplazar NaN y valores infinitos por None en todo el DataFrame
        data.replace([np.inf, -np.inf], None, inplace=True)
        data.fillna(None, inplace=True)
        # Asegúrate de que todos los valores sean JSON serializables
        for col in data.columns:
            if data[col].dtype == 'float64':
                data[col] = data[col].apply(lambda x: None if (pd.isna(x) or pd.isinf(x)) else x)
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (float, int)) and (np.isinf(value) or pd.isna(value)):
                data[key] = None
            elif isinstance(value, dict):
                data[key] = clean_invalid_values(value)  # Llamada recursiva para diccionarios anidados
            elif isinstance(value, list):
                data[key] = [clean_invalid_values(item) for item in value]  # Llamada recursiva para elementos de la lista
    elif isinstance(data, list):
        data = [clean_invalid_values(item) for item in data]  # Llamada recursiva para elementos de la lista
    return data

def clean_data(data):
    # Limpiar 'puntuacion'
    for phase in ['methodologies', 'first_phase', 'second_phase', 'third_phase', 'fourth_phase', 'fifth_phase', 'sixth_phase']:
        for item in data[phase]:
            if 'puntuacion' in item and isinstance(item['puntuacion'], str):
                # Quitar el signo '%' y convertir a número flotante
                if item['puntuacion'].endswith('%'):
                    item['puntuacion'] = float(item['puntuacion'].replace('%', '').strip())
                else:
                    item['puntuacion'] = float(item['puntuacion'].strip()) if item['puntuacion'] else None
            # Reemplazar 'None' en 'url' con una cadena vacía
            if 'url' in item and item['url'] is None:
                item['url'] = ''
            # Reemplazar 'None' en 'comentario' con una cadena vacía
            if 'comentario' in item and item['comentario'] is None:
                item['comentario'] = ''

    return data


def calc_top_methodologies_and_techniques(data, **kwargs):
    excel_file = 'app/lista_innovacion.xlsx'  # Replace with your Excel file path
    df_notes = pd.read_excel(excel_file, sheet_name='comentarios', skiprows=1)

    if 'df_innovation_filter' in kwargs:
        df_innovation_filter = kwargs['df_innovation_filter']
    
    urgency = data["urgencia"]
    complexity = data["complejidad"]
    uncertainty = data["incertidumbre"]
    collaboration = data["colaboracion"]
    resources = data["recursos"]
    flexibility = data["flexibilidad"]
    velocity = data["velocidad"]
    risk  = data["riesgo"]
    user = data["usuario"]

    df_innovation_filter['calc_urgencia']  = (5 -  (df_innovation_filter['Urgencia'] - urgency).abs())
    df_innovation_filter['calc_complejidad'] = (5 - (df_innovation_filter['Complejidad'] - complexity).abs())
    df_innovation_filter['calc_incertidumbre'] = (5 - (df_innovation_filter['Incertidumbre'] - uncertainty).abs())
    df_innovation_filter['calc_colaboracion'] = (5 - (df_innovation_filter['Colaboración'] - collaboration).abs())
    df_innovation_filter['calc_recursos'] = (5 - (df_innovation_filter['Recursos Disponibles'] - resources).abs())
    df_innovation_filter['calc_flexibilidad'] = (5 - (df_innovation_filter['Flexibilidad'] - flexibility).abs())
    df_innovation_filter['calc_velocidad'] = (5 - (df_innovation_filter['Velocidad de implementación'] - velocity).abs())
    df_innovation_filter['calc_riesgo'] = (5 - (df_innovation_filter['Factor de Riesgo'] - risk).abs())
    df_innovation_filter['calc_usuario'] = (5 - (df_innovation_filter['Conocimiento del usuario'] - user).abs())

    df_innovation_filter['total'] = round((df_innovation_filter.filter(regex='^calc_').sum(axis=1) / 45) * 100, 1)

    # Top 3 methodologies
    df_methodologies = df_innovation_filter[df_innovation_filter['Tipo'] == 'Metodología']
    methodologies = df_methodologies[["Nombre", "total", "Plantilla"]].sort_values(by='total', ascending=False).head(3).values

    df_techniques = df_innovation_filter[df_innovation_filter['Tipo'] == 'Técnica']
    selected_phases = data["fase_innovacion"]
    phases = [
        '1. Identificación de la necesidad o problema',
        '2. Generación de ideas',
        '3. Selección de ideas',
        '4. Desarrollo del prototipo',
        '5. Pruebas y validación',
        '6. Implementación'
    ]

    for phase in phases:
        if phase in selected_phases:
            df_techniques[f"calc_{phase}"] = df_techniques[phase] * df_techniques['total']
        else:
            df_techniques[f"calc_{phase}"] = [0] * len(df_techniques)


    first_phase = df_techniques[["Nombre", f"calc_{phases[0]}", "Plantilla"]].sort_values(by=f"calc_{phases[0]}",
                                                                                           ascending=False).head(3).values if df_techniques[f"calc_{phases[0]}"].sum() > 0 else "No Seleccionado"
    second_phase = df_techniques[["Nombre", f"calc_{phases[1]}", "Plantilla"]].sort_values(by=f"calc_{phases[1]}",
                                                                                            ascending=False).head(3).values if df_techniques[f"calc_{phases[1]}"].sum() > 0 else "No Seleccionado"
    third_phase = df_techniques[["Nombre", f"calc_{phases[2]}", "Plantilla"]].sort_values(by=f"calc_{phases[2]}",
                                                                                           ascending=False).head(3).values if df_techniques[f"calc_{phases[2]}"].sum() > 0 else "No Seleccionado"
    fourth_phase = df_techniques[["Nombre", f"calc_{phases[3]}", "Plantilla"]].sort_values(by=f"calc_{phases[3]}",
                                                                                            ascending=False).head(3).values if df_techniques[f"calc_{phases[3]}"].sum() > 0 else "No Seleccionado"
    fifth_phase = df_techniques[["Nombre", f"calc_{phases[4]}", "Plantilla"]].sort_values(by=f"calc_{phases[4]}",
                                                                                           ascending=False).head(3).values if df_techniques[f"calc_{phases[4]}"].sum() > 0 else "No Seleccionado"
    sixth_phase = df_techniques[["Nombre", f"calc_{phases[5]}", "Plantilla"]].sort_values(by=f"calc_{phases[5]}",
                                                                                           ascending=False).head(3).values if df_techniques[f"calc_{phases[5]}"].sum() > 0 else "No Seleccionado"

    result = {
        "methodologies": get_dict(methodologies, df_notes=df_notes),
        "first_phase": get_dict(first_phase, phases[0], df_notes),
        "second_phase": get_dict(second_phase, phases[1], df_notes),
        "third_phase": get_dict(third_phase, phases[2], df_notes),
        "fourth_phase": get_dict(fourth_phase, phases[3], df_notes),
        "fifth_phase": get_dict(fifth_phase, phases[4], df_notes),
        "sixth_phase": get_dict(sixth_phase, phases[5], df_notes)
    }
    result = clean_invalid_values(result)
    return result