from models.cadeaux import Gift


class Special_Gift(Gift):
    def __init__(self, name, value, stock, magic=False):
        super().__init__(name, value, stock)
        self._magic = magic

    def __str__(self):
        return super().__str__() + " - Cadeau magique" if self.magic else ""
