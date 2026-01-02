# app/endpoints/router.py

from fastapi import FastAPI
from api.endpoints import dofbot

def create_router(app: FastAPI):
    """
    アプリにエンドポイントルーターを登録する関数。
    :param app: FastAPIアプリケーションインスタンス
    """
    app.include_router(dofbot.router)

