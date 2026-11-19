# SPEC.md — Akito · Regalos a distancia

**Encargo para Antigravity.** Construir una One-Page en español para personas que quieren enviar un regalo a su pareja o a un amigo que vive lejos. La acción principal es preparar una dedicatoria, ver cómo se sentiría recibirla y consultar a Akito por WhatsApp. La página debe servir también a quien llega con su mensaje listo y quiere consultar enseguida.

## Stack técnico y estructura obligatoria

- **Stack:** **Vite + HTML5 semántico + CSS3 nativo (con Custom Properties) + JavaScript Vanilla (ES Modules)**. No usar React, Vue, Angular, Tailwind ni librerías externas de animación (GSAP, Framer Motion, etc.).
- **Estructura sugerida:**
  - `Akito/` (carpeta con el manual y los JPG originales de identidad)
  - `index.html` (todo el contenido principal renderizado en el HTML inicial)
  - `src/styles/` (`tokens.css`, `base.css`, `sections.css`, `animations.css`)
  - `src/scripts/` (`config.js`, `main.js`, `workshop.js`, `scroll-reveal.js`)
  - `public/assets/` (activos optimizados extraídos de `Akito/`)
- **Configuración de contacto:** Centralizar el número comercial en `src/scripts/config.js` leyendo `import.meta.env.VITE_WHATSAPP_NUMBER || ""` (solo dígitos con indicativo de país, sin `+` ni espacios). Mientras esté vacío, activar automáticamente el modo «Copiar consulta».

## 1. Resumen del concepto y narrativa

**Concepto creativo — «Del otro lado del hilo».** La portada muestra dos momentos del mismo atardecer. A la izquierda, unas manos sostienen una caja bajo un cielo azul. A la derecha, otras manos esperan bajo una luz coral. En el espacio marfil que separa las escenas vive el titular. Un hilo carmesí sale de la primera escena, atraviesa ese espacio y alcanza la segunda. El vacío entre ambas imágenes representa los kilómetros.

El visitante sigue ese mismo hilo hasta una postal en blanco. Escribe para alguien concreto y pulsa **«Abrir mi regalo de muestra»**. La caja se abre y aparece su propia dedicatoria. Ese cambio de perspectiva —primero escribir como remitente y luego leer como destinatario— es el momento central. Al continuar a WhatsApp, Akito recibe la intención, el destino y las palabras que el visitante decidió compartir.

El manual vincula el nombre Akito con *akai* (rojo), *ito* (hilo) y la idea de unión del *Musubi*. Traducirlo en la continuidad del trazo y en los dos extremos de la composición. Reservar el eslogan oficial **«Conectando historias sin importar los kilómetros»** para el cierre. Hablar de tú, con frases que también funcionen entre amigos.

## 2. Sistema de diseño y activos

El manual fija la identidad, los colores, los usos del logotipo y las familias tipográficas de referencia. Las medidas, los estados de interfaz y la composición siguientes son decisiones de diseño para esta web.

| Elemento | Especificación |
|---|---|
| Blanco Marfil · `#FAF7F2` | Fondo de página, papel de la dedicatoria y texto sobre botones carmesí. |
| Azul Crepuscular · `#1A2238` | Titulares, cuerpo, iconos funcionales y fondo del footer. |
| Rojo Carmesí · `#C81E2B` / `#B81D24` | Primer tono para hilo, selección y CTA principal. Segundo tono para hover y pulsación del CTA. En el footer, mantener los enlaces en marfil. |
| Coral Atardecer · `#E88D67` | Luz en la ilustración y degradados del cielo. Reservarlo para superficies pictóricas. |
| Tipografía | Cargar **Fraunces (peso 600)** para H1/H2 y **DM Sans (pesos 400 y 600)** para cuerpo y controles desde Google Fonts (sirviendo WOFF2 con `<link rel="preconnect">` y `display=swap`). Respaldo: Georgia y Arial respectivamente. H1 de 40 a 76 px, interlínea 1,04. H2 de 32 a 48 px, interlínea 1,12. Cuerpo 16–18 px, interlínea 1,55. Mayúsculas espaciadas a 0,12 em solo en «REGALOS A DISTANCIA». |
| Botones y enlaces | Primario carmesí, texto marfil, altura mínima 48 px, relleno horizontal 22 px, radio 8 px. Secundario marfil con borde azul de 1 px. Enlace de texto subrayado. Foco con doble anillo visible, marfil interior de 2 px y azul exterior de 3 px. |
| Papel y profundidad | Caja dibujada en perspectiva suave, cordón trenzado y postal marfil con borde azul al 20 %, radio 4 px. Única sombra en la postal y la tapa: desplazamiento vertical 8 px, desenfoque 24 px, azul al 12 %. El resto del contenido descansa sobre el fondo de página. |
| Retícula y trazo | Ancho útil máximo 1200 px. Espaciado en múltiplos de 8 px. Hilo narrativo de 2 px, extremos redondos. Sus tramos se encuentran en el límite entre escenas y nunca cruzan letras, campos ni botones. |

