from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

@app.route("/health")
def data():
        return render_template('indexcardio.html')
       #return message

if __name__=="__main__":
        app.run(host='0.0.0.0',debug=True,port=5050)
 
