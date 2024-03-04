from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_io = SocketIO(app)

# 라우팅
# - 채팅 기능을 실험해보기 위한 html
@app.route('/')
def index():
    return render_template('index.html')

def msg_received(methods=['GET', 'POST']):
    print("CALLBACK : msg received")

    # DB connection -> save


# 소켓 연결 (클라이언트 - 서버)
@socket_io.on('my event')
def handle_chat_event(json, methods=['GET', 'POST']):
    print(f'데이터 수신 완료 : {json}')
    socket_io.emit('my response', json, callback=msg_received)

if __name__ == '__main__':
    socket_io.run(app, debug=True)


