from models.cadeaux import Gift


class Child:
    def __init__(self, name, age, gender, behaviour, gifts=[]):
        self._gifts = gifts
        self._name = name
        self._age = age if age <= 14 else -1
        self._gender = gender
        self._behaviour = (
            behaviour if behaviour in ["moyen", "sage", "turbulent"] else "moyen"
        )
        self._reward = {"moyen": 5, "sage": 10, "turbulent": 0}[self.behaviour]

    def __str__(self):
        return f"{self.name} ({self.age} ans, {self.gender}, comportement: {self.behaviour}), {len(self.gifts)} cadeaux dans sa liste"

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    @property
    def behaviour(self):
        return self._behaviour

    @behaviour.setter
    def behaviour(self, behaviour):
        if behaviour in ["moyen", "sage", "turbulent"]:
            self._behaviour = behaviour

    @property
    def gifts(self):
        return self._gifts

    @gifts.setter
    def gifts(self, gifts):
        self._gifts = gifts

    @property
    def reward(self):
        return self._reward

    @reward.setter
    def reward(self, reward):
        self._reward = reward

    def may_have_gift(self, gift):
        if self.behaviour == "turbulent":
            return False
        elif self.age <= 14 and (self.behaviour == "moyen" or self.behaviour == "sage"):
            return self.reward
