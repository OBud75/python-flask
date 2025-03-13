import yfinance as yf
import matplotlib.pyplot as plt

class StockData:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = None

    def fetch_data(self, start_date, end_date):
        try:
            self.data = yf.download(self.ticker, start=start_date, end=end_date)
            print(f"Données récupérées pour {self.ticker}.")
        except Exception as e:
            print(f"Erreur lors de la récupération des données : {e}")

class StockGraph:
    @staticmethod
    def plot_stock(data, title="Graphique des actions", output_file="models/tesla_stock_2023.png"):
        # if data is not None and not data.empty:
        #     plt.figure(figsize=(10, 5))
        #     plt.plot(data['Close'], label='Prix de clôture')
        #     plt.title(title)
        #     plt.xlabel("Date")
        #     plt.ylabel("Prix ($)")
        #     plt.legend()
        #     plt.grid()
        #     plt.savefig(output_file) 
        #     print(f"Graphique enregistré sous le nom : {output_file}")
        # else:
        #     print("Aucune donnée disponible pour tracer le graphique.")

        # Ajouter un "early return" permet d'éviter le "else" et donc réduire le niveau d'indentation
        # En inversant la condition on peut d'abord gérer le cas particulier et ensuite faire la
        # logique principale sans avoir à l'indenter.
        # C'est souvent apprécié pour améliorer la lisibilité du code, encore une fois il n'y
        # a pas de règle absolue, à vous de juger si le "else" apporte en clareté.
        if data is None or data.empty:
            print("Aucune donnée disponible pour tracer le graphique.")
            return

        plt.figure(figsize=(10, 5))
        plt.plot(data['Close'], label='Prix de clôture')
        plt.title(title)
        plt.xlabel("Date")
        plt.ylabel("Prix ($)")
        plt.legend()
        plt.grid()
        plt.savefig(output_file) 
        print(f"Graphique enregistré sous le nom : {output_file}")

if __name__ == "__main__":
    tesla_stock = StockData("TSLA")
    tesla_stock.fetch_data(start_date="2023-01-01", end_date="2023-12-01")

    StockGraph.plot_stock(tesla_stock.data, title="Évolution de l'action Tesla (TSLA)", output_file="models/tesla_stock_2023.png")
    # On peut immaginer une fonction plot_stock qui prendrait en argument uniquement l'instance de StockData
    # def plot(stock: StockData):
        # title = f"Évolution de l'action {stock.ticker} ({stock.ticker})"
        # output_file = f"models/{stock.ticker}_stock.png"