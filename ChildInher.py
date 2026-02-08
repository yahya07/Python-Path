from OopsDemo import Calcolator


class ChildInher(Calcolator):

  firstVab = 'Yahya'

  def __init__(self, a=0, b=0):
    super().__init__(a, b)
    self.firstVab = ChildInher.firstVab

  def taking(self):
    print(self.firstVab)

  def set_firstVab(self, val):
    """Set the `firstVab` value on this instance."""
    self.firstVab = val

  def get_firstVab(self):
    """Return the current `firstVab` value."""
    return self.firstVab

  def greet(self):
    """Print a greeting and call parent's welcome message."""
    print("Hello from ChildInher")
    try:
      self.wellcominMsg()
    except Exception:
      # If parent method is not available or fails, still continue
      pass


obj = ChildInher()
print(obj.wellcominMsg)
