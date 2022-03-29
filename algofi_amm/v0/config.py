
from enum import Enum
from base64 import b64encode
from .approval_programs import MAINNET_APPROVAL_PROGRAM_25BP_CONSTANT_PRODUCT, MAINNET_APPROVAL_PROGRAM_75BP_CONSTANT_PRODUCT, \
    TESTNET_APPROVAL_PROGRAM_30BP_CONSTANT_PRODUCT, TESTNET_APPROVAL_PROGRAM_100BP_CONSTANT_PRODUCT, CLEAR_STATE_PROGRAM
from ..contract_strings import algofi_pool_strings as pool_strings
from ..contract_strings import algofi_manager_strings as manager_strings

# constants
ALGO_ASSET_ID = 1

# nanoswap pools
TESTNET_NANOSWAP_POOLS = {(77279127, 77279142): 77282939}  # (asset1_id, asset2_id) -> app_id
MAINNET_NANOSWAP_POOLS = {(31566704, 465865291): 658337046,
                          (312769, 465865291): 659677335,
                          (312769, 31566704): 659678644}

# valid pool app ids
b64_to_utf_keys = {
    b64encode(bytes(pool_strings.asset1_id, "utf-8")).decode("utf-8"): pool_strings.asset1_id,
    b64encode(bytes(pool_strings.asset2_id, "utf-8")).decode("utf-8"): pool_strings.asset2_id,
    b64encode(bytes(pool_strings.pool, "utf-8")).decode("utf-8"): pool_strings.pool,
    b64encode(bytes(manager_strings.validator_index, "utf-8")).decode("utf-8"): manager_strings.validator_index,
    b64encode(bytes(pool_strings.balance_1, "utf-8")).decode("utf-8"): pool_strings.balance_1,
    b64encode(bytes(pool_strings.balance_2, "utf-8")).decode("utf-8"): pool_strings.balance_2,
    b64encode(bytes(pool_strings.cumsum_volume_asset1, "utf-8")).decode("utf-8"): pool_strings.cumsum_volume_asset1,
    b64encode(bytes(pool_strings.cumsum_volume_asset2, "utf-8")).decode("utf-8"): pool_strings.cumsum_volume_asset2,
    b64encode(bytes(pool_strings.cumsum_volume_weighted_asset1_to_asset2_price, "utf-8")).decode("utf-8"): pool_strings.cumsum_volume_weighted_asset1_to_asset2_price,
    b64encode(bytes(pool_strings.cumsum_volume_weighted_asset2_to_asset1_price, "utf-8")).decode("utf-8"): pool_strings.cumsum_volume_weighted_asset2_to_asset1_price,
    b64encode(bytes(pool_strings.cumsum_time_weighted_asset2_to_asset1_price, "utf-8")).decode("utf-8"): pool_strings.cumsum_time_weighted_asset2_to_asset1_price,
    b64encode(bytes(pool_strings.cumsum_time_weighted_asset1_to_asset2_price, "utf-8")).decode("utf-8"): pool_strings.cumsum_time_weighted_asset1_to_asset2_price,
    b64encode(bytes(pool_strings.cumsum_fees_asset1, "utf-8")).decode("utf-8"): pool_strings.cumsum_fees_asset1,
    b64encode(bytes(pool_strings.cumsum_fees_asset2, "utf-8")).decode("utf-8"): pool_strings.cumsum_fees_asset2
}

utf_to_b64_keys = {v: k for k, v in b64_to_utf_keys.items()}

# enums
class Network(Enum):
    """Network enum
    """
    MAINNET = 0
    TESTNET = 1


class PoolType(Enum):
    """Pool type enum
    """
    CONSTANT_PRODUCT_25BP_FEE = 1
    CONSTANT_PRODUCT_30BP_FEE = 2
    CONSTANT_PRODUCT_75BP_FEE = 3
    CONSTANT_PRODUCT_100BP_FEE = 4
    NANOSWAP = 5


class PoolStatus(Enum):
    """Pool status enum
    """
    UNINITIALIZED = 0
    ACTIVE = 1


