from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from forms import RegistrationForm, LoginForm, ProductForm, DashboardLoginForm, CategoryForm
from functools import wraps

app = Flask(__name__, template_folder="templates")
app.secret_key = "market"

def loginRequired(f):
    @wraps(f)
    def decorator_function(*args,**kwargs):
        if "logged_in" in session:
            return f(*args,**kwargs)
        else:
            flash("Bu sayfayı görüntülemek için giriş yapın","danger")
            return redirect(url_for("login"))
    return decorator_function

def adminRequired(f):
    @wraps(f)
    def decorator_function(*args,**kwargs):
        if session["rolId"] == '1':
            return f(*args,**kwargs)
        else:
            flash("Bu sayfayı görüntülemeye izniniz yok","danger")
            return redirect(url_for("index"))
    return decorator_function

dashboardUsername = 'EMarketÜrünGiriş'
dashboardParola = 'EMarketÜrünGiriş'


app.config["MYSQL_HOST"]="127.0.0.1"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="e-market"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/categories")
def categories():
    cursor = mysql.connection.cursor()
    query = "Select * from categories"
    result = cursor.execute(query)
    if result > 0:
        categories = cursor.fetchall()
        return render_template("categories.html", categories=categories)
    else:
        flash("Hiç kategori yok","danger")
        return render_template("index.html")

@app.route("/category/<string:id>")
def category(id):
    cursor = mysql.connection.cursor()
    query = "Select * from categories where id = %s"
    result = cursor.execute(query,(id, ))
    if result > 0:
        category = cursor.fetchone()
        return render_template("category.html", category=category)
    else:
        return render_template("category.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/product/<string:id>")
def product(id):
    cursor = mysql.connection.cursor()
    query = "Select * from products where id = %s"
    result = cursor.execute(query,(id, ))
    if result > 0:
        product = cursor.fetchone()
        return render_template("product.html", product=product)
    else:
        return render_template("product.html")
    

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)
        rolId = '2'
        cursor = mysql.connection.cursor()
        query = "Insert into user(name, username, email, password,rolId) VALUES(%s, %s, %s, %s, %s)"
        cursor.execute(query,(name, username, email, password, rolId))
        mysql.connection.commit()
        cursor.close()
        flash("Kayıt Başarılı","success")
        return redirect(url_for("index"))
    else:
        return render_template("register.html", form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        username = form.username.data
        password = form.password.data
        cursor = mysql.connection.cursor()
        query = "Select * from user where username = %s"
        result = cursor.execute(query,(username,))
        if result>0:
            data=cursor.fetchone()
            real_passw=data["password"]
            if ((password == real_passw) or sha256_crypt.verify(password,real_passw)):
                flash("Başarılı giriş yaptınız..","success")
                session["logged_in"] = True
                session["username"] = username
                session["rolId"] = data["rolId"]
                return redirect(url_for("index"))
            else:
                flash("Şifre hatalı","warning")
                return redirect(url_for("login"))
        else:
            flash("Böyle bir kullanıcı yok","danger")
            return redirect(url_for("register"))
    else:
        return render_template("login.html", form=form) 

@app.route("/products")
def products():
    cursor = mysql.connection.cursor()
    query = "Select * from products"
    result = cursor.execute(query)
    if result >0:
        products=cursor.fetchall()
        return render_template("products.html",products=products)
    else:
        return render_template("products.html")

@app.route("/dashboardLogin",methods=["GET","POST"])
@adminRequired
def dashboardLogin():
    form = DashboardLoginForm(request.form)
    if request.method == "POST":
        dashboardLoginName = form.dashboardLoginName.data
        dashboardLoginPassword = form.dashboardLoginPassword.data
        if dashboardUsername == dashboardLoginName and dashboardParola == dashboardLoginPassword:
            flash("Giriş Başarılı","success")
            return redirect(url_for("dashboard"))
        else:
            flash("Hatalı Giriş","danger")
            return redirect(url_for("index"))
    else:
        return render_template("dashboardLogin.html", form=form)

@app.route("/dashboard")
@adminRequired
def dashboard():
    cursor = mysql.connection.cursor()
    query = "Select * from products"
    result=cursor.execute(query)
    if result >0:
        products=cursor.fetchall()
        return render_template("dashboard.html",products=products)
    else:
        return render_template("dashboard.html",products=products)
        

@app.route("/addproduct", methods=["GET","POST"])
@adminRequired
def addproduct():
    form = ProductForm(request.form)
    if request.method == "POST" and form.validate:
        name = form.name.data
        image = form.image.data
        feature = form.feature.data
        category = form.category.data
        stokAdet = form.stokAdet.data
        price = form.price.data
        cursor = mysql.connection.cursor()
        query = "Insert into products(name, image, feature, category, stokAdet, price) VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(query,(name, image, feature, category, stokAdet, price))
        mysql.connection.commit()
        cursor.close()
        flash("Ürün Eklendi","success")
        return redirect(url_for("products"))
    else:
        return render_template("addproduct.html", form=form)

@app.route("/sepetim/<string:id>",methods=["POST"])
def sepetim(id):
    cursor = mysql.connection.cursor()
    query = "Select * from products where id = %s"
    result = cursor.execute(query,(id, ))
    if result > 0:
        product = cursor.fetchone()
        return render_template("products.html", product=product)
    else:
        return render_template("products.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Çıkış Yapıldı","success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)