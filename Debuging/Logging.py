# There are Five Levels Of 'Log'
# debug(lowest)
# info
# worning
# error
# critical(highest)

# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)


logging.debug('Start Of Program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n) :

        total *= i
        n+1
        logging.debug('i is (%s)' % (i))
        logging.debug('total is (%s)' %(total))

    logging.debug('Reurn Value (%s)' % (total))
    return total

print(factorial(5))

logging.debug('End of program')