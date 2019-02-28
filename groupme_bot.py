import requests
import time
from funcs import add_word, get_word, leninc, indexinc
from random import randint
from key import token, groupaddr, bot_id
from markovchain import read_text, mchain, message

myurl = 'https://api.groupme.com/v3/bots/post'

request_params = { 'token':token}

while True:
    response = requests.get(groupaddr, params = request_params)
    if (response.status_code == 200):
        response_messages = response.json()['response']['messages']
    

        for m in response_messages:
            text =''
            string = m['text']
            strlist = string.split() 

            #Call/Response Harry
            if strlist[0] == '/help':
                text = 'COMMANDS\n--------------------------------\nadd word: "Harry ____"\nget phrase: "Show me Harry"'
            
            if strlist[0] == 'Harry':
                add_word(strlist[1])
                text = 'added ' + strlist[1] + ' to the wordbank'
            
            if strlist[0] == 'Show' and strlist[1] == 'me' and strlist[2] == 'Harry':
                text = get_word()
            
            #Markov Chain Harry
            if strlist[0] != 'Harry' and strlist[0] != '/help' and 'h/' not in string:
                avglen = int(round(leninc(len(strlist)) / indexinc()))
                if m['name'] == 'Eliott Brown':
                    txt = open("elog.txt", "a+")
                    txt.write(string + ' ')
                    txt.close()
                    contents = read_text("elog.txt")
                    chain1 = {}
                    emarkovchain = mchain(contents, chain1)
                    print(emarkovchain)
                if m['name'] == 'Ozan Ergungor':
                    txt = open("olog.txt", "a+")
                    txt.write(string + ' ')
                    txt.close()
                    contents = read_text("olog.txt")
                    chain2 = {}
                    omarkovchain = mchain(contents, chain2)
                    print(omarkovchain)
                if m['name'] == 'Izuho Suzuki':
                    txt = open("ilog.txt", "a+")
                    txt.write(string + ' ')
                    txt.close()
                    contents = read_text("ilog.txt")
                    chain3 = {}
                    imarkovchain = mchain(contents, chain3)
                    print(imarkovchain)
                if m['name'] == 'Martin Konstantinov':
                    txt = open("mlog.txt", "a+")
                    txt.write(string + ' ')
                    txt.close()
                    contents = read_text("mlog.txt")
                    chain4 = {}
                    mmarkovchain = mchain(contents, chain4)
                    print(mmarkovchain)
                if m['name'] == 'Alvaro Matos':
                    txt = open("alog.txt", "a+")
                    txt.write(string + ' ')
                    txt.close()
                    contents = read_text("alog.txt")
                    chain5 = {}
                    amarkovchain = mchain(contents, chain5)
                    print(amarkovchain)
                if m['name'] == 'Damian Viramontes':   
                    txt = open("dlog.txt", "a+")
                    txt.write(string + ' ')
                    txt.close()
                    contents = read_text("dlog.txt")
                    chain6 = {}
                    dmarkovchain = mchain(contents, chain6)
                    print(dmarkovchain)
                
                if strlist[0] == 'h/Eliott':
                    text = message(emarkovchain, avglen)
                if strlist[0] == 'h/Ozan':
                    text = message(omarkovchain, avglen)
                if strlist[0] == 'h/Izuho':
                    text = message(imarkovchain, avglen)
                if strlist[0] == 'h/Martin':
                    text = message(mmarkovchain, avglen)
                if strlist[0] == 'h/Alvaro':
                    text = message(amarkovchain, avglen)
                if strlist[0] == 'h/Damian':
                    text = message(dmarkovchain, avglen)

            body = {'bot_id': bot_id, 'text': text}
            #requests.post(url = myurl, data = body)
            request_params['since_id'] = m['id']
            break

    time.sleep(5)