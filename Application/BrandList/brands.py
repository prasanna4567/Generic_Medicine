brands = ['Dolo', 'Dolo2', 'Dolo3', 'Dolo4', 'Cipla', 'Sun', 'Vicks', 'Asprin', 'Zydus']

def getAvailableBrands():
    return brands

def filterBrands(filterText):
    if len(filterText) == 0:
        return brands
    return [s for s in brands if filterText in s]