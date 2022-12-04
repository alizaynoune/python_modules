

class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        if isinstance(new_account, Account):
            # if account alredy exists
            if next((a for a in self.accounts if a.name == new_account.name),
                    None):
                return False
            self.accounts.append(new_account)
            return True
        return False

    def corrupted(self, account):
        list_attributes = dir(account)
        # even number of attributes
        # print('len', len(list_attributes), account.name)
        if not len(list_attributes) % 2:
            return True
        # an attribute starting with 'b'
        if (next((a for a in list_attributes if a.startswith('b')), None)):
            return True
        # no attribute strarting with zip or addr
        if not (next((a for a in list_attributes if a.startswith('zip')),
                     None)) or not (next((a for a in list_attributes
                                          if a.startswith('addr')), None)):
            return True
        # no attributes name, id or value
        if not hasattr(account, 'name') or not hasattr(account, 'id')\
                or not hasattr(account, 'value'):
            return True
        # attributes name not being a string ,
        # id not beig int, value not being int or float
        if not isinstance(account.name, str)\
                or not isinstance(account.id, int)\
                or not isinstance(account.value, (int, float)):
            return True
        return False

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if isinstance(origin, str) and isinstance(dest, str)\
                and isinstance(amount, (float, int)) and amount >= 0:
            dest_account = next(
                (a for a in self.accounts if a.name == dest), None)
            origin_account = next(
                (a for a in self.accounts if a.name == origin), None)
            if not origin_account or not dest_account\
                    or origin_account.value < amount:
                return False
            if self.corrupted(origin_account) or self.corrupted(dest_account):
                return False
            if origin != dest:
                origin_account.value -= amount
                dest_account.value += amount
            return True

        return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account = next((a for a in
                        self.accounts if a.name == name), None)
        if not account:
            return False
        list_attributes = dir(account)
        if not (next((a for a in list_attributes if a.startswith('zip')),
                     None)):
            setattr(account, 'zip', 25000)
        if not (next((a for a in list_attributes if a.startswith('addr')),
                     None)):
            setattr(account, 'addr', 'Morocco Khouribga')
        if not hasattr(account, 'id') or not isinstance(account.id, int):
            setattr(account, 'id', Account.ID_COUNT)
            Account.ID_COUNT += 1
        attr_b = (next((a for a in list_attributes if a.startswith('b')),
                       None))
        if (attr_b):
            delattr(account, attr_b)
        if not hasattr(account, 'value') or not isinstance(account.value,
                                                           (int, float)):
            setattr(account, 'value', 0)
        if not len(dir(account)) % 2:
            if not hasattr(account, 'info'):
                setattr(account, 'info', None)
            elif not hasattr(account, 'fix_len_attributes'):
                setattr(account, 'fix_len_attributes', None)
            else:
                delattr(account, 'fix_len_attributes')
        return True
