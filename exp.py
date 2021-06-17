import pymysql

db = pymysql.connect(host='120.77.177.229', user='root', password='123456', port=3306, db='music_maneger')
cursor = db.cursor()
