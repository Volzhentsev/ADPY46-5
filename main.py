from log_function.logger import log_decorator

@log_decorator('log_file.txt')
def calculate_salary(month, salary):
    return month * salary

if __name__ == '__main__':

    calculate_salary(12, 10000)