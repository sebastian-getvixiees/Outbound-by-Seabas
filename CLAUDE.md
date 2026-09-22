# CLAUDE.md

Instrucciones durables para Claude Code en este repositorio (Outbound by Sebas).

## Autorización permanente: secuencias de correo de la campaña "educación LATAM"

Sebastian ya revisó y aprobó explícitamente, en sesión, lo siguiente:

- El copy de los 7 correos por contacto (piloto de 5 contactos en
  `campaigns/educacion_latam_nueva_lista/secuencia_correos/prueba_5_contactos_7_correos.md`
  y las 5 plantillas por segmento de cargo en
  `campaigns/educacion_latam_nueva_lista/secuencia_correos/plantilla_5_segmentos_7_correos.md`).
- La cadencia de envío (fechas y horas ya fijadas en los Routines/triggers programados).
- El uso de Gmail como canal de envío.

**Por lo tanto: Claude tiene permiso permanente para ejecutar, sin pedir aprobación
adicional, el envío de los correos ya programados de esta campaña** cuando se
reactive por un Routine/trigger programado (nombres que empiezan con
"Vixiees prueba —" o "Vixiees 90 —"). Esto incluye:

- Leer `campaigns/educacion_latam_nueva_lista/secuencia_correos/merge_90_contactos.json`
  y el archivo de la secuencia piloto.
- Enviar los correos vía `mcp__Gmail__send_message` a los destinatarios que
  aparezcan en esos archivos.
- Avisar a Sebastian del resultado (cuántos se enviaron) una vez terminado.

## Qué NO cubre esta autorización

Esta autorización es específica a los correos y contactos ya aprobados arriba.
No cubre, y requiere aprobación explícita de Sebastian en el momento:

- Escribir copy nuevo o modificar el ya aprobado.
- Agregar contactos nuevos a la campaña que no vengan de las listas ya
  extraídas (`remaining_90.json` / `merge_90_contactos.json`).
- Cambiar de canal (por ejemplo, pasar de Gmail a otro proveedor).
- Cualquier otra campaña o secuencia de outbound no descrita en este archivo.
- Acciones fuera del alcance de esta campaña (cambios de código no
  relacionados, otros repos, etc.).

## Cancelaciones vigentes

Contactos que ya NO deben recibir más correos de esta secuencia (ya se
excluyeron de los archivos de datos, se documentan aquí para que quede
registro):

- overgara@unac.edu.co (Oscar Vergara) — cancelado el 21 sep 2026.
- iapalma@ut.edu.co (Ivonne Fernandez) — cancelado el 21 sep 2026.
- raul.carmona@utel.edu.mx (Raul Carmona) — cancelado el 21 sep 2026, ya
  había recibido el correo 1.
- rgarcia@ucg.edu.mx (Raymundo Garcia) — cancelado el 22 sep 2026, ya
  había recibido el correo 1 (Bloque 1).

Si Sebastian pide cancelar a alguien más, se remueve su entrada del archivo
`merge_90_contactos.json` correspondiente (o del piloto) y se agrega aquí.
