def subtract_digits(number):
    original_digits = len(str(number))
    iterations = 0
    output = []
    while iterations < 100 and number > 0:
        digits = len(str(number))
        subtract_value = int('1' * digits)
        if subtract_value > number:
            subtract_value = int('1' * (digits - 1))
        number -= subtract_value
        number_str = f"{number:0{original_digits}}"
        output.append(list(map(int, list(number_str))))
        iterations += 1
    return output

def print_output(output):
    for row in output:
        print(" ".join(map(str, row)))
    # Calculate column sums and averages
    sums = [sum(col) for col in zip(*output)]
    averages = [round(sum_ / len(output)) for sum_ in sums]
    print("sums = ", " ".join(map(str, sums)))
    print("averages = ", " ".join(map(str, averages)))

number = 12222233212319898989897898912121221424545377878998899898
output = subtract_digits(number)
print_output(output)
