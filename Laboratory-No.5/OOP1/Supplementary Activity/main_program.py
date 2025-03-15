import projectilemotion

angle = 20.0
speed = 11.0

r, h = projectilemotion.projectilemotion_solver(angle, speed)


print(f"""
A long jumper leaves the ground at an angle of 20.0° above the horizontal and at a speed of 11.0 m/s.
    (a) How far does he jump in the horizontal direction? {round(r, 2)}m
    (b) What is the maximum height reached? {round(h, 2)}m
    """)