# lookup functions
def get_validator_index(network, pool_type):
    """Gets the validator index for a given pool type and network

    :param network: network :class:`Network` ("testnet" or "mainnet")
    :type network: str
    :param pool_type: a :class:`PoolType` object for the type of pool (e.g. 30bp, 100bp fee)
    :type pool_type: :class:`PoolType`
    :return: validator index for given type of pool
    :rtype: int
    """

    if network == Network.MAINNET:
        if (pool_type == PoolType.CONSTANT_PRODUCT_25BP_FEE):
            return 0
        elif (pool_type == PoolType.CONSTANT_PRODUCT_75BP_FEE):
            return 1
    elif network == Network.TESTNET:
        if (pool_type == PoolType.CONSTANT_PRODUCT_30BP_FEE):
            return 0
        elif (pool_type == PoolType.CONSTANT_PRODUCT_100BP_FEE):
            return 1
        elif (pool_type == PoolType.NANOSWAP):
            return -1


def get_approval_program_by_pool_type(pool_type, network):
    """Gets the approval program for a given pool type

    :param pool_type: a :class:`PoolType` object for the type of pool (e.g. 30bp, 100bp fee)
    :type pool_type: :class:`PoolType`
    :param pool_type: a :class:`PoolType` object for the type of pool (e.g. 30bp, 100bp fee)
    :type pool_type: :class:`PoolType`
    :return: approval program bytecode for given pool type as list of ints
    :rtype: list
    """

    if network == Network.MAINNET:
        if (pool_type == PoolType.CONSTANT_PRODUCT_25BP_FEE):
            return bytes(MAINNET_APPROVAL_PROGRAM_25BP_CONSTANT_PRODUCT)
        elif (pool_type == PoolType.CONSTANT_PRODUCT_75BP_FEE):
            return bytes(MAINNET_APPROVAL_PROGRAM_75BP_CONSTANT_PRODUCT)
    elif network == Network.TESTNET:
        if (pool_type == PoolType.CONSTANT_PRODUCT_30BP_FEE):
            return bytes(TESTNET_APPROVAL_PROGRAM_30BP_CONSTANT_PRODUCT)
        elif (pool_type == PoolType.CONSTANT_PRODUCT_100BP_FEE):
            return bytes(TESTNET_APPROVAL_PROGRAM_100BP_CONSTANT_PRODUCT)


def get_clear_state_program():
    """Gets the clear state program

    :return: clear state program bytecode as list of ints
    :rtype: list
    """

    return bytes(CLEAR_STATE_PROGRAM)


def get_manager_application_id(network, is_nanoswap):
    """Gets the manager application id for the given network

    :param network: network :class:`Network` ("testnet" or "mainnet")
    :type network: str
    :return: manager application id for the given network
    :rtype: int
    """

    if (network == Network.MAINNET):
        if is_nanoswap:
            return 658336870
        return 605753404
    elif (network == Network.TESTNET):
        if is_nanoswap:
            return 77282916
        return 66008735


def get_swap_fee(pool_type):
    """Gets the swap fee for a given pool type

    :param pool_type: a :class:`PoolType` object for the type of pool (e.g. 30bp, 100bp fee)
    :type pool_type: :class:`PoolType`
    :return: swap fee for a given pool type
    :rtype: float
    """

    if (pool_type == PoolType.CONSTANT_PRODUCT_25BP_FEE):
        return 0.0025
    elif (pool_type == PoolType.CONSTANT_PRODUCT_30BP_FEE):
        return 0.003
    elif (pool_type == PoolType.CONSTANT_PRODUCT_75BP_FEE):
        return 0.0075
    elif (pool_type == PoolType.CONSTANT_PRODUCT_100BP_FEE):
        return 0.01
    elif (pool_type == PoolType.NANOSWAP):
        return 0.001 # TODO


def get_usdc_asset_id(network):
    """Gets asset id of USDC for a given network

    :param network: network :class:`Network` ("testnet" or "mainnet")
    :type network: str
    :return: asset id of USDC for a given network
    :rtype: int
    """

    if (network == Network.MAINNET):
        return 31566704
    elif (network == Network.TESTNET):
        return 51435943


def get_stbl_asset_id(network):
    """Gets asset id of STBL for a given network

    :param network: network :class:`Network` ("testnet" or "mainnet")
    :type network: str
    :return: asset id of STBL for a given network
    :rtype: int
    """

    if (network == Network.MAINNET):
        return 465865291
    elif (network == Network.TESTNET):
        return 51437163