import fastapi
from fastapi.responses import HTMLResponse


app = fastapi.FastAPI()


@app.get("/v1/health")
def health():
    return {"ok": True}


@app.get("/", response_class=HTMLResponse)
def index(name: str = "World"):
    return f"""
<!DOCTYPE html>
<html>
<body>

<h2 title="I'm a header">Hello, {name}</h2>

<p title="I'm a tooltip">Mouse over this paragraph, to display the title attribute as a tooltip.</p>

</body>
</html>
    """
