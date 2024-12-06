from datetime import datetime, timedelta

class GestionDate:
    def __init__(self):
        self.maintenant = datetime.now()

    def date_il_y_a_x_jours(self, days):
        il_y_a_x_jours = self.maintenant - timedelta(days=days)
        return il_y_a_x_jours.strftime('%Y-%m-%d')