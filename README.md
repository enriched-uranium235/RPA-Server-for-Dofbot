# Dofbot自動操縦用RPA

<span style="color: red; ">本ツールは開発途中です。動作は保証しません。</span>

　このツールはYahboom社のDofbotをAIエージェントから操縦することを目的に開発しているRPAサーバーです。

## 動作環境
- Windows10
- Windows11

## 使い方
- Githubからソースコードを手元のPCにダウンロードします。

```
git clone https://github.com/enriched-uranium235/RPA-Server-for-Dofbot
```

- 以下のコマンドでPythonの仮想環境を作成します。

```
python -m venv .venv
```

- 仮想環境に入ります。

```
.venv\Scripts\activate
```

- requirements.txtに記載の依存ライブラリを仮想環境にインストールします。

```
pip install -r requirements.txt
```

- Yahboom社の公式サイト(http://www.yahboom.net/study/Dofbot-Pi )にアクセスし、手元のDofbotに対応した操作用のアプリケーションをダウンロードします。本ツールで使用するのは左メニューのDownloadのPC Softwareのリンク先にあるYahboomArmEn.zipに入っているコンテンツになります。

- ダウンロードしたzipファイルを展開後中に入っているDofbot.exeを起動してロボットアームと接続できるかを確認した後で3DS, Video, Dofbot.exe, config.iniをDofbotAutoControl配下に複製します。

必要ファイルを複製後のツリー
```
DofbotAutoControl
  ├ .venv
  ├ 3DS
  ├ operate_recorder
  ├ server
  ├ Video
  ├ .gitignore
  ├ config.ini
  ├ Dofbot.exe
  ├ README.en.md
  ├ README.md
  └ requirements.txt
```

- Dofbot.exeをダブルクリックして起動後仮想環境で以下のコマンドでアプリの自動制御に必要な座標の情報を出力して調べます。
```
python operate_recorder/record.py
```

- 以下必要な座標情報
  - Connectボタンの座標
  - Networkのラジオボタンの座標
  - Host Address入力欄の座標
  - Communication入力欄の座標
  - Communication ConfigurationのダイアログのConnectボタンの座標
  - Dofbot制御アプリを最前面に出すための座標(接続成功時Edgeでブラウザ画面が表示されるので制御アプリを再度最前面に出すため)
  - ControlDofbot1~6の座標

- config.tomlにて必要情報を入力していきます。
```
[dofbot]
min_servo1=0
max_servo1=180
min_servo2=0
max_servo2=180
min_servo3=0
max_servo3=180
min_servo4=0
max_servo4=180
min_servo5=0
max_servo5=180
min_servo6=0
max_servo6=180
dofbot_ip="127.0.0.1"
dofbot_port=6000
dofbot_app_connect_button_coodinate=[0, 0]
dofbot_check_network_coodinate=[0, 0]
dofbot_app_ip_input_coodinate=[0, 0]
dofbot_app_port_input_coodinate=[0, 0]
dofbot_app_connect_submit_button_coodinate=[0, 0]
dofbot_app_use_coodinate=[0, 0]
dofbot_app_servo1_scroll_coodinate=[0, 0]
dofbot_app_servo2_scroll_coodinate=[0, 0]
dofbot_app_servo3_scroll_coodinate=[0, 0]
dofbot_app_servo4_scroll_coodinate=[0, 0]
dofbot_app_servo5_scroll_coodinate=[0, 0]
dofbot_app_servo6_scroll_coodinate=[0, 0]
```

  - min_servo1, ... , max_servo6はアームのそれぞれのサーボの角度の設定できる最小値と最大値を表します。本棚の上等高いところにアームが置いてある場合はmin_servo1とmax_servo1を90固定にして動かさないのが推奨です。
  - dofbot_ipは制御するdofbotのIPアドレスを入力します。
  - dofbot_portは制御するdofbotのポート番号を入力します。
  - dofbot_app_connect_button_coodinateはツール起動後自動で起動するDofbot制御アプリのIPアドレスとポート番号の設定画面を開くために必要です。
  - dofbot_check_network_coodinateは設定画面が開いた後IPアドレスとポート番号を設定するために必要な座標です。
  - dofbot_app_ip_input_coodinateは接続対象のDofbotのIPアドレスを入力するために必要な座標です。
  - dofbot_app_port_input_coodinateは接続対象のDofbotのポート番号を入力するために必要な座標です。
  - dofbot_app_connect_submit_button_coodinateはIPアドレスとポート番号入力後設定を保存するためのConnectボタンを押すために必要です。
  - dofbot_app_use_coodinateはDofbotに接続成功した際に設定ダイアログは自動で閉じられますが、Edgeのブラウザが最前面に表示されるため、制御用アプリを再度最前面に表示するためにEdgeブラウザが表示されている箇所以外の座標を用意してください。
  - dofbot_app_servo1_scroll_coodinate ~ dofbot_app_servo6_scroll_coodinateはDofbotの各サーボを制御するために必要な座標です。

- config.tomlの設定が終わったら仮想環境で以下のコマンドでサーバーを起動します。
```
python server/sephiroth/kether/main.py
```

- http://localhost:6001 でサーバーが起動し、Dofbotの制御アプリが手元PCの最前面に出ていたら同一ネットワーク環境の他端末から以下のようにcurlコマンドを飛ばしたり他端末のPostmanからリクエストを飛ばすことでロボットアームを制御できます。

```sh
curl -X POST http://(サーバーを動かしているPCのIPアドレス):6001/api/v1/controller \
    -H "Content-Type: application/json" \
    -d '{"servo1": 0, "servo2": 0, "servo3": 0, "servo4": 0, "servo5": 0, "servo6": 0}'
```