import puppy_state
import state_asleep

class StatePlaying(puppy_state.PuppyState):
  '''The puppy\'s playing state'''

  def play(self, puppy):
    puppy.inc_plays()
    if(puppy.plays >= 3):
      puppy.change_state(state_asleep.StateAsleep)
      puppy.reset()
      return "You throw the ball again and the puppy excitedly chases it.\nThe puppy played so much it fell asleep!"
    #else
    return "You throw the ball again and the puppy excitedly chases it."

  def feed(self,puppy):
    return "The puppy is too focused on playing with the ball to eat."