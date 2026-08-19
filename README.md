
<p align="center">
  <img src="images/blackbeltbjjBanner.png" alt="Fabio Vieira Machado" width="100%">
</p>

## Using authentic data to better understand Earth's climate system.

----------------------------------------------------
# Hi, I'm Fabio
----------------------------------------------------

Climate Scientist • Oceanographer • Scientific Python Developer

Welcome to my GitHub profile!

I develop reproducible Python tools for climate variability, ocean–atmosphere interactions, and oceanographic data analysis, with a focus on ENSO variability, the Pacific Warm Pool, time-series analysis, statistical modelling, and scientific visualization. My goal is to combine scientific research, open-source software, and education to better understand climate variability and make authentic climate data more accessible.

----------------------------------------------------
## About Me
----------------------------------------------------

Featured Projects
### Coastal Engineering & Climate Adaptation (New Zealand)

#### 1. Mapeamento de Risco de Inundação Costeira e Elevação do Nível do Mar (Onerahi, Whangārei)
*   **Objetivo:** Identificar zonas de infraestrutura civil vulneráveis a cenários combinados de Elevação do Nível do Mar (SLR) do IPCC e ressacas de tempestade até o ano 2100 no Whangārei Harbour.
*   **Resultados de Engenharia:** Determinação do limite crítico de inundação a **3.00 metros**, revelando que as áreas mais baixas da simulação possuem alto risco de perda de ativos estruturais caso medidas de adaptação não sejam implementadas.
*   **Stack:** Python (`NumPy`, `Pandas`, `Matplotlib`).
*   [👉 Visualizar Código-Fonte](coastal_flooding_analysis.py) | [👉 Visualizar Mapa de Inundação](whangarei_coastal_flooding_map.png)

#### 2. Análise de Eventos Extremos de Ondas e Limites de Projeto (Bream Bay, Northland)
*   **Objetivo:** Estabelecer a linha de base do clima de ondas local, dando suporte aos limites de design de engenharia para infraestrutura costeira em Northland.
*   **Insights práticos:** Determinação do Percentil 95 ($H_s = 2.45m$) como limite de segurança operacional e mapeamento de picos de tempestade ($4.41m$) para cálculo de sobrevivência de ativos estruturais (marinas e quebra-mares).
*   **Stack:** Python (`NumPy`, `Pandas`, `Matplotlib`).
*   [👉 Visualizar Código-Fonte](wave_analysis.py) | [👉 Visualizar Gráfico de Engenharia](bream_bay_wave_analysis.png)

### ENSO Time-Series Analysis & SST Mapping
Professional Python pipeline for analysing OISST using global observational datasets.

*   **Methodology:** Processed global Sea Surface Temperature (SST) to identify spatial thermal patterns linked to ocean-atmosphere interactions, highlighting the historical 1998 Strong El Niño event.
*   **Technical Stack:** Python (`Xarray`, `NetCDF4`, `Cartopy` / `Matplotlib`, assisted by advanced AI prompt engineering).
*   [👉 View Climate Visualization](timeseries/ENSO_INDICES/wavelets/pwp_mascara/outputs/figures/methodological_domain/methodological_domain_figure_1998-03-31_el_nino.png)

![SST Map Visualization](timeseries/ENSO_INDICES/wavelets/pwp_mascara/outputs/figures/methodological_domain/methodological_domain_figure_1998-03-31_el_nino.png)


### Pacific Warm Pool (PWP) Dynamics & Wavelet Analysis
Investigating annual and interannual variability of the Pacific Warm Pool using advanced climate diagnostics, nonlinear detrending, and spectral decomposition.

*   **Methodology:** Applied Continuous Wavelet Transform (CWT) to isolate low-frequency variability, tracking physical shifts in the PWP centroid boundaries, total surface area, and zonal core migration.
*   **Algorithm Verification:** Developed a robust **Synthetic Validation Pipeline** featuring known multi-frequency signals and stochastic noise components to benchmark, calibrate, and verify the accuracy of the Wavelet spectral decomposition code before deploying it on raw observational datasets.
*   **Technical Stack:** Python (`Xarray`, `SciPy.signal`, `PyWavelets` / `Wavelet-Analysis`), Core Climate Diagnostics.

#### Spectral, Time-Series Visualizations, Climate Signal Diagnostics & Code Validation::
*   [👉 View Wavelet Power Spectrum - Longitude Core Shifts](timeseries/ENSO_INDICES/wavelets/pwp_mascara/outputs/figures/pwp_wavelet_tc/pwp_wavelet_tc_longitude.png)
*   [👉 View Wavelet Power Spectrum - PWP Total Area Expansion](timeseries/ENSO_INDICES/wavelets/pwp_mascara/outputs/figures/pwp_wavelet_tc/pwp_wavelet_tc_area.png) 
*   **Technical Stack:** Python (`Statsmodels.tsa.seasonal.STL`, `PyWavelets` / `SciPy.signal`, `Xarray`, `Matplotlib`).

#### 📊 
*   [👉 View Wavelet Power Spectrum - Longitude Core Shifts](timeseries/ENSO_INDICES/wavelets/pwp_mascara/outputs/figures/pwp_wavelet_tc/pwp_wavelet_tc_longitude.png)
*   [👉 View Wavelet Power Spectrum - PWP Total Area Expansion](timeseries/ENSO_INDICES/wavelets/pwp_mascara/outputs/figures/pwp_wavelet_tc/pwp_wavelet_tc_area.png)

