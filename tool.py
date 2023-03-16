from a1_collect import collect_a as ex_collect
from a2_model import model_a as ex_model
from use_model import use_model as ex_vec
import time
import os
import sys

csv_text=",,,"
save_js_num=-1

if not os.path.exists('pkl'):
    os.mkdir('pkl')

##################################
input_file_name="url_list.txt"
url_num=int(sys.argv[3])
mode=int(sys.argv[1])
parameter=int(sys.argv[2])
tool_type=int(sys.argv[4]) 
outputfd="pkl"
##################################

if tool_type==0 or tool_type==1:
    save_js_num=ex_collect.collect(input_file_name,url_num)

    model=ex_model.model(url_num)

if tool_type==0 or tool_type==2:
    csv_text=ex_vec.ex_vec(mode,url_num,parameter,outputfd)
