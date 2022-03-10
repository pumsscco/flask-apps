# flask-apps
借此项目，全面实战flask2.0的各种功能
* flask-sqlalchemy是要实战的，虽然go版本没有使用ORM来操作数据库，但这里还是先延用django框架的实现思路来处理
* 此次除实现gin框架项目的全部功能外，还要研究**celery**的用法，顺带把golang的**machinery**也学会
* 原本打算支持get，看来是不成了，如果做rest api，post带参数是正常做法
* 干脆做一个前后端一体化的项目，先拿考勤来作试验，界面可以参照golang的项目！
# sql
经查，使用以下语句实现了数据库模型的导出
```bash
sqlacodegen mysql://flask:bTzxVYVt5PQT2SgsJ4JzjNEW@mysql:3306/flask > models.py
```
以上方法似乎不是特别好，所以改用
```bash
flask-sqlacodegen 'mysql://flask:bTzxVYVt5PQT2SgsJ4JzjNEW@mysql/flask' --tables attendance --outfile "attn/models.py"  --flask
```
重新实现了一遍，效果更符合预期
# 项目规划
* attendance: 考勤项目
* crh: 楚留香项目
* pal4: 仙剑四项目
* rest: REST API接口
* stock: 股票项目
以上项目中，除rest项目为纯后端项目外，其它项目均为前后端一体项目，自用之前bootstrap作为前端的模式
# 考勤
仍从该项目开始编写，从简单到难
# 股票
比考勤复杂些，但仍是单表
# 楚留香
开始变复杂了，有更多表了
# 仙剑四
相当复杂的关系网，接近于真实项目了！