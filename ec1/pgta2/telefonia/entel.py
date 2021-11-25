import math

def call(phone_number: str, call_duration: float, call_operator: str):
    call_dec, call_int = math.modf(call_duration)
    if (call_operator == "entel"):
        return (call_int + 1) * 0.45
    elif call_duration < 1:
        return (call_int + 1) * 1
    elif call_duration >= 1 and call_duration < 5:
        return (call_int + 1) * 1.3
    else:
        return (call_int + 1) * 0.6
