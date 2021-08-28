from library.json_lib import *
# import os
import sqlite3
link_db = 'database/pokeinfo.db'
link_json = 'pokemon/pokedex.json'
connection = sqlite3.connect('database/pokeinfo.db')
print("Connect successful")
content = read_json_local(link_json)
for item in range(0,len(content),1):
    ID_  = content[item]["id"]
    name = content[item]["name"]["english"]
    type_poke = content[item]["type"][0]
    Hp = content[item]["base"]["HP"]
    Atk = content[item]["base"]["Attack"]
    Def = content[item]["base"]["Defense"]
    Speed = content[item]["base"]["Speed"]
    sql_sequence = "INSERT INTO poke_info values (?,?,?,?,?,?,?)"
    connection.execute(sql_sequence,(ID_,name,type_poke,Hp,Atk,Def,Speed))
    connection.commit()
print("Upload successful")
connection.close()
