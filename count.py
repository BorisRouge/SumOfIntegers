def sum_of_digits(number):
    result = 0
    while number:
        result, number = result + number % 10, number // 10
    return result


def count_1(n):
    groups = {x: 0 for x in range(64)}
    for customer in range(n+1):
        group = sum_of_digits(customer)
        groups[group] += 1
    return groups


def count_2(n_customers, n_first_id):
    groups = {x: 0 for x in range(64)}
    for customer in range(n_first_id, n_customers+1):
        group = sum_of_digits(customer)
        groups[group] += 1
    return groups
