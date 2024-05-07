import puppy_state
import state_playing
import state_asleep

class StateEating(puppy_state.PuppyState):
  '''The puppy\'s eating state'''

  def play(self, puppy):
    puppy.inc_plays()
    puppy.change_state(state_playing.StatePlaying())
    return "The puppy looks up from its food and chases after the ball."

  def feed(self, puppy):
    puppy.inc_feeds()
    if(puppy.feeds >= 3):
      puppy.change_state(state_asleep.StateAsleep())
      puppy.reset() #reset feeding counter
      return "The puppy continues to eat as you add another scoop of kibble to its bowl.\nThe puppy ate so much it fell asleep!"
    #else
    return "The puppy continues to eat as you add another scoop of kibble to its bowl."