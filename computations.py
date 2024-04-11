def energy_usage(meb, mngb, mfb):
    kgCO2 = (meb * 12 * 0.0005) + (mngb * 12 * 0.0053) + (mfb * 12 * 2.32)
    return round(kgCO2, 2)


def waste(waste_generated, waste_recycled):
    waste_out = (waste_generated * 12) * (0.57 - (waste_recycled / 100))
    return round(waste_out, 2)


def travel(km, fuelefficiency):
    travel_comp = km * (1 / (fuelefficiency)) * 2.31  # assumption is 6L per 100 km
    return round(travel_comp, 2)
