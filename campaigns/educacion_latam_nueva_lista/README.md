# Nueva lista — Sector educación LATAM (Colombia, México, Chile)

Lista nueva de instituciones educativas privadas (y algunas públicas con operación
comercial de admisiones, en Chile) para la campaña outbound de Vixiees, generada
para ampliar la lista inicial ya trabajada por el equipo.

## Quién es el comprador (ICP)

Vixiees vende un software que fuerza el proceso comercial de un equipo de ventas
(no reemplaza el CRM: se instala encima). El comprador típico es quien es dueño
del equipo comercial/de admisiones de la institución:

- **Perfil 1 (el más común y de más valor):** Director Comercial y de Admisión,
  Jefe/Director de Admisiones, Director de Mercadeo, Coordinador de Promoción y
  Admisiones.
- **Perfil 2:** Gerente/Rector en instituciones medianas donde la dirección
  general también lleva el proceso comercial de cerca.
- **Perfil 3:** Founder/Director General en instituciones pequeñas que hace de
  todo.

El encaje real está en instituciones donde admisiones funciona como un embudo de
ventas B2C: un equipo de asesores comerciales trabaja una base de leads
(aspirantes) para cerrar matrículas.

## Qué hay en `leads.csv`

127 instituciones nuevas — **45 Colombia, 40 México, 42 Chile** — repartidas en
los mismos bloques de nicho que ya usa el equipo (universidades virtuales,
universidades privadas presenciales, formación técnica/ETDH, academias de
idiomas, edtech y bootcamps, escuelas especializadas de alto ticket, escuelas de
negocio/educación continua, preparación de pruebas).

Columnas:

| Columna | Contenido |
|---|---|
| `Empresa` | Nombre de la institución |
| `Pais` | Colombia / Mexico / Chile |
| `Sitio_Web` | Dominio o URL oficial |
| `Tipo_Institucion` | Descripción corta del tipo de institución |
| `Bloque_Nicho` | Bloque de nicho (A–H) |
| `Nombre_Contacto` / `Cargo` | Persona identificada como responsable de admisiones/comercial, cuando se encontró públicamente |
| `Email` | Correo del contacto nombrado, o correo institucional del área de admisiones/mercadeo |
| `Telefono` | Teléfono publicado (del contacto o de la institución) |
| `LinkedIn` | Perfil del contacto, si se encontró |
| `Fuente` | URL(s) de donde salió cada dato — para poder verificar antes de escribir |
| `Confianza` | Ver abajo |
| `Notas` | Contexto adicional, advertencias sobre el rol, etc. |

### Niveles de `Confianza` — 30 nombradas / 65 institucionales / 32 sin contacto

- **Contacto nombrado (30 filas):** se encontró una persona real, con nombre y
  cargo publicado (LinkedIn, directorio institucional, prensa), en un rol de
  admisiones/comercial/mercadeo.
- **Email institucional (65 filas):** no se confirmó un responsable nombrado,
  pero sí un correo departamental publicado oficialmente en el sitio de la
  institución (admisiones@, mercadeo@, contacto@, etc.).
- **Sin contacto público (32 filas):** institución real y verificada (sitio
  confirmado), pero sin correo ni nombre público disponible en la investigación
  — quedan como objetivo a nivel de cuenta para buscar el contacto manualmente
  (ej. LinkedIn Sales Navigator, Lusha, o llamando directamente).

**Importante:** ningún nombre, cargo o correo fue inventado ni generado por
patrón (tipo `nombre.apellido@dominio`). Todo dato de contacto no vacío tiene una
URL de origen en la columna `Fuente`. "Verificado" aquí significa *"visto
publicado en una fuente pública citable"*, no *verificado por SMTP/deliverability* —
antes de enviar en volumen, vale la pena pasar la lista por una herramienta de
verificación de correos (la que ya usan, Lusha, o similar).

## Exclusiones aplicadas

Se excluyó explícitamente cualquier institución que ya estuviera en:

- **Colombia:** la lista maestra de 136 instituciones (`Vixiees_educacion_privada_Colombia
  ordenado por bloques.xlsx`) marcada como ya contactada, con deal creado, o
  cliente (Areandina, Unisabana, Autónoma de Manizales, Salazar y Herrera, Jorge
  Tadeo Lozano, Uninorte, Externado, Kuepa, Santillana, Taller Cinco, CORBAC,
  Instituto UNITEC, Poligran, Remington, CUN, Corporación Universitaria
  Iberoamericana, CEIPA, UNIMINUTO, Universidad Manuela Beltrán, Universidad
  Santo Tomás/VUAD).
- **México y Chile:** todas las instituciones que aparecen en la hoja de
  seguimiento de llamadas "Vixiees. Lista 2" y en "Vixiees_Contactos_Secuencia.xlsx"
  (ya contactadas por el equipo).

No hay solapamiento entre esta lista nueva y las instituciones ya trabajadas.

## Siguiente paso sugerido

1. Verificar deliverability de los correos antes de la campaña (herramienta de
   verificación de email).
2. Para las 32 filas "Sin contacto público", buscar el contacto puntual vía
   Lusha/Sales Navigator antes de escribir.
3. Cargar la lista al mismo sistema de seguimiento que usan hoy (columnas
   compatibles con el formato de "Sector educación Colombia. Lista 1").
