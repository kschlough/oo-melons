"""Classes for melon orders."""

import random
import datetime
# random.randint(5,9)

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    
    def __init__(self, species, qty, order_type, tax):
        """ Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    #solution
    def get_base_price(self):
        """Calculate base price using splurge pricing and rush hour fee."""

        # Splurge rate
        base_price = random.randrange(5, 10)

        now = datetime.datetime.now()

        # Is it rush hour?
        if now.hour >= 8 and now.hour <= 11 and now.weekday() < 5:
            base_price += 4

        return base_price

    def get_total(self, base_price):
        """Calculate price, including tax."""
        
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
    # solution
    # def mark_inspection(self, passed):
        # self.passed_inspection = passed
