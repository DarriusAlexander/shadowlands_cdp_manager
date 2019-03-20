from shadowlands.contract import Contract
from hexbytes import HexBytes

from shadowlands.tui.debug import debug
import pdb

# [contracts.SAI_PIT]: [
#      { version: 1, address: addresses.PIT, abi: abis.daiV1.pit }
# ],

class SaiProxy(Contract):

#    def resolve(self, name):
#        if not name.endswith(".eth"):
#            name += '.eth'
#        _namehash = namehash(name)
#        return self.functions.addr(_namehash).call()
# 
#
#    def set_address(self, name, address_target):
#        if not name.endswith(".eth"):
#            name += '.eth'
#
#        _namehash = namehash(name)
#
#        fn = self._contract.functions.setAddr(_namehash, HexBytes(address_target))
#        return fn
    MAINNET="0x190c2cfc69e68a8e8d5e2b9e2b9cc3332caff77b"
    KOVAN="0xadb7c74bce932fc6c27dda3ac2344707d2fbb0e6"
    ABI='''
    [{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"cup","type":"bytes32"},{"name":"wad","type":"uint256"}],"name":"draw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"cup","type":"bytes32"},{"name":"jam","type":"uint256"},{"name":"wad","type":"uint256"},{"name":"otc_","type":"address"}],"name":"wipeAndFree","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"cup","type":"bytes32"},{"name":"wad","type":"uint256"}],"name":"lockAndDraw","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"wad","type":"uint256"}],"name":"lockAndDraw","outputs":[{"name":"cup","type":"bytes32"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"registry_","type":"address"},{"name":"tub_","type":"address"}],"name":"createAndOpen","outputs":[{"name":"proxy","type":"address"},{"name":"cup","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"cup","type":"bytes32"},{"name":"otc_","type":"address"}],"name":"shut","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"cup","type":"bytes32"},{"name":"wad","type":"uint256"},{"name":"otc_","type":"address"}],"name":"wipe","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"cup","type":"bytes32"},{"name":"wad","type":"uint256"}],"name":"wipe","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"}],"name":"open","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"cup","type":"bytes32"}],"name":"shut","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"cup","type":"bytes32"}],"name":"lock","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"registry_","type":"address"},{"name":"tub_","type":"address"},{"name":"wad","type":"uint256"}],"name":"createOpenLockAndDraw","outputs":[{"name":"proxy","type":"address"},{"name":"cup","type":"bytes32"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"cup","type":"bytes32"},{"name":"lad","type":"address"}],"name":"give","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"registry_","type":"address"},{"name":"tub_","type":"address"}],"name":"createOpenAndLock","outputs":[{"name":"proxy","type":"address"},{"name":"cup","type":"bytes32"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"cup","type":"bytes32"},{"name":"jam","type":"uint256"}],"name":"free","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"tub_","type":"address"},{"name":"cup","type":"bytes32"},{"name":"jam","type":"uint256"},{"name":"wad","type":"uint256"}],"name":"wipeAndFree","outputs":[],"payable":true,"stateMutability":"payable","type":"function"}]
'''

 