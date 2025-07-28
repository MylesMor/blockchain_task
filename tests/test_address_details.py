import pytest
import sys
import pandas as pd
import pandas.testing as pdt
import os

# Add the parent folder to sys.path so python can find the module
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from address_details import retrieve_address_details, save_to_csv

def test_address_details():
    # Invalid address
    with pytest.raises(ValueError):
        retrieve_address_details("0x47z")
    
    # Test with smart contract
    contract = retrieve_address_details("0xdac17f958d2ee523a2206206994597c13d831ec7")
    assert contract['is_smart_contract'] == True

    # Test with standard address
    address = retrieve_address_details("0xDC4939aD0cC5A640E03593428eE2DE906D89e98D")
    print(address)
    assert address['is_smart_contract'] == False


def test_save_to_csv():

    # Check file is saved
    address = "0xDC4939aD0cC5A640E03593428eE2DE906D89e98D"
    address_det = retrieve_address_details(address)
    save_to_csv(address_det)

    final_address = address_det['address']
    file_name = f'./data/{final_address}_details.csv'
    assert os.path.isfile(file_name) == True

    # Check file matches what was retrieved
    df = pd.read_csv(file_name)
    expected_df = pd.DataFrame([address_det])

    df['balance_eth'] = df['balance_eth'].astype(float)
    expected_df['balance_eth'] = expected_df['balance_eth'].astype(float)

    df['balance_eth'] = df['balance_usd'].astype(float)
    expected_df['balance_eth'] = expected_df['balance_usd'].astype(float)
    
    pdt.assert_frame_equal(df, expected_df)
    




