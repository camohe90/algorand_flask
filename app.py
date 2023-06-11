from beaker import client, localnet
from flask import Flask, render_template, request

from contract import app_blockchain, hello, multiplicacion, resta, suma

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/deploy", methods=["POST"])
def deploy():
    accounts = localnet.kmd.get_accounts()
    sender = accounts[0]

    app_client = client.ApplicationClient(
        client=localnet.get_algod_client(),
        app=app_blockchain,
        sender=sender.address,
        signer=sender.signer,
    )

    app_id, app_addr, txid = app_client.create()

    return_value = app_client.call(hello, name="Pycon").return_value
    print(app_id)

    return render_template("index.html", message=return_value)


@app.route("/add", methods=["POST"])
def add():
    numero1 = int(request.form["num1"])
    numero2 = int(request.form["num2"])

    accounts = localnet.kmd.get_accounts()
    sender = accounts[0]

    app_client = client.ApplicationClient(
        client=localnet.get_algod_client(),
        app=app_blockchain,
        app_id=7,
        sender=sender.address,
        signer=sender.signer,
    )

    return_value = app_client.call(suma, num1=numero1, num2=numero2).return_value

    return render_template("index.html", message="Llame suma", result=return_value)


@app.route("/subtract", methods=["POST"])
def subtract():
    numero1 = int(request.form["num1"])
    numero2 = int(request.form["num2"])

    accounts = localnet.kmd.get_accounts()
    sender = accounts[0]

    app_client = client.ApplicationClient(
        client=localnet.get_algod_client(),
        app=app_blockchain,
        app_id=7,
        sender=sender.address,
        signer=sender.signer,
    )
    return_value = app_client.call(resta, num1=numero1, num2=numero2).return_value
    return render_template("index.html", message="Llame resta", result=return_value)


@app.route("/multiply", methods=["POST"])
def multipy():
    numero1 = int(request.form["num1"])
    numero2 = int(request.form["num2"])

    accounts = localnet.kmd.get_accounts()
    sender = accounts[0]

    app_client = client.ApplicationClient(
        client=localnet.get_algod_client(),
        app=app_blockchain,
        app_id=7,
        sender=sender.address,
        signer=sender.signer,
    )
    return_value = app_client.call(
        multiplicacion, num1=numero1, num2=numero2
    ).return_value
    return render_template("index.html", message="Llame multi", result=return_value)


if __name__ == "__main__":
    app.run(debug=True)
