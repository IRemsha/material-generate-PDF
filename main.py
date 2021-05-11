def generate_pdf(request, data):
    font_config = FontConfiguration()

    html_template = render_to_string('portable_document/technical_specification_template.html', data)

    html = HTML(string=html_template, base_url=request.build_absolute_uri())

    pdf = html.write_pdf(font_config=font_config, presentational_hints=True)
    # Используйте эту запись, чтобы просто получить PDF-фаил локально
    # html.write_pdf('out.pdf', font_config=font_config, presentational_hints=True)
    pdf_in_memory = io.BytesIO(pdf)

    return pdf_in_memory
