from shadowlands.sl_dapp import SLFrame

from decimal import Decimal, InvalidOperation

import pdb
from shadowlands.tui.debug import debug

class LockEthFrame(SLFrame):

    def initialize(self):

        #pdb.set_trace()
        self.add_divider()
        self.add_label("Current account balance (ETH):", add_divider=False)
        self.add_label(str(round(self.dapp.collateral_eth_value(self.dapp.cup_id) / self.dapp.WAD, 4)), add_divider=False)
        self.add_divider(draw_line=True)
        self.add_label("How much ETH would you like to deposit?", add_divider=False)
        self.deposit_textbox_value = self.add_textbox("ETH Value:", default_value='1')
        self.add_divider(draw_line=True)
        self.add_label("Projected liquidation price:", add_divider=False)
        self.add_label(self.projected_liquidation_price)
        self.add_label("Projected collateralization ratio:", add_divider=False)
        self.add_label(self.projected_collateralization_ratio)
        self.add_ok_cancel_buttons(self.lock_eth_choice, ok_text="Deposit")

    def lock_eth_choice(self):
        if self.deposit_eth_value() == Decimal(0.0):
            self.dapp.add_message_dialog("0 ETH is not a valid choice")
            return

        self.dapp.lock_eth(self.dapp.cup_id, self.deposit_eth_value())
        self.close()

    def projected_liquidation_price(self):
        return str(round(self.dapp.projected_liquidation_price(self.dapp.cup_id, self.deposit_eth_value()), 4))

    def projected_collateralization_ratio(self):
        return str(round(self.dapp.projected_collateralization_ratio(self.dapp.cup_id, self.deposit_eth_value()), 4))

    def deposit_eth_value_string(self):
        return str(self.deposit_eth_value())

    def deposit_eth_value(self):
        try:
            return Decimal(self.deposit_textbox_value() )
        except (TypeError, InvalidOperation):
            return Decimal(0.0)