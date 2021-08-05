#! /usr/bin/env python
# coding=utf-8
import requests
import time

while True:
  apontime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

  ssh=[]
  sshoff=[]
  #放网址的txt 
  file = open(r'ssh.txt')
  # file = open(file) 
  lines = file.readlines() 
    
  for line in lines: 
      temp=line.replace('\n','') 
      ssh.append(temp) 

    
    # print("ssh total:"+str(len(ssh))+str(ssh))
  for i in range(0,len(ssh)):
    try:
      ssh_status = requests.get(str(ssh[i])).status_code
      if ssh_status == 200:
        pass
      else:
        sshoff.append(ssh[i])
    except Exception as e:
        # print(ssh[i]+" is offline")
        sshoff.append(ssh[i])
    pass
    continue
    # time.sleep(2)
    # print("ssh online:"+str(len(sshon))+str(sshon))
    # print("ssh offline:"+str(len(sshoff))+str(sshoff))
  sshon = [i for i in ssh if i not in sshoff]
    # sshon = list(set(ssh).difference(set(sshoff))) #去重
    # sshon = list(set(ssh)^set(sshoff)) #去重
    # print("ssh online:"+str(len(sshon))+str(sshon))
  file.close()
  
  with open('sshoffline.txt', 'w') as off:
    for i in sshoff:
      off.write(i + '\n')

  with open('sshonline.txt', 'w') as on:
    for i in sshon:
      on.write(i + '\n')
  


  # fileoff=open('aponssh\sshoffline.txt','w+')
  # fileoff.write(str(sshoff))
  # fileoff.close()

  # fileon=open('aponssh\sshonline.txt','w+')
  # fileon.write(str(sshon))
  # fileon.close()
  # print(str(sshoff))
  sshonlog="["+str(apontime)+"] ssh total: ["+str(len(ssh))+"] | ssh online: ["+str(len(sshon))+"] "
  sshofflog="["+str(apontime)+"] ssh offline: ["+str(len(sshoff))+"] "+ str(sshoff)
  sshlog=sshonlog+'\n'+sshofflog +'\n'
  open("log.txt", 'a').write(sshlog + '\n')

  time.sleep(60)

# class RepeatingTimer(Timer): 
#     def run(self):
#         while not self.finished.is_set():
#             self.function(*self.args, **self.kwargs)
#             self.finished.wait(self.interval)
# t = RepeatingTimer(10.0, sshcheck('http.txt'))
# t.start()



# app=Flask(__name__)

# @app.route('/sshoffline')
# def sshoffline():
#   list =sshcheck('http.txt')

#   return render_template("ssh.html",list=list)

# app.run(host='0.0.0.0',port='5000',debug=True,threaded=True)

# @app.route('/sshonline')
# def sshonline():
#   html = "<html><body><ul>"
#   for i in range(0,len(sshon)) 
#     html += f"""
    
#       {sshon[i]}
#       <br/>
#       <br/>
    
#   </ul>
#   """
#   html += "</body></html>"
#   print(len(sshon))
#   return html

# @app.route('/sshoffline')
# def sshoffline():
#   # offline=sshcheck()
#   # print(len(sshoff))
#   html = "<html><body>"
#   html += f"""
#     <h1><center>apon ssh offline</center></h1>
#     <h2>ssh offline:</h3>
#   """ 
#   # for i in range(0,len(offline)):
#   #   html += f"""
#   #     <ul>
#   #     <a href="{offline[i]}" target="_blank">{offline[i]}</a>
#   #     <br/>
#   #     </ul>
#   #   """

    
#   html += "</body></html>"
#   # print(len(offline))
#   return html

# app.debug=True
# app.run(host='0.0.0.0',port='5000',debug=True)


