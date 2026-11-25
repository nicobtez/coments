# Recorre assets/fuentes y assets/sonidos y genera assets/biblioteca.json
import json, os
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
tipos = {"fuentes": (".ttf", ".otf", ".woff", ".woff2"), "sonidos": (".mp3", ".wav", ".ogg", ".m4a", ".aac")}
out = {}
for carpeta, exts in tipos.items():
    d = os.path.join(base, carpeta); os.makedirs(d, exist_ok=True)
    out[carpeta] = [{"nombre": os.path.splitext(f)[0].replace("_", " ").replace("-", " ").strip(), "archivo": carpeta + "/" + f}
                    for f in sorted(os.listdir(d), key=str.lower) if f.lower().endswith(exts)]
with open(os.path.join(base, "biblioteca.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=2)
print("Biblioteca actualizada:")
for k, v in out.items():
    print(f"  {k}: {len(v)}", *[f"\n     - {x['nombre']}" for x in v])
