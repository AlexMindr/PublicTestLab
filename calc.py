import traceback

import requests


def add2(x,y):
    response = requests.get(f'http://127.0.0.1:5000/add/{x}+{y}')
    if response.ok:
        return response.text

    return 'Bad Response!'

def add(x, y):
    """Add Function"""
    if type(x) == int and type(y)==int:
        return x+y
    elif  type(x)==int and  type (y)==str:
            try :
                return x + int(y)

            except  :
                raise ValueError ('String cannot be converted!')

    elif type(x) ==  str and type(y)==int:
        try:
            return y + int(x)

        except:
            raise ValueError('String cannot be converted!')

    elif type(x) == int and type(y)==list:
            for i in range(len(y)):
                try:
                    y[i]=int(y[i]) + x

                except:
                    raise ValueError('List cannot be converted!')
            return y
    elif type(y) == int and type(x)==list:
        for i in range(len(x)):
            try:
                x[i] = int(x[i]) + y

            except:
                raise ValueError('List cannot be converted!')
        return x
    elif type(x) == int and type(y)==tuple:
            for i in range(len(y)):
                try:
                    x = x + int(y[i])

                except:
                    raise ValueError('Tuple cannot be converted!')
            return x
    elif type(y) == int and type(x)==tuple:
            for i in range(len(x)):
                try:
                   y=y+int(x[i])

                except:
                    raise ValueError('Tuple cannot be converted!')
            return y
    elif type(x) == int and type(y)==dict:
            for i in (list(y.keys())):

                try:
                   y[i]=int(y[i])+x

                except:
                    raise ValueError('Dict cannot be converted!')
            return y
    elif type(y) == int and type(x)==dict:
            for i in (list(x.keys())):

                try:
                   x[i]=int(x[i])+y

                except:
                    raise ValueError('Dict cannot be converted!')
            return x
    elif type(x) == str and type(y)==str:
                try:
                   sum=int(x)+int(y)

                except:
                    raise ValueError('Strings cannot be converted!')

                return sum
    elif type(x) == str and type(y) == list:
        for i in range(len(y)):
            try:
                y[i] = int(y[i]) + int(x)

            except:
                raise ValueError('String or List cannot be converted!')
        return y
    elif type(y) == str and type(x) == list:
        for i in range(len(x)):
            try:
                x[i] = int(x[i]) + int(y)

            except:
                raise ValueError('String or List cannot be converted!')
        return x
    elif type(x) == str and type(y)==tuple:
            for i in range(len(y)):
                try:
                    x = int(x) + int(y[i])

                except:
                    raise ValueError('Tuple or String cannot be converted!')
            return x
    elif type(y) == str and type(x)==tuple:
            for i in range(len(x)):
                try:
                   y=int(y)+int(x[i])

                except:
                    raise ValueError('Tuple or String cannot be converted!')
            return y
    elif type(x) == str and type(y)==dict:
            for i in (list(y.keys())):

                try:
                   y[i]=int(y[i])+int(x)

                except:
                    raise ValueError('Dict or String cannot be converted!')
            return y
    elif type(y) == str and type(x)==dict:
            for i in (list(x.keys())):

                try:
                   x[i]=int(x[i])+int(y)

                except:
                    raise ValueError('Dict or String cannot be converted!')
            return x
    elif type(x) == list and type(y) == list:
        if len(x)==len(y):
            for i in range(len(y)):
                try:
                    y[i] = int(y[i]) + int(x[i])

                except:
                    raise ValueError(' Lists cannot be converted!')
            return y
        else:
            sum=0
            for i in range(len(y)):
                try:
                    sum=sum+int(y[i])

                except:
                    raise ValueError(' Lists cannot be converted!')
            for i in range(len(x)):
                try:
                    sum = sum + int(x[i])

                except:
                    raise ValueError(' Lists cannot be converted!')
            return sum

    elif type(x) == list and type(y) == tuple:
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    x[i] = int(y[i]) + int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return x
        else:
            sum = 0
            for i in range(len(y)):
                try:
                    sum = sum + int(y[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            for i in range(len(x)):
                try:
                    sum = sum + int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return sum

    elif type(x) == tuple and type(y) == list:
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    y[i] = int(y[i]) + int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return y
        else:
            sum = 0
            for i in range(len(y)):
                try:
                    sum = sum + int(y[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            for i in range(len(x)):
                try:
                    sum = sum + int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return sum

    elif type(x) == list and type(y) == dict:
        sum=0
        for i in (list(y.keys())):

            try:
                sum = sum + int(y[i])
            except:
                raise ValueError('Dict or List cannot be converted!')
        for i in range(len(x)):
            try:
                sum = sum + int(x[i])

            except:
                raise ValueError(' Dict or List cannot be converted!')
        return sum

    elif type(x) == dict and type(y) == list:
        sum=0
        for i in (list(x.keys())):

            try:
                sum = sum + int(x[i])
            except:
                raise ValueError('Dict or List cannot be converted!')
        for i in range(len(y)):
            try:
                sum = sum + int(y[i])

            except:
                raise ValueError(' Dict or List cannot be converted!')
        return sum

    elif type(x) == tuple and type(y) == tuple:
        l=[]
        if len(x)==len(y):
            for i in range(len(y)):
                try:
                    l.append ( int(y[i]) + int(x[i]))

                except:
                    raise ValueError(' Tuples cannot be converted!')
            return l
        else:
            sum=0
            for i in range(len(y)):
                try:
                    sum=sum+int(y[i])

                except:
                    raise ValueError(' Tuples cannot be converted!')
            for i in range(len(x)):
                try:
                    sum = sum + int(x[i])

                except:
                    raise ValueError(' Tuples cannot be converted!')
            return sum

    elif type(x) == tuple and type(y) == dict:
        sum=0
        for i in (list(y.keys())):

            try:
                sum = sum + int(y[i])
            except:
                raise ValueError('Dict or Tuple cannot be converted!')
        for i in range(len(x)):
            try:
                sum = sum + int(x[i])

            except:
                raise ValueError(' Dict or List cannot be converted!')
        return sum

    elif type(x) == dict and type(y) == tuple:
        sum=0
        for i in (list(x.keys())):

            try:
                sum = sum + int(x[i])
            except:
                raise ValueError('Dict or Tuple cannot be converted!')
        for i in range(len(y)):
            try:
                sum = sum + int(y[i])

            except:
                raise ValueError(' Dict or Tuple cannot be converted!')
        return sum

    elif type(x) == dict and type(y) == dict:
        if x.keys()==y.keys():
            for i in (list(x.keys())):

                try:
                    x[i] =int(y[i]) + int(x[i])
                except:
                    raise ValueError('Dicts cannot be converted!')
            return x
        else:
            sum=0
            for i in (list(x.keys())):
                try:
                    sum =sum + int(x[i])
                except:
                    raise ValueError('Dicts cannot be converted!')
            for i in (list(y.keys())):
                try:
                    sum =sum + int(y[i])
                except:
                    raise ValueError('Dicts cannot be converted!')
            return sum


def subtract(x, y):
    """Subtract Function"""
    if type(x) == int and type(y) == int:
        return x - y
    elif type(x) == int and type(y) == str:
        try:
            return x - int(y)

        except:
            raise ValueError('String cannot be converted!')

    elif type(x) == str and type(y) == int:
        try:
            return int(x)-y

        except:
            raise ValueError('String cannot be converted!')

    elif type(x) == int and type(y) == list:
        for i in range(len(y)):
            try:
                y[i] = int(y[i]) - x

            except:
                raise ValueError('List cannot be converted!')
        return y
    elif type(y) == int and type(x) == list:
        for i in range(len(x)):
            try:
                x[i] = int(x[i]) - y

            except:
                raise ValueError('List cannot be converted!')
        return x
    elif type(x) == int and type(y) == tuple:
        for i in range(len(y)):
            try:
                x = x - int(y[i])

            except:
                raise ValueError('Tuple cannot be converted!')
        return x
    elif type(y) == int and type(x) == tuple:
        for i in range(len(x)):
            try:
                y = y - int(x[i])

            except:
                raise ValueError('Tuple cannot be converted!')
        return y
    elif type(x) == int and type(y) == dict:
        for i in (list(y.keys())):

            try:
                y[i] = int(y[i]) - x

            except:
                raise ValueError('Dict cannot be converted!')
        return y
    elif type(y) == int and type(x) == dict:
        for i in (list(x.keys())):

            try:
                x[i] = int(x[i]) - y

            except:
                raise ValueError('Dict cannot be converted!')
        return x
    elif type(x) == str and type(y) == str:
        try:
            dif = int(x) - int(y)

        except:
            raise ValueError('Strings cannot be converted!')

        return dif
    elif type(x) == str and type(y) == list:
        for i in range(len(y)):
            try:
                y[i] = int(y[i]) - int(x)

            except:
                raise ValueError('String or List cannot be converted!')
        return y
    elif type(y) == str and type(x) == list:
        for i in range(len(x)):
            try:
                x[i] = int(x[i]) - int(y)

            except:
                raise ValueError('String or List cannot be converted!')
        return x
    elif type(x) == str and type(y) == tuple:
        for i in range(len(y)):
            try:
                x = int(x) - int(y[i])

            except:
                raise ValueError('Tuple or String cannot be converted!')
        return x
    elif type(y) == str and type(x) == tuple:
        for i in range(len(x)):
            try:
                y = int(y) - int(x[i])

            except:
                raise ValueError('Tuple or String cannot be converted!')
        return y
    elif type(x) == str and type(y) == dict:
        for i in (list(y.keys())):

            try:
                y[i] = int(y[i]) - int(x)

            except:
                raise ValueError('Dict or String cannot be converted!')
        return y
    elif type(y) == str and type(x) == dict:
        for i in (list(x.keys())):

            try:
                x[i] = int(x[i]) - int(y)

            except:
                raise ValueError('Dict or String cannot be converted!')
        return x
    elif type(x) == list and type(y) == list:

        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    x[i] = int(x[i]) - int(y[i])

                except:
                    raise ValueError(' Lists cannot be converted!')
            return x
        else:
            dif = 0
            for i in range(len(y)):
                try:
                    dif = dif - int(y[i])

                except:
                    raise ValueError(' Lists cannot be converted!')
            for i in range(len(x)):
                try:
                   dif = dif + int(x[i])

                except:
                    raise ValueError(' Lists cannot be converted!')
            return dif

    elif type(x) == list and type(y) == tuple:
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    x[i] = int(x[i]) - int(y[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return x
        else:
            dif = 0
            for i in range(len(y)):
                try:
                    dif = dif - int(y[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            for i in range(len(x)):
                try:
                    dif = dif + int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return dif

    elif type(x) == tuple and type(y) == list:
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    y[i] = int(y[i]) - int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return y
        else:
            dif = 0
            for i in range(len(y)):
                try:
                    dif = dif - int(y[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            for i in range(len(x)):
                try:
                    dif = dif + int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return dif

    elif type(x) == list and type(y) == dict:
        dif = 0
        for i in (list(y.keys())):

            try:
                dif = dif - int(y[i])
            except:
                raise ValueError('Dict or List cannot be converted!')
        for i in range(len(x)):
            try:
                dif = dif + int(x[i])

            except:
                raise ValueError(' Dict or List cannot be converted!')
        return dif

    elif type(x) == dict and type(y) == list:
        dif = 0
        for i in (list(x.keys())):

            try:
                dif = dif - int(x[i])
            except:
                raise ValueError('Dict or List cannot be converted!')
        for i in range(len(y)):
            try:
                dif = dif + int(y[i])

            except:
                raise ValueError(' Dict or List cannot be converted!')
        return dif

    elif type(x) == tuple and type(y) == tuple:
        l = []
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    l.append(int(x[i]) - int(y[i]))

                except:
                    raise ValueError(' Tuples cannot be converted!')
            return l
        else:
            dif = 0
            for i in range(len(y)):
                try:
                    dif = dif - int(y[i])

                except:
                    raise ValueError(' Tuples cannot be converted!')
            for i in range(len(x)):
                try:
                    dif = dif + int(x[i])

                except:
                    raise ValueError(' Tuples cannot be converted!')
            return dif

    elif type(x) == tuple and type(y) == dict:
        dif = 0
        for i in (list(y.keys())):

            try:
                dif = dif - int(y[i])
            except:
                raise ValueError('Dict or Tuple cannot be converted!')
        for i in range(len(x)):
            try:
                dif = dif + int(x[i])

            except:
                raise ValueError(' Dict or List cannot be converted!')
        return dif

    elif type(x) == dict and type(y) == tuple:
        dif = 0
        for i in (list(x.keys())):

            try:
                dif = dif + int(x[i])
            except:
                raise ValueError('Dict or Tuple cannot be converted!')
        for i in range(len(y)):
            try:
                dif = dif - int(y[i])

            except:
                raise ValueError(' Dict or Tuple cannot be converted!')
        return dif

    elif type(x) == dict and type(y) == dict:
        if x.keys() == y.keys():
            for i in (list(x.keys())):

                try:
                    x[i] = int(x[i]) - int(y[i])
                except:
                    raise ValueError('Dicts cannot be converted!')
            return x
        else:
            dif = 0
            for i in (list(x.keys())):
                try:
                    dif = dif + int(x[i])
                except:
                    raise ValueError('Dicts cannot be converted!')
            for i in (list(y.keys())):
                try:
                    dif = dif - int(y[i])
                except:
                    raise ValueError('Dicts cannot be converted!')
            return dif


def multiply(x, y):
    """Multiply Function"""
    if type(x) == int and type(y) == int:
        return x * y
    elif type(x) == int and type(y) == str:
        try:
            return x * int(y)

        except:
            raise ValueError('String cannot be converted!')

    elif type(x) == str and type(y) == int:
        try:
            return y * int(x)

        except:
            raise ValueError('String cannot be converted!')

    elif type(x) == int and type(y) == list:
        for i in range(len(y)):
            try:
                y[i] = int(y[i]) * x

            except:
                raise ValueError('List cannot be converted!')
        return y
    elif type(y) == int and type(x) == list:
        for i in range(len(x)):
            try:
                x[i] = int(x[i]) * y

            except:
                raise ValueError('List cannot be converted!')
        return x
    elif type(x) == int and type(y) == tuple:
        for i in range(len(y)):
            try:
                x = x * int(y[i])

            except:
                raise ValueError('Tuple cannot be converted!')
        return x
    elif type(y) == int and type(x) == tuple:
        for i in range(len(x)):
            try:
                y = y * int(x[i])

            except:
                raise ValueError('Tuple cannot be converted!')
        return y
    elif type(x) == int and type(y) == dict:
        for i in (list(y.keys())):

            try:
                y[i] = int(y[i]) * x

            except:
                raise ValueError('Dict cannot be converted!')
        return y
    elif type(y) == int and type(x) == dict:
        for i in (list(x.keys())):

            try:
                x[i] = int(x[i]) * y

            except:
                raise ValueError('Dict cannot be converted!')
        return x
    elif type(x) == str and type(y) == str:
        try:
            prod = int(x) * int(y)

        except:
            raise ValueError('Strings cannot be converted!')

        return prod
    elif type(x) == str and type(y) == list:
        for i in range(len(y)):
            try:
                y[i] = int(y[i]) * int(x)

            except:
                raise ValueError('String or List cannot be converted!')
        return y
    elif type(y) == str and type(x) == list:
        for i in range(len(x)):
            try:
                x[i] = int(x[i]) * int(y)

            except:
                raise ValueError('String or List cannot be converted!')
        return x
    elif type(x) == str and type(y) == tuple:
        for i in range(len(y)):
            try:
                x = int(x) * int(y[i])

            except:
                raise ValueError('Tuple or String cannot be converted!')
        return x
    elif type(y) == str and type(x) == tuple:
        for i in range(len(x)):
            try:
                y = int(y) * int(x[i])

            except:
                raise ValueError('Tuple or String cannot be converted!')
        return y
    elif type(x) == str and type(y) == dict:
        for i in (list(y.keys())):

            try:
                y[i] = int(y[i]) * int(x)

            except:
                raise ValueError('Dict or String cannot be converted!')
        return y
    elif type(y) == str and type(x) == dict:
        for i in (list(x.keys())):

            try:
                x[i] = int(x[i]) * int(y)

            except:
                raise ValueError('Dict or String cannot be converted!')
        return x
    elif type(x) == list and type(y) == list:
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    y[i] = int(y[i]) * int(x[i])

                except:
                    raise ValueError(' Lists cannot be converted!')
            return y
        else:
            prod = 1
            for i in range(len(y)):
                try:
                    prod = prod * int(y[i])

                except:
                    raise ValueError(' Lists cannot be converted!')
            for i in range(len(x)):
                try:
                    prod = prod * int(x[i])

                except:
                    raise ValueError(' Lists cannot be converted!')
            return prod

    elif type(x) == list and type(y) == tuple:
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    x[i] = int(y[i]) * int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return x
        else:
            prod = 1
            for i in range(len(y)):
                try:
                    prod = prod * int(y[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            for i in range(len(x)):
                try:
                    prod = prod * int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return prod

    elif type(x) == tuple and type(y) == list:
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    y[i] = int(y[i]) * int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return y
        else:
            prod = 1
            for i in range(len(y)):
                try:
                    prod = prod * int(y[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            for i in range(len(x)):
                try:
                    prod = prod * int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')
            return prod

    elif type(x) == list and type(y) == dict:
        prod = 1
        for i in (list(y.keys())):

            try:
                prod = prod * int(y[i])
            except:
                raise ValueError('Dict or List cannot be converted!')
        for i in range(len(x)):
            try:
                prod = prod * int(x[i])

            except:
                raise ValueError(' Dict or List cannot be converted!')
        return prod

    elif type(x) == dict and type(y) == list:
        prod = 1
        for i in (list(x.keys())):

            try:
                prod = prod * int(x[i])
            except:
                raise ValueError('Dict or List cannot be converted!')
        for i in range(len(y)):
            try:
                prod = prod * int(y[i])

            except:
                raise ValueError(' Dict or List cannot be converted!')
        return prod

    elif type(x) == tuple and type(y) == tuple:
        l = []
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    l.append(int(y[i]) * int(x[i]))

                except:
                    raise ValueError(' Tuples cannot be converted!')
            return l
        else:
            prod = 1
            for i in range(len(y)):
                try:
                    prod = prod * int(y[i])

                except:
                    raise ValueError(' Tuples cannot be converted!')
            for i in range(len(x)):
                try:
                    prod = prod * int(x[i])

                except:
                    raise ValueError(' Tuples cannot be converted!')
            return prod

    elif type(x) == tuple and type(y) == dict:
        prod = 1
        for i in (list(y.keys())):

            try:
                prod = prod * int(y[i])
            except:
                raise ValueError('Dict or Tuple cannot be converted!')
        for i in range(len(x)):
            try:
                prod = prod * int(x[i])

            except:
                raise ValueError(' Dict or List cannot be converted!')
        return prod

    elif type(x) == dict and type(y) == tuple:
        prod = 1
        for i in (list(x.keys())):

            try:
                prod = prod * int(x[i])
            except:
                raise ValueError('Dict or Tuple cannot be converted!')
        for i in range(len(y)):
            try:
                prod = prod * int(y[i])

            except:
                raise ValueError(' Dict or Tuple cannot be converted!')
        return prod

    elif type(x) == dict and type(y) == dict:
        if x.keys() == y.keys():
            for i in (list(x.keys())):

                try:
                    x[i] = int(y[i]) * int(x[i])
                except:
                    raise ValueError('Dicts cannot be converted!')
            return x
        else:
            prod = 1
            for i in (list(x.keys())):
                try:
                    prod = prod * int(x[i])
                except:
                    raise ValueError('Dicts cannot be converted!')
            for i in (list(y.keys())):
                try:
                    prod = prod * int(y[i])
                except:
                    raise ValueError('Dicts cannot be converted!')
            return prod


def divide(x, y):
    """Divide Function"""
    if type(x) == int and type(y) == int:
        if int(y) == 0:
            raise ValueError('Cannot divide by 0 !')
        return x / y
    elif type(x) == int and type(y) == str:
        try:
            return x / int(y)

        except:
            if int(y) == 0:
                raise ValueError('Cannot divide by 0 !')
            raise ValueError('String cannot be converted!')

    elif type(x) == str and type(y) == int:
        try:
            return int(x) / y

        except:
            if int(y) == 0:
                raise ValueError('Cannot divide by 0 !')
            raise ValueError('String cannot be converted!')

    elif type(x) == int and type(y) == list:
        for i in range(len(y)):
            try:
                y[i] = int(y[i]) / x

            except:
                if int(x) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('List cannot be converted!')
        return y
    elif type(y) == int and type(x) == list:
        for i in range(len(x)):
            try:
                x[i] = int(x[i]) / y

            except:
                if int(y) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('List cannot be converted!')
        return x
    elif type(x) == int and type(y) == tuple:
        for i in range(len(y)):
            try:
                x = x / int(y[i])

            except:
                if int(y[i]) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('Tuple cannot be converted!')
        return x
    elif type(y) == int and type(x) == tuple:
        for i in range(len(x)):
            try:
                y = y / int(x[i])

            except:
                if int(x[i]) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('Tuple cannot be converted!')
        return y
    elif type(x) == int and type(y) == dict:
        for i in (list(y.keys())):

            try:
                y[i] = int(y[i]) / x

            except:
                if int(x) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('Dict cannot be converted!')
        return y
    elif type(y) == int and type(x) == dict:
        for i in (list(x.keys())):

            try:
                x[i] = int(x[i]) / y

            except:
                if int(y) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('Dict cannot be converted!')
        return x
    elif type(x) == str and type(y) == str:
        try:
            div = int(x) / int(y)

        except:
            if int(y) == 0:
                raise ValueError('Cannot divide by 0 !')
            raise ValueError('Strings cannot be converted!')

        return div
    elif type(x) == str and type(y) == list:
        for i in range(len(y)):
            try:
                y[i] = int(y[i]) / int(x)

            except:
                if int(x) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('String or List cannot be converted!')
        return y
    elif type(y) == str and type(x) == list:
        for i in range(len(x)):
            try:
                x[i] = int(x[i]) / int(y)

            except:
                if int(y) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('String or List cannot be converted!')
        return x
    elif type(x) == str and type(y) == tuple:
        for i in range(len(y)):
            try:
                x = int(x) / int(y[i])

            except:
                if int(y[i]) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('Tuple or String cannot be converted!')
        return x
    elif type(y) == str and type(x) == tuple:
        for i in range(len(x)):
            try:
                y = int(y) / int(x[i])

            except:
                if int(x[i]) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('Tuple or String cannot be converted!')
        return y
    elif type(x) == str and type(y) == dict:
        for i in (list(y.keys())):

            try:
                y[i] = int(y[i]) / int(x)

            except:
                if int(x) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('Dict or String cannot be converted!')
        return y
    elif type(y) == str and type(x) == dict:
        for i in (list(x.keys())):

            try:
                x[i] = int(x[i]) / int(y)

            except:
                if int(y) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('Dict or String cannot be converted!')
        return x
    elif type(x) == list and type(y) == list:

        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    x[i] = int(x[i]) / int(y[i])

                except:
                    if int(y[i]) == 0:
                        raise ValueError('Cannot divide by 0 !')
                    raise ValueError(' Lists cannot be converted!')
            return x
        else:
            div = 1
            for i in range(len(x)):
                try:
                    div = div * int(x[i])

                except:
                    raise ValueError(' Lists cannot be converted!')

            for i in range(len(y)):
                try:
                    div = div / int(y[i])

                except:
                    if int(y[i]) == 0:
                        raise ValueError('Cannot divide by 0 !')
                    raise ValueError(' Lists cannot be converted!')
            return div

    elif type(x) == list and type(y) == tuple:
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    x[i] = int(x[i]) / int(y[i])

                except:
                    if int(y[i]) == 0:
                        raise ValueError('Cannot divide by 0 !')
                    raise ValueError(' List or Tuple cannot be converted!')
            return x
        else:
            div = 1
            for i in range(len(x)):
                try:
                    div = div * int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')

            for i in range(len(y)):
                try:
                    div = div / int(y[i])

                except:
                    if int(y[i]) == 0:
                        raise ValueError('Cannot divide by 0 !')
                    raise ValueError(' List or Tuple cannot be converted!')
            return div

    elif type(x) == tuple and type(y) == list:
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    y[i] = int(y[i]) / int(x[i])

                except:
                    if int(x[i]) == 0:
                        raise ValueError('Cannot divide by 0 !')
                    raise ValueError(' List or Tuple cannot be converted!')
            return y
        else:
            div = 1
            for i in range(len(x)):
                try:
                    div = div * int(x[i])

                except:
                    raise ValueError(' List or Tuple cannot be converted!')

            for i in range(len(y)):
                try:
                    div = div / int(y[i])

                except:
                    if int(y[i]) == 0:
                        raise ValueError('Cannot divide by 0 !')
                    raise ValueError(' List or Tuple cannot be converted!')
            return div

    elif type(x) == list and type(y) == dict:
        div = 1
        for i in range(len(x)):
            try:
                div = div * int(x[i])

            except:
                raise ValueError(' Dict or List cannot be converted!')

        for i in (list(y.keys())):

            try:
                div = div / int(y[i])
            except:
                if int(y[i]) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('Dict or List cannot be converted!')
        return div

    elif type(x) == dict and type(y) == list:
        div = 1
        for i in range(len(y)):
            try:
                div = div * int(y[i])

            except:
                raise ValueError(' Dict or List cannot be converted!')

        for i in (list(x.keys())):

            try:
                div = div / int(x[i])
            except:
                if int(x[i]) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('Dict or List cannot be converted!')
        return div

    elif type(x) == tuple and type(y) == tuple:
        l = []
        if len(x) == len(y):
            for i in range(len(y)):
                try:
                    l.append(int(x[i]) / int(y[i]))

                except:
                    if int(y[i]) == 0:
                        raise ValueError('Cannot divide by 0 !')
                    raise ValueError(' Tuples cannot be converted!')
            return l
        else:
            div = 1
            for i in range(len(x)):
                try:
                    div = div * int(x[i])

                except:
                    raise ValueError(' Tuples cannot be converted!')

            for i in range(len(y)):
                try:
                    div = div / int(y[i])

                except:
                    if int(y[i]) == 0:
                        raise ValueError('Cannot divide by 0 !')
                    raise ValueError(' Tuples cannot be converted!')
            return div

    elif type(x) == tuple and type(y) == dict:
        div = 1
        for i in range(len(x)):
            try:
                div = div * int(x[i])
            except:
                raise ValueError(' Dict or List cannot be converted!')
        for i in (list(y.keys())):
            try:
                div = div / int(y[i])
            except:
                if int(y[i]) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError('Dict or Tuple cannot be converted!')
        return div

    elif type(x) == dict and type(y) == tuple:
        div = 1
        for i in (list(x.keys())):

            try:
                div = div * int(x[i])
            except:
                raise ValueError('Dict or Tuple cannot be converted!')
        for i in range(len(y)):
            try:
                div = div / int(y[i])

            except:
                if int(y[i]) == 0:
                    raise ValueError('Cannot divide by 0 !')
                raise ValueError(' Dict or Tuple cannot be converted!')
        return div

    elif type(x) == dict and type(y) == dict:
        if x.keys() == y.keys():
            for i in (list(x.keys())):

                try:
                    x[i] = int(x[i]) / int(y[i])
                except:
                    if int(y[i]) == 0:
                        raise ValueError('Cannot divide by 0 !')
                    raise ValueError('Dicts cannot be converted!')
            return x
        else:
            div = 1
            for i in (list(x.keys())):
                try:
                    div = div * int(x[i])
                except:
                    raise ValueError('Dicts cannot be converted!')
            for i in (list(y.keys())):
                try:
                    div = div / int(y[i])
                except:
                    if int(y[i]) == 0:
                        raise ValueError('Cannot divide by 0 !')
                    raise ValueError('Dicts cannot be converted!')
            return div





