
def is_critical_hit(luck):
   if luck > 70:
       return True
   else:
       return False

def calculate_raw_damage(base_attack, is_critical_hit):
    if is_critical_hit:
        base_attack = base_attack * 2
        return base_attack

    

def calculate_final_health(current_health, raw_damage, defense):
    """
    Calculates final health after damage.
    Actual damage = raw_damage - defense.
    Damage cannot be negative.
    Final health cannot go below 0.
    """
    # TODO: Implement this function
    pass
