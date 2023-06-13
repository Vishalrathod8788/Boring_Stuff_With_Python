import traceback

try :
    raise Exception('This is the error message.')
except :
    errorFile = open('error.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The Traceback info was written error_log.txt')
