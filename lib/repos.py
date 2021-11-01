class Repo():
    all = []

    def __init__(self, name):
        self._name = name
        self._save()
    
    def _save(self):
        self.all.append(self)

    @property
    def name(self):
        return self._name

    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]
