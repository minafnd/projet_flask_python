from flask import Flask, request, render_template

app = Flask(__name__) 



@app.route("/")
# décorateur : mis avant une fonction et permet de'enrichir la fonction se situant en dessous avec d'autres fonction
# dans ce cas ci, cela veut dire que si l'utilisateur entre l'adresse "/", alors le message ci dessous s'affichera
def home():
    return "Welcome to the home page"

@app.route("/accueil")
def accueil():
    return "Welcome to the accueil"

@app.route("/products/<int:productid>")
def products(productid):
    product_from_db = {
        "id": productid,
        "name": "Sample Product",
        "price": 19.90,
        "description": "This is a sample product description."
    }
    # query string (-> format ?currency=euro&store=metz) : affine un peu plus le résultat
    store = request.args.get('store', 'online')
    currency = request.args.get('currency', 'euro')
    

    return render_template("produit.html", product=product_from_db, store=store)
    
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        pass
    return render_template("contact.html")

# ça va indiquer à flask quelle est la base du fichier
if __name__ == "__main__":
    app.run(debug=True)
    # debut=True à désactiver en prod

