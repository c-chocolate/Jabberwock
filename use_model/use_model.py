import numpy as np
import pandas as pd
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import os
import itertools
import statistics
import math
import shutil
import time
import sys

def ex_vec(mode,a_model_num,parameter,outputfd):
    ####################################################################
    vec_size=100
    epoch_num=10
    min_count=5
    dm=1

    if mode==1:
        vec_size=int(parameter)
        name="_vec"+str(vec_size)+"_dm"+str(dm)
        print("<USE_MODEL : use_model.py / vec_size:"+str(vec_size)+">")
    elif mode==2:
        epoch_num=int(parameter)
        name="_epoch"+str(epoch_num)+"_dm"+str(dm)
        print("<USE_MODEL : use_model.py / epoch_num:"+str(epoch_num)+">")
    elif mode==3:
        min_count=int(parameter)
        name="_mincount"+str(min_count)+"_dm"+str(dm)
        print("<USE_MODEL : use_model.py / min_count:"+str(min_count)+">")
    elif mode==4:
        dm=int(parameter)
        name="_dm"+str(dm)
        print("<USE_MODEL : use_model.py / dm:"+str(dm)+">")   
    ####################################################################

    csv_text=","+str(vec_size)+","+str(epoch_num)+","+str(min_count)+","+str(dm)


    if os.path.exists('use_model/error_txt'):
        shutil.rmtree('use_model/error_txt')
    os.mkdir('use_model/error_txt')

    if os.path.exists('use_model/model'):
        shutil.rmtree('use_model/model')
    os.mkdir('use_model/model')    

    error_file_path='use_model/error_txt/use_model_error_file_list.txt'

    wat_split_data=[]
    for num1 in range(a_model_num):
        wat_path="a2_o_wat/"+str(num1+1)+".wat"
        try:
            f1=open(wat_path,'r')
            watdata=f1.read()
            f1.close()
            if watdata:
                watsplit = watdata.split("\n")
                wat_split_data.append(watsplit)
        except FileNotFoundError as e:
            print("***filenotfound_error:"+str(num1+1)+str(e))
            f3=open(error_file_path,'a')
            f3.write(str(num1+1)+"\n")
            f3.close()

    print("<TRAINING>")
    trainings = [TaggedDocument(data, [i]) for i,data in enumerate(wat_split_data)]
    doc2vec = Doc2Vec(documents= trainings,vector_size=vec_size,epochs=epoch_num,min_count=min_count,dm=dm)
    doc2vec.save("use_model/model/doc2vec"+name+".model")
    print("<SAVE : doc2vec"+name+".model>")

    vector=list(map(doc2vec.infer_vector,wat_split_data))
    print("<COMPLETE : vectoraize>")

    data=dict(
        data=vector,
        )
    df=pd.DataFrame(data=data)

    df.to_pickle(outputfd+'/data'+name+'.pkl')

    return csv_text

if __name__=="__main__":
    mode=1
    url_num=3
    parameter=10
    outputfd="pkl"
    result=ex_vec(mode,url_num,parameter,outputfd)