import abc

class PuppyState(abc.ABC):
  '''
  An interface for puppy states
  <Abstract> play(puppy): string - Dictates how the puppy reacts to playing
  <Abstract> feed(puppy): string - Dictates how the puppy reacts to food
  '''

  @abc.abstractmethod
  def play(self, puppy) -> str:
    '''Dictates how the puppy reacts to playing'''
    pass

  @abc.abstractmethod
  def feed(self, puppy) -> str:
    '''Dictates how the puppy reacts to food.'''
    pass