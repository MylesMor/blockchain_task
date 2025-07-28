## Ethereum Address Details Retriever
A script which takes in a cryptocurrency address hash, retrieves details such as balance, whether it's a smart contract and its transaction count in Ethereum mainnet.

### Prerequisites
Python 3.x installed (preferably 3.6+)
pip package installer available

### Installation

1. Clone the repository (or download the source code):

```bash
git clone https://github.com/mylesmor/blockchain_task
cd blockchain_task
```

2. Create a virtual environment (optional):

```bash
python -m venv venv
```

3. Activate the virtual environment (optional):

- On macOS/Linux:
```bash
source venv/bin/activate
```

- On Windows:
```
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage
To run the Python script, use:

```bash
python address_details.py {CRYPTO_ADDRESS_HASH}
```
Replace {CRYPTO_ADDRESS_HASH} with the address you want to retrieve details for.

## Example
```bash
python address_details.py 0xDC4939aD0cC5A640E03593428eE2DE906D89e98D
```

### Testing
To run the tests, use:

```bash
pytest
```


