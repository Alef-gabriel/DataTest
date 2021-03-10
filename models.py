import sqlalchemy as db

engine = db.create_engine('sqlite:///D:/CNPJ_full.db')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('empresas', metadata, autoload=True, autoload_with=engine)
query = db.select([census])

ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()

print(ResultSet.get_all())