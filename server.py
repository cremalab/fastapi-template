import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from config.settings import App, Cors
from source.routes import example

app = FastAPI()

# middleware
app.add_middleware(GZipMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=Cors.allow_origins,
    allow_methods=Cors.allow_methods,
    allow_headers=Cors.allow_headers,
    allow_credentials=True,
)

app.include_router(example.router, prefix="/examples", tags=["Examples"])
# add other routes here

if __name__ == "__main__":

    uvicorn.run(
        "server:app",
        host=App.host,
        port=App.port,
        log_config=uvicorn.config.LOGGING_CONFIG,
        proxy_headers=True,
        reload=App.dev,
    )
