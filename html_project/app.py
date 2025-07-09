from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/order",methods=["GET","POST"])
def order():
    if request.method=="POST":
        name=request.form["name"]
        adress=request.form["adress"]
        medicine=request.form["medicine"]
        with open("orders.txt","a")as f:
            f.write(f"{name} | {adress} | {medicine}\n")
        return f"thank you {name},your medicine '{medicine}' will be delivered via drone"
    return render_template("order.html")
@app.route("/contact") 
def contact():
    return render_template("contact.html")
if __name__=="__main__":
    app.run(debug=True)
