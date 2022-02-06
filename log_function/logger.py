import time

def log_decorator(file_name):
    def _log_decorator(old_function):
        def new_function(*args, **kwargs):
            a = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
            result = old_function(*args, **kwargs)
            log_data = (f'Вызвана функция:{old_function},\n Время вызова:{a},\n C аргументами:{args},{kwargs},\n C результатом:{result}\n')
            with open(file_name, 'a', encoding='utf-8') as f:
                f.write(log_data)
            return result
        return new_function
    return _log_decorator