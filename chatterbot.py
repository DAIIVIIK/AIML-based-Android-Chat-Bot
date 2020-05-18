from flask import Flask,jsonify,request
import aiml
import requests
import json

kernel = aiml.Kernel()
kernel.learn("chatterbot.xml")
kernel.respond("load aiml b")

app=Flask(__name__)
@app.route('/')
def hello():
	fp=open('conversations.txt','a')
	fp.write('user: '+request.args['param']+'\n')

	name=kernel.respond(request.args['param'])
	fp.write('chatterbot: '+name+'\n')
	fp.close()
	return name
@app.route('/home')
def there():
	return "Ganupa"
if __name__=='__main__':
    app.run()



# Create the kernel and learn AIML files


# Press CTRL-C to break this loop
# while True:

#     print (kernel.respond(input("Enter your message >> ")))

#     domain=kernel.getPredicate('domain')
#     link="https://jobs.github.com/positions.json?"
#     par={'description':domain}
#     r = requests.get(url = link, params = par) 
#     r.text
#     data = json.loads(r.text)
#     for item in data:
#         print ("job Title: %s" % (item['title']))
#         print ("****************************************")
#     
