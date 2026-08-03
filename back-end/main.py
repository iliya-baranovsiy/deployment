from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from conf import conf

app = FastAPI(title="Deploy api", version="1.0.0")

router = APIRouter(prefix="/api")
app.include_router(router=router)

prod = [
    "gunicorn",
    "main:app",
    "-k",
    "uvicorn_worker.UvicornWorker",
    "-w",
    "4",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@router.get("/")
async def get_hello():
    return {"message": "hello !", "key": {conf.secret_dataq}, "after deploy": f"deploy {1 + "test"}"}
