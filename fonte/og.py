"""Gera public/og.jpg (1200x630): a prévia do link no WhatsApp, LinkedIn e afins.

Uso: .recorte-venv/bin/python fonte/og.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
FONTES = RAIZ / "node_modules" / "@fontsource"
W, H = 1200, 630
PAGINA = (12, 11, 20)


def degrade_vertical(tamanho, topo, meio, pe):
    w, h = tamanho
    g = Image.new("RGB", (1, h))
    for y in range(h):
        t = y / (h - 1)
        a, b, k = (topo, meio, t / 0.5) if t < 0.5 else (meio, pe, (t - 0.5) / 0.5)
        g.putpixel((0, y), tuple(round(a[i] + (b[i] - a[i]) * k) for i in range(3)))
    return g.resize((w, h))


def main() -> None:
    img = Image.new("RGB", (W, H), PAGINA)

    # halo violeta à direita
    halo = Image.new("L", (W, H), 0)
    ImageDraw.Draw(halo).ellipse((560, 40, 1160, 700), fill=120)
    halo = halo.filter(ImageFilter.GaussianBlur(110))
    img.paste(Image.new("RGB", (W, H), (96, 84, 255)), (0, 0), halo)

    # PORTFÓLIO gigante no degradê da logo
    anton = lambda tam: ImageFont.truetype(str(FONTES / "anton/files/anton-latin-400-normal.woff2"), tam)
    titulo = anton(250)
    caixa = ImageDraw.Draw(img).textbbox((0, 0), "PORTFÓLIO", font=titulo)
    tw = caixa[2] - caixa[0]
    mascara = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mascara).text(((W - tw) / 2 - caixa[0], 70 - caixa[1]), "PORTFÓLIO", font=titulo, fill=255)
    img.paste(degrade_vertical((W, H), (160, 132, 255), (91, 130, 245), (16, 57, 77)), (0, 0), mascara)

    d = ImageDraw.Draw(img)
    # logo e nome
    logo = Image.open(RAIZ / "fonte/logo-lr.png").convert("RGB").resize((72, 72), Image.LANCZOS)
    img.paste(logo, (64, 56))
    nome = anton(118)
    d.text((64, 330), "LEONARDO", font=nome, fill=(241, 239, 250))
    nb = d.textbbox((64, 330), "LEONARDO", font=nome)
    d.rounded_rectangle((nb[2] + 8, nb[3] - 26, nb[2] + 34, nb[3]), 4, fill=(47, 240, 200))
    sans = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    d.text((66, nb[3] + 26), "DESENVOLVEDOR FULL-STACK", font=sans, fill=(63, 230, 204))
    leve = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)
    d.text((66, nb[3] + 70), "Sistemas e sites sob medida · agenda, Pix, WhatsApp e IA", font=leve, fill=(172, 168, 190))

    img.save(RAIZ / "public/og.jpg", quality=88, optimize=True)
    print(RAIZ / "public/og.jpg")


if __name__ == "__main__":
    main()
