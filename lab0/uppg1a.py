name = input("Vad heter du: ")
print(f"Hej {name}!")

age = input("Mata in din ålder: ")
print(f"Du föddes år {2025 - int(age)} (probably)")

state = input("Vilket län föddes du i: ")

half_name = name[:int(len(name) / 2)]
half_state = state[int(len(state) / 2):]
print(f"Första halvan av ditt namn och andra halvan av ditt län är: {half_name}{half_state}")