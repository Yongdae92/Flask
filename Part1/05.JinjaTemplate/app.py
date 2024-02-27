from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'title':'Flask Jinja Template',
        'user':'GOAT 진우',
        'is_admin':True,
        'item_list':['Iitem1', 'Item2', 'Item3']  
    }

    # (1) 렌더링할 html vㅏ일명 입력
    # (2) html 넘겨줄 데이터 입력
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)