from datetime import datetime, timedelta

class GestionDate:
    def __init__(self):
        # Un peu dangereux car cela force le code appelant à faire
        # attention à bien instancier une GestionDate à chaque fois
        # Typiquement si on lance le code à 23h59 et 59 secondes
        # gestion_date = GestionDate()
        # ... 1 seconde passe pour x ou y raison ...
        # gestion_date.date_il_y_a_x_jours(5) sera faux
        self.maintenant = datetime.now()

    def date_il_y_a_x_jours(self, days):
        il_y_a_x_jours = self.maintenant - timedelta(days=days)
        return il_y_a_x_jours.strftime('%Y-%m-%d')

# Evitez au maximum de mélanger anglais et français.
# Le français est acceptable pour les commentaires si vous savez
# qu'uniquement des lecteurs francophones devront lire le code.
# Autrement on préferera uniformiser et n'utiliser que l'anglais.

# Ici une simple fonction peut suffire
def date_days_ago(days):
    return (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")


# Quelques possibilités avec une classe
class Date:
    def days_ago(self, days: int):
        return self._format(datetime.now() - timedelta(days=days))

    def _format(self, date: datetime):
        return date.strftime("%Y-%m-%d")


# On peut potentiellement utiliser des classmethod. Pas forcément
# une bonne idée cela dépendra des cas d'utilisation, dans le doute
# j'aurai tendance à instancier la classe à chaque fois et donc ne
# pas faire de classmethods, si cela vous smeble plus cohérent d'utiliser
# directement la classe un peu comme un module utilitaire alors oui.
class DateUtil:
    @classmethod
    def days_ago(cls, days: int):
        return cls._format(datetime.now() - timedelta(days=days))

    @staticmethod
    # On peut aussi utiliser une méthode statique étant donné que
    # la fonction n'a pas besoin d'accéder à la classe (ce sont
    # des préférences, personnellement je préfère éviter mais
    # c'est tout à fait logique ici de rendre la méthode statique
    # pour éviter de passer la classe ou l'instance en paramètre)
    def _format(date: datetime):
        return date.strftime("%Y-%m-%d")



if __name__ == "__main__":
    print(Date().days_ago(1))
    print(DateUtil.days_ago(1))
