"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    
    def __init__(self, species, qty, order_type, tax):
        """ Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == "Christmas":
            base_price = 5 * 1.5

        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and (self.qty < 10):
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type = "domestic", tax = 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type = "international", tax = 0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Special government order that inherits from AbstractMelonOrder """
    
    def __init__ (self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty, order_type = "government", tax = 0)
        self.passed_inspection = False
    
    def mark_inspection(self):
        """Return if melon passes inspection"""
        self.passed_inspection = True

        return self.passed_inspection
