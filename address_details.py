from web3 import Web3
import requests
import pandas as pd
import os
import sys


def retrieve_address_details(address: str) -> object:

    # Ethereum RPC URL retrieved from https://chainlist.org
    RPC_URL = "https://eth.llamarpc.com"

    # Price data provided by CoinGecko
    COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids=ethereum"

    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if (not w3.is_connected):
        raise Exception("Unable to connect to Ethereum chain, please try again or change the RPC URL")
    
    try:
        checksum_address: str = Web3.to_checksum_address(address)
    except ValueError:
        raise ValueError("Invalid address hash, please check it and try again")
    

    try:
        balance = w3.eth.get_balance(checksum_address)
        nonce = w3.eth.get_transaction_count(checksum_address)
        code = w3.eth.get_code(checksum_address)
    except:
        raise Exception("Failed to retrieve stats from RPC, please try again or change RPC URL")
    
    try:
        price_usd: float = requests.get(COINGECKO_URL).json()['ethereum']['usd']
    except Exception as e:
        price_usd = None
        print("Failed to retrieve price data for ethereum, continuing...")

    eth_balance =  Web3.from_wei(balance, 'ether')

    is_smart_contract = False
    if code != b'0x' and code != b'':
        is_smart_contract = True

    details = {
        "address": checksum_address,
        "balance_eth": eth_balance,
        "balance_wei": balance,
        "balance_usd": price_usd if price_usd == None else float(eth_balance) * float(price_usd),
        "transaction_count": nonce,
        "is_smart_contract": is_smart_contract
    }

    return details


def save_to_csv(address_details: object) -> None:
    os.makedirs('data', exist_ok=True)

    df = pd.DataFrame([address_details])
    filename = f"./data/{address_details['address']}_details.csv"
    df.to_csv(filename, index=False)

    print("Address details saved to CSV file:", filename)



if __name__ == '__main__':
    if len(sys.argv[1:]) != 1:
        raise Exception("Invalid number of arguments, there should be one argument being the crypto address hash")
    
    address_details = retrieve_address_details(sys.argv[1])
    save_to_csv(address_details)




