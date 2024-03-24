from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/contacts/")
def contacts():
    developer_name = 'Ilon Mask'
    address = 'egwddd'
    developer_phone = "88005553535"
    return render_template('contacts.html', name = developer_name, address = address, phone = developer_phone)

if __name__ == "__main__":
    app.run(debug=True)