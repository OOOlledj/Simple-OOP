'''
000000 000000 000000
0    0 0    0 0    0
0    0 0    0 000000
0    0 0    0 0     
0    0 0    0 0
000000 000000 0
'''

oleja = ['Oleg Serejkin', 21 ,'Student', 2265]
spock = ['Spock the Spock', 35, 'Engineer', 2254]
mccoy = ['Leo McCoy', 'Chief medic', 2266]

#неудобно, так как код трудночитаем, обработки ошибок нет
#mccoy не имеет возраста, при обращении получим:
#'Chief medic'
#поэтому удобнее использовать классы

class Dog:
    
    #breeds = 'Akita' #Атрибут класса
    
    def __init__(self, name, age, breed = 'Usuall dog'):
        self.name = name
        self.age = age
        
        
    #def description(self):
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self,sound):
        return self.name + ' says ' + sound
    

class AmericanAkita(Dog):
    def speak(self, sound = 'WOOOFFF'):
        return self.name + ' says ' + sound
       #return super().speak(sound) #call parent method
       
example1 = AmericanAkita('Samanta', 3)
example2 = Dog('Tungus', 3)

print(type(example1))#определить класс/тип
print(isinstance(example2, Dog))#является ли объектом такого-то класса
print((isinstance(example1,Dog)))#объект дочернего класса является объектом родитлеьского класса
print(type(example1)==type(example2))
