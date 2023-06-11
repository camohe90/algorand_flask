from beaker import client, localnet

from contract import app_blockchain, hello

app_blockchain.build().export("./artifacts")

accounts = localnet.kmd.get_accounts()
sender = accounts[0]

app_client = client.ApplicationClient(
    client=localnet.get_algod_client(),
    app=app_blockchain,
    sender=sender.address,
    signer=sender.signer,
)

app_id, app_addr, txid = app_client.create()
print(app_id)
return_value = app_client.call(hello, name="Beaker").return_value
print(return_value)
