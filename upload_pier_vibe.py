#!/usr/bin/env python3

"""PIER-VIBE v1.0.0 Upload - PyPI"""

import requests
import hashlib
import os
import glob

# التوكن الجديد لـ PIER-VIBE

print("="*60)
print("🌉 PIER-VIBE v1.0.0 Upload - PyPI")
print("="*60)
print("Predictive Intelligence Engine for Resonance, Vibration, and Integrity in Bridge Environments")
print("Domain: Systems Safety & Engineering (AI-augmented) · MARITIME-AI-01")
print("="*60)

# قراءة README.md
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
print(f"📄 README.md: {len(readme)} characters")

# البحث عن ملفات التوزيع
wheel_files = glob.glob("dist/*.whl")
tar_files = glob.glob("dist/*.tar.gz")

if not wheel_files and not tar_files:
    print("\n❌ No distribution files found. Building package...")
    os.system("python -m build")
    
    wheel_files = glob.glob("dist/*.whl")
    tar_files = glob.glob("dist/*.tar.gz")

print(f"\n📦 Distribution files:")
for f in wheel_files + tar_files:
    print(f"   • {os.path.basename(f)}")

upload_success = False

for filepath in wheel_files + tar_files:
    filename = os.path.basename(filepath)
    print(f"\n📤 Uploading: {filename}")

    # تحديد نوع الملف
    if filename.endswith('.tar.gz'):
        filetype = 'sdist'
        pyversion = 'source'
    else:
        filetype = 'bdist_wheel'
        pyversion = 'py3'

    # حساب الهاشات
    with open(filepath, 'rb') as f:
        content = f.read()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()

    # بيانات الرفع لـ PIER-VIBE
    data = {
        ':action': 'file_upload',
        'metadata_version': '2.1',
        'name': 'pier-vibe-engine',
        'version': '1.0.0',
        'filetype': filetype,
        'pyversion': pyversion,
        'md5_digest': md5_hash,
        'sha256_digest': sha256_hash,
        'description': readme,
        'description_content_type': 'text/markdown',
        'author': 'Samir Baladi',
        'author_email': 'gitdeeper@gmail.com',
        'license': 'MIT',
        'summary': 'PIER-VIBE: Predictive Intelligence Engine for Resonance, Vibration, and Integrity in Bridge Environments — A Critical Framework for Subsurface Scour Mechanics, Dynamic Wave-Structure Interaction, and Resonance Fatigue Governance in Offshore and Riverine Bridges',
        'home_page': 'https://pier-vibe.netlify.app',
        'requires_python': '>=3.9',
        'keywords': 'bridge scour, wave-structure interaction, resonance fatigue, fluid-structure-soil coupling, Navier-Stokes, Palmgren-Miner, physics-informed neural networks, structural health monitoring, offshore bridge safety, BSHI'
    }

    # رفع الملف
    with open(filepath, 'rb') as f:
        response = requests.post(
            'https://upload.pypi.org/legacy/',
            files={'content': (filename, f, 'application/octet-stream')},
            data=data,
            auth=('__token__', TOKEN),
            timeout=90,
            headers={'User-Agent': 'PIER-VIBE-Uploader/1.0.0'}
        )

    print(f"   Status: {response.status_code}")

    if response.status_code == 200:
        print("   ✅✅✅ SUCCESS!")
        upload_success = True
    else:
        print(f"   ❌ Error: {response.text[:300]}")
        if response.status_code == 403:
            print("\n   ⚠️ Permission denied. Please check:")
            print("      1. Token permissions (requires 'Upload' scope)")
            print("      2. Package name 'pier-vibe-engine' is available")
        elif response.status_code == 400:
            print("\n   ⚠️ Bad request. Please check metadata.")

print("\n" + "="*60)
if upload_success:
    print("✅ PIER-VIBE v1.0.0 uploaded successfully!")
    print("🔗 https://pypi.org/project/pier-vibe-engine/1.0.0/")
else:
    print("⚠️ Upload completed with some issues.")
    print("🔗 https://pypi.org/project/pier-vibe-engine/")
print("="*60)

print("\n📦 Install PIER-VIBE:")
print("   pip install pier-vibe-engine")
print("")
print("📖 Documentation:")
print("   https://pier-vibe.netlify.app")
print("")
print("🌉 Real-Time Bridge Dashboard:")
print("   https://pier-vibe.netlify.app/dashboard")
