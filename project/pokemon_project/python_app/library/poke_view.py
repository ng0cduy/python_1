from library.sql_lib import *
class Pokemon(Database):
    def __init__(self,path_db):
        Database.__init__(self,path_db)
    def read_poke_info(self):
        chuoi_sql = "SELECT * FROM poke_info"
        noi_dung = Database.get_all(self,chuoi_sql)
        ds_poke =[]
        for dong in noi_dung:
            pokemon = {"ID": dong[0],"Name":str(dong[1]).capitalize(),"Type":str(dong[2]).capitalize(),"HP":dong[3],"Attack":dong[4],"Defense":dong[5],"Speed":dong[6]}
            ds_poke.append(pokemon)
        return ds_poke
    def add_pkm (self,ID_,Name_,Type_,HP_,Attack_,Defense_,Speed_):
        chuoi_sql = "INSERT INTO poke_info VALUES(?,?,?,?,?,?,?)"
        kq=Database.execute(self,chuoi_sql,(ID_,Name_,Type_,HP_,Attack_,Defense_,Speed_))
        return kq
    def find_pkm(self,keyword):
        con_seq = "%"+keyword+"%"
        sql_seq = 'SELECT * FROM poke_info Where Name like ?'
        content = Database.get_all(self,sql_seq,(con_seq,))
        poke_list = []
        for pokemon in content:
            pokemon_ = {"ID": pokemon[0],"Name":pokemon[1],"Type":pokemon[2],"HP":pokemon[3],"Attack":pokemon[4],"Defense":pokemon[5],"Speed":pokemon[6]}
            poke_list.append(pokemon)
        return poke_list
    def del_pkm(self,ID):
        sql_seq = 'DELETE FROM poke_info Where ID = ?'
        result = Database.execute(self,sql_seq,(ID,))
        return result
    def update_pkm(self,ID_,name_,type_,HP_,atk_,def_,sp_):
        sql_seq = "UPDATE poke_info SET \
                    name = ?,\
                    type=  ?,\
                    HP=    ?,\
                    Attack=?,\
                    Defense=?,\
                    Speed=  ? \
                    Where ID=?"
        result = Database.execute(self,sql_seq,(name_,type_,HP_,atk_,def_,sp_,ID_))
        return result
