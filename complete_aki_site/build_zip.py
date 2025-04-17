#!/usr/bin/env python3
from zipfile import ZipFile
from pathlib import Path

# 1. Pfad zu deinem Projektordner (hier am Beispiel 'complete_aki_site')
project_dir = Path(".")

# 2. Admin-Ordner anlegen und CMS-Dateien schreiben
admin_dir = project_dir / "admin"
admin_dir.mkdir(exist_ok=True)

# 3. Netlify CMS Loader einbinden
(admin_dir / "index.html").write_text("""<!doctype html>
<html>
  <head><meta charset="utf-8"/><title>Admin-Bereich</title></head>
  <body><script src="https://unpkg.com/netlify-cms@^2.0.0/dist/netlify-cms.js"></script></body>
</html>""", encoding="utf-8")

# 4. CMS-Konfigurationsdatei erstellen
(admin_dir / "config.yml").write_text("""backend:
  name: git-gateway
  branch: main

media_folder: "images/uploads"
public_folder: "/images/uploads"

collections:
  - name: "manifest"
    label: "Manifest"
    files:
      - file: "index.html"
        label: "Manifest"
        name: "manifest"
        fields:
          - {label: "Text", name: "body", widget: "markdown"}""", encoding="utf-8")

# 5. ZIP-Archiv bauen
zip_path = Path("aki-rebellion-complete-with-cms.zip")
with ZipFile(zip_path, 'w') as zipf:
    for file in project_dir.rglob("*"):
        zipf.write(file, arcname=file.relative_to(project_dir))

print(f"🔖 ZIP erstellt: {zip_path.resolve()}")
