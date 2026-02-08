from fastapi import FastAPI
from routes import router
from exceptions import global_exception_handler

app = FastAPI(title="Resource Allocation API")
app.add_exception_handler(Exception, global_exception_handler)
app.include_router(prefix="/projects", router=router)


@app.get("/")
def init():
    return {"status": "ok"}
