from utils import extract_term


class Term:
    def __init__(self, *, coeff, variable, power):
        if power == 0:
            variable = None

        self.coeff = coeff
        self.variable = variable
        self.power = power

    @classmethod
    def parse_from_string(cls, s):
        coeff, variable, power = extract_term(s)

        if power is None:
            power = 0

        return cls(coeff=coeff, variable=variable, power=power)

    @classmethod
    def constant(cls, value):
        return cls(coeff=value, variable=None, power=0)

    @property
    def is_constant(self):
        return self.variable is None and self.power == 0

    def derivative(self):
        if self.is_constant:
            return Term.constant(0)

        return Term(
            coeff=self.coeff * self.power,
            variable=self.variable,
            power=max(0, self.power - 1)
        )

    def __add__(self, other):
        return Term(
            coeff=self.coeff + other.coeff,
            variable=self.variable,
            power=self.power
        )

    def __eq__(self, other):
        return (
            self.coeff == other.coeff
                and self.variable == other.variable
                and self.power == other.power
                and self.constant == other.constant
        )

    def __str__(self):
        if self.is_constant:
            return str(self.coeff)

        coeff_part = ''
        power_part = ''

        if self.coeff > 1:
            coeff_part = f'{self.coeff}*'

        if self.power > 1:
            power_part = f'^{self.power}'

        return f'{coeff_part}{self.variable}{power_part}'

    def __repr__(self):
        return str(self)


class Polynomial:
    def __init__(self, terms):
        self._terms = {}

        for term in terms:
            self.add_term(term)

    def add_term(self, term):
        if term.power not in self._terms:
            self._terms[term.power] = term
        else:
            self._terms[term.power] += term

    def __str__(self):
        sorted_terms = []

        for term_power in sorted(self._terms.keys(), reverse=True):
            sorted_terms.append(str(self._terms[term_power]))

        return '+'.join(sorted_terms)


    @classmethod
    def parse_from_string(cls, s):
        unparsed_terms = s.split('+')

        terms = [
            Term.parse_from_string(t) for t in unparsed_terms
        ]

        return cls(terms)
