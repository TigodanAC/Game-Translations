init -3 python:
    class Player(object):
        def __init__(self, code, state, progresses=[], **kwargs):
            self.code = code
            self.state_name = state
            self.progresses = progresses
            self.__dict__.update(kwargs)
        
        @property
        def state(self):
            return get(self.state_name)
        
        def __str__(self):
            return self.state.name
        
        @property
        def name(self):
            return self.state.name
        @name.setter
        def name(self, value):
            self.state.name = value
        
        @property
        def virtue(self):
            return self.state.virtue
        
        @property
        def credit(self):
            return self.state.credit
        
        @property
        def cash(self):
            return self.state.cash
        
        @property
        def buy(self):
            return self.state.buy      
        
        @property
        def pay(self):
            return self.state.pay  
        
        @property
        def earn(self):
            return self.state.earn
        
        @property
        def zero(self):
            return self.state.zero
        
        @property
        def revenues(self):
            return self.state.revenues
        
        @property
        def expanses(self):
            return self.state.expanses
        
        @property
        def account_book(self):
            return self.state.account_book


    class PlayerState(object):
        def __init__(self, name="MC", cash=0, **kwargs):
            self.__dict__.update(kwargs)
            self.name = name
            self.cash = Cash(self, cash)
            self.revenues = []
            self.expanses = []
            self.days_worked_of_week = 0
            self.credit = Attr(3, name=_("Credit"), owner=self)
            self.virtue = Attr(50, name=_("Virtue"), owner=self)
            self.account_book = []
        
        @property
        def revenue(self):
            revenue = Attr.sum(self.revenues)
            revenue.name = "Revenue"
            revenue.value *= 1.0
            return revenue
        
        @property
        def expanse(self):
            expanse = Attr.sum(self.expanses)
            expanse.name = "Expense"
            return expanse
        
        @property
        def income(self):
            return self.revenue - self.expanse
        
        def get_wage(self):
            return self.days_worked_of_week * 50.0 * self.work.stage
        
        @property
        def wage(self):
            return self.get_wage
        
        def earn(self, value, thing="", handle=True):
            returned = self.cash.add(value)
            if handle:
                if returned is 1:
                    Handle.cash_earn(self, value, thing)
                    self.account_book.append(Revenue(value, thing, store.t))
                elif returned is 0:
                    pass
                else:
                    pass
        
        def pay(self, value, thing="", handle=True):
            returned = self.cash.pay(value)
            if handle:
                if returned is 1:
                    Handle.payment_succeeded(self, thing, value)
                    self.account_book.append(Expanse(-value, thing, store.t))
                elif returned is 0:
                    Handle.payment_failed(thing) 
                else:
                    pass
            return returned
        
        def buy(self, value, thing="", handle=True):
            returned = self.cash.buy(value)
            if handle:
                if returned is 1:
                    Handle.purchase_succeeded(self, thing, value)
                    self.account_book.append(Expanse(-value, thing, store.t))
                elif returned is 0:
                    Handle.purchase_failed(thing) 
                else:
                    pass
            return returned
        
        def zero(self, thing="", handle=True):
            old_val = self.cash.zero()
            if handle:
                Handle.cash_zero(self, old_val)
                self.account_book.append(Expanse(-old_val, thing, store.t))
        
        
        def increase_credit(self, handle=True):
            if self.credit < 3:
                self.credit += 1
            if self.credit is 3:
                self.credit.set(3)
            if handle:
                Handle.increase(self.credit, 1)
        
        def decrease_credit(self, handle=True):
            self.credit -= 1
            if handle:
                Handle.decrease(self.credit, 1)
        
        def increase_virtue(self, handle=True):
            self.virtue += 1
            if handle:
                Handle.increase(self.virtue, 1)
        
        def decrease_virtue(self):
            self.virtue -= 1
            if handle:
                Handle.increase(self.virtue, 1)
            if virtue <= 0:
                self.virtue.set(0)
        
        @property
        def title(self):
            pstg = self.virtue
            if 0 <= pstg <= 20:
                return "Harem Master"
            elif 20 < pstg <= 30:
                return "Playboy"
            elif 30 < pstg <= 40:
                return "Charming Dude"
            elif 40 < pstg <= 50:
                return "Man of Virtue"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
