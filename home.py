from flask import Flask, render_template
 
myobj = Flask(__name__)

@myobj.route("/")
def home():
    name = "Lisa"
    city_names=["Paris", "London" , "Rome" , "Tahiti"]
    length=len(city_names)
    city = ""
    for i in city_names:
        city=city+"<li>"+i+"</li>"
        
    return '''
    <html>
    <head>
    <title> Home </title>
    </head>
    <body>
    <h1>Welcome ''' + name + ''' </h1>
        <a href="www.google.com"> notgoogle </a>
        <ul>'''+city+'''</ul>

        </body>
        </html>'''
#myobj.run(debug=True)
