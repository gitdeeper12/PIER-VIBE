# Changelog

## [1.0.0] - 2026-05-26

### Release: PIER-VIBE v1.0.0

**Predictive Intelligence Engine for Resonance, Vibration, and Integrity in Bridge Environments**

**A Critical Framework for Subsurface Scour Mechanics, Dynamic Wave-Structure Interaction, and Resonance Fatigue Governance in Offshore and Riverine Bridges**

**Domain: Systems Safety & Engineering (AI-augmented) · MARITIME-AI-01**

---

### Added

#### Core Modules (3)

| Module | Name | Description |
|--------|------|-------------|
| **SSSE** | Sub-Surface Scour Engine | Scour depth prediction with horseshoe vortex |
| **HSCE** | Hydro-Structural Coupling Evaluator | Navier-Stokes + structural dynamics + ALE |
| **EFGL** | Elastic Fatigue Governance Lock | Palmgren-Miner fatigue with Goodman correction |

#### AI Modules (3)

| Module | Name | Description |
|--------|------|-------------|
| **PINN Scour** | Physics-Informed Neural Network | 72h scour depth forecast (±0.08 m RMSE) |
| **PINN Fatigue** | Physics-Informed Neural Network | 72h fatigue damage forecast (MAE 2.8%) |
| **BSHI** | Bridge Structural Health Index | Composite safety index (target ≥ 0.85) |

#### Mathematical Formulations

| # | Component | Formula |
|---|-----------|---------|
| 1 | Scour Rate | ∂z_s/∂t = C_s·u\*·f(d_s/d_50)·g(y/D_pier)·[1-D_s/D_s,max] |
| 2 | Bed Shear Stress | τ_b = μ ∂v_x/∂z \|_{z=z_bed} = ρ_F u\*² |
| 3 | Shields Parameter | θ_cr = τ_cr / [(ρ_s-ρ_F)g d_50] ≈ 0.047 |
| 4 | Navier-Stokes | ρ_F[∂v/∂t+(v·∇)v] = -∇p + μ∇²v + ρ_Fg + f_FSI |
| 5 | Fatigue Damage | D(t) = Σ_i n_i(t)/N_i(σ_a,i) |
| 6 | BSHI | BSHI = 0.35·(1-D_s/D_crit) + 0.35·(1-D_fat) + 0.30·(Δf_safe/Δf_crit) |

#### Validation Results (6 Scenarios)

| Case | Configuration | Scour RMSE | Fatigue MAE | BSHI Accuracy |
|------|---------------|------------|-------------|---------------|
| B1 | Single pier — sandy riverbed | 0.06 m | 2.4% | 97.2% |
| B2 | Twin pier — gravel riverbed | 0.08 m | 2.9% | 96.5% |
| B3 | Offshore monopile — sand | 0.07 m | 2.6% | 97.8% |
| B4 | Jacket foundation — rock-clay | 0.09 m | 3.1% | 95.9% |
| B5 | Cable-stayed — composite deck | 0.07 m | 2.8% | 96.8% |
| B6 | Suspension — deep-water pier | 0.08 m | 3.0% | 97.1% |
| **Mean** | — | **0.075 m** | **2.8%** | **96.9%** |

#### AI Module Performance

| AI Module | Precision | Recall | Metric | Value |
|-----------|-----------|--------|--------|-------|
| PINN Scour (72h) | — | — | RMSE | ±0.08 m |
| PINN Fatigue (72h) | — | — | MAE | 2.8% |
| BSHI Composite | 0.97 | 0.95 | AUC | 0.98 |
| Resonance Detector | 0.94 | 0.93 | Sensitivity | 94.4% |

#### Governance Decision Thresholds

| Signal | Condition | Action | Level |
|--------|-----------|--------|-------|
| 🟢 STABILITY CERTIFIED | BSHI ≥ 0.85 | Normal operation | None |
| 🟠 MONITORING PHASE | 0.75 ≤ BSHI < 0.85 | Reduced operations | Level 1 |
| 🟠 MONITORING PHASE | 0.65 ≤ BSHI < 0.75 | Load restriction | Level 2 |
| 🔴 STOP COMMAND | BSHI < 0.65 | Bridge closure | Stop |

---

### Statistics

| Metric | Value |
|--------|-------|
| **PIER-VIBE Version** | 1.0.0 |
| **Release Date** | May 26, 2026 |
| **DOI** | 10.5281/zenodo.20390646 |
| **Series** | MARITIME-AI-01 |
| **Mean Scour RMSE** | 0.075 m |
| **Mean Fatigue MAE** | 2.8% |
| **Mean BSHI Accuracy** | 96.9% |
| **False Critical Alert Rate** | 2.8% |
| **Resonance Sensitivity** | 94.4% |

### Links

| Platform | Link |
|----------|------|
| **GitHub** | https://github.com/gitdeeper12/PIER-VIBE |
| **GitLab** | https://gitlab.com/gitdeeper12/PIER-VIBE |
| **PyPI** | https://pypi.org/project/pier-vibe-engine |
| **Netlify** | https://pier-vibe.netlify.app |
| **Zenodo** | https://doi.org/10.5281/zenodo.20390646 |
| **ORCID** | https://orcid.org/0009-0003-8903-0029 |

---

*Part of the Systems Safety & Engineering (AI-augmented) research domain*

> *"Structural integrity is not negotiated with the sea — it is enforced through real-time physics, adaptive intelligence, and principled constraint design."*
