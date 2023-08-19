# Morse code

# Write a function named morse_code() that takes two arguments: short_signal and long_signal.
# This function should return the Morse code for SOS (3 short signals, 3 long signals, 3 short signals).

def morse_code(short_signal, long_signal):
    s = short_signal
    l = long_signal
    sos = [s, s, s, l, l, l, s, s, s]
    return " ".join(sos)
print(morse_code(" . ", " - "))
