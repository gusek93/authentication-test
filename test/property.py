# Getters /Setter 예시

# class Celsius():

#     def __init__(self, temperature=0):
#         self.set_temperature(temperature)
        
#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32
    
    
#     # getter 메서드
#     def get_temperature(self):
#         return self._temperature
    
#     # setter 메서드
#     def set_temperature(self, value):
#         if value < -271.15:
#             raise ValueError('-273.15 미만의 온도는 없습니다.')
#         self._temperature = value
        
        
# human = Celsius(37)

# print(human.get_temperature())


# print(human.to_fahrenheit())


# human.set_temperature(-300)

# print(human.to_fahrenheit())


# property 사용
# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature
        
#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32
    
#     # getter
#     def get_temperature(self):
#         print('Getting value')
#         return self._temperature
    
#     # setter
#     def set_temperature(self, value):
#         print('Setting value')
#         if value < -273.15:
#             raise ValueError("온도 없음")
#         self._temperature = value
        
#     temperature = property(get_temperature, set_temperature)
    

# human = Celsius(37)

# print(human.temperature)

# print(human.to_fahrenheit())

# human.temperature = -300


# 데코레이터 사용 문법
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
        
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    @property
    def temperature(self):
        print("Getting value")
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        print("Setting value")
        if value < -273.15:
            raise ValueError('없음')
        self._temperature = value
        

human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)
        
    