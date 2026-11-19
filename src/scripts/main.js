import { HAS_WHATSAPP } from './config.js';
import { initWorkshop } from './workshop.js';
import { initScrollReveal } from './scroll-reveal.js';

document.documentElement.dataset.contacto = HAS_WHATSAPP ? 'whatsapp' : 'copiar';

initScrollReveal();
initWorkshop();
