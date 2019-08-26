#应用级别的初始化
#可以用pycharm的快捷键。alt+enter键快速导入。
from app import create_app

app = create_app()



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=app.config['DEBUG'], port=81)

