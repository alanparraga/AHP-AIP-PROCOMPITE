import pandas as pd
import numpy as np
from fractions import Fraction

def leer_matriz_csv(ruta):
    df = pd.read_csv(ruta, sep=";", index_col=0, encoding="utf-8-sig")
    # Convertir fracciones tipo '1/3' en decimales
    def convertir_valor(x):
        try:
            return float(Fraction(str(x).strip()))
        except:
            return float(x)
    df = df.map(convertir_valor)
    return df.values

def calcular_pesos(matriz):
    valores, vectores = np.linalg.eig(matriz)
    indice_max = np.argmax(valores)
    vector_pesos = np.real(vectores[:, indice_max])
    return vector_pesos / np.sum(vector_pesos)

def razon_consistencia(matriz):
    n = matriz.shape[0]
    valores, _ = np.linalg.eig(matriz)
    lambda_max = np.max(np.real(valores))
    CI = (lambda_max - n) / (n - 1)
    RI = {1:0, 2:0, 3:0.58, 4:0.9, 5:1.12, 6:1.24, 7:1.32, 8:1.41, 9:1.45, 10:1.49}
    return CI / RI[n]

def agregar_pesos_individuales(lista_de_pesos):
    """
    Implementa la Agregación de Prioridades Individuales (AIP) 
    utilizando la media geométrica de los vectores de prioridad de cada experto.
    """
    log_pesos = [np.log(p) for p in lista_de_pesos]
    promedio_log = sum(log_pesos) / len(log_pesos)
    pesos_agregados = np.exp(promedio_log)
    return pesos_agregados / np.sum(pesos_agregados)

def sintetizar_global(pesos_criterios, pesos_social, pesos_org, pesos_terr, pesos_alternativas):
    global_alternativas = np.zeros(7)

    # --- Criterio Social (6 subcriterios) ---
    for i in range(6):
        global_alternativas += pesos_criterios[0] * pesos_social[i] * pesos_alternativas[i]

    # --- Criterio Organizacional (7 subcriterios) ---
    for i in range(7):
        global_alternativas += pesos_criterios[1] * pesos_org[i] * pesos_alternativas[6 + i]

    # --- Criterio Territorial (6 subcriterios) ---
    for i in range(6):
        global_alternativas += pesos_criterios[2] * pesos_terr[i] * pesos_alternativas[13 + i]

    return global_alternativas / np.sum(global_alternativas)

