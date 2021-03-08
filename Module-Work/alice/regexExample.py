#%%
import pandas as pd 
alice_Df = pd.read_csv('./alice.txt', sep='\n\n')
# %%
alice_Df.head()
# %%
alice_Df.columns = ['text']
#%%
searchTerm = 'cat'
# %%
alice_Df[alice_Df['text'].str.contains(searchTerm)]
# %%
someString = 'Ring a string about rings'
# %%
someString.__contains__('ring')
# %%
pattern = 'ring'
# %%
import re
#%%

result = re.search(pattern=pattern, string = someString)
# %%
result.group(0)
# %%
result2 = re.search('\w+ing', someString)
# %%
result2.group(0)
# %%
