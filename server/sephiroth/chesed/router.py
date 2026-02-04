# app/endpoints/router.py

from fastapi import FastAPI
from hod import endpoints

def create_router(app: FastAPI):
    """
    アプリにエンドポイントルーターを登録する関数。
    :param app: FastAPIアプリケーションインスタンス
    """
    app.include_router(endpoints.router)

