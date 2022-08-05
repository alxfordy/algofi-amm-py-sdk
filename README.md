# algofi-amm-py-sdk

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/Algofiorg/algofi-amm-py-sdk/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/Algofiorg/algofi-amm-py-sdk/tree/main)
[![Documentation Status](https://readthedocs.org/projects/algofi-amm-py-sdk/badge/?version=latest)](https://algofi-amm-py-sdk.readthedocs.io/en/latest/?badge=latest)

Official Python SDK for the Algofi DEX

## Documentation
https://algofi-amm-py-sdk.readthedocs.io/en/latest/index.html

## Design Goal
This SDK is useful for developers who want to programatically interact with the Algofi DEX.

## Status

This SDK is currently under active early development and should not be considered stable.

## Installation
algofi-amm-py-sdk is not yet released on PYPI. It can be installed directly from this repository with pip:

`pip install git+https://github.com/Algofiorg/algofi-amm-py-sdk` 

To run examples:
1. create an examples/.env file
mnemonic=[25 char mnemonic]
2. Fund the account for mnemonic with test ALGO + test ASAs
3. Run examples (e.g. python3 add_liquidity.py). Be sure to set the correct asset ids and amounts.

## Examples

### Add liquidity (add_liquidity)
[add_liquidity.py](https://github.com/Algofiorg/algofi-amm-py-sdk/blob/main/examples/add_liquidity.py)

This example shows how to add liquidity to an existing pool

### Burn LP token (burn)
[burn.py](https://github.com/Algofiorg/algofi-amm-py-sdk/blob/main/examples/burn.py)

This example shows how to burn LP tokens into their underlying assets

### Create pool (create_pool)
[create_pool.py](https://github.com/Algofiorg/algofi-amm-py-sdk/blob/main/examples/create_pool.py)

This example shows how to create a new pool

### Flash loan (flash_loan)
[flash_loan.py](https://github.com/Algofiorg/algofi-amm-py-sdk/blob/main/examples/flash_loan.py)

This example shows how to perform a flash loan from an Algofi DEX pool

### Swap exact for (swap_exact_for)
[swap_exact_for.py](https://github.com/Algofiorg/algofi-amm-py-sdk/blob/main/examples/swap_exact_for.py)

This example shows how to swap an exact amount of an asset A into another asset B within a given pool (A, B)

### Swap for exact (swap_for_exact)
[swap_for_exact.py](https://github.com/Algofiorg/algofi-amm-py-sdk/blob/main/examples/swap_for_exact.py)

This example shows how to swap an amount of asset A for an exact amount of asset B within a given pool (A, B)

# License

algofi-amm-py-sdk is licensed under a MIT license except for the exceptions listed below. See the LICENSE file for details.
