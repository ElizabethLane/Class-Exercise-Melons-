"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    def __init__(self, species, qty, country_code, passed_inspection):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = None
        self.tax = 0
        self.country_code = country_code
        self.passed_inspection = False

    def get_total(self):
        """Calculate price."""
        base_price = 5
        if self.species == "Christmas melons":
            base_price = float(base_price) * 1.5

        total = float(1 + self.tax) * float(self.qty * base_price)

        if self.qty < 10 and self.country_code is not "USA":
            total = float(total) + 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder): 
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty, 'USA')
        self.tax = 0.08
    


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, country_code)
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty, passed_inspection):
        super(GovernmentMelonOrder, self).__init__(species, qty, 'USA', passed_inspection)

    def mark_inspection(self):
        self.passed_inspection = True

