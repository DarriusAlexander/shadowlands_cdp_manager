from shadowlands.sl_dapp import SLFrame

import decimal
from decimal import Decimal, InvalidOperation

import pdb
from shadowlands.tui.debug import debug

class LockEthFrame(SLFrame):

    def proj_collat_ratio(self):
        try:
            return self.projected_collateralization_ratio 
        except:
            return "Unavailable"

    def initialize(self):
        self.add_label("How much ETH would you like to deposit?", add_divider=False)
        self.deposit_textbox_value = self.add_textbox("ETH Value:", default_value='1')
        self.add_label("Current account balance (ETH):", add_divider=False)
        self.add_label(str(self.dapp.node.eth_balance)[0:12])
        self.add_label("Projected liquidation price:", add_divider=False)
        self.add_label(self.projected_liquidation_price)
        self.add_label("Projected collateralization ratio:", add_divider=False)
        self.add_label(self.projected_collateralization_ratio)
        self.add_button_row(
            [
                ("Deposit", self.lock_eth_choice, 0),
                ("Back", self.close, 1)
            ]
        )

    def lock_eth_choice(self):
        if self.deposit_eth_value() == Decimal(0.0):
            self.dapp.add_message_dialog("0 is not a valid choice")
            return

        #debug(); pdb.set_trace()

        
        self.dapp.add_transaction_dialog(
            self.dapp.ds_proxy.lock(
                self.dapp.sai_proxy.address, 
                self.dapp.tub.address,
                self.dapp.cup_id, 
            ),
            tx_value=self.deposit_eth_value(),
            title="Lock Collateral",
            gas_limit=300000,
        )

        self.close()
        return
 

        #self.dapp.add_transaction_dialog(
        #    self.dapp.ds_proxy.lock(
        #        self.dapp.tub.address, 
        #        self.dapp.cup_id, 
        #        self.deposit_eth_value()
        #    ),
        #    tx_value=self.deposit_eth_value(),
        #    title="Lock Collateral",
        #    gas_limit=230000,
        #)
 
        #self.dapp.lock_eth(self.dapp.cup_id, self.deposit_eth_value())
        self.close()

    def projected_liquidation_price(self):
        try:
            return str(self.dapp.projected_liquidation_price(0, self.deposit_eth_value()))[0:12]
        except (decimal.InvalidOperation):
            return "Undefined"

    def projected_collateralization_ratio(self):
        try:
            return str(self.dapp.projected_collateralization_ratio(0,  self.deposit_eth_value()))[0:12]
        except (decimal.DivisionByZero, decimal.InvalidOperation):
            return "Undefined"

    def deposit_eth_value_string(self):
        return str(self.deposit_eth_value())

    def deposit_eth_value(self):
        try:
            return Decimal(self.deposit_textbox_value() )
        except (TypeError, InvalidOperation):
            return Decimal(0.0)
