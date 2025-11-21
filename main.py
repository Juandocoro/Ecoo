
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()



templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

@app.get("/template")
async def read_template(request: Request):
    return templates.TemplateResponse("pagina.html", {"request": request})