def main():
    # ==============================
    # 1. CRITERIOS (3x3) - AIP
    # ==============================
    pesos_criterios_ind = []
    crs_criterios = []
    for i in range(1, 7):
        matriz = leer_matriz_csv(f"criterios3x3_especialista{i}.csv")
        pesos_criterios_ind.append(calcular_pesos(matriz))
        crs_criterios.append(razon_consistencia(matriz))
    
    pesos_criterios = agregar_pesos_individuales(pesos_criterios_ind)
    print("Pesos criterios agregados (AIP):", pesos_criterios)
    print("Consistencia promedio Criterios:", np.mean(crs_criterios))

    # ==============================
    # 2. SUBCRITERIOS SOCIALES (6x6) - AIP
    # ==============================
    pesos_social_ind = []
    crs_social = []
    for i in range(1, 7):
        matriz = leer_matriz_csv(f"criterios6x6s_especialista{i}.csv")
        pesos_social_ind.append(calcular_pesos(matriz))
        crs_social.append(razon_consistencia(matriz))
        
    pesos_social = agregar_pesos_individuales(pesos_social_ind)
    print("Pesos subcriterios - Social (AIP):", pesos_social)
    print("Consistencia promedio Social:", np.mean(crs_social))

    # ==============================
    # 3. SUBCRITERIOS ORGANIZACIONALES (7x7) - AIP
    # ==============================
    pesos_org_ind = []
    crs_org = []
    for i in range(1, 7):
        matriz = leer_matriz_csv(f"criterios7x7o_especialista{i}.csv")
        pesos_org_ind.append(calcular_pesos(matriz))
        crs_org.append(razon_consistencia(matriz))
        
    pesos_org = agregar_pesos_individuales(pesos_org_ind)
    print("Pesos subcriterios - Organizacional (AIP):", pesos_org)
    print("Consistencia promedio Organizacional:", np.mean(crs_org))

    # ==============================
    # 4. SUBCRITERIOS TERRITORIALES (6x6) - AIP
    # ==============================
    pesos_terr_ind = []
    crs_terr = []
    for i in range(1, 7):
        matriz = leer_matriz_csv(f"criterios6x6t_especialista{i}.csv")
        pesos_terr_ind.append(calcular_pesos(matriz))
        crs_terr.append(razon_consistencia(matriz))
        
    pesos_terr = agregar_pesos_individuales(pesos_terr_ind)
    print("Pesos subcriterios - Territorial (AIP):", pesos_terr)
    print("Consistencia promedio Territorial:", np.mean(crs_terr))

    # ==============================
    # 5. MATRICES DE ALTERNATIVAS (19 archivos)
    # ==============================
    alternativas_files = [
        # Sociales
        "alternativas7x7_empleo.csv",
        "alternativas7x7_joven.csv",
        "alternativas7x7_mujer.csv",
        "alternativas7x7_impacto.csv",
        "alternativas7x7_emprendedores.csv",
        "alternativas7x7_capacidad.csv",
        # Organizacionales
        "alternativas7x7_produc.csv",
        "alternativas7x7_costos.csv",
        "alternativas7x7_mercado.csv",
        "alternativas7x7_aliados.csv",
        "alternativas7x7_tecnologia.csv",
        "alternativas7x7_calidad.csv",
        "alternativas7x7_certificaciones.csv",
        # Territoriales
        "alternativas7x7_acceso.csv",
        "alternativas7x7_servicios.csv",
        "alternativas7x7_electricidad.csv",
        "alternativas7x7_comunica.csv",
        "alternativas7x7_medio.csv",
        "alternativas7x7_instrumento.csv"
    ]
    pesos_alternativas = []
    for i, archivo in enumerate(alternativas_files, start=1):
        matriz = leer_matriz_csv(archivo)
        pesos_alt = calcular_pesos(matriz)
        cr_alt = razon_consistencia(matriz)
        print(f"Pesos alternativas - Subcriterio {i} ({archivo}):", pesos_alt)
        print(f"Consistencia alternativas - Subcriterio {i}:", cr_alt)
        pesos_alternativas.append(pesos_alt)

    # ==============================
    # 6. SÍNTESIS GLOBAL
    # ==============================
    ranking_final = sintetizar_global(pesos_criterios, pesos_social, pesos_org, pesos_terr, pesos_alternativas)

    cadenas = {
        "CP1": "CP - HORTALIZAS",
        "CP2": "CP - CUY",
        "CP3": "CP - GALLINAS",
        "CP4": "CP - PALTA",
        "CP5": "CP - TRUCHA",
        "CP6": "CP - CRIANZA DE PORCINOS",
        "CP7": "CP - QUINUA"
    }

    resultados = pd.DataFrame({
        "Cadena Productiva": [cadenas[f"CP{i+1}"] for i in range(7)],
        "Ponderación Global": ranking_final
    }).sort_values(by="Ponderación Global", ascending=False)

    print("\n✅ Ranking final de las 7 cadenas productivas - Provincia de Andahuaylas (Apurímac, Perú)")
    print("\n✅ Método: Proceso Analítico Jerárquico con la Técnica de Agregación de Prioridades Individuales (AIP)")
    print("\n✅ MODELO DE DECISIÓN AHP-AIP-PROCOMPITE")
    print("\n✅ PRIORIZACIÓN:")
    print(resultados.to_string(index=False))

    resultados.to_csv("ranking_cadenas_productivas.csv", index=False, encoding="utf-8-sig")
    
    print("\n✅ Ranking exportado a 'ranking_cadenas_productivas.csv'")
    print("\n✅ ORCID: https://orcid.org/0009-0003-2932-6725")
    print("\n")

if __name__ == "__main__":
    main()