### Climate Data for Education
Educational resources and interactive pipelines demonstrating how authentic, large-scale climate datasets can be used to teach advanced statistics, time-series decomposition, and data science.

*   **Methodology:** Developed curriculum-ready visualization workflows focusing on signal extraction. The core module demonstrates how to dissect raw climate signals into long-term secular trends and short-term interannual anomalies.
*   **Technical Stack:** Python (`Pandas`, `Statsmodels`, `Matplotlib`), Signal Decomposition, Climate Literacy.
*   [👉 View Educational Python Pipeline](wave_analysis/educational_pipeline.py)

#### Featured Classroom Visualization (Raw Signal, Trend & Anomalies):
This multi-panel diagnostic chart acts as a visual teaching aid to demonstrate climate variance, helping students isolate the underlying global warming trend from seasonal and interannual noise.

## Pacific Warm Pool (PWP) Dynamics & STL Decomposition
Investigating the annual and interannual variability of the Pacific Warm Pool (area and centroid longitude) using advanced climate diagnostics and non-linear signal processing.

*   **Methodology:** Implemented **STL Decomposition (Seasonal & Trend decomposition using LOESS)** to robustly decouple long-term climate change trends from seasonal cycles and stochastic anomalies in the PWP domain. 
*   **Technical Stack:** Python (`Statsmodels.tsa.seasonal.STL`, `Xarray`, `SciPy`, `Matplotlib`).

### Climate Signal Diagnostics (Raw, Trend & Anomalies):
*   [👉 View STL Decomposition - PWP Total Area Expansion](timeseries/ENSO_INDICES/wavelets/pwp_mascara/outputs/figures/pwp_stl/pwp_stl_area.png)
*   [👉 View STL Decomposition - Longitude Core Shifts](timeseries/ENSO_INDICES/wavelets/pwp_mascara/outputs/figures/pwp_stl/pwp_stl_longitude.png)
*   [👉 View STL Decomposition - PWP Total Area and Longitude](timeseries/ENSO_INDICES/wavelets/pwp_mascara/outputs/figures/pwp_stl/)
*   [👉 View Pipeline Code Verification - Synthetic Wavelet Validation Chart](timeseries/ENSO_INDICES/wavelets/pwp_mascara/outputs/figures/pwp_wavelet_tc/pwp_wavelet_tc_synthetic_validation.png)

----------------------------------------------------
## Research Interests
----------------------------------------------------

Climate variability
El Niño–Southern Oscillation (ENSO)
Pacific Warm Pool dynamics
Sea Surface Temperature (SST) analysis
Time-series analysis and forecasting
Wavelet analysis
Statistical modelling
Scientific computing with Python
Climate education using authentic datasets

----------------------------------------------------
## Featured Projects
----------------------------------------------------

ENSO Time-Series Analysis

Pacific Warm Pool

Climate Data for Education

### ENSO Time-Series Analysis

Professional Python pipeline for analysing and forecasting Niño SST indices.

---

## Pacific Warm Pool

Investigating annual and interannual variability of the Pacific Warm Pool.

Research tools investigating the spatial and temporal variability of the Pacific Warm Pool, including centroid analysis, wavelet methods, and climate diagnostics.

---

## Climate Data for Education

Educational resources demonstrating how authentic climate datasets can support the teaching of statistics and data science.

----------------------------------------------------
## Skills
----------------------------------------------------

## Programming

Python
MatLab
NavLab
Git
GitHub

## Scientific Python

NumPy
Pandas
SciPy
Statsmodels
Matplotlib

## Research Areas

Time-Series Analysis
Climate Data Analysis
Statistical Forecasting
Ocean–Atmosphere Interactions
Scientific Visualization
Phase diagram
Wavelet analysis

## More

VS Code
Jupyter
NOAA Climate Data
Machine Learning

----------------------------------------------------
## Current Work
----------------------------------------------------

Project: Warm Pool & ENSO Time-Series Analysis

## Scientific Workflow

Climate Data

↓

Quality Control

↓

Statistical Analysis

↓

Time-Series Modelling

↓

Wavelet analysis

↓

Forecasting

↓

Scientific Visualisation

↓

Publication

## Currently Working On

I am currently developing open and reproducible software for:

Daily Sea Surface Temperature analysis (1981–present)
ENSO monitoring and forecasting
Pacific Warm Pool variability
Climate time-series modelling
Scientific software for research and education

- Daily SST analysis (1981–present)
- ENSO monitoring forecasting
- Pacific Warm Pool dynamics
- Python climate analysis toolkit
- Educational resources using authentic climate datasets

----------------------------------------------------
GitHub Statistics
----------------------------------------------------

This GitHub account documents the development of scientific software, climate analysis workflows, and educational resources. Each repository is designed to be reproducible, well documented, and suitable for both research and teaching.

- contribution activity

- language usage

- repository statistics

- streaks

- trophies

These update automatically.

----------------------------------------------------
## Philosophy
----------------------------------------------------

I believe that scientific research should be:

Reproducible
Transparent
Open-source
Well documented
Accessible to researchers, educators, and students

----------------------------------------------------
##  Contact
----------------------------------------------------

Email: fvmachado.oceanscience@gmail.com./.

ORCID: https://orcid.org/0000-0003-0723-075X ./.

Google Scholar: https://scholar.google.com/citations?hl=en&user=RkFTqu8AAAAJ ./.

LinkedIn ./.


Outside research, I enjoy Brazilian Jiu-Jitsu, surfing, bodyboarding, and spending time at the beach
