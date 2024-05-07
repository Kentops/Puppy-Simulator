import puppy_state
import state_eating

class StateAsleep(puppy_state.PuppyState):
  '''
  Defines the puppy's actions while asleep
  '''

  def play(self, puppy):
    return "The puppy is asleep. It doesn't want to play right now."

  def feed(self, puppy):
    #Change puppy's state to eating
    puppy.inc_feeds()
    puppy.change_state(state_eating.StateEating())
    return "The puppy wakes up and comes running to eat."