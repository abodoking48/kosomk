from flask import Flask, redirect, render_template, request

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["DEBUG"] = True



users = []
SPORTS=['football' , 'tennis' , 'volleyball' , 'Basketball']

@app.route('/')
def index():
    return render_template('test.html' , SPORTS=SPORTS)


@app.route('/register' , methods = ['GET' , 'POST']) 
def register():
    name= request.form.get('name')
    sport= request.form.getlist('sport')
    print (sport)
    if not name:
        return render_template('failure.html' , message= "u need write ur name")
    #if sport not in SPORTS:
     #   return render_template('failure.html' , message = "u need provide sport")

    users.append({
        'name' :name ,
        'sport' : sport
    })
    print(users)
    return render_template('register.html', users=users )
    


if __name__ == "__main__":
    app.run(debug=True)
