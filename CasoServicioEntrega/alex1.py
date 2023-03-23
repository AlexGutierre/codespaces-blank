#Alex David Gutierrez Puello T00064365
class Package:
    def __init__(self, code, weight, cost_per_gram, description):
        self.code = code
        self.weight = max(weight, 0)
        self.cost_per_gram = max(cost_per_gram, 0)
        self.description = description
    
    def calculate(self):
        return self.weight * self.cost_per_gram

class StandardPackage(Package):
    def __init__(self, code, weight, cost_per_gram, description, delivery_fee):
        super().__init__(code, weight, cost_per_gram, description)
        self.delivery_fee = max(delivery_fee, 0)
    
    def calculate(self):
        return super().calculate() + self.delivery_fee

class OverweightPackage(Package):
    def __init__(self, code, weight, cost_per_gram, description, overweight_cost_per_gram):
        super().__init__(code, weight, cost_per_gram, description)
        self.overweight_cost_per_gram = max(overweight_cost_per_gram, 0)
    
    def calculate(self):
        if self.weight <= 1000:
            return super().calculate()
        else:
            overweight = self.weight - 1000
            overweight_cost = overweight * self.overweight_cost_per_gram
            return super().calculate() + overweight_cost


# Ejemplo de uso
package1 = StandardPackage("001", 500, 0.01, "Paquete estándar", 500)
print("Costo del envío para el paquete estándar: $", package1.calculate())

package2 = OverweightPackage("002", 1500, 0.01, "Paquete sobrepeso", 0.1)
print("Costo del envío para el paquete sobrepeso: $", package2.calculate())
