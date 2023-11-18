# Define the network client
from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)

# Create a wallet using the testnet faucet:
# https://xrpl.org/xrp-testnet-faucet.html

test_wallet = generate_faucet_wallet(client, debug=True)

print(test_wallet)

# print output

# public_key:: 022FA613294CD13FFEA759D0185007DBE763331910509EF8F1635B4F84FA08AEE3
# private_key:: -HIDDEN-
# classic_address: raaFKKmgf6CRZttTVABeTcsqzRQ51bNR6Q