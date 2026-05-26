
🚀 Deployment Guide for PIER-VIBE (MARITIME-AI-01)

Package Deployment (PyPI)

```bash
pip install build twine
python -m build
twine upload dist/*
```

Docker Deployment

```bash
docker build -t pier-vibe:latest .
docker run -it --rm pier-vibe:latest --water-depth 25 --config configs/offshore_monopile.yaml
```

CI/CD Pipeline (GitLab CI)

The .gitlab-ci.yml includes: test, build, deploy, mirror

Trigger Deployment:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Netlify Deployment

```bash
cd Netlify/
netlify deploy --prod
```

Verification

```bash
pip install pier-vibe-engine
curl https://doi.org/10.5281/zenodo.20390646
curl https://pier-vibe.netlify.app
```

