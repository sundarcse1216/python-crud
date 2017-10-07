class RedriveProps:
    def __init__(self):
        pass

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def f_name(self):
        return self.f_name

    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, emp_id):
        self._emp_id - emp_id

    @f_name.setter
    def f_name(self, f_name):
        self._f_name = f_name

    @property
    def l_name(self):
        return self._fname

    @l_name.setter
    def l_name(self, l_name):
        self._l_name = l_name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address
