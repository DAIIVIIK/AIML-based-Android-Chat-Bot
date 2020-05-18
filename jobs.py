# import aiml
# import aiml
# import requests
# import json

# # Create the kernel and learn AIML files
# kernel = aiml.Kernel()
# kernel.learn("chatterbot.xml")
# kernel.respond("load aiml b")

# # Press CTRL-C to break this loop
# while True:

#     print (kernel.respond(input("Enter your message >> ")))

#     domain=kernel.getPredicate('domain')
#     link="https://jobs.github.com/positions.json?"
#     par={'description':domain}
#     r = requests.get(url = link, params = par) 
#     r.text
#     data = json.loads(r.text)
#     for item in data:
#     	print ("job Title: %s" % (item['title']))
#     	print ("****************************************")
#     
import sys
import requests
import json
link="https://jobs.github.com/positions.json?"
par={'description': sys.argv[-1]}
r=requests.get(url=link,params=par)
r.text
data=json.loads(r.text)
for item in data:
    print ("job Title: %s" % (item['title']))
    print ("****************************************")
