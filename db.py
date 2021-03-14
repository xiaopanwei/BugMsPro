import pymysql.cursors


def get_connection():
    connection = pymysql.connect(
        host='cdb-q35wa9cy.cd.tencentcdb.com', port=10094,
        user='root',
        password='a123456789',
        db='xpw_bugpro',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return connection
