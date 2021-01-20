from dotenv import load_dotenv
load_dotenv('.env')
import os # for importing env vars for the bot to use
from sqlalchemy import create_engine

def add_data(df):
    connect = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (
        os.environ['DB_USER'],
        os.environ['DB_PWD'],
        os.environ['DB_HOST'],
        os.environ['DB_PORT'],
        os.environ['DB_DB']
    )
    
    engine = create_engine(connect)
    df.to_sql(
        'kapsarc_task', 
        con=engine, 
        index=False, 
        if_exists='replace'
    )

    print("to_sql() done (sqlalchemy)")
        