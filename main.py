from scrapeDetails import scrapeDetails
from scrapeParcels import scrapeParcels
from getParcelIDs import getParcelIDs

urls = []
parcels = []
parcels = getParcelIDs.importXlsx()
# urls = scrapeParcels.Parcels()
scrapeDetails.Details(parcels)