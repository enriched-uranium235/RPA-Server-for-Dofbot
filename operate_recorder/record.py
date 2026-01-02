from pynput import mouse

# マウスのクリックイベントを処理する関数
def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at ({x}, {y}) with {button}")
    else:
        print(f"Mouse released at ({x}, {y}) with {button}")

# マウスの移動イベントを処理する関数
def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

# マウスのスクロールイベントを処理する関数
def on_scroll(x, y, dx, dy):
    print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")

# リスナーを開始、Enterキーで終了
def start_listener():
    with mouse.Listener(
        on_click=on_click,
        on_move=on_move,
        on_scroll=on_scroll) as listener:
        print("Mouse listener started. Press Enter to stop.")
        input()  # Enterキーが押されるまで待機
        listener.stop()  # リスナーを停止
    print("Mouse listener stopped.")

if __name__ == "__main__":
    start_listener()