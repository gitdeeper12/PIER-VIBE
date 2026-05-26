
📦 Installation Guide for PIER-VIBE (MARITIME-AI-01)

Quick Install (PyPI)

```bash
pip install pier-vibe-engine
```

Install from Source

```bash
git clone https://github.com/gitdeeper12/PIER-VIBE.git
cd PIER-VIBE
pip install -e .
```

Verify Installation

```python
import pier_vibe
print(pier_vibe.__version__)  # 1.0.0
print(pier_vibe.__doi__)      # 10.5281/zenodo.20390646
```

```bash
python -c "from pier_vibe import BridgeGovernor; print('PIER-VIBE ready')"
```

Requirements

Package Version Required
Python ≥ 3.9
numpy ≥ 1.21.0
scipy ≥ 1.7.0
torch ≥ 2.0.0
xgboost ≥ 1.7.0

Launch Dashboard

```bash
streamlit run examples/streamlit_live.py
```

Dashboard: http://localhost:8501
