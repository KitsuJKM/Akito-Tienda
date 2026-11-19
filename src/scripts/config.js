/**
 * Configuración de contacto centralizada.
 * Número comercial: solo dígitos con indicativo de país (sin "+" ni espacios).
 * Si queda vacío, la web activa automáticamente el modo «Copiar consulta».
 */
export const WHATSAPP_NUMBER = (import.meta.env.VITE_WHATSAPP_NUMBER || '').replace(/\D/g, '');

export const HAS_WHATSAPP = WHATSAPP_NUMBER.length > 0;
