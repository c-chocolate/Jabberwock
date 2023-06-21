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

def ex_vec(mode,benign_model_num,malicious_model_num,parameter,save_fd):
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


    if os.path.exists(save_fd+'/model'):
        shutil.rmtree(save_fd+'/model')
    os.mkdir(save_fd+'/model')    
    if os.path.exists(save_fd+'/pkl'):
        shutil.rmtree(save_fd+'/pkl')
    os.mkdir(save_fd+'/pkl') 

    error_file_path=save_fd+'use_model_error_file_list.txt'

    wat_split_data_benign=[]
    for num1 in range(benign_model_num):
        wat_path="benign_data/a2_o_wat/"+str(num1+1)+".wat"
        try:
            f1=open(wat_path,'r')
            watdata=f1.read()
            f1.close()
            if watdata:
                watsplit = watdata.split("\n")
                wat_split_data_benign.append(watsplit)
        except FileNotFoundError as e:
            print("***filenotfound_error:"+str(num1+1)+str(e))
            f3=open(error_file_path,'a')
            f3.write(str(num1+1)+"\n")
            f3.close()
    wat_split_data_malicious=[]
    for num2 in range(malicious_model_num):
        wat_path="malicious_data/a2_o_wat/"+str(num2+1)+".wat"
        try:
            f1=open(wat_path,'r')
            watdata=f1.read()
            f1.close()
            if watdata:
                watsplit = watdata.split("\n")
                wat_split_data_malicious.append(watsplit)
        except FileNotFoundError as e:
            print("***filenotfound_error:"+str(num2+1)+str(e))
            f3=open(error_file_path,'a')
            f3.write(str(num2+1)+"\n")
            f3.close()
    print(len(wat_split_data_benign))
    print(len(wat_split_data_malicious))
    if len(wat_split_data_benign)<len(wat_split_data_malicious):
        wat_split_data=wat_split_data_benign+wat_split_data_malicious[:len(wat_split_data_benign)]
    else:
        wat_split_data=wat_split_data_benign[:len(wat_split_data_malicious)]+wat_split_data_malicious
    print(len(wat_split_data))


    print("<TRAINING>")
    trainings = [TaggedDocument(data, [i]) for i,data in enumerate(wat_split_data)]
    doc2vec = Doc2Vec(documents= trainings,vector_size=vec_size,epochs=epoch_num,min_count=min_count,dm=dm)
    doc2vec.save(save_fd+"/model/doc2vec"+name+".model")
    print("<SAVE : doc2vec"+name+".model>")

    vector_benign=list(map(doc2vec.infer_vector,wat_split_data_benign))
    vector_malicious=list(map(doc2vec.infer_vector,wat_split_data_malicious))
    print("<COMPLETE : vectoraize>")

    data_benign=dict(
        data=vector_benign,
        )
    df_benign=pd.DataFrame(data=data_benign)
    df_benign.to_pickle(save_fd+'/pkl/data_benign'+name+'.pkl')

    data_malicious=dict(
        data=vector_malicious,
        )
    df_malicious=pd.DataFrame(data=data_malicious)
    df_malicious.to_pickle(save_fd+'/pkl/data_malicious'+name+'.pkl')

    return csv_text

if __name__=="__main__":
    mode=1
    url_num=3
    parameter=10
    save_fd="pkl"
    result=ex_vec(mode,url_num,parameter,save_fd)