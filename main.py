from flask import Flask,jsonify
import yaml,pymysql,redis,json
app = Flask(__name__)
def get_config():
    cnf=yaml.safe_load(open("config.yml"))
    return cnf
def mysql_conn():
    cnf=get_config()
    m=pymysql.connect(
        host=cnf["mysql"]["host"],
        user=cnf["mysql"]["user"],
        password=cnf["mysql"]["pass"],
        db=cnf["mysql"]["db"],
        port=cnf["mysql"]["port"],
        cursorclass=pymysql.cursors.DictCursor
    )
    return m
def redis_conn():
    cnf=get_config()
    r=redis.Redis(
        host=cnf['redis']['host'],
        port=cnf['redis']['port'],
        db=cnf['redis']['db'],
        password=cnf['redis']['pass']
    )
    return r

@app.route('/attendance/<duration>')
def attn_rec(duration):
   if duration == "latest":
        r=redis_conn()
        latest=""
        tmp=r.get("attendance:latest")
        print(tmp)
        if tmp: latest=json.loads(tmp)
        if not latest:
            m=mysql_conn()
            cur=m.cursor()
            sql="select checkin,checkout,comments from attendance order by checkin desc limit 1"
            cur.execute(sql)
            latest=cur.fetchone()
            latest_d={
                "checkin": str(latest["checkin"]),
                "checkout": str(latest["checkout"]),
                "comments": str(latest["comments"])
            }
            latest_s=json.dumps(latest_d)
            r.set("attendance:latest",latest_s)
        return jsonify(latest)
if __name__ == "__main__":
    app.run(host='0.0.0.0')


