# Digital Monitoring Concept for Nano-Modified Asphalt Pavements

A lightweight Python prototype that connects published laboratory evidence on nano-modified Warm Mix Asphalt (WMA) with Building Information Modeling (BIM) asset management concepts. 

## Overview
Warm Mix Asphalt (WMA) allows production temperatures to be reduced by 30-40°C, lowering emissions but increasing vulnerability to moisture-induced stripping. Integrating nano-additives (e.g., nano-silica) enhances moisture resistance and dynamic modulus. 

This repository provides a digital-twin engine that transforms static laboratory performance parameters into a dynamic asset condition model. Using a customized decay algorithm based on simulated climatic stressors (precipitation and temperature), the script simulates moisture degradation (Tensile Strength Ratio - TSR) over a 5-year lifecycle. The output is structured for ingestion into 7D BIM environments (e.g., Autodesk Revit via Dynamo) for predictive maintenance visualization.

## Features
* **Object-Oriented Pavement Modeling:** Instantiates pavement segments with unique material properties derived from laboratory testing.
* **Climate Stress Simulation:** Synthesizes monthly temperature and precipitation data to calculate dynamic mechanical degradation.
* **BIM-Ready Export:** Generates standardized `.csv` and `.json` outputs mapped to structural asset IDs for seamless integration into structural health monitoring dashboards.

## Citation
If you utilize this code or conceptual framework in your research, please cite the associated technical report:

> Hasib, S. N. R. (2026). *From Laboratory Performance to Digital Monitoring: A Python-Based BIM / Digital-Twin Prototype for Nano-Modified Warm Mix Asphalt Pavements*. ResearchGate. DOI: 10.13140/RG.2.2.24448.19202