**Preparación de los archivos de `Akito/` (Paso 1 obligatorio antes de maquetar).** El ZIP contiene un manual y siete JPG. Antes de escribir la interfaz, procesar los archivos en `public/assets/` usando un script reproducible (ej. Python con Pillow o Node con Sharp) y **pausar o mostrar el resultado de los recortes y transparencias para verificación visual**, prestando especial atención a evitar bordes sucios o halos al remover fondos de JPG.

| Archivo | Uso y tratamiento |
|---|---|
| `manual_de_identidad_de_marca_akito.md` | Referencia principal para copy oficial, color y proporciones. Dejar libre alrededor de cada marca un espacio equivalente a la altura de la «o» de Akito. |
| `Banner Akito Anime referencia.jpg` | La imagen ya lleva marca y eslogan en el centro. Extraer dos viñetas del original de 3168 × 1344: partir del 25 % izquierdo para las manos con la caja y del 20 % derecho para las manos que esperan. Ajustar los cortes hasta excluir toda letra y conservar los gestos. Exportar versiones responsivas en WebP (`hero-left.webp`, `hero-right.webp`) con dimensiones explícitas. |
| `Logo Akito.jpg` y `variantes del logotipo para fondo claro y fondo oscuro.jpg` | Aislar la firma central positiva para el header (`logo-positivo.png`) y la firma negativa de la mitad inferior para el footer (`logo-negativo.png`). Eliminar muestras laterales y fondo usando suavizado de bordes (anti-aliasing) sobre el color destino. Conservar el trazo carmesí, el descriptivo y las proporciones originales. |
| `Favicon de Akito.jpg` y `Logo perfil.jpg` | Del primero, exportar favicon de 32 y 512 px con isotipo sobre marfil (`favicon-32.png`, `favicon-512.png`). Por debajo de 40 px usar únicamente el isotipo. El segundo es el avatar social con marco circular y se reserva para ese uso. |
| `Kit visual para redes.jpg` | Aislar el motivo de los pasos para «Cómo funciona» y el signo de pregunta para «Antes de enviarlo». Recortar las etiquetas integradas (o vectorizarlos limpiamente en SVG si el recorte de JPG deja artefactos). Los títulos de sección serán texto HTML. |
| `Open Graph Akito.jpg` | Exportar a 1200 × 630 px (`og-akito.jpg`). Conservar la marca y el eslogan dentro del encuadre. Usar esta pieza en las meta etiquetas `og:image`. |

**Ilustración de la caja interactiva (SVG inline multicapa).** En el archivo no hay fotografías de productos ni referencias de inventario; la caja representa la experiencia de preparar un detalle. Construirla como un **SVG inline original y multicapa** (sin depender de imágenes externas faltantes), con luz cálida desde la derecha mediante `<linearGradient>` suaves y grupos `<g>` independientes para animar con CSS:
- `#caja-base`: base kraft en perspectiva suave.
- `#caja-tapa`: tapa independiente con su sombra (`8px 24px` azul al 12 %).
- `#cordon-izq` y `#cordon-der`: dos extremos de cordón trenzado carmesí que se separan al abrir.
- Contenedor superpuesto para la **postal HTML/CSS** (papel marfil `#FAF7F2`, borde azul al 20 %, radio 4 px) para que el texto escrito por el usuario sea seleccionable, accesible y responda al salto de línea sin recortarse.

## 3. Arquitectura sección por sección

