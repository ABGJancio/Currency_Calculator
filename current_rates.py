import requests
import csv


def get_rates_list():
    """Get actual 'bid' and 'ask' rates for currencies from NBP API."""
    response = requests.get(
        "http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()[0]['rates']
    global rates
    rates = [[item['currency'], item['code'], item['bid'], item['ask']]
             for item in data]
    return rates


def export_rates_to_csv():
    """Export database for currency rates to .csv file."""
    get_rates_list()
    with open('current_rates.csv', 'w', newline='') as csvfile:
        rates_writer = csv.writer(
            csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in rates:
            rates_writer.writerow(item)
    return


if __name__ == "__main__":
    export_rates_to_csv()
