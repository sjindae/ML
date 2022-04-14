from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')    # 하면
def index():       # 함수 실행됨
    return 'hello world' # render_template('index.html')

if __name__ == '__main__':    # 자기가 자기 파일 실행했을 경우 run 해라.
    app.run(debug=True)    # debug=True : 서비스 중간에 스스로 restart해준다.

# 웹서비스 기본 포트 : 80