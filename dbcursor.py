import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://gencord:Universemandarin5#@cluster0.vlpfp.mongodb.net/gencord?retryWrites=true&w=majority")
print("Connected to db")
db = cluster["gencordbot"]
currency_collection = db["currency"]
characters_collection = db["characters"]
genshin_collection = db["genshindata"]



class genshindata():
    @staticmethod
    def check_user(d_id):
        if genshin_collection.find({"_id" : d_id}).count() > 0:
            return True
    @staticmethod
    def add_user(d_id, g_id, wl, g_name, g_rank):
        post = {"_id" : d_id, "g_id" : g_id, "wl" : wl, "g_name" : g_name, "g_rank" : g_rank}
        characters_collection.insert_one(post)
        
        



def add_user(userid):
    try:
        if currency_collection.find({"_id" : userid}).count() > 0:
            return "exists"
        post1 = {"_id" : userid, "primogems" : 300, "mora" : 50000}
        post2 = {"_id" : userid, "characters" : {}}
        currency_collection.insert_one(post1)
        characters_collection.insert_one(post2)
        return "noerr"
    except:
        return "err"



def get_user_bal(userid):
    #data = {"primogems" : 0, "mora" : 0}
    query = {"_id" : userid}
    result = currency_collection.find_one(query)
    if str(result) == "None":
        return None
    return dict(result)

def update_bal_p(userid, amount):
    amount = int(amount)
    currency_collection.update_one({"_id" : userid}, {"$set" : {"primogems" : amount}})

def update_bal_m(userid, amount):
    amount = int(amount)
    currency_collection.update_one({"_id" : userid}, {"$set" : {"mora" : amount}})


def add_character(userid, character):
    userid = int(userid)
    character = str(character)
    current_characters = characters_collection.find_one({"_id" : userid})
    char_dict = current_characters["characters"]
    if character in char_dict:
        c_level = char_dict[character]
        c_level = int(c_level)
        c_level = c_level + 1
        char_dict[character] = c_level
    else:
        char_dict.update({character : 0})
    
    characters_collection.update_one({"_id" : userid}, {"$set" : {"characters" : char_dict}})


def get_characters(userid):
    userid = int(userid)
    current_characters = characters_collection.find_one({"_id" : userid})
    if current_characters == None:
        return None
    else:
        return current_characters["characters"]


def gift_primos(g_id, r_id, amount):
    g_id = int(g_id)
    r_id = int(r_id)
    current_balance_g = get_user_bal(g_id)
    current_balance_r = get_user_bal(r_id)
    if current_balance_g == None:
        return None
    elif current_balance_r == None:
        return None

    if int(current_balance_g["primogems"]) < amount:
        return False

    new_p_g = int(current_balance_g["primogems"]) - amount
    new_p_r = int(current_balance_r["primogems"]) + amount
    update_bal_p(g_id, new_p_g)
    update_bal_p(r_id, new_p_r)
    return True

        


    



