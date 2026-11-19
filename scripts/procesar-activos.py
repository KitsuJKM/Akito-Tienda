#!/usr/bin/env python3
"""
Procesa los originales de `Akito/` y genera los activos optimizados en `public/assets/`.

Uso:  python3 scripts/procesar-activos.py
Requisitos: Pillow (con soporte WebP) y NumPy.

Técnica de transparencias (logos e iconos):
  Los JPG traen la marca sobre un fondo liso (marfil o azul). En vez de "borrar" un
  color con umbral duro (que deja halos), se estima el alfa de cada píxel proyectando
  su color sobre el segmento fondo→tinta:  a = <p - fondo, tinta - fondo> / |tinta - fondo|²
  Después se fija el RGB al color exacto de marca de la tinta más cercana. Así los bordes
  conservan su suavizado (anti-aliasing) pero sin restos del fondo original, y se ven
  limpios sobre el color destino (marfil en cabecera, azul en footer).
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "Akito"
DESTINO = RAIZ / "public" / "assets"

# Paleta oficial (manual de identidad)
MARFIL = (0xFA, 0xF7, 0xF2)
AZUL = (0x1A, 0x22, 0x38)
CARMESI = (0xC8, 0x1E, 0x2B)


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def abrir(nombre: str) -> Image.Image:
    return Image.open(ORIGEN / nombre).convert("RGB")


def guardar_webp(img: Image.Image, nombre: str, calidad: int = 80) -> None:
    img.save(DESTINO / nombre, "WEBP", quality=calidad, method=6)
    print(f"  {nombre:28s} {img.width}×{img.height}")


def guardar_png(img: Image.Image, nombre: str, paleta: bool = False) -> None:
    # Las marcas aisladas solo tienen 1–2 tonos con distintos niveles de alfa:
    # una paleta de 256 entradas las reproduce sin pérdida visible y pesa ~5× menos.
    if paleta:
        img = img.quantize(colors=256, method=Image.FASTOCTREE, dither=Image.NONE)
    img.save(DESTINO / nombre, "PNG", optimize=True)
    print(f"  {nombre:28s} {img.width}×{img.height}")


def redimensionar_ancho(img: Image.Image, ancho: int) -> Image.Image:
    alto = round(img.height * ancho / img.width)
    return img.resize((ancho, alto), Image.LANCZOS)


def color_fondo(img: Image.Image, caja) -> np.ndarray:
    """Mediana del color en una zona sin marca (estable frente a la textura del papel)."""
    zona = np.asarray(img.crop(caja), dtype=np.float32).reshape(-1, 3)
    return np.median(zona, axis=0)


def aislar(img: Image.Image, fondo, tintas, destino_rgb, umbral=(0.10, 0.85)) -> Image.Image:
    """
    Devuelve una imagen RGBA con la marca aislada.
    - fondo: color RGB del fondo medido en el original.
    - tintas: colores RGB de cada tinta tal como aparecen en el original.
    - destino_rgb: color de marca exacto que se asigna a cada tinta.
    - umbral: alfa por debajo del primer valor -> 0 (textura/ruido JPG);
              por encima del segundo -> 1 (núcleo sólido). Entre ambos, rampa lineal.
    """
    p = np.asarray(img, dtype=np.float32)
    f = np.asarray(fondo, dtype=np.float32)
    d = p - f

    alfas, distancias = [], []
    for t in tintas:
        v = np.asarray(t, dtype=np.float32) - f
        a = (d @ v) / float(v @ v)
        alfas.append(np.clip(a, 0, 1))
        # Distancia del píxel a la recta fondo→tinta: decide a qué tinta pertenece
        resto = d - a[..., None] * v
        distancias.append(np.linalg.norm(resto, axis=-1))

    idx = np.argmin(np.stack(distancias), axis=0)
    alfa = np.take_along_axis(np.stack(alfas), idx[None], axis=0)[0]

    lo, hi = umbral
    alfa = np.clip((alfa - lo) / (hi - lo), 0, 1)

    salida = np.zeros((*alfa.shape, 4), dtype=np.uint8)
    for i, rgb in enumerate(destino_rgb):
        salida[idx == i, :3] = rgb
    salida[..., 3] = np.round(alfa * 255).astype(np.uint8)
    return Image.fromarray(salida, "RGBA")


def recortar_a_contenido(img: Image.Image, margen: int) -> Image.Image:
    """Recorta al área con alfa > 0 y añade un margen transparente uniforme."""
    caja = img.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox()
    img = img.crop(caja)
    lienzo = Image.new("RGBA", (img.width + 2 * margen, img.height + 2 * margen), (0, 0, 0, 0))
    lienzo.paste(img, (margen, margen))
    return lienzo


def ajustar_ancho_rgba(img: Image.Image, ancho: int) -> Image.Image:
    """Redimensiona en alfa premultiplicado para no oscurecer ni aclarar los bordes."""
    alto = round(img.height * ancho / img.width)
    return img.convert("RGBa").resize((ancho, alto), Image.LANCZOS).convert("RGBA")


# ---------------------------------------------------------------------------
# 1. Hero: viñetas del banner (3168 × 1344)
# ---------------------------------------------------------------------------
def hero():
    print("Hero")
    banner = abrir("Banner Akito Anime referencia.jpg")
    assert banner.size == (3168, 1344), banner.size

    # Escritorio / tableta: paneles a altura completa.
    # Izquierda: 25 % (x 0–792). El texto «Conectando…» empieza en x≈850.
    # Derecha: 20 % (x 2534–3168). El texto termina en x≈2322.
    izq = banner.crop((0, 0, 792, 1344))
    der = banner.crop((2534, 0, 3168, 1344))
    for ancho in (396, 792):
        guardar_webp(redimensionar_ancho(izq, ancho), f"hero-left-{ancho}.webp")
    for ancho in (317, 634):
        guardar_webp(redimensionar_ancho(der, ancho), f"hero-right-{ancho}.webp")

    # Móvil: franja de 144 px de alto con las dos manos enfrentadas (proporción 6:5).
    izq_movil = banner.crop((0, 480, 720, 1080))     # caja y manos que entregan
    der_movil = banner.crop((2560, 520, 3168, 1027))  # manos que esperan
    for img, base in ((izq_movil, "hero-left-movil"), (der_movil, "hero-right-movil")):
        guardar_webp(img.resize((346, 288), Image.LANCZOS), f"{base}.webp")


# ---------------------------------------------------------------------------
# 2. Logos: firma positiva (cabecera) y negativa (footer)
# ---------------------------------------------------------------------------
def logos():
    print("Logos")
    # Positiva: firma central de «Logo Akito.jpg» (2752 × 1536). Se excluyen
    # la muestra «Isotipo» (izquierda) y el avatar circular (derecha).
    original = abrir("Logo Akito.jpg")
    firma = original.crop((860, 270, 1900, 1200))
    fondo = color_fondo(original, (1300, 40, 1500, 200))
    tinta_roja = (205, 32, 52)
    tinta_azul = (39, 48, 63)
    positivo = aislar(firma, fondo, [tinta_roja, tinta_azul], [CARMESI, AZUL])
    positivo = recortar_a_contenido(positivo, margen=8)
    guardar_png(ajustar_ancho_rgba(positivo, 640), "logo-positivo.png", paleta=True)

    # Negativa: mitad inferior de «variantes…jpg» (2048 × 2048).
    variantes = abrir("variantes del logotipo para fondo claro y fondo oscuro.jpg")
    mitad = variantes.crop((560, 1100, 1490, 1950))
    fondo_osc = color_fondo(variantes, (100, 1100, 300, 1300))
    tinta_roja_osc = (205, 32, 52)
    tinta_marfil = (250, 247, 242)
    negativo = aislar(mitad, fondo_osc, [tinta_roja_osc, tinta_marfil], [CARMESI, MARFIL])
    negativo = recortar_a_contenido(negativo, margen=8)
    guardar_png(ajustar_ancho_rgba(negativo, 640), "logo-negativo.png", paleta=True)



# ---------------------------------------------------------------------------
# 3. Favicons: isotipo aislado sobre marfil
# ---------------------------------------------------------------------------
def favicons():
    print("Favicons")
    # El lazo de «Favicon de Akito.jpg» viene desenfocado en el original, así que el
    # isotipo se toma de la firma nítida de «Logo Akito.jpg» (mismo dibujo, sin texto).
    original = abrir("Logo Akito.jpg")
    zona = original.crop((880, 270, 1880, 745))
    fondo = color_fondo(original, (1300, 40, 1500, 200))
    iso = aislar(zona, fondo, [(205, 32, 52)], [CARMESI])
    iso = recortar_a_contenido(iso, margen=0)

    for lado, nombre in ((512, "favicon-512.png"), (32, "favicon-32.png")):
        # Isotipo al 84 % del lado (94 % en 32 px para que se lea), centrado sobre marfil.
        util = round(lado * (0.94 if lado == 32 else 0.84))
        fuente = iso
        if lado == 32:
            # A 32 px el trazo original quedaría por debajo de 1 px; se engrosa
            # ligeramente (dilatación del alfa) para que el isotipo siga legible.
            alfa = iso.getchannel("A").filter(ImageFilter.MaxFilter(13))
            fuente = Image.merge("RGBA", (*iso.convert("RGB").split(), alfa))
        icono = ajustar_ancho_rgba(fuente, util)
        lienzo = Image.new("RGBA", (lado, lado), MARFIL + (255,))
        lienzo.alpha_composite(icono, ((lado - icono.width) // 2, (lado - icono.height) // 2))
        guardar_png(lienzo.convert("RGB"), nombre)


# ---------------------------------------------------------------------------
# 4. Iconos del kit visual: «Cómo funciona» y «Preguntas» (sin etiquetas)
# ---------------------------------------------------------------------------
def iconos():
    print("Iconos")
    kit = abrir("Kit visual para redes.jpg")  # 2752 × 1536
    fondo = color_fondo(kit, (1200, 1250, 1500, 1450))
    tinta = (200, 30, 50)
    for caja, nombre in (
        ((100, 520, 580, 995), "icono-pasos.png"),
        ((2172, 520, 2652, 995), "icono-pregunta.png"),
    ):
        icono = aislar(kit.crop(caja), fondo, [tinta], [CARMESI], umbral=(0.12, 0.8))
        icono = recortar_a_contenido(icono, margen=4)
        guardar_png(ajustar_ancho_rgba(icono, 192), nombre, paleta=True)


# ---------------------------------------------------------------------------
# 5. Open Graph y avatar social
# ---------------------------------------------------------------------------
def social():
    print("Social")
    og = abrir("Open Graph Akito.jpg")  # 2848 × 1504 (≈1,894:1)
    objetivo = 1200 / 630
    alto = round(og.width / objetivo)
    y = (og.height - alto) // 2
    og = og.crop((0, y, og.width, y + alto)).resize((1200, 630), Image.LANCZOS)
    og.save(DESTINO / "og-akito.jpg", "JPEG", quality=84, optimize=True, progressive=True)
    print(f"  {'og-akito.jpg':28s} 1200×630")

    # Avatar circular: reservado para redes (no se usa en la web).
    avatar = abrir("Logo perfil.jpg").resize((512, 512), Image.LANCZOS)
    guardar_png(avatar, "avatar-akito-512.png")


def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    hero()
    logos()
    favicons()
    iconos()
    social()


if __name__ == "__main__":
    main()
