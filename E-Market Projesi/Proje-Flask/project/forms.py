from wtforms import Form, StringField, IntegerField, PasswordField, DecimalField,TextAreaField, validators

class RegistrationForm(Form):
    rolId = StringField("2")
    name = StringField("Ad Soyad", validators=[validators.Length(min=5, max=30)])
    username = StringField("Kullanıcı Adı", validators=[validators.Length(min=5, max=30)])
    email = StringField("E-posta", validators=[validators.Email(message="Lütfen geçerli bir email adresi girin")])
    password = PasswordField("Parola", validators=[validators.DataRequired("Lütfen bir parola belirleyin"),
    validators.EqualTo(fieldname="confirm",message="Parolanız aynı değil"),
    validators.Length(min=8)])
    confirm = PasswordField("Parolayı doğrulayın")

class LoginForm(Form):
    username = StringField("Kullanıcı Adı")
    password= PasswordField("Parola")

class ProductForm(Form):
    name = StringField("Ürün Adı", validators=[validators.Length(min=5, max=30),
                                validators.DataRequired(message="Ürün Adı Girin")])
    image = StringField("Fotoğraf Adı", validators=[validators.Length(min=5, max=30)])
    feature = TextAreaField("Ürün Özellikleri")
    category = StringField("Ürün Kategori", validators=[validators.Length(min=5, max=30),
                                validators.DataRequired(message="Kategori Bilgisi Girin")])
    stokAdet = IntegerField("Ürün Adedi", validators=[validators.Length(min=1, max=30)])
    price = DecimalField("Ürün Fiyatı", validators=[validators.DataRequired(message="Fiyat Bilgisi Girin")])

class DashboardLoginForm(Form):
    dashboardLoginName = StringField("Kullanıcı Adı")
    dashboardLoginPassword = PasswordField("Parola")

class CategoryForm(Form):
    categoryName = StringField("Kategori Adı")

