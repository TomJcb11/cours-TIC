from models.enfant import Child
from models.cadeaux import Gift
from models.cadeau_special import Special_Gift


class GiftHandler:
    def __init__(self, gift_list, child_list):
        self._gift_list = gift_list
        self._child_list = child_list

    @property
    def gift_list(self):
        return self._gift_list

    @property
    def child_list(self):
        return self._child_list

    def remove_gift_from_list(
        self, gift_name
    ):  # agit comme un setter mais c'est pas pareil
        for gift in self._gift_list:
            while gift.name == gift_name:
                self._gift_list.remove(gift)

    def add_gift_to_list(self, gift):
        self._gift_list.append(gift)

    def check_gift_availability(self, gift_name):
        for gift in self._gift_list:
            if gift.name == gift_name:
                return gift.stock
        return False

    def update_gift_stock(self, gift_name, quantity):
        for gift in self._gift_list:
            if gift.name == gift_name:
                gift.stock -= quantity
                return True
        return False

    def find_gift_for_child(self, gift_value):
        for gift in self._gift_list:
            if not gift_value:
                return "Pas de cadeaux pour lui, il mérite même pas un charbon"
            for gift in self._gift_list:
                a = min(gift_value - gift.value)
            if gift.value == gift_value:
                self.update_gift_stock(gift.name, 1)
                return gift
        return False

    def add_child_to_list(self, child):
        self._child_list.append(child)

    def remove_child_from_list(self, child_name):
        for child in self._child_list:
            while child.name == child_name:
                self._child_list.remove(child)

    def deal_to_child(self):
        for child in self._child_list:
            child.reward_level = child.may_have_gift()
            self.find_gift_for_child(child.reward_level)