| Sección y objetivo | Distribución y elementos gráficos | Texto visible y acciones |
|---|---|---|
| **Cabecera · orientarse** | Barra marfil en el flujo normal. Firma positiva a la izquierda. A la derecha, dos enlaces y un botón. | «Cómo funciona», «Preguntas» y **«Armar un regalo»**. El logo vuelve al inicio. |
| **Hero · entender el servicio** · `#inicio` | Tríptico de 28 % / 44 % / 28 %. Viñeta azul con la caja, columna marfil de texto, viñeta coral con las manos. Alinear los extremos interiores del cordón con un trazo curvo debajo de los CTA. | Descriptivo «REGALOS A DISTANCIA». H1 **«Hay palabras que merecen llegar en una caja.»** Bajada «Preparamos regalos personalizados para parejas y amigos que viven lejos. Empieza con lo que quieres decirle.» CTA «Armar un regalo». Enlace «Cómo funciona». |
| **Cómo funciona · explicar el servicio** · `#como-funciona` | Motivo de los pasos junto al H2. Tres nudos sobre una línea horizontal con texto debajo, en orden de lectura. En móvil, línea vertical a la izquierda del texto. | H2 «De tus manos a las suyas». **1. Cuéntanos para quién es.** «Empieza con un recuerdo o una frase que solo ustedes entiendan.» **2. Dale forma con Akito.** «Por WhatsApp consultamos contigo las opciones para esa persona y su ciudad.» **3. Acuerden la entrega.** «Antes de confirmar, revisa con Akito el detalle, el valor y la fecha.» |
| **Taller · escribir y probar el regalo** · `#armar` | Escritorio en dos columnas 52 % / 48 %. A la izquierda, formulario sobre marfil. A la derecha, caja cerrada (SVG multicapa) y control de apertura al pie. Al abrir, la postal ocupa el mismo espacio. En móvil, formulario seguido de caja y acción de contacto. | H2 **«¿Qué te gustaría decirle?»** Instrucción «Elige una intención o empieza con tus propias palabras.» Selector, dedicatoria y destino definidos en §4. Botones «Abrir mi regalo de muestra» y **«Consultar por WhatsApp»**. Junto al contacto: «Se abrirá un borrador que puedes revisar antes de enviarlo.» |
| **Preguntas · resolver dudas antes de consultar** · `#preguntas` | Motivo de pregunta junto al H2 «Antes de enviarlo». Tres filas de acordeón (`<details>` / `<summary>`), separadas por líneas finas, con indicador de expansión (+/−) en el extremo derecho. | **«¿Puedo enviárselo a un amigo?»** → «Sí. Akito prepara detalles para parejas y amigos a distancia.» **«¿Llegan a su ciudad?»** → «Escribe la ciudad en tu consulta y Akito te confirmará la cobertura.» **«¿Cuánto cuesta y cuándo llega?»** → «El valor y la fecha dependen del detalle y del destino. Puedes consultarlos antes de decidir.» |
| **Footer · cerrar el recorrido** | Banda azul crepuscular. Firma negativa a la izquierda. A la derecha, el hilo termina en un punto junto al eslogan en marfil. En móvil, apilar ambos bloques. | «Conectando historias sin importar los kilómetros». Enlaces «Armar un regalo» y «Volver al inicio». |

## 4. Interactividad y microinteracciones

| Disparador | Comportamiento exacto | Técnica y alternativa |
|---|---|---|
| Entrar al hero | Mostrar titular y controles en el primer render. Una sola vez, revelar el tramo de hilo bajo el texto de izquierda a derecha en 650 ms, con desaceleración. | Trazo SVG decorativo y animación CSS (`stroke-dashoffset`). Con `prefers-reduced-motion: reduce`, presentar el hilo completo desde el inicio. |
| Desplazarse por los tres pasos | Cuando el centro de un paso entra en la mitad inferior visible de la pantalla, rellenar su nudo y extender el segmento hasta él en 240 ms. Al retroceder, conservar los tramos revelados. | `IntersectionObserver` y transición CSS. Mantener siempre legibles los tres textos. Si falta soporte, mostrar la línea completa. Scroll nativo en todo el recorrido. |
| Elegir una intención | Ofrecer tres opciones de selección única: «Te extraño», «Gracias» y «Celebremos». Estado inicial sin selección. Al elegir, marcar con borde carmesí y un visto. Mostrar debajo una sugerencia y el botón «Usar esta frase». | Radio buttons nativos estilizados (`role="radiogroup"`). Frases respectivas: «Hoy me hizo falta contarte esto en persona.», «Me acordé de esa vez que estuviste para mí.» y «Ojalá pudiera estar ahí para brindar contigo.» Cambiar la selección conserva el texto escrito. |
| Usar o editar la frase | «Usar esta frase» copia la sugerencia al campo «Tu dedicatoria». Si ya contiene otro texto, mostrar «¿Reemplazar tu dedicatoria?» con «Reemplazar» y «Conservar». Campo opcional de 240 caracteres, con contador visible. Campo opcional «Ciudad de entrega», máximo 80 caracteres. | Estado local en memoria durante la visita. La postal abierta refleja las ediciones como texto plano (`textContent`), conserva saltos de línea (`white-space: pre-wrap; overflow-wrap: anywhere;`) y muestra la frase completa. Con dedicatoria vacía muestra «Aquí irán tus palabras.» solo en la muestra. |
| Abrir el regalo de muestra | Tras pulsar, los dos extremos del cordón se separan 12 px en 160 ms. A los 160 ms, la tapa sube 18 px y gira −6° durante 220 ms. A los 320 ms, la postal asciende 24 px y aparece en 240 ms. El control pasa a «Cerrar la muestra». Al cerrar, volver a la caja en 180 ms. Mantener el foco en el control. | Capas SVG/HTML 2D y transiciones CSS de `opacity` y `transform`. Bloquear clics redundantes mientras dura la transición. Exponer `aria-expanded` y región viva al lector de pantalla. Con movimiento reducido, intercambiar los dos estados al instante. Abrir la muestra es opcional para consultar. |
| Pasar el cursor, tocar o usar teclado | En puntero preciso (`@media (hover: hover)`), oscurecer el primario en 140 ms. Al pulsarlo, desplazarlo 1 px hasta soltar. En toque, ejecutar con una pulsación. En teclado, activar los controles nativos y mostrar el anillo de foco. | CSS para estados de control. La caja se abre exclusivamente por activación intencional. |
| Abrir una pregunta o navegar por anclas | Preguntas cerradas al inicio. Cada encabezado alterna su respuesta y el signo +/−, sin cerrar otras respuestas. Las anclas llevan al título correspondiente y trasladan allí el foco. | Elementos `<details>` / `<summary>` nativos. `scroll-behavior: smooth` solo si el usuario admite movimiento. |

