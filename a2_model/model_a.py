import subprocess
import re
import random
import os
import shutil
import base64

def model(jsdatanum,save_fd):
    #jsdatanum=5000

    if os.path.exists(save_fd+'/a2_o_base_str_txt'):
        shutil.rmtree(save_fd+'/a2_o_base_str_txt')
    if os.path.exists(save_fd+'/a2_o_wobfuscator'):    
        shutil.rmtree(save_fd+'/a2_o_wobfuscator')
    if os.path.exists(save_fd+'/a2_o_wasm'):
        shutil.rmtree(save_fd+'/a2_o_wasm')
    if os.path.exists(save_fd+'/a2_o_wat'):
        shutil.rmtree(save_fd+'/a2_o_wat')
    if os.path.isfile(save_fd+'/a2_error_file_list.txt'):
        os.remove(save_fd+'/a2_error_file_list.txt')

    os.mkdir(save_fd+'/a2_o_base_str_txt')
    os.mkdir(save_fd+'/a2_o_wobfuscator')
    os.mkdir(save_fd+'/a2_o_wasm')
    os.mkdir(save_fd+'/a2_o_wat')

    print("<CHANGE>")  

    for num1 in range(jsdatanum):
        jspath=save_fd+"/a1_o_jsdata/"+str(num1+1)+".js"
        wobfuscator_o_path=save_fd+"/a2_o_wobfuscator/"+str(num1+1)
        sp1=subprocess.run(['node', 'a2_model/wobfuscator_tool/Wobfuscator/build/index.js', '-f', jspath, '-o',wobfuscator_o_path],stdout=subprocess.PIPE)

        try:
            f1 = open(wobfuscator_o_path,'r')
            data=f1.read()
            f1.close()
            data=data.replace(" ","").replace("\t","").replace("\n","")
            try:
                findstr = re.findall('(?<=__wasmStringModules=\[\').+?(?=\'\])',data)[0]
                base_str_list=findstr.split("','")
                choise_base=random.choice(base_str_list)
                choise_base_path=save_fd+"/a2_o_base_str_txt/"+str(num1+1)+".txt"
                try:
                    f2=open(choise_base_path,'w')
                    f2.write(choise_base)
                    f2.close()
                except FileNotFoundError as e:
                    print("***choise_error:"+str(num1+1)+str(e))
                if os.path.isfile(wobfuscator_o_path):
                    os.remove(wobfuscator_o_path)
            except IndexError as e:
                print("***find_error:"+str(num1+1)+str(e))
                f3=open(save_fd+"/a2_error_file_list.txt",'a')
                f3.write(str(num1+1)+"\n")
                f3.close()
                continue
        except FileNotFoundError as e:
            print("***filenotfound_error:"+str(num1+1)+str(e))
            f3=open(save_fd+"/a2_error_file_list.txt",'a')
            f3.write(str(num1+1)+"\n")
            f3.close()
            continue

        wasm_a_o_path=save_fd+"/a2_o_wasm/"+str(num1+1)+".wasm"
        sp2=subprocess.run(['base64', '-d', choise_base_path],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if sp2.stderr!="":
            with open(wasm_a_o_path, "wb") as f:
                f.write(sp2.stdout)
        if os.path.isfile(choise_base_path):
            os.remove(choise_base_path)

        wat_a_o_path=save_fd+"/a2_o_wasm/"+str(num1+1)+".wat"
        sp3=subprocess.run(['wasm2wat', wasm_a_o_path, '-o',wat_a_o_path],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if os.path.isfile(wasm_a_o_path):
            os.remove(wasm_a_o_path)
        wat_new_path=save_fd+"/a2_o_wat"
        sp4=subprocess.run(['mv', wat_a_o_path, wat_new_path], stdout=subprocess.PIPE, text=True)
        if sp4.returncode!=0:
            print("ERROR %s" % str(num1+1))
            f3=open(save_fd+"/a2_error_file_list.txt",'a')
            f3.write(str(num1+1)+"\n")
            f3.close()
    return 0

if __name__=="__main__":
    jsdatanum=5000
    result=model(jsdatanum)