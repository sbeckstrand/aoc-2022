input = open("input.txt", "r")
signal = input.read()
input.close()

def find_first_marker(signal, size=4):
    for i in range(0, len(signal)):
        if len(set(signal[i:i+size])) == size:
            return i + size  

print(find_first_marker(signal))
print(find_first_marker(signal, 14))