class Articles:
    def __init__(self, type_, id_, title, created, updated):
        self.type_ = type_
        self.id_ = id_
        self.title = title
        self.created = created
        self.updated = updated

    @property
    def type_(self):
        return self._type
    
    @type_.setter
    def type_(self, value):
        if helper.validation(value):
            self._type = value
        else:
            raise ValueError

    @property
    def id_(self):
        return self._id

    @id_.setter
    def id_(self, value):
        if helper.validation(value):
            self._id = value
        else:
            raise ValueError

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if helper.validation(value):
            self._title = value
        else:
            raise ValueError

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, value):
        if helper.validation(value):
            self._created = value
        else:
            raise ValueError

    @property
    def updated(self):
        return self._updated
    
    @updated.setter
    def updated(self, value):
        if helper.validation(value):
            self._updated = value
        else:
            raise ValueError
