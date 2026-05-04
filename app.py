from fastapi import FastAPI, Response
from pydantic import BaseModel
from celery.result import AsyncResult
from celery_app import convert_markdown_to_pdf

class Markdown(BaseModel):
    markdown: str

app = FastAPI()

@app.post("/")
async def root(markdown: Markdown):
    conversion_task = convert_markdown_to_pdf.delay(markdown.markdown)
    return {"job_id": conversion_task.id}

@app.get("/pdf/{job_id}")
async def get_pdf(job_id: str):
    response = AsyncResult(job_id)
    # send the PDF directly if it's ready
    if response.ready():
        return Response(content=response.result, media_type="application/pdf")
    # otherwise send JSON with some info
    else:
        return {
            "job_id": job_id,
            "status": response.status,
        }