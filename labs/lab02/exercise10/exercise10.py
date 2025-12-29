
def calculate_base_usage(distance):
   usage = (distance / 10) * 1.5
   return usage

def apply_mode_bonus(usage, is_sport_mode):
   if is_sport_mode:
      usage = usage * 1.5
      current_battery = 100 - usage
      return current_battery

def has_enough_battery(distance, current_battery, is_sport_mode):
   usage = (distance / 10) * 1.5
   if is_sport_mode:
      usage = usage * 1.5
      if current_battery > usage:
        return True
      else:
        return False