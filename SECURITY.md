
Security Policy for PIER-VIBE (MARITIME-AI-01)

Supported Versions

Version Supported Notes
1.0.x ✅ Yes Current stable
< 1.0 ❌ No Pre-release only

Reporting a Vulnerability

Please report via email to: gitdeeper@gmail.com

Security Considerations

SSSE (Sub-Surface Scour)

· Input validation on sediment parameters
· Scour depth bounds checking

HSCE (Hydro-Structural Coupling)

· Wave and current velocity validation
· ALE mesh quality verification

EFGL (Fatigue Lock)

· Stress cycle validation
· Damage accumulation bounds

AI Modules (PINN Scour, PINN Fatigue, BSHI)

· Model input validation
· Prediction confidence bounds

Responsible Disclosure

1. Reporter notifies us privately
2. We confirm and develop fix (7-14 days)
3. Fix released with patch version
4. Public disclosure after 30 days
   EOF
   echo "✅ SECURITY.md"

17. setup.cfg

cat > setup.cfg << 'EOF'
[metadata]
license_files = LICENSE

[flake8]
max-line-length = 100
extend-ignore = E203, W503

[isort]
profile = black
line_length = 100

[mypy]
ignore_missing_imports = True
