class Value:

  # connective tissue of graphs is done by using children
  # _prev tells the children of the value but not the operation
  # for knowing the operations, we create _op
  def __init__(self, data, _children=(), _op=''):  # _children is tuple
    self.data = data
    self.grad = 0.0
    self._prev = set(_children)
    self._op = _op

  # print out nicer looking expression when +, * are called
  def __repr__(self):
    return f"Value(data={self.data})"

  # python does not know how to add two value objects
  # Hence, we use __add__ to tell python how to do it (+)
  def __add__(self, other):
    out = Value(self.data + other.data, (self, other), '+')
    return out

  def __mul__(self, other):
    out = Value(self.data * other.data, (self, other), '*')
    return out
  
# working example
# a = Value(2.0)
# b = Value(-3.0)
# c = Value(10.0)
# d = a * b + c
# d
