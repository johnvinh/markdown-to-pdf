import markdown
from weasyprint import HTML

def markdown_to_pdf(markdown_text: str) -> bytes:
    html_text = markdown.markdown(markdown_text)
    return HTML(string=html_text).write_pdf()