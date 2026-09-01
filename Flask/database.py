from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:demopassword@mysql:3307/demodb')
