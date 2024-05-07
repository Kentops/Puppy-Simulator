import state_asleep

class Puppy:
  '''
  The puppy class
  <<get>> plays: int - Play limit
  <<get>> feeds: int - Feed limit
  _state: PuppyState - The state of the puppy
  change_state(new_state) - sets the puppy's state
  throw_ball(self): str - calls _state.play()
  give_food(self): str - calls _state.feed()
  inc_plays(self) - plays += 1
  inc_feeds(self) - feeds += 1
  reset(self) - plays and feeds = 0
  '''

  def __init__(self):
    '''Constructs a puppy and starts it sleeping'''
    self._plays = 0
    self._feeds = 0
    self._state = state_asleep.StateAsleep()

  def change_state(self, state):
    '''Changes the puppy\'s state'''
    self._state = state

  def throw_ball(self):
    '''Calls self._state.play()'''
    #State changes will be dealt with in the state classes
    return self._state.play(self) 
    #self is passed in to represent this puppy

  def give_food(self):
    '''Calls self._state.feed()'''
    return self._state.feed(self)

  def inc_plays(self):
    '''Increments _plays'''
    self._plays += 1

  def inc_feeds(self):
    '''Increments _feeds'''
    self._feeds += 1

  def reset(self):
    '''Resets the _plays and _feeds attributes to 0'''
    self._plays,self._feeds = 0,0 #unnecessary compression


  @property
  def plays(self):
    '''Accessor method for _plays.'''
    return self._plays

  @property
  def feeds(self):
    '''Accessor method for feeds.'''
    return self._feeds