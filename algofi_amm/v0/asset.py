
import pprint
from .config import PoolType, PoolStatus, Network, get_usdc_asset_id, get_stbl_asset_id, ALGO_ASSET_ID

# asset decimals
ALGO_DECIMALS = 6
USDC_DECIMALS = 6
STBL_DECIMALS = 6

class Asset():

    def __init__(self, amm_client, asset_id):
        """Constructor method for :class:`Asset`
        :param amm_client: a :class:`AlgofiAMMClient` for interacting with the AMM
        :type amm_client: :class:`AlgofiAMMClient`
        :param asset_id: asset id
        :type asset_id: int
        """

        self.asset_id = asset_id
        self.amm_client = amm_client

        if asset_id == 1:
            self.creator = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY5HFKQ"
            self.decimals = ALGO_DECIMALS
            self.default_frozen = False
            self.freeze = None
            self.manager = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY5HFKQ"
            self.name = "Algorand"
            self.reserve = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY5HFKQ"
            self.total = 10000000000
            self.unit_name = "ALGO"
            self.url = "https://www.algorand.com/"
        else:
            asset_info = amm_client.indexer.asset_info(asset_id)
            self.creator = asset_info["asset"]["params"]["creator"]
            self.decimals = asset_info["asset"]["params"]["decimals"]
            self.default_frozen = asset_info["asset"]["params"].get("default-frozen", False)
            self.freeze = asset_info["asset"]["params"].get("freeze", None)
            self.manager = asset_info["asset"]["params"].get("manager", None)
            self.name = asset_info["asset"]["params"].get("name", None)
            self.reserve = asset_info["asset"]["params"].get("reserve", None)
            self.total = asset_info["asset"]["params"].get("total", None)
            self.unit_name = asset_info["asset"]["params"].get("unit-name", None)
            self.url = asset_info["asset"]["params"].get("url", None)
    
    def __str__(self):
        """Returns a pretty string representation of the :class:`Asset` object
        :return: string representation of asset
        :rtype: str
        """
        return pprint.pformat({"asset_id": self.asset_id, "creator": self.creator, "decimals": self.decimals, "default_frozen": self.default_frozen,
                "freeze": self.freeze, "manager": self.manager, "name": self.name, "reserve": self.reserve, "total": self.total,
                "unit_name": self.unit_name, "url": self.url})

    def __hash__(self) -> int:
        """Returns an int which is the asset_id of the :class:`Asset` current object
        :return: asset_id
        :rtype: int
        """
        return self.asset_id

    def get_scaled_amount(self, amount):
        """Returns an integer representation of asset amount scaled by asset's decimals
        :param amount: amount of asset
        :type amount: float
        :return: int amount of asset scaled by decimals
        :rtype: int
        """

        return int(amount * 10**self.decimals)

    def refresh_price(self):
        """Returns the dollar price of the asset with a simple matching algorithm
        """

        usdc_asset_id = get_usdc_asset_id(self.amm_client.network)
        stbl_asset_id = get_stbl_asset_id(self.amm_client.network)

        # is testnet
        pool_type = PoolType.CONSTANT_PRODUCT_30BP_FEE if (self.amm_client.network == Network.TESTNET) else PoolType.CONSTANT_PRODUCT_25BP_FEE
        usdc_pool = self.amm_client.get_pool(pool_type, self.asset_id, usdc_asset_id)
        if (usdc_pool == PoolStatus.ACTIVE):
            self.price = usdc_pool.get_pool_price(self.asset_id)
            return
        
        stbl_pool = self.amm_client.get_pool(pool_type, self.asset_id, stbl_asset_id)
        if (stbl_pool.pool_status == PoolStatus.ACTIVE):
            self.price = stbl_pool.get_pool_price(self.asset_id)
            return
        
        algo_pool = self.amm_client.get_pool(pool_type, self.asset_id, ALGO_ASSET_ID)
        if (algo_pool.pool_status == PoolStatus.ACTIVE):
            price_in_algo = algo_pool.get_pool_price(self.asset_id)
            usdc_algo_pool = self.amm_client.get_pool(pool_type, usdc_asset_id, ALGO_ASSET_ID)
            if (usdc_algo_pool.pool_status == PoolStatus.ACTIVE):
                self.price = price_in_algo * usdc_algo_pool.get_pool_price(ALGO_ASSET_ID)
                return

        # unable to find price
        self.price = 0
