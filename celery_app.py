from celery import Celery
from markdown_to_pdf import markdown_to_pdf

app = Celery("markdown_to_pdf", broker="redis://redis:6379/0", backend="redis://redis:6379/1")

@app.task
def convert_markdown_to_pdf(markdown: str):
    return markdown_to_pdf(markdown)