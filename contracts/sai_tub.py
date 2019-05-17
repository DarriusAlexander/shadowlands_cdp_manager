from shadowlands.contract import Contract
from hexbytes import HexBytes

from shadowlands.tui.debug import debug
import pdb

# [contracts.SAI_PIT]: [
#      { version: 1, address: addresses.PIT, abi: abis.daiV1.pit }
# ],

class SaiTub(Contract):

    def cup(self, cdp_id):
        return self.functions.cups(self.bytes32(cdp_id)).call()

    def tab(self, cdp_id):
        return self.functions.tab(self.bytes32(cdp_id)).call()

    def mat(self):
        return self.functions.mat().call()

    def tag(self):
        return self.functions.tag().call()

    def per(self):
        return self.functions.per().call()

    def axe(self):
        return self.functions.axe().call()

    def ink(self, cdp_id):
        return self.functions.ink(self.bytes32(cdp_id)).call()

    def fee(self):
        return self.functions.fee().call()

    def rum(self):
        return self.functions.rum().call()

    def rap(self, cdp_id):
        return self.functions.rap(self.bytes32(cdp_id)).call()

    def pie(self):
        return self.functions.pie().call()

    # TXs
    def open(self):
        return self.functions.open()

    def give(self, cup_id, guy):
        return self.functions.give(self.bytes32(cup_id), guy)


    #def lock(self, cdp_id, amount):
    #    fn = self.functions.lock(
    #        bytes32(cdp_id), 
    #        self.toWei(amount, 'ether')
    #    )
    #    return fn

    #def shut(self, cdp_id):
    #    fn = self.functions.shut(
    #        bytes32(cdp_id) 
    #    )
    #    return fn



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
    MAINNET="0x448a5065aebb8e423f0896e6c5d525c040f59af3"
    KOVAN="0xa71937147b55Deb8a530C7229C442Fd3F31b7db2"
    ABI='''
    [{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"join","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"sin","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"skr","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"gov","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"era","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"cup","type":"bytes32"}],"name":"ink","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"rho","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"air","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"rhi","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"flow","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"cap","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"cup","type":"bytes32"}],"name":"bite","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"cup","type":"bytes32"},{"name":"wad","type":"uint256"}],"name":"draw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"wad","type":"uint256"}],"name":"bid","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"cupi","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"axe","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"tag","outputs":[{"name":"wad","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"off","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vox","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"gap","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"cup","type":"bytes32"}],"name":"rap","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"cup","type":"bytes32"},{"name":"wad","type":"uint256"}],"name":"wipe","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"gem","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"tap_","type":"address"}],"name":"turn","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"per","outputs":[{"name":"ray","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"exit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"pip_","type":"address"}],"name":"setPip","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"pie","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"fit_","type":"uint256"},{"name":"jam","type":"uint256"}],"name":"cage","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"rum","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"sai","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"param","type":"bytes32"},{"name":"val","type":"uint256"}],"name":"mold","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"tax","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"drip","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"cup","type":"bytes32"},{"name":"wad","type":"uint256"}],"name":"free","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"mat","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"pep","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"out","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"cup","type":"bytes32"},{"name":"wad","type":"uint256"}],"name":"lock","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"cup","type":"bytes32"}],"name":"shut","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"cup","type":"bytes32"},{"name":"guy","type":"address"}],"name":"give","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"fit","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"chi","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"vox_","type":"address"}],"name":"setVox","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"pip","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"pep_","type":"address"}],"name":"setPep","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"fee","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"cup","type":"bytes32"}],"name":"lad","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"din","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"wad","type":"uint256"}],"name":"ask","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"cup","type":"bytes32"}],"name":"safe","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"pit","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"cup","type":"bytes32"}],"name":"tab","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"open","outputs":[{"name":"cup","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"tap","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"cups","outputs":[{"name":"lad","type":"address"},{"name":"ink","type":"uint256"},{"name":"art","type":"uint256"},{"name":"ire","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"sai_","type":"address"},{"name":"sin_","type":"address"},{"name":"skr_","type":"address"},{"name":"gem_","type":"address"},{"name":"gov_","type":"address"},{"name":"pip_","type":"address"},{"name":"pep_","type":"address"},{"name":"vox_","type":"address"},{"name":"pit_","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"lad","type":"address"},{"indexed":false,"name":"cup","type":"bytes32"}],"name":"LogNewCup","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"}]
'''

 
