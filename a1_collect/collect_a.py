import os
import shutil
import urllib.error
import urllib.request
import random
import http.client
import requests
import re
import socket
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

def get_html(url):
    if url.startswith('http'):
        request = urllib.request.Request(url, headers=headers)
    else:
        request = urllib.request.Request('http://'+url, headers=headers)
    try:
        resp = urllib.request.urlopen(request, timeout=5)
        html=resp.read()
        if html:
            return html
        else:
            return None
    except (socket.timeout, urllib.error.HTTPError, urllib.error.URLError, http.client.BadStatusLine, http.client.IncompleteRead, http.client.HTTPException,
        UnicodeError, UnicodeEncodeError,requests.exceptions.ConnectionError,ConnectionResetError) as e: # possibly plaintext or HTTP/1.0
        #print("HTML_ERROR:", url,e)
        print("***find_error:"+url+str(e))
        return None
    except:
        raise

def get_js_link(url):
    html = get_html(url)
    linkheader=re.search(r'.+\/',url).group()
    if html:
        try:
            decodehtml = html.decode('utf-8')
            decodehtml = decodehtml.replace(' ','')
            findjssrc = re.findall(r'src=[\",\'][a-z,A-Z,0-9,\-,\_,\.,\!,\',\(,\),\~,\s,\/]+\.js[\",\']',decodehtml) 
            findjshref = re.findall(r'href=[\",\'][a-z,A-Z,0-9,\-,\_,\.,\!,\',\(,\),\~,\s,\/]+\.js[\",\']',decodehtml) 
            findjs = findjssrc + findjshref
            findjsurl = re.findall(r'https?://[a-z,A-Z,0-9,\-,\_,\.,\!,\',\(,\),\~,\s,\/]+\.js[\",\']',decodehtml)

            for index, value in enumerate(findjs):
                findjs[index] = value.replace('src=','')
                findjs[index] = findjs[index].replace('href=','')
                findjs[index] = findjs[index].replace('"','')
                findjs[index] = findjs[index].replace("'","")
                
                if findjs[index][:2]=='//':
                    findjsurl.append('http:' + findjs[index])
                    findjs[index] = ''
                elif findjs[index][:1]=='/':
                    findjs[index]=findjs[index][1:]

            for index, value in enumerate(findjsurl):
                findjsurl[index] = value.replace('\"','')
                findjsurl[index] = findjsurl[index].replace("\'","")
            return findjs, findjsurl
        except (UnicodeDecodeError):
            print("***unicodedecode_error")
            return None,None
    else:
        return None, None

def link_to_url(url, link):
    if '/?' in url:
        url=re.search(r'.+\/\?',url).group()
        url=url[:-2]
    elif '/#' in url:
        url=re.search(r'.+\/\#',url).group()
        url=url[:-2]
    elif url.endswith("/"):
        url=url[:-1]

    if '/' in url.replace('://',''):
        linkheader=re.search(r'.+\/',url).group()
        linkheader=linkheader[:-1]
    else:
        linkheader=url

    if link!='':
        url=linkheader+"/"+ link
        return url
    else:
        return None


def collect(input_file_name,input_url_num):

    mode=0  
    done_url_num=382 
    save_url_num=1 

    if mode!=1:
        if os.path.exists('a1_o_jsdata'):
            shutil.rmtree('a1_o_jsdata')
        if os.path.isfile('a1_collect/error_file_list.txt'):
            os.remove('a1_collect/error_file_list.txt')
        if os.path.isfile('a1_collect/done_url_list.txt'):
            os.remove('a1_collect/done_url_list.txt')

        os.mkdir('a1_o_jsdata')

    f1=open(input_file_name, "r")
    urllist=f1.read().splitlines()[0:input_url_num]
    f1.close()

    for num1,url in enumerate(urllist):
        if (mode==1 and (num1+1)<=done_url_num):
            print("<SKIP URL "+str(num1+1)+"/"+str(len(urllist))+">:"+url)
            continue

        print("<URL "+str(num1+1)+"/"+str(len(urllist))+">:"+url)
        f2=open("a1_collect/done_url_list.txt",'a')
        f2.write("<URL "+str(num1+1)+"/"+str(input_url_num)+">:"+url+"\n")
        f2.close()

        jslink, jsurllink = get_js_link(url)
        js_url_list=[]
        if jslink!=None:
            for index, value in enumerate(jslink):
                from_link=link_to_url(url,value)
                js_url_list.append(from_link)
        if jsurllink:
            js_url_list+=jsurllink
      
        js_url_list=[i for i in js_url_list if i != None]
        js_url_list_num=len(js_url_list)
        for num2 in range(js_url_list_num):
            js_url=random.choice(js_url_list)
            js_url_list.remove(js_url)
            js_path="a1_o_jsdata/"+str(save_url_num)+".js"
            request = urllib.request.Request(js_url, headers=headers)
            try:
                resp = urllib.request.urlopen(request, timeout=10)
                data=resp.read().decode('utf-8')
                if data:
                    with open(js_path, mode='w') as save_file:
                        save_file.write(data)
                        print("<SAVE> : "+str(save_url_num)+".js")
                        save_url_num+=1
                        break
            except (socket.timeout, urllib.error.HTTPError, urllib.error.URLError, http.client.BadStatusLine, http.client.IncompleteRead, http.client.HTTPException,
                UnicodeError, UnicodeEncodeError,requests.exceptions.ConnectionError,ConnectionResetError) as e: # possibly plaintext or HTTP/1.0
                print(type(e))
                print("***html_error:"+str(save_url_num)+str(e))
            except:
                raise

    return save_url_num-1

if __name__=="__main__":
    input_file_name="a1_collect/test.txt"
    input_url_num=1000
    result=collect(input_file_name,input_url_num)