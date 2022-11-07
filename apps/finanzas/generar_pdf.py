import jinja2
import pdfkit

# * Funcion para crear pdf general
def pdf_create(ruta_template, output_path, info, rutacss='static/assets/css/volt.min.css', page_size='Letter', m_top='0.5in', m_right='0.5in', m_bottom='0.5in', m_left='0.5in'):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template, '')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)

    option = {
        'page-size': page_size,
        'margin-top': m_top,
        'margin-right': m_right,
        'margin-bottom': m_bottom,
        'margin-left': m_left,
        'encoding': 'UTF-8',
    }

    ruta_salida = output_path

    # ? Verificar que ruta tomar dependiendo el SO
    try:
        config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
    except OSError:
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdfkit.from_string(html, ruta_salida, css=rutacss, options=option, configuration=config)
    
    return ruta_salida