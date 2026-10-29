# AHP-AIP-PROCOMPITE: An Integrated AHP-AIP Decision Model for Prioritizing Productive Chains in Peruvian Subnational Governments

**Autor:** José A. Párraga-Condezo  
**ORCID:** 0009-0003-2932-6725  

*Repositorio asociado a una investigación en MCDM.*

>Este repositorio complementa el manuscrito sometido a evaluación por pares en la revista científica Industrial Data (UNMSM).
---

## Descripción General

Este repositorio contiene la implementación oficial en Python del modelo computacional **AHP-AIP-PROCOMPITE**. Es una propuesta metodológica orientada a mejorar la selección y priorización de cadenas productivas en gobiernos regionales y locales del Perú, bajo el mecanismo de cofinanciamiento PROCOMPITE.

El modelo contribuye a fortalecer la transparencia, consistencia y objetividad en la asignación de recursos públicos, permitiendo evaluar alternativas mediante criterios técnicos, económicos, sociales y territoriales.

---

## Objetivo

Desarrollar un modelo de decisión multicriterio capaz de priorizar cadenas productivas de manera consistente y reproducible, incorporando la opinión de múltiples expertos y actores clave mediante herramientas ampliamente validadas en la literatura científica.

---

## Propuesta Técnica

La metodología integra al Proceso Analítico Jerárquico (AHP) con la técnica de Agregación de Prioridades Individuales (AIP) automatizado en Python. De igual manera, realiza el cálculo del ratio de consistencia para evaluar los juicios de los expertos.

---

## Contexto de Aplicación

El modelo ha sido diseñado para apoyar los procesos de evaluación y priorización de las cadenas productivas en el marco de PROCOMPITE, instrumento de gestión pública que busca mejorar la competitividad de los agentes económicos organizados mediante mecanismos de cofinanciamiento orientados al desarrollo económico local y regional de Perú.

---

## Estructura del Repositorio

    AHP-AIP-PROCOMPITE/
    │
    ├── AHP-AIP-PROCOMPITE.py
    ├── requirements.txt
    ├── LICENSE
    ├── alternativas7x7_*.csv
    ├── criterios3x3_*.csv
    ├── criterios6x6s_*.csv
    ├── criterios6x6t_*.csv
    ├── criterios7x7o_*.csv
    └── otros archivos CSV de entrada

### Descripción de archivos

- `AHP-AIP-PROCOMPITE.py`: Script principal que implementa el modelo de decisión.
- `*.csv`: Matrices de comparación por pares para criterios y alternativas.
- `requirements.txt`: Dependencias requeridas para la ejecución.
- `LICENSE`: Licencia MIT.

---

## Funcionalidades

El sistema permite:

- Construcción de matrices de comparación por pares.
- Cálculo de prioridades locales y globales mediante AHP.
- Evaluación de consistencia mediante CI y CR.
- Agregación de prioridades individuales utilizando AIP.
- Obtención de rankings finales de alternativas.
- Comparación objetiva de cadenas productivas.
- Soporte para decisiones grupales bajo entornos multicriterio.

---

## Salidas del Modelo

La ejecución del modelo de decisión genera los siguientes resultados:

- Pesos relativos de los criterios y alternativas evaluadas.
- Ratios de Consistencia (CR) para validar matemáticamente la coherencia de los juicios emitidos.
- Prioridades individuales estructuradas por cada experto o evaluador participante y agregación AIP.
- Ranking final objetivo de las cadenas productivas priorizadas.

---

## Instalación y Ejecución

Clonar el repositorio:

    git clone https://github.com/alanparraga/AHP-AIP-PROCOMPITE.git
    cd AHP-AIP-PROCOMPITE

Instalar dependencias:

    pip install -r requirements.txt

Ejecutar el motor de decisión:

    python AHP-AIP-PROCOMPITE.py

---

## Citación

Si utiliza este software o la metodología asociada en investigaciones académicas, trabajos técnicos o proyectos institucionales, por favor cite:

    Párraga-Condezo, J. A. (2026).
    AHP-AIP-PROCOMPITE: An Integrated AHP-AIP Decision Model for Prioritizing Productive Chains in Peruvian Subnational Governments
    Repositorio GitHub.
    https://github.com/alanparraga/AHP-AIP-PROCOMPITE

---

## Licencia

Este proyecto se distribuye bajo los términos de la licencia MIT. Consulte el archivo `LICENSE` para más detalles.

---

## Contacto

aparraga@aumentiva.com  
jose.parraga@unmsm.edu.pe
