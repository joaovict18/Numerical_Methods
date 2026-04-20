import decimal

# Set decimal module to 50 float point
decimal.getcontext().prec = 50
D = decimal.Decimal

# Here we define real values and the measured ones
real_a, measured_a = D('20.0'), D('20.5')
real_b, measured_b = D('10.10'), D('10.5') 

def calculate_errors(real, measured):
    abs_error = abs(real - measured)
    # Prevents division by zero
    rel_error = (abs_error / abs(real)) * 100 if real != 0 else 0
    return abs_error, rel_error

def show(label, real, measured):
    ea, er = calculate_errors(real, measured)
    print(f"{label:<5} | Abs: {float(ea):.2f} | Rel: {float(er):.2f}%")


print(f"{"Op":<5} | {"Abs Error":<13} | {"Rel Error"}")
print("-" * 50)

# Show the 4 operations to view propagation
show("Sum", real_a + real_b, measured_a + measured_b)
show("Sub", real_a - real_b, measured_a - measured_b)
show("Mult", real_a * real_b, measured_a * measured_b)
show("Div", real_a / real_b, measured_a / measured_b)
