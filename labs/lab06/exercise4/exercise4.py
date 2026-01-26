def synchronize_databases(legacy_list, modern_set, blacklist):
    # Ensure proper set types
    modern_ids = set(modern_set)
    blacklist_emails = set(blacklist)

    sanitized_legacy_ids = set()

    # Safely process legacy records
    for item in legacy_list:
        try:
            record_id, email = item
        except (TypeError, ValueError):
            # Skip malformed legacy records
            continue

        if email not in blacklist_emails:
            sanitized_legacy_ids.add(record_id)

    # IDs missing from modern system
    lost_set = sanitized_legacy_ids - modern_ids

    # IDs present in modern but not in legacy
    ghost_set = modern_ids - sanitized_legacy_ids

    return lost_set, ghost_set



        
        
