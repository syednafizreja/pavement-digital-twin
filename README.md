# pavement-digital-twin
# Digital Monitoring Concept for Nano-Modified Asphalt Pavements

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![DOI](https://img.shields.io/badge/DOI-10.13140%2FRG.2.2.24448.19202-blue)](https://doi.org/10.13140/RG.2.2.24448.19202)

A lightweight Python prototype that connects published laboratory evidence on nano-modified Warm Mix Asphalt (WMA) with Building Information Modeling (BIM) asset management concepts[cite: 4]. 

## Overview
Warm Mix Asphalt (WMA) allows production temperatures to be reduced by 30-40°C, lowering emissions but increasing vulnerability to moisture-induced stripping[cite: 100]. Integrating nano-additives (e.g., nano-silica) enhances moisture resistance and dynamic modulus[cite: 100]. 

This repository provides a digital-twin engine that transforms static laboratory performance parameters into a dynamic asset condition model. Using a customized decay algorithm based on simulated climatic stressors (precipitation and temperature), the script simulates moisture degradation (Tensile Strength Ratio - TSR) over a 5-year lifecycle. The output is structured for ingestion into 7D BIM environments (e.g., Autodesk Revit via Dynamo) for predictive maintenance visualization[cite: 115, 133].

## Features
* **Object-Oriented Pavement Modeling:** Instantiates pavement segments with unique material properties (Baseline TSR, decay coefficients) derived from laboratory testing.
* **Climate Stress Simulation:** Synthesizes monthly temperature and precipitation data to calculate dynamic mechanical degradation.
* **BIM-Ready Export:** Generates standardized `.csv` and `.json` outputs mapped to structural asset IDs for seamless integration into structural health monitoring dashboards.

## Installation & Usage
Clone the repository and run the simulation engine using standard Python libraries (`pandas`, `numpy`).

```bash
git clone [https://github.com/syednafizreja/pavement-digital-twin.git](https://github.com/syednafizreja/pavement-digital-twin.git)
cd pavement-digital-twin
python digital_twin_engine.py
