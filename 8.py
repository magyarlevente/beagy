def predict_altitude(P_hpa, P0_hpa=1013.25):
    """
    Calculates altitude in meters from atmospheric pressure.

    Parameters:
        P_hpa  - measured pressure in hPa
        P0_hpa - reference sea-level pressure in hPa (default: 1013.25)

    Returns:
        altitude in meters (float)
    """
    h = 44331 * (1 - (P_hpa / P0_hpa) ** (1 / 5.2558))
    return h

if __name__ == "__main__":

    pressures = [1013.25, 1000.0, 980.0, 950.0, 900.0]

    print("Predicted altitude based on pressure:")
    print("=====================================")

    for P in pressures:
        altitude = predict_altitude(P)
        print(f"Pressure: {P:.2f} hPa → Altitude: {altitude:.2f} m")

    print("=====================================")
