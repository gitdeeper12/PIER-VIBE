<div align="center">

# PIER-VIBE

### Predictive Intelligence Engine for Resonance, Vibration, and Integrity in Bridge Environments

**A Critical Framework for Subsurface Scour Mechanics, Dynamic Wave-Structure Interaction, and Resonance Fatigue Governance in Offshore and Riverine Bridges**

**An AI-Augmented Hydro-Structural Continuum Mechanics Framework for Bridge Pier Safety Governance**

---

[![PyPI version](https://img.shields.io/pypi/v/pier-vibe-engine?color=0D2B45&label=PyPI&logo=pypi&logoColor=white)](https://pypi.org/project/pier-vibe-engine)
[![PyPI downloads](https://img.shields.io/pypi/dm/pier-vibe-engine?color=1B4F7A&label=Downloads&logo=pypi&logoColor=white)](https://pypi.org/project/pier-vibe-engine/#files)
[![Python versions](https://img.shields.io/pypi/pyversions/pier-vibe-engine?color=306998&logo=python&logoColor=white)](https://pypi.org/project/pier-vibe-engine)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20390646-blue.svg)](https://doi.org/10.5281/zenodo.20390646)
[![OSF Preregistration](https://img.shields.io/badge/OSF-Registered-blue?logo=osf&logoColor=white)](https://doi.org/10.17605/OSF.IO/YKWEG)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0003-8903-0029)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Domain](https://img.shields.io/badge/Domain-Systems%20Safety%20%26%20Engineering-red)](https://doi.org/10.5281/zenodo.20390646)
[![Sub-domain](https://img.shields.io/badge/Sub--domain-MARITIME--AI--01-darkred)](https://doi.org/10.5281/zenodo.20390646)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange)](https://github.com/gitdeeper12/PIER-VIBE)

</div>

---

## 📌 Overview

**PIER-VIBE** is a fully coupled, AI-augmented hydro-structural continuum mechanics framework that treats **bridge structural safety as a continuously governed dynamic invariant** — not a static design property frozen at the completion of a finite element run.

> *"A bridge pier is not a static obstacle in water. It is a moving boundary-value problem embedded in a continuously evolving hydrodynamic and geotechnical field. PIER-VIBE formalizes and governs this evolution, enforcing structural integrity against subsurface scour, wave-structure resonance, and fatigue accumulation in real time."*

Contemporary bridge safety relies on periodic inspection cycles and static load ratings that cannot capture the nonlinear, spatiotemporally coupled dynamics of scour evolution, resonance emergence, and fatigue propagation. PIER-VIBE provides a principled three-module governance pipeline that classifies any bridge operational state in real time as:

| Signal | Safety Status | Action |
|---|---|---|
| 🟢 **STABILITY CERTIFIED** | `BSHI ≥ 0.85` | All constraints satisfied — normal operation |
| 🟠 **MONITORING PHASE** | `0.65 ≤ BSHI < 0.85` | Reduced operations + PINN scour forecast |
| 🔴 **STOP COMMAND** | `BSHI < 0.65` | Bridge closure + emergency inspection |

---

## 🗂️ Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Domain Positioning](#-domain-positioning)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [PIER-VIBE Pipeline](#-pier-vibe-pipeline)
- [Scoring & Safety Bounds](#-scoring--safety-bounds)
- [Platforms & Mirrors](#-platforms--mirrors)
- [Clone & Download](#-clone--download)
- [Citation](#-citation)
- [License](#-license)
- [Author](#-author)

---

## ✨ Key Features

- **Three-module coupled pipeline** — SSSE (Scour), HSCE (Hydro-Structural), EFGL (Fatigue Lock)
- **AI-augmented governance** — Physics-Informed Neural Network (PINN) for scour forecasting, PINN for fatigue accumulation, BSHI composite index
- **24–72 hour advance warning** — vs. 2–6 hours for conventional SHM systems
- **Closed-form + PINN scour depth prediction** — Melville-Coleman scour equation with PINN correction
- **Full fluid-structure-soil coupling** — Navier-Stokes + structural dynamics + Biot consolidation
- **Resonance frequency drift detection** — real-time natural frequency monitoring with 94.4% sensitivity
- **Global Bridge Structural Health Index (BSHI)** — weighted composite of scour, fatigue, and resonance safety margins
- **0.075 m RMSE scour prediction** — validated across 6 canonical bridge configurations
- **Full open-source distribution** — available across 11 platforms

---

## 🏛️ Domain Positioning

PIER-VIBE is the **fifth project** in the **Systems Safety & Engineering (AI-augmented)** domain portfolio, classified as **MARITIME-AI-01**.

| Project | Sub-classification | Core Safety Mechanism |
|---|---|---|
| **OSEF** | Aviation Safety Systems | AI-augmented flight envelope protection |
| **Limit Cycle Flight Dynamics** | Aerospace Engineering | Nonlinear dynamical stability certification |
| **DAMS-SLIP v1.1.1** | GEOTECH-AI-01 | AI-augmented seepage and piping governance |
| **TUNNEL-SHIELD v1.0.0** | GEOTECH-AI-02 | AI-augmented TBM excavation safety governance |
| **PIER-VIBE v1.0.0** | **MARITIME-AI-01** | **AI-augmented bridge scour and resonance governance** |

> The unifying principle across all five projects: **safety is a dynamical invariant enforced through physics-grounded AI governance, not a static design constant frozen at the point of commissioning.**

---

## 📁 Project Structure

```

PIER-VIBE/
│
├── pier_vibe/                              # Core Python package
│   ├── init.py                         # Package entry point & public API
│   ├── pipeline.py                         # Main PIER-VIBE governance pipeline
│   ├── safety.py                           # Safety certification & BSHI logic
│   │
│   ├── modules/                            # Three governing modules
│   │   ├── init.py
│   │   ├── ssse.py                         # Module 1: Sub-Surface Scour Engine
│   │   ├── hsce.py                         # Module 2: Hydro-Structural Coupling Evaluator
│   │   └── efgl.py                         # Module 3: Elastic Fatigue Governance Lock
│   │
│   ├── ai/                                 # AI augmentation components
│   │   ├── init.py
│   │   ├── pinn_scour.py                   # PINN: scour depth forecasting
│   │   ├── pinn_fatigue.py                 # PINN: fatigue accumulation forecasting
│   │   ├── bshi.py                         # Bridge Structural Health Index
│   │   └── weights/                        # Pre-trained model checkpoints
│   │       ├── pinn_scour_v1.pt
│   │       ├── pinn_fatigue_v1.pt
│   │       └── bshi_calibration.json
│   │
│   ├── fluid/                              # Fluid dynamics (Navier-Stokes)
│   │   ├── init.py
│   │   ├── navier_stokes.py                # Incompressible NS solver
│   │   ├── turbulence.py                   # k-ω SST turbulence closure
│   │   ├── wave_forces.py                  # Morison equation wave loading
│   │   └── horseshoe_vortex.py             # Pier-induced vortex dynamics
│   │
│   ├── structural/                         # Structural dynamics
│   │   ├── init.py
│   │   ├── eigenanalysis.py                # Natural frequency computation
│   │   ├── mode_shapes.py                  # Mode shape extraction
│   │   ├── damping.py                      # Structural damping matrix
│   │   └── frequency_drift.py              # Real-time frequency tracking
│   │
│   ├── scour/                              # SSSE subsystem
│   │   ├── init.py
│   │   ├── melville_coleman.py             # Scour rate equation
│   │   ├── bed_shear.py                    # Bed shear stress τ_b computation
│   │   ├── horseshoe.py                    # Horseshoe vortex amplification
│   │   └── equilibrium_depth.py            # HEC-18 equilibrium scour
│   │
│   ├── fatigue/                            # EFGL subsystem
│   │   ├── init.py
│   │   ├── palmgren_miner.py               # Cumulative damage D(t)
│   │   ├── rainflow.py                     # Cycle counting algorithm
│   │   ├── sn_curves.py                    # S-N curve for detail categories
│   │   └── goodman.py                      # Mean stress correction
│   │
│   ├── coupling/                           # Fluid-Structure-Soil coupling
│   │   ├── init.py
│   │   ├── ale.py                          # Arbitrary Lagrangian-Eulerian
│   │   ├── added_mass.py                   # Hydrodynamic added mass M_a
│   │   ├── added_damping.py                # Hydrodynamic added damping C_a
│   │   └── biot.py                         # Biot consolidation (soil coupling)
│   │
│   ├── fem/                                # Finite element discretization
│   │   ├── init.py
│   │   ├── mesh.py                         # Adaptive hybrid mesh
│   │   ├── amr.py                          # Adaptive mesh refinement
│   │   ├── boundary_conditions.py          # In-situ stress, wave BC
│   │   ├── solver.py                       # Nonlinear FEM solver
│   │   └── convergence.py                  # Convergence criteria
│   │
│   ├── monitoring/                         # Real-time monitoring layer
│   │   ├── init.py
│   │   ├── accelerometer.py                # Tri-axial accelerometer parser
│   │   ├── strain_gauge.py                 # Vibrating-wire strain gauge
│   │   ├── piezometer.py                   # Foundation pore pressure
│   │   ├── scour_sensor.py                 # Sonar/MR/TDR scour sensor
│   │   ├── meteorological.py               # Wind, wave, current sensors
│   │   └── aggregator.py                   # Multi-sensor temporal aggregation
│   │
│   ├── kalman/                             # Kalman filter state estimation
│   │   ├── init.py
│   │   ├── filter.py                       # Kalman filter implementation
│   │   ├── measurement.py                  # Measurement model H
│   │   └── covariance.py                   # Error covariance P and R
│   │
│   └── utils/                              # Shared utilities
│       ├── init.py
│       ├── metrics.py                      # BSHI, scour RMSE, fatigue MAE
│       ├── validators.py                   # Input validation & safety bounds
│       └── constants.py                    # Canonical parameter registry
│
├── visualization/                          # Real-time visualization subsystem
│   ├── init.py
│   ├── app.py                              # Streamlit application entry point
│   ├── dashboard.py                        # Main bridge safety dashboard layout
│   ├── scour_map.py                        # Scour hole evolution heatmap
│   ├── frequency_plot.py                   # Natural frequency drift plot
│   ├── fatigue_damage.py                   # Cumulative damage visualization
│   └── components/
│       ├── signal_panel.py                 # 🔴🟠🟢 safety signal panel
│       ├── forecast_panel.py               # PINN scour + fatigue forecast
│       └── sensor_live.py                  # Live sensor reading panel
│
├── archival/                               # Operational data archival
│   ├── init.py
│   ├── writer.py                           # Append-only JSON/CSV record writer
│   ├── checksum.py                         # SHA-256 tamper-evidence layer
│   └── partitioner.py                      # Per-bridge time-window partitioner
│
├── simulation/                             # Benchmark simulation environment
│   ├── init.py
│   ├── scenarios.py                        # Six canonical bridge configurations
│   ├── environmental_models.py             # Wave, current, wind profiles
│   ├── benchmarks.py                       # Full validation suite runner
│   ├── parameters.py                       # Canonical v1.0.0 parameter registry
│   └── results/                            # Pre-computed validation outputs
│       ├── B1_single_pier_sand.json
│       ├── B2_twin_pier_gravel.json
│       ├── B3_offshore_monopile.json
│       ├── B4_jacket_foundation.json
│       ├── B5_cable_stayed.json
│       └── B6_suspension_deepwater.json
│
├── examples/                               # Usage examples & tutorials
│   ├── quickstart.py                       # Minimal working example
│   ├── basic_safety_check.ipynb            # Jupyter: single-bridge safety evaluation
│   ├── scour_scenario.ipynb                # Jupyter: flood-induced scour scenario
│   ├── resonance_scenario.ipynb            # Jupyter: wind-induced resonance scenario
│   ├── fatigue_scenario.ipynb              # Jupyter: fatigue accumulation scenario
│   ├── streamlit_live.py                   # Launch real-time bridge dashboard
│   └── ai_forecast_demo.py                 # PINN scour + fatigue demonstration
│
├── tests/                                  # Unit and integration tests
│   ├── test_ssse.py
│   ├── test_hsce.py
│   ├── test_efgl.py
│   ├── test_pinn_scour.py
│   ├── test_pinn_fatigue.py
│   ├── test_bshi.py
│   ├── test_kalman.py
│   ├── test_pipeline.py
│   └── test_archival.py
│
├── docs/                                   # Documentation source
│   ├── architecture.md                     # Pipeline & module architecture reference
│   ├── mathematics.md                      # Full hydro-structural mathematical formalism
│   ├── ai_modules.md                       # PINN scour / PINN fatigue documentation
│   ├── scour_mechanics.md                  # Scour rate equation & HEC-18 guide
│   ├── governance.md                       # BSHI governance protocol reference
│   └── api_reference.md                    # Full Python API reference
│
├── paper/                                  # Research paper artifacts
│   ├── PIER-VIBE_Research_Paper.pdf        # Published paper (PDF)
│   ├── PIER-VIBE_Research_Paper.docx       # Editable Word version
│   └── figures/
│       ├── pipeline_diagram.svg
│       ├── scour_hole_evolution.svg
│       ├── frequency_drift.svg
│       └── ai_forecast_validation.svg
│
├── .gitlab-ci.yml                          # GitLab CI/CD pipeline
├── .github/                                # GitHub Actions workflows
│   └── workflows/
│       ├── tests.yml
│       └── publish.yml
├── pyproject.toml                          # Build system configuration
├── setup.cfg                               # Package metadata
├── requirements.txt                        # Runtime dependencies
├── requirements-dev.txt                    # Development dependencies
├── CHANGELOG.md                            # Version history
├── CONTRIBUTING.md                         # Contribution guidelines
├── CODE_OF_CONDUCT.md
├── AUTHORS.md                              # Author and contributor registry
├── LICENSE                                 # MIT License
└── README.md                               # This file

```

---

## 🚀 Quick Start

### Installation

```bash
# Install from PyPI
pip install pier-vibe-engine

# Install from source
git clone https://github.com/gitdeeper12/PIER-VIBE.git
cd PIER-VIBE
pip install -e .
```

Minimal Example

```python
from pier_vibe import BridgeGovernor

# Initialize the safety governor
governor = BridgeGovernor(
    bridge_config="configs/offshore_monopile.yaml",
    water_depth_m=25.0,
    sensor_stream="live"    # or path to historical CSV
)

# Run full PIER-VIBE pipeline
result = governor.evaluate()

print(result.signal)              # "STABILITY_CERTIFIED" | "MONITORING" | "STOP_COMMAND"
print(result.bshi)                # Bridge Structural Health Index [0, 1]
print(result.scour_depth_m)       # Current scour depth (metres)
print(result.fatigue_damage)      # Cumulative fatigue damage D(t)
print(result.frequency_drift_pct) # Natural frequency drift (%)
print(result.governance_level)    # "none" | "level_1" | "level_2" | "stop"
```

With Full AI Augmentation

```python
from pier_vibe import BridgeGovernor
from pier_vibe.ai import PINNScourForecaster, PINNFatigueForecaster, BSHICalculator

governor = BridgeGovernor(
    bridge_config="configs/offshore_monopile.yaml",
    ai_modules={
        "scour_pinn":   PINNScourForecaster.from_pretrained("default"),
        "fatigue_pinn": PINNFatigueForecaster.from_pretrained("default"),
        "bshi":         BSHICalculator.from_pretrained("default"),
    }
)

result = governor.evaluate(forecast_hours=72)
print(result.scour_forecast_72h)    # Scour depth at T+72h (PINN prediction)
print(result.fatigue_forecast_72h)  # Fatigue damage at T+72h (PINN prediction)
print(result.resonance_risk)        # "normal" | "elevated" | "critical"
```

Flood-Induced Scour Scenario

```python
from pier_vibe import BridgeGovernor
from pier_vibe.simulation import FloodScenario

scenario = FloodScenario(
    peak_velocity_mps=3.5,
    duration_hours=72,
    bridge_config="configs/single_pier_sand.yaml"
)

governor = BridgeGovernor(bridge_config="configs/single_pier_sand.yaml")
results = governor.run_transient(scenario, dt_hours=0.5, T_max_hours=120)

print(results.max_scour_depth)     # 2.8 m (equilibrium depth)
print(results.scour_warning_hours) # 48 hours before critical depth
print(results.bshi_min)            # Minimum BSHI during event
```

Launch Real-Time Bridge Safety Dashboard

```bash
# Start Streamlit safety monitoring dashboard
streamlit run examples/streamlit_live.py

# Dashboard available at: http://localhost:8501
# Live scour hole heatmap · Frequency drift plot · Fatigue damage · 🔴🟠🟢 signal
```

---

🧩 PIER-VIBE Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Sensor Telemetry: Accelerometers · Strain Gauges · Piezometers · Sonar │
│  Environmental: Wind Speed · Wave Height · Current Profile · Water Level│
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
         ┌─────────────────────┼────────────────────┐
         │                     │                    │
         ▼                     ▼                    ▼
    SSSE                  HSCE                  EFGL
    Sub-Surface Scour    Hydro-Structural      Elastic Fatigue
    Engine               Coupling Evaluator    Governance Lock
    Melville-Coleman     Navier-Stokes +       Palmgren-Miner
    Horseshoe Vortex     Added Mass/Damping    Rainflow Counting
    Equilibrium Depth    Eigenfrequency        S-N Curves
         │                     │                    │
         └─────────────────────┼────────────────────┘
                               │
         ┌─────────────────────┼────────────────────┐
         │                     │                    │
         ▼                     ▼                    ▼
    PINN Scour           PINN Fatigue         BSHI Calculator
    Depth Forecast       Damage Forecast      Composite Index
    Physics-constrained  Physics-constrained  w_s·w_f·w_r
    24-72h horizon       72h MAE < 3.1%       BSHI ≥ 0.85
         │                     │                    │
         └─────────────────────┼────────────────────┘
                               │
                               ▼
                    Kalman Filter State
                    Sensor Fusion + Physics Model
                    Minimum-variance estimate
                               │
                               ▼
                    BSHI Functional
                    BSHI = w_s·(1-D_s/D_crit) + w_f·(1-D_fat) + w_r·Δf_safe/Δf_crit
                    w_s=0.35  w_f=0.35  w_r=0.30
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
             Safety Signal         Archival & Dashboard
             🔴🟠🟢                JSON/CSV + SHA-256
             Bridge Closure        Streamlit + Plotly
```

Module Descriptions

# Module Governing Equation Description
1 SSSE ∂z_s/∂t = C_s·u\*·f(d_s/d_50)·g(y/D_pier)·[1-D_s/D_s,max] Melville-Coleman scour rate with horseshoe vortex amplification
2 HSCE ρ_F[∂v/∂t+(v·∇)v] = -∇p + μ∇²v + ρ_Fg + f_FSI Navier-Stokes with ALE fluid-structure coupling
3 EFGL D(t) = Σ_i n_i(t)/N_i(σ_a,i) Palmgren-Miner cumulative fatigue with Goodman correction
AI-1 PINN Scour L = λ_data·L_data + λ_phys·L_phys Physics-constrained scour forecasting from sensor data
AI-2 PINN Fatigue L = λ_data·L_data + λ_phys·(dD/dt - Palmgren-Miner RHS) Physics-constrained fatigue accumulation forecast
AI-3 BSHI BSHI = w_s·(1-D_s/D_crit) + w_f·(1-D_fat) + w_r·Δf_safe/Δf_crit Composite bridge structural health index

---

📊 Scoring & Safety Bounds

```
Safety certification criteria:
  BSHI     (Bridge Structural Health Index)                    ≥  0.85
  D_s       (Current scour depth)                              ≤  D_s,crit
  D_fat     (Cumulative fatigue damage)                        ≤  0.80
  Δf_safe   (Frequency separation from excitation)             ≥  Δf_crit

BSHI functional form:
  BSHI = 0.35·(1 - D_s/D_s,crit) + 0.35·(1 - D_fat) + 0.30·(Δf_safe/Δf_crit)

Scour depth (Melville-Coleman):
  ∂z_s/∂t = C_s · u\*(t) · f(d_s/d_50) · g(y/D_pier) · [1 - D_s/D_s,max]

Critical bed shear stress (Shields):
  τ_cr = θ_cr · (ρ_s - ρ_F) · g · d_50,  θ_cr ≈ 0.047
```

Benchmark validation results (v1.0.0):

Case Configuration Scour RMSE Fatigue MAE BSHI Accuracy Resonance Sensitivity
B1 Single pier — sandy riverbed 0.06 m 2.4% 97.2% 94.8%
B2 Twin pier — gravel riverbed 0.08 m 2.9% 96.5% 93.7%
B3 Offshore monopile — sand 0.07 m 2.6% 97.8% 95.1%
B4 Jacket foundation — rock-clay 0.09 m 3.1% 95.9% 92.8%
B5 Cable-stayed — composite deck 0.07 m 2.8% 96.8% 94.6%
B6 Suspension — deep-water pier 0.08 m 3.0% 97.1% 95.3%
Mean — 0.075 m 2.8% 96.9% 94.4%

AI module performance:

AI Module Precision Recall AUC / MAE False Alarm Rate
PINN Scour Depth (72h) — — ±0.08 m (RMSE) N/A
PINN Fatigue Damage (72h) — — 2.8% (MAE) N/A
BSHI Composite Index 0.97 0.95 0.98 (AUC) 2.8%
Resonance Drift Detector 0.94 0.93 0.96 (AUC) 3.1%

Governance decision thresholds:

Level Condition Action Escalation
🟢 Certified BSHI ≥ 0.85 Normal operation None
🟠 Level 1 0.75 ≤ BSHI < 0.85 Reduced operations + PINN forecast Monitor hourly
🟠 Level 2 0.65 ≤ BSHI < 0.75 Load restriction + scour countermeasures Alert engineer
🔴 Stop BSHI < 0.65 Bridge closure + emergency inspection Immediate action

---

🌐 Platforms & Mirrors

Platform URL Role
🐙 GitHub (Primary) github.com/gitdeeper12/PIER-VIBE Source code, issues, PRs
🦊 GitLab (Mirror) gitlab.com/gitdeeper12/PIER-VIBE CI/CD mirror
🪣 Bitbucket (Mirror) bitbucket.org/gitdeeper-12/PIER-VIBE Enterprise mirror
🏔️ Codeberg (Mirror) codeberg.org/gitdeeper12/PIER-VIBE Open-source community
📦 PyPI pypi.org/project/pier-vibe-engine Python package distribution
🔬 Zenodo doi.org/10.5281/zenodo.20390646 Citable DOI, paper & data
📋 OSF Project osf.io/fxthu Research project registry
📝 OSF Preregistration doi.org/10.17605/OSF.IO/YKWEG Pre-registered study protocol
🌐 Website pier-vibe.netlify.app Live documentation & dashboard
🧑‍🔬 ORCID orcid.org/0009-0003-8903-0029 Researcher identity
🗄️ Internet Archive archive.org/details/osf-registrations-ykweg-v1 Permanent archival copy

🌐 Official Website Pages

Page URL
Homepage pier-vibe.netlify.app
Dashboard pier-vibe.netlify.app/dashboard
Results pier-vibe.netlify.app/results
Documentation pier-vibe.netlify.app/documentation

---

🔄 Clone & Download

Git Clone

```bash
# GitHub (Primary)
git clone https://github.com/gitdeeper12/PIER-VIBE.git

# GitLab (Mirror)
git clone https://gitlab.com/gitdeeper12/PIER-VIBE.git

# Bitbucket (Mirror)
git clone https://bitbucket.org/gitdeeper-12/PIER-VIBE.git

# Codeberg (Mirror)
git clone https://codeberg.org/gitdeeper12/PIER-VIBE.git
```

Direct ZIP Download

Source Link
GitHub PIER-VIBE-main.zip
GitLab PIER-VIBE-main.zip
Bitbucket PIER-VIBE-main.zip
Codeberg PIER-VIBE-main.zip
PyPI files pypi.org/project/pier-vibe-engine/#files
Zenodo record doi.org/10.5281/zenodo.20390646

---

📖 Citation

If PIER-VIBE contributes to your research, please cite using one of the following formats.

📦 PyPI Package

```bibtex
@software{baladi2026piervibe_pypi,
  author       = {Baladi, Samir},
  title        = {{PIER-VIBE}: Predictive Intelligence Engine for Resonance,
                  Vibration, and Integrity in Bridge Environments},
  year         = {2026},
  version      = {1.0.0},
  publisher    = {Python Package Index},
  url          = {https://pypi.org/project/pier-vibe-engine},
  note         = {Python package, MIT License,
                  Systems Safety \& Engineering (AI-augmented)}
}
```

🔬 Zenodo Archive (Paper & Data)

```bibtex
@dataset{baladi2026piervibe_zenodo,
  author       = {Baladi, Samir},
  title        = {{PIER-VIBE}: Predictive Intelligence Engine for Resonance,
                  Vibration, and Integrity in Bridge Environments —
                  Research Paper and Simulation Data},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.20390646},
  url          = {https://doi.org/10.5281/zenodo.20390646},
  note         = {Bridge Engineering Core · FSI · Systems Safety}
}
```

📝 OSF Preregistration

```bibtex
@misc{baladi2026piervibe_osf,
  author       = {Baladi, Samir},
  title        = {{PIER-VIBE} Framework: Pre-registered Study Protocol for
                  AI-Augmented Structural Integrity Governance in
                  Offshore and Riverine Bridges},
  year         = {2026},
  publisher    = {Open Science Framework},
  doi          = {10.17605/OSF.IO/YKWEG},
  url          = {https://doi.org/10.17605/OSF.IO/YKWEG},
  note         = {OSF Preregistration}
}
```

📄 Research Paper

```bibtex
@article{baladi2026piervibe,
  author       = {Baladi, Samir},
  title        = {{PIER-VIBE}: A Critical Framework for Subsurface Scour Mechanics,
                  Dynamic Wave-Structure Interaction, and Resonance Fatigue
                  Governance in Offshore and Riverine Bridges},
  year         = {2026},
  month        = {May},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.20390646},
  url          = {https://doi.org/10.5281/zenodo.20390646},
  note         = {Ronin Institute / Rite of Renaissance,
                  Systems Safety \& Engineering (AI-augmented)}
}
```

APA (inline)

Baladi, S. (2026). PIER-VIBE: A Critical Framework for Subsurface Scour Mechanics, Dynamic Wave-Structure Interaction, and Resonance Fatigue Governance in Offshore and Riverine Bridges (Version 1.0.0). Zenodo. https://doi.org/10.5281/zenodo.20390646

---

📜 License

This project is licensed under the MIT License — see the LICENSE file for details.

```
MIT License

Copyright (c) 2026 Samir Baladi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

👤 Author

Samir Baladi
Interdisciplinary AI Researcher — Neural Engineering, Computational Systems Safety & Bridge Engineering
Ronin Institute / Rite of Renaissance

Contact Link
📧 Email gitdeeper@gmail.com
🧑‍🔬 ORCID 0009-0003-8903-0029
🐙 GitHub github.com/gitdeeper12
🌐 Website pier-vibe.netlify.app

---

<div align="center">

Systems Safety & Engineering (AI-augmented) · MARITIME-AI-01 · Version 1.0.0 · May 2026

https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20390646-blue.svg
https://img.shields.io/pypi/v/pier-vibe-engine?color=0D2B45
https://img.shields.io/badge/License-MIT-yellow.svg

"Structural integrity is not negotiated with the sea — it is enforced through real-time physics, adaptive intelligence, and principled constraint design."

</div>
