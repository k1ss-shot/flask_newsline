DATABASE = {
    'host': 'localhost',
    'database': 'db_news',
    'user': 'postgres',
    'password': 'postgres',
    'port': 5432,
}

SQLALCHEMY_DATABASE_URI = (
    'postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(database)s' % DATABASE
)