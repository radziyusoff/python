import warnings
from sqlalchemy import types, create_engine,exc as sa_exc	

engine = create_engine("mysql+pymysql://{login}:{password}@{ip_address}/{schema}".format(user=f"{login}",pw=f"{password}",db=f"{schema}"),connect_args={'connect_timeout': 10})
with warnings.catch_warnings():
  warnings.simplefilter("ignore", category=sa_exc.SAWarning)
  conn = engine.connect().execution_options(stream_results=True)
engine.dispose()
