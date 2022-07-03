import uvicorn
# import yaml

from fastapi import FastAPI

# with open("settings.yaml") as settings_file:
#     settings = yaml.safe_load(settings_file)
# main_parameters = {}
# if not settings["openapi_console"]:
#     main_parameters["docs_url"] = None

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# mag nooit weg!
if __name__ == '__main__':
    uvicorn.run(app="main:app", reload=True)
