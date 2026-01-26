def audit_zero_trust(baseline_set, current_log_list):
    current_log = set(current_log_list)
    authorized = (baseline_set & current_log)
    alerts = (current_log - baseline_set)
    inactive = (baseline_set - current_log)

    complete = (authorized, alerts, inactive)

    return complete



            





    
