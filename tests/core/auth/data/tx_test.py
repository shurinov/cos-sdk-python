from secret_sdk.core.auth import StdTx


def test_deserializes_stdtx(load_json_examples):
    # current: /txs?tx.height=1781815
    # migrate to: /cosmos/tx/v1beta1/txs?events=tx.height=1781836
    data = load_json_examples("./StdTx.data.json")
    for example in data["txs"]:
        parsed = StdTx.from_data(example["tx"]).to_data()
        for key in parsed.keys():
            assert parsed[key] == example["tx"][key]
