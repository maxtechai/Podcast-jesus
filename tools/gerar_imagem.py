#!/usr/bin/env python3
"""Gera imagens com a API da Agnes (OpenAI-compatível).

Uso:
  python3 tools/gerar_imagem.py <nome_do_prompt> [--size 1536x1024] [--model agnes-image-2.5-flash]
  python3 tools/gerar_imagem.py --list
  python3 tools/gerar_imagem.py jesus_estudio --ref imagens/jesus_retrato.png

--ref usa uma imagem como referência (mesmo rosto/roupa/estilo) com o modelo
agnes-image-2.0-flash. Use sempre o retrato do personagem como referência.

Os prompts ficam em tools/prompts.json. A imagem é salva em imagens/<nome>.png.
A chave vem de AGNES_API_KEY (no ambiente na nuvem, o proxy injeta a chave
sozinho: rode com AGNES_API_KEY=proxy-injected).
"""
import argparse
import base64
import json
import os
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
API = "https://apihub.agnes-ai.com/v1/images/generations"


def main():
    prompts = json.loads((ROOT / "tools" / "prompts.json").read_text(encoding="utf-8"))
    ap = argparse.ArgumentParser()
    ap.add_argument("name", nargs="?")
    ap.add_argument("--size", default="1536x1024")
    ap.add_argument("--model", default="agnes-image-2.5-flash")
    ap.add_argument("--suffix", default="", help="sufixo no nome do arquivo (variações)")
    ap.add_argument("--ref", action="append", default=[], help="imagem de referência (pode repetir)")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    if a.list or not a.name:
        print("\n".join(k for k in prompts if not k.startswith("_")))
        return
    key = os.environ.get("AGNES_API_KEY")
    if not key:
        sys.exit("Defina AGNES_API_KEY")

    prompt = prompts["_style"] + " " + prompts[a.name]
    payload = {"model": a.model, "prompt": prompt, "n": 1,
               "size": a.size, "response_format": "b64_json"}
    if a.ref:
        prompt = ("Keep this exact same stylized 3D animated character, same face, hair, "
                  "clothes and 3D animation style. " + prompt)
        mime = {".png": "image/png", ".webp": "image/webp"}
        payload.update(model="agnes-image-2.0-flash", prompt=prompt, image=[
            f"data:{mime.get(pathlib.Path(r).suffix.lower(), 'image/jpeg')};base64,"
            + base64.b64encode(pathlib.Path(r).read_bytes()).decode() for r in a.ref])
    body = json.dumps(payload).encode()
    req = urllib.request.Request(API, data=body, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=600) as r:
        data = json.load(r)["data"][0]

    out = ROOT / "imagens" / f"{a.name}{a.suffix}.png"
    out.parent.mkdir(exist_ok=True)
    out.write_bytes(base64.b64decode(data["b64_json"]))
    print(out)


if __name__ == "__main__":
    main()
