from multiprocessing import Process
from sys import prefix

import strawberry
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from modules import light_module, music_module
from modules.light_module import Mutation as LightMutation
from modules.light_module import Query as LightQuery
from modules.music_module import Mutation as MusicMutation
from modules.music_module import Query as MusicQuery
from targets.executor import CommandExecutor
from targets.local_agent import LocalAgent

app = FastAPI(title="Kafka Publisher API")

origins = [
    "http://localhost.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@strawberry.type
class Query(MusicQuery, LightQuery):
    pass


@strawberry.type
class Mutation(MusicMutation, LightMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
processes = []
targets = {
    "command_executor": CommandExecutor(name="command_executor"),
    "local_agent": LocalAgent(name="local_agent"),
}


@app.on_event("startup")
async def startup_event():
    global processes
    processes = [
        Process(target=target.run, daemon=True, name=target.name)
        for target in targets.values()
    ]
    for process in processes:
        process.start()


@app.on_event("shutdown")
async def shutdown_event():
    for process in processes:
        process.kill()
        processes.remove(process)


# uvicorn main:app --host 0.0.0.0 --port 8080 --reload
@app.get("/get_processes")
def get_threads():
    return {
        process.name: {
            "informations": targets.get(process.name).get_informations(),
            "is alive": process.is_alive(),
        }
        for process in processes
    }


@app.post("/terminate_process")
def delete_thread(name: str):
    for process in processes:
        if process.name == name:
            process.kill()
            processes.remove(process)
            return "success"


@app.get("/get_targets")
def get_targets():
    return [target.name for target in targets]


@app.post("/start_target")
def start_process(name):
    for process in processes:
        if process.name == name:
            return "process already exists"
    for target in targets:
        if target.name == name:
            process = Process(target=target.run, daemon=True, name=target.name)
            process.start()
            processes.append(process)
            return "process started"
