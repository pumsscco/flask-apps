# 考勤应用

开发环境的运行方式：
```bash
#先激活virtualenv环境
source attn/bin/activate
#再配置flask环境变量
export FLASK_APP=attn.py
export FLASK_DEBUG=1
export FLASK_ENV=development
#最后带专用端口跑
flask run -p 5001
```

# 分页
之前项目没实现分页，这回必须实现了
* 通过借用原书中的范例，再加上修复错误，初步实现了分页功能
* 通过sqlalchemy的text过滤法，解决了月份间隔的计算问题

# 中文
通过app的配置项解决了json化时，中文显示不正常的问题
```python
app.config['JSON_AS_ASCII'] = False
```
