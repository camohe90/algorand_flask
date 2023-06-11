from beaker import *
from pyteal import *

app_blockchain = Application("Contract")

@app_blockchain.external
def hello(name: abi.String, *, output: abi.String) -> Expr:
    return output.set(Concat(Bytes("Hello, "), name.get()))

@app_blockchain.external
def suma(num1:abi.Uint64, num2: abi.Uint64, *, output:abi.Uint64) -> Expr:
    return output.set(num1.get() + num2.get())

@app_blockchain.external
def resta(num1:abi.Uint64, num2: abi.Uint64, *, output:abi.Uint64) -> Expr:
    return (
        If(num1.get()>num2.get())
        .Then(output.set(num1.get() - num2.get()))
        .Else(output.set(num2.get() - num1.get()))
    )

@app_blockchain.external
def multiplicacion(num1:abi.Uint64, num2: abi.Uint64, *, output:abi.Uint64) -> Expr:
    return output.set(num1.get() * num2.get())


if __name__ == "__main__":
    app_blockchain.build().export("./artifacts")
