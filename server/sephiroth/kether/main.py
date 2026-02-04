# app/main.py
import sys
import os

# プロジェクトのルートディレクトリをモジュール検索パスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI
from chesed.router import create_router
from chokmah.config_manager import create_config, ConfigManager
from geburah.start_dofbot import start_dofbot

app = FastAPI()
config = create_config()
config_manager = ConfigManager(config)
config_manager.set_config(config)
create_router(app)

if __name__ == "__main__":
    start_dofbot(config)
    # ポート6001でサーバーを起動
    try:
        uvicorn.run("kether.main:app", host="0.0.0.0", port=6001, reload=True)
    except KeyboardInterrupt:
        print("Server stopped.")