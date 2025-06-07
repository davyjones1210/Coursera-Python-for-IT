import logging

logging.warning('This is a warning message')
logging.error('This is an error message')

logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')

logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.info('This message will be written to app.log')

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.error('This is an error with a custom format')

def user_login(username, password):
    logging.info(f"Attempting to log in user: {username}")
    # ... (some code for authentication)
    if authentication_failed:
        logging.error(f"Login failed for user: {username}")
    else:
        logging.info(f"Successfully logged in user: {username}")

    