from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
from pprint import pprint
import requests
from flask import Flask, make_response, jsonify, current_app
from flask import request
from flask_restful import Resource, Api

from sklearn.feature_extraction.text import TfidfVectorizer
from numpy import dot
from sklearn.metrics.pairwise import cosine_similarity as cossim
from scipy.spatial.distance import cosine
from sklearn.decomposition import TruncatedSVD, PCA
from sklearn.datasets import load_iris
# Create your views here.
global pokee
pokee = "디아루가"

def cos_sim(A, B): # cosine similarity function
    return np.dot(A, B)/(np.linalg.norm(A)*np.linalg.norm(B))

def poke_recommend(poke):
    if poke in pokelist: # if pokemon exists in the list
        poke_idx = pokelist.index(poke)
        poke_sim = []
        poke_ret = []
        for i in range(len(pokelist)): # calculate cosine similarity with other pokemon
            poke_sim.append([i, cos_sim(data.iloc[poke_idx][2:].tolist(), data.iloc[i][2:].tolist())])
        poke_sim.sort(key=lambda x: x[1], reverse = True) # sort highest to lowest cosine similarity 
        poke_out = [pokelist[poke_sim[1][0]], pokelist[poke_sim[2][0]], pokelist[poke_sim[3][0]]] # find 3 most similar pokemons(first is identical pokemon)
        poke_ret.append(poke_out)
        poke_ret.append(poke_sim)
        return poke_ret # list consists of 2 elements, 1st: recommended pokemon lists, 2nd: 
    else:
        # NUGU recall "다시 한 번 포켓몬을 말씀해주세요"
        return None
def difgen_recommend(poke):
    if poke in pokelist: # if pokemon exists in the list
        
        pokname = pd.read_csv('./pokedataused/pokedatacos2.csv')
        pokname.set_index(pokname['name'], inplace = True)
        pokname= pokname.drop(['name'], axis = 1)
        poknum = pokname.drop(['dexnum','poppoint','sets'], axis = 1)
        poknum = poknum[poknum['prime'] == 1]
        df = pd.read_csv('./pokedataused/cospokysptn.csv')
        df.set_index(pokname.index, inplace = True)
        '''dfusrch = df.loc[:, df.columns.isin(dfpokso['name'])]
        dfusrchu = dfusrch.copy()'''
        
        dfusr = df.sort_values(by = poke, axis = 0, ascending = False)
        chui = [dfusr[poke].index[0],dfusr[poke].index[1],dfusr[poke].index[2]]
        return chui 
    else:
        return None
#pokemon dataframe
global data, pokelist
data = pd.read_csv("./pokedataused/pokedata.csv") # read data
pokelist = data['name'].tolist()

global dfpok
dfpok = pd.read_csv('./pokedataused/pokedatacos2.csv')
#dfpok = dfpok.drop(['Unnamed: 0'], axis = 1)
'''pokdex = pd.Series(dfpok.index + 1, index=dfpok['name'])
dfusr = pd.read_csv('./pokedataused/pseudouser.csv')
dfpokso = pd.read_csv('./pokedataused/train241.csv')
df = pd.read_csv('./pokedataused/cospokysptn.csv')'''
app = Flask(__name__)
api = Api(app)#외부에서 접속 되려면 python manage.py runserver 0.0.0.0:8000

#@app.route('/poketalk', methods= ['POST'])
#with app.app_context():
class arceus(Resource):#APIView
    
    global pokenametrans
    pokenametrans = ("./configure_package/pokenametrans.json")
    def healthCheck():
        return "OK"
    def post(self, pokee): #returning replies
        #poke = request.POST.get["pokname"]
        #poke = json.loads(request.body)
        
        porke = request.get_json()
        print(porke)    
        pokename = pokenametrans(porke)
        
        pokereply = poke_recommend(pokename)
        pokereply = poke_recommend(porke)#sample
        response_builder = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {
                "pokemonreply1": pokereply[0],
                "pokemonreply2": pokereply[1],
                "pokemonreply3": pokereply[2],
             },
        }
        return jsonify(response_builder)
api.add_resource(arceus, '/')
if __name__ == "__main__":
    app.run(debug=True)
{
    "version": "2.0",
    "action": {
         "actionName": "",#액션의 이름
         "parameters": {#액션에서 설정된 파라미터 이름
              "brand": {
                 "type": "BRAND",
                 "value": "BRAND_NAME"
               },
              "product":{
                 "type": "PRODUCT",
                 "value": "PRODUCT_NAME"
               }
          }
    }
}
#poke_out =[]
'''poke_out = poke_recommend(poke)[0] # recommended 3 pokemons

pokepoke = difgen_recommend(poke)
popopo = answers(pokepoke)
print(poke_out)
print(pokepoke)'''