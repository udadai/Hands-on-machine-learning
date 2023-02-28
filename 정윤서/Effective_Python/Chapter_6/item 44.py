# 잘못된 예시
class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms

    def getOhms(self):
        return self._ohms

    def setOhms(self, ohms):
        self._ohms = ohms

r0 = OldResistor(50e3)
print('Before: ', r0.getOhms())
r0.setOhms(10e3)
print('After: ', r0.getOhms())
print("---------------------------")

# 올바른 예시
class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

r1 = Resistor(50e3)
r1.ohms = 10e3
r1.ohms += 5e3
print('수정 후: ', r1.ohms)
print("---------------------------")

# @property 사용
class VoltageResistacne(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0
    
    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

r2 = VoltageResistacne(1e3)
print(f'Before: {r2.current:.2f} amps')
r2.voltage = 10
print(f'After: {r2.current:.2f} amps')
print("---------------------------")

# Specifying a setter
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'ohms must be > 0; got {ohms}')
        self._ohms = ohms

r3 = BoundedResistance(1e3)
#r3.ohms = 0
#BoundedResistance(-5)

# parent classes의 attributes 수정 못하게 하기
class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Ohms is immutable")
        self._ohms = ohms

r4 = FixedResistance(1e3)
#r4.ohms = 2e3

# behavior you implement is not surprising
class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

r7 = MysteriousResistor(10)
r7.current = 0.01
print(f'Before: {r7.voltage:.2f}')
r7.ohms
print(f'After: {r7.voltage:.2f}')
print("---------------------------")