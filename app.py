from fastapi import FastAPI, Response
from pydantic import BaseModel
from markdown_to_pdf import markdown_to_pdf

class Markdown(BaseModel):
    markdown: str

app = FastAPI()

@app.post("/")
async def root(markdown: Markdown):
    pdf_file = markdown_to_pdf(markdown.markdown)
    return Response(content=pdf_file, media_type="application/pdf")