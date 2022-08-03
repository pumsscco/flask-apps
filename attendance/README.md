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

