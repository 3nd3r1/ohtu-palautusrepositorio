from matchers import PlaysIn, HasAtLeast, HasFewerThan, And, All, Or


class QueryBuilder:
    def __init__(self, query=All()):
        self._query = query

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._query))

    def hasAtLeast(self, value, attribute):
        return QueryBuilder(And(HasAtLeast(value, attribute), self._query))

    def hasFewerThan(self, value, attribute):
        return QueryBuilder(And(HasFewerThan(value, attribute), self._query))

    def oneOf(self, *matchers):
        return QueryBuilder(And(Or(*matchers), self._query))

    def build(self):
        return self._query
