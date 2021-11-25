import math

def call(phone_number: str, call_duration: float, call_operator: str):
    call_dec, call_int = math.modf(call_duration)
    if (call_operator == "movistar"):
        return (call_int + 1) * 0.5
    elif call_duration < 1:
        return (call_int + 1) * 1.2
    elif call_duration >= 1 and call_duration < 5:
        return (call_int + 1) * 1
    else:
        return (call_int + 1) * 0.8
