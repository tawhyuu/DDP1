weight = float(input('Weight:'))*0.45359237
height = float(input('Height:'))*0.0254

print(weight)
print(height)

bmi = weight/(height**2)
print(bmi)

if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Normal')
elif bmi < 30:
    print('Overweight')
else:
    print('Obesse')