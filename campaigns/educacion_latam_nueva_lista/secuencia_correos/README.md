# Secuencia de 8 correos — personalizada por contacto

Genera y contiene la secuencia de 8 correos (la ya redactada y aprobada por
Sebastian para el sector educación) personalizada para cada uno de los 127
contactos de `../leads.csv`.

## Archivos

- **`plantilla_8_correos.md`** — la fuente de verdad. Los 8 correos originales
  con dos campos de fusión: `{{SALUDO}}` e `{{INSTITUCION}}`. Editar el copy
  aquí si algo debe cambiar — el script vuelve a generar todo automáticamente.
- **`generar_secuencia.py`** — script que combina la plantilla con `leads.csv`
  y produce `secuencia_personalizada.csv`. Sin llamadas a IA por correo: es
  una fusión de campos (mail-merge) determinística, así que es instantáneo y
  reproducible.
- **`secuencia_personalizada.csv`** — 127 filas (una por contacto), cada una
  con `Correo_1_Asunto`/`Correo_1_Cuerpo` … `Correo_8_Asunto`/`Correo_8_Cuerpo`
  ya con el saludo y el nombre de la institución insertados.

## Cómo se arma el saludo

- Si el contacto tiene nombre (`Nombre_Contacto` no vacío): `Hola {primer nombre},`
- Si no (fila "Email institucional" o "Sin contacto público"): `Hola equipo de {Institución},`

El resto del copy es el mismo texto aprobado por Sebastian; solo se
personaliza el saludo y una mención puntual de la institución por correo. La
cadencia entre correos (cada cuántos días se envía cada uno) no está fijada
acá — es una decisión operativa de a quién y cuándo se enrola.

## Regenerar

```
python3 generar_secuencia.py
```

Vuelve a leer `../leads.csv` y `plantilla_8_correos.md` y sobreescribe
`secuencia_personalizada.csv`. Útil si se actualiza la lista de leads o se
ajusta el copy de la plantilla.
