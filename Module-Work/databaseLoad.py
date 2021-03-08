#%%
from sqlalchemy import create_engine
import pandas as pd
# %%
# conn string example 'postgresql://scott:tiger@localhost/mydatabase'
connectionEngineObject = create_engine('postgresql://postgres:0440@localhost/PH-EmployeeDB', echo=True)
# %%
connectionEngineObject.table_names()
# %%
alice_Df = pd.read_csv('./alice/alice.txt', sep='\n\n')
# %%
alice_Df.to_sql(
    name='AliceInWonderland',
    con=connectionEngineObject,
    index=True,
    index_label='paragraphId'
)
# %%
