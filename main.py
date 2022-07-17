import parseador
import errores
import reporte

miParser = parseador.Parser('eventos_classic.json')

buscador = errores.Buscador(miParser.eventos)

buscador.tiposErrores(miParser.cliente)

elReporte = reporte.GetHTML(buscador.devolucion)

elReporte.get_html()