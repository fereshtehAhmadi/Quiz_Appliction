def log_user_register(username, date_time_obj):
    handler = open('registerations.log', 'a')
    handler.write(f'{username} {date_time_obj}\n')
    handler.close()
 