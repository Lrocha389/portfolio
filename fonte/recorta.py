"""Recorta o fundo do retrato e gera o WebP do hero.

Uso:
  .recorte-venv/bin/python fonte/recorta.py fonte/foto.jpg [x0,y0,x1,y1] [apagar: x,y x,y ...]

O recorte opcional (em pixels da foto original) enquadra cabeça e ombros;
sem ele, usa a foto inteira. Sai em public/img/leonardo-perfil.webp (900 px de largura, com alfa)
e numa prévia PNG em fonte/foto-recorte.png.
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps
from rembg import new_session, remove

RAIZ = Path(__file__).resolve().parent.parent


def main() -> None:
    entrada = Path(sys.argv[1])
    original = ImageOps.exif_transpose(Image.open(entrada))
    ja_recortada = "A" in original.getbands()  # PNG já sem fundo: usa o alfa dele
    foto = original.convert("RGBA" if ja_recortada else "RGB")

    x0 = y0 = 0
    if len(sys.argv) > 2:
        x0, y0, x1, y1 = (int(v) for v in sys.argv[2].split(","))
        foto = foto.crop((x0, y0, x1, y1))

    recorte = foto if ja_recortada else remove(foto, session=new_session("u2net_human_seg"), post_process_mask=True)
    alfa = recorte.getchannel("A")

    # apaga uma área (a mão, por exemplo): polígono em pixels da foto original
    if len(sys.argv) > 3:
        pontos = [tuple(int(v) for v in par.split(",")) for par in sys.argv[3].split()]
        pontos = [(x - x0, y - y0) for x, y in pontos]
        borracha = Image.new("L", alfa.size, 0)
        ImageDraw.Draw(borracha).polygon(pontos, fill=255)
        borracha = borracha.filter(ImageFilter.GaussianBlur(14))
        alfa = Image.composite(Image.new("L", alfa.size, 0), alfa, borracha)

    # tira o halo claro da parede: encolhe a borda 2 px e suaviza
    alfa = alfa.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1.2))
    recorte.putalpha(alfa)

    # leve ajuste para assentar no fundo escuro da página
    rgb, alfa = recorte.convert("RGB"), recorte.getchannel("A")
    rgb = ImageEnhance.Contrast(rgb).enhance(1.08)
    rgb = ImageEnhance.Brightness(rgb).enhance(0.94)
    recorte = Image.merge("RGBA", (*rgb.split(), alfa))

    recorte.save(RAIZ / "fonte" / "foto-recorte.png")
    largura = 900
    altura = round(recorte.height * largura / recorte.width)
    final = recorte.resize((largura, altura), Image.LANCZOS)
    saida = RAIZ / "public" / "img" / "leonardo-perfil.webp"
    final.save(saida, "WEBP", quality=90, method=6)
    print(f"{saida} {largura}x{altura}")


if __name__ == "__main__":
    main()
