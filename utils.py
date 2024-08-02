import markdown
import pdfkit

def convert_markdown_to_pdf(markdown_path, pdf_path):
    # Markdown dosyasını oku
    with open(markdown_path, 'r', encoding='utf-8') as markdown_file:
        markdown_text = markdown_file.read()

    # Markdown'ı HTML'e dönüştür
    html_text = markdown.markdown(markdown_text)

    # `wkhtmltopdf` executable path
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

    # HTML'i PDF'ye dönüştür
    pdfkit.from_string(html_text, pdf_path, configuration=config)