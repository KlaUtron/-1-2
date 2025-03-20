vide = input ("Какое у вас животное? ")
name_pet = input ("Как зовут вашего питомца? ")
age_pet_str = input ("Сколько лет вашему питоцу? ")

age_pet = int(age_pet_str)
if age_pet >= 5:
    print(f'{vide} по кличке "{name_pet}". Возраст: {age_pet} лет' )
else:
    print(f'{vide} по кличке "{name_pet}". Возраст: {age_pet} года' )