## 5. CTA y conversión

| Ubicación | Control | Resultado |
|---|---|---|
| Cabecera, hero y footer | **Armar un regalo** | Ir a `#armar`, enfocar el H2 (`tabindex="-1"`) y conservar cualquier dato ya escrito. |
| Cabecera y hero | **Cómo funciona** | Ir a `#como-funciona`. «Preguntas» lleva a `#preguntas`. |
| Taller, después de la muestra en el orden de lectura | **Consultar por WhatsApp** | Abrir el enlace oficial de conversación con el borrador descrito abajo. Funciona con todos los campos vacíos. El usuario decide si lo envía. |
| Taller, si `WHATSAPP_NUMBER` está vacío | **Copiar consulta** | Sustituye al CTA de WhatsApp. Copiar el mismo borrador con `navigator.clipboard.writeText` y anunciar «Consulta copiada» en una región `aria-live="polite"`. Si falla la copia, presentar un `<textarea readonly>` seleccionable con «Selecciona y copia tu consulta». En este modo, sustituir también la ayuda del CTA por «Guarda tu consulta para compartirla con Akito». |

**Borrador exacto.** Primer renglón: «Hola, Akito. Quiero preparar un regalo a distancia.» Añadir un renglón por dato presente, en este orden: «Intención: {opción}», «Ciudad de entrega: {ciudad}», «Dedicatoria: {texto}». Último renglón siempre presente: «¿Me ayudan con las opciones, el valor y la entrega?» Quitar espacios sobrantes al principio y al final de cada campo (`trim()`). Excluir datos vacíos y el texto de muestra. Codificar el mensaje completo una sola vez con `encodeURIComponent()` para conservar tildes, emojis, signos y saltos.

**Destino.** Usar el formato `https://wa.me/{numero_internacional}?text={mensaje_codificado}`. El número comercial se configura en `src/scripts/config.js` (mediante `VITE_WHATSAPP_NUMBER` o constante directa), con indicativo de país y solo dígitos. El ZIP no trae ese número; hasta que se configure, la web opera en modo «Copiar consulta». Tras abrir el chat (`target="_blank" rel="noopener noreferrer"`), conservar el borrador en la página al regresar. La apertura del chat no confirma un pedido. Catálogo con precios, cobro, rastreo y QR multimedia quedan fuera de esta primera fase.

## 6. Criterios técnicos, responsividad y aceptación

| Ancho | Composición que debe implementarse |
|---|---|
| **1024 px o más** | Márgenes mínimos de 48 px. Hero de tres paneles, con viñetas al ras de sus laterales y texto centrado. Taller en dos columnas, con CTA de consulta bajo ambas. Separación vertical entre secciones de 96 px. |
| **768–1023 px** | Márgenes de 32 px. Hero con titular y CTA arriba, dos viñetas contiguas debajo. Mantener los tres pasos en línea. Taller en dos columnas iguales. Separación de 72 px. |
| **320–767 px** | Márgenes de 20 px. Cabecera con isotipo aislado de 32 px y botón «Armar un regalo». Omitir los enlaces de cabecera en este ancho. Hero con texto primero y las dos manos enfrentadas debajo en una franja de 144 px de alto, separadas por un canal marfil de 24 px con hilo. Pasos verticales, taller de una columna y CTA principal a ancho completo. Separación de 56 px. |

