from a1_collect import collect_a as ex_collect
from a2_model import model_a as ex_model
from use_model import use_model_nonlabel as ex_vec_nonlabel
from use_model import use_model_label as ex_vec_label
import time
import os
import sys
import argparse

csv_text=",,,"
save_js_num=-1


parser = argparse.ArgumentParser()
parser.add_argument("--benign_list", default="benign_list.txt", type=str)    
parser.add_argument("--malicious_list", default="malicious_list.txt", type=str)     
parser.add_argument("--nonlabel_list", default="nonlabel_list.txt", type=str)    
parser.add_argument("-l", "--label_mode", default=0, type=int)
parser.add_argument("-b", "--benign_num", default=100, type=int)
parser.add_argument("-m", "--malicious_num", default=100, type=int)
parser.add_argument("-n", "--nonlabel_num", default=100, type=int)
parser.add_argument("-v", "--vec_mode", default=1, type=int)
parser.add_argument("-p", "--parameter", default=100, type=int)
parser.add_argument("-t", "--tool_type", default=0, type=int)
args = parser.parse_args()

benign_urllist_file_name=args.benign_list
malicious_urllist_file_name=args.malicious_list
nonlabel_urllist_file_name=args.nonlabel_list
label_mode=args.label_mode
nonlabel_num=args.nonlabel_num
benign_num=args.benign_num
malicious_num=args.malicious_num
vec_mode=args.vec_mode
parameter=args.parameter
tool_type=args.tool_type

##################################

if label_mode==1:
    save_fd="benign_data"
    if tool_type==0 or tool_type==1:
        save_js_num=ex_collect.collect(benign_urllist_file_name,benign_num,save_fd)
        model=ex_model.model(benign_num,save_fd)

    save_fd="malicious_data"
    if tool_type==0 or tool_type==1:
        save_js_num=ex_collect.collect(malicious_urllist_file_name,malicious_num,save_fd)
        model=ex_model.model(malicious_num,save_fd)

    save_fd="label_data"
    if tool_type==0 or tool_type==2:
        csv_text=ex_vec_label.ex_vec(vec_mode,benign_num,malicious_num,parameter,save_fd)

elif label_mode==2:
    save_fd="non_label_data"
    if tool_type==0 or tool_type==1:
        save_js_num=ex_collect.collect(nonlabel_urllist_file_name,nonlabel_num,save_fd)
        model=ex_model.model(nonlabel_num,save_fd)
    if tool_type==0 or tool_type==2:
        csv_text=ex_vec_nonlabel.ex_vec(vec_mode,nonlabel_num,parameter,save_fd)
