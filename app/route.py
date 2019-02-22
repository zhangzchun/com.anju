

# 总路由文件
from app.app import app

# 导入分路由
from app.route_case import case
from app.route_company import company
from app.route_designer import designer
from app.route_diary import diary

from app.route_search import search
from app.route_comment import comment

from app.route_strategy import strategy
from app.route_user import user


# 构建蓝图
# 案例
app.register_blueprint(case,url_prefix='/api/case')
# 公司
app.register_blueprint(company,url_prefix='/api/company')
# 设计师
app.register_blueprint(designer,url_prefix='/api/designer')
# 日记
app.register_blueprint(diary,url_prefix='/api/diary')

# 搜索
app.register_blueprint(search,url_prefix='/api/search')
# 评论
app.register_blueprint(comment,url_prefix='/api/comment')

# 攻略
app.register_blueprint(strategy,url_prefix='/api/strategy')
# 用户
app.register_blueprint(user,url_prefix='/api/user')


@app.route('/api/v1')
def index():
    return 'INDEX'
@app.errorhandler(404)
def miss(e):
    return '该页面不存在', 404
@app.errorhandler(500)
def error(e):
    return '服务器正在维护...', 500
