from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    main_data = {
        "Город": "Чебоксары",
        "Район":"Московский",
        "Компания":"Iserv"
    }
    context = {
        'name':'Maria',
        'age':'15',
        'spes':'dev'
    }

    return render_template('index.html', main_data=main_data, context=context)
@app.route("/contacts/")
def contacts():
    developer_name = 'Ilon Mask'
    address = 'egwddd'
    developer_phone = "88005553535"
    return render_template('contacts.html', name = developer_name, address = address, phone = developer_phone)
@app.route("/results/")
def resulsts():
    data = ''#['python', 'js', 'GO', 'C#', 'C++', 'lua', 'React', 'SQL', 'Postgesgl']
    return render_template('results.html', data=data)
if __name__ == "__main__":
    app.run(debug=True)