**Implementación y rendimiento.** Todo el contenido principal debe existir en `index.html` desde el primer render. Exportar viñetas responsivas en WebP con `width` y `height` explícitos para evitar saltos de diseño. Cargar la imagen principal con `fetchpriority="high"` y diferir recursos fuera de la primera pantalla (`loading="lazy"`). Objetivos de transferencia inicial en móvil: imágenes visibles ≤ 250 KB en total y JavaScript propio ≤ 60 KB comprimido. Objetivos de experiencia: LCP ≤ 2,5 s, CLS ≤ 0,1 e INP ≤ 200 ms.

**Accesibilidad y publicación.** Un H1, jerarquía H2 por sección, enlace inicial «Saltar al contenido», etiquetas `<label>` persistentes y controles táctiles de al menos 44 × 44 px. Texto normal con contraste mínimo 4,5:1. Ocultar a tecnologías de asistencia (`aria-hidden="true"`) el hilo, los nudos y las capas decorativas. El enlace del logo se llama «Akito, inicio». Título de pestaña «Akito | Regalos a distancia». Meta descripción «Prepara una dedicatoria y consulta un regalo personalizado para tu pareja o tus amigos a distancia.» Mantener dedicatoria y ciudad fuera de analítica, `localStorage` y registros.

**Pruebas de aceptación antes de entregar**

- A 320, 390, 768, 1024 y 1440 px se ven ambas manos, el titular aparece una vez y ninguna línea de texto toca el hilo. No hay desplazamiento horizontal.
- Desde el hero se llega al taller con una activación. Con teclado se puede elegir una intención, escribir, abrir y cerrar la muestra, consultar y desplegar preguntas. El orden de foco sigue la lectura.
- Cambiar de intención tras escribir conserva la dedicatoria. Probar «Conservar» y «Reemplazar». La postal admite 240 caracteres, una palabra larga sin espacios, saltos de línea y emojis sin recortar texto ni cubrir el botón.
- Con movimiento reducido, la composición y la consulta siguen completas. En pantalla táctil, ninguna acción depende de arrastrar, mantener pulsado o pasar el cursor.
- Con `WHATSAPP_NUMBER` configurado, verificar en móvil y escritorio que el borrador llega al chat correcto. Probar «Barranquilla», «Tú & yo 🎁» y una consulta vacía. Sin número, probar la copia y su alternativa manual. En ningún caso la página anuncia un pedido confirmado.

## 7. Control de versiones, GitHub y flujo de trabajo

- **Repositorio remoto:** `https://github.com/KitsuJKM/Akito-Tienda`
- **Modelo de ramas (GitHub Flow):**
  - `main`: Rama principal siempre estable y lista para desplegar. **No hacer commits directos a `main`** durante el desarrollo de funcionalidades.
  - Ramas de trabajo cortas por hito, creadas desde `main`:
    - `chore/setup-y-activos` → Inicialización de Vite, carpeta `Akito/`, `.gitignore`, `.env.example` y procesamiento de imágenes.
    - `feat/estructura-y-estilos` → `index.html`, tokens CSS, cabecera, hero, pasos, preguntas y footer responsivos.
    - `feat/taller-interactivo` → SVG multicapa de la caja, animaciones, lógica de dedicatoria, WhatsApp y modo «Copiar consulta».
    - `fix/ajustes-qa` → Correcciones de pruebas de aceptación, accesibilidad y rendimiento.
- **Regla de commits (Conventional Commits):** Mensajes cortos, claros y atómicos en español usando prefijos (`feat:`, `style:`, `fix:`, `chore:`, `docs:`).
- **Versionado (SemVer con Git Tags):**
  - `v0.1.0`: Proyecto inicializado y activos recortados/verificados.
  - `v0.2.0`: Maquetación completa y responsiva (320 px a 1440 px).
  - `v0.3.0`: Interactividad del taller, caja SVG y flujo de WhatsApp/copiado.
  - `v1.0.0`: Primera fase completa tras pasar todas las pruebas de aceptación.
- **Higiene del repositorio y seguridad:**
  - Configurar `.gitignore` desde el primer commit excluyendo `node_modules/`, `dist/`, `.env` y archivos temporales del sistema.
  - Incluir `.env.example` con `VITE_WHATSAPP_NUMBER=` vacío como plantilla (nunca subir números privados o secretos en `.env`).
  - Antes de hacer *merge* (o abrir Pull Request) hacia `main`, ejecutar `npm run build` y confirmar que compila sin errores ni advertencias críticas.