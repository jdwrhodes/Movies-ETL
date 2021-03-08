#%%
import pandas as pd 
# %%
pokedex_df = pd.read_csv('Pokemon.csv')
# %%
pokedex_list = ["Type 1", "HP", "Attack", "Sp. Atk", "Sp. Def", "Speed"]
# %%
pokedex_new_df = pokedex_df[pokedex_list]
# %%
type_average_df = pokedex_new_df.groupby('Type 1').mean()
# %%
type_average_df['power_level'] = type_average_df[["HP", "Attack", "Sp. Atk", "Sp. Def", "Speed"]].sum(axis=1)
# %%
type_average_df.sort_values(ascending=False, inplace=True, by='power_level')
# %%
type_average_df.to_csv('power_pokedex.csv')
# %%
