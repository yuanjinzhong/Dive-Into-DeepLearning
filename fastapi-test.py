from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# 启动命令：uvicorn fastapi-test:app --reload
# uvicorn fastapi-test:app 命令含义如下:
#
# fastapi-test：fastapi-test.py 文件（一个 Python "模块"）。
# app：在 fastapi-test.py 文件中通过 app = FastAPI() 创建的对象。
# --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。