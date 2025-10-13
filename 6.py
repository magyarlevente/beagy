def sea_level_pressure(P_hpa, T_c, h_m=125.0):
    term = 1 - (0.0065 * h_m) / (T_c + 0.0065 * h_m + 273.15)
    P0 = P_hpa * (term ** -5.257)
    return P0


def tendency(prev_P0, curr_P0, threshold=1.6):
    delta = curr_P0 - prev_P0
    if delta <= -threshold:
        return "falling"
    elif delta >= threshold:
        return "rising"
    else:
        return "steady"


def zambretti_forecast(curr_P, prev_P, T, h=125.0):
    curr_P0 = sea_level_pressure(curr_P, T, h)
    prev_P0 = sea_level_pressure(prev_P, T, h)

    tend = tendency(prev_P0, curr_P0)

    Z = None
    forecast = "Unknown"

    if tend == "falling" and 985 <= curr_P0 <= 1050:
        Z = 127 - 0.12 * curr_P0
        Zr = int(round(Z))
        table = {
            1: "Settled Fine",
            2: "Fine Weather",
            3: "Fine, Becoming Less Settled",
            4: "Fairly Fine, Showery Later",
            5: "Showery, Becoming More Unsettled",
            6: "Unsettled, Rain Later",
            7: "Rain at Times, Worse Later",
            8: "Rain at Times, Becoming Very Unsettled",
            9: "Very Unsettled, Rain"
        }
        Zr = min(max(Zr, 1), 9)
        forecast = table[Zr]

    elif tend == "steady" and 960 <= curr_P0 <= 1033:
        Z = 144 - 0.13 * curr_P0
        Zr = int(round(Z))
        table = {
            10: "Settled Fine",
            11: "Fine Weather",
            12: "Fine, Possibly Showers",
            13: "Fairly Fine, Showers Likely",
            14: "Showery, Bright Intervals",
            15: "Changeable, Some Rain",
            16: "Unsettled, Rain at Times",
            17: "Rain at Frequent Intervals",
            18: "Very Unsettled, Rain"
        }
        Zr = min(max(Zr, 10), 18)
        forecast = table[Zr]

    elif tend == "rising" and 947 <= curr_P0 <= 1030:
        Z = 185 - 0.16 * curr_P0
        Zr = int(round(Z))
        table = {
            20: "Settled Fine",
            21: "Fine Weather",
            22: "Becoming Fine",
            23: "Fairly Fine, Improving",
            24: "Fairly Fine, Possibly Showers Early",
            25: "Showery Early, Improving",
            26: "Changeable, Mending",
            27: "Rather Unsettled, Clearing Later",
            28: "Unsettled, Probably Improving",
            29: "Unsettled, Short Fine Intervals",
            30: "Very Unsettled, Finer at Times",
            31: "Stormy, Possibly Improving",
            32: "Stormy, Much Rain"
        }
        Zr = min(max(Zr, 20), 32)
        forecast = table[Zr]

    else:
        forecast = f"P0={curr_P0:.2f} hPa is outside valid range for '{tend}' condition."

    return {
        "curr_P0": curr_P0,
        "prev_P0": prev_P0,
        "tendency": tend,
        "Z": Z,
        "forecast": forecast
    }

if __name__ == "__main__":
    examples = [
        {"curr_P": 1013.0, "prev_P": 1016.0, "T": 15.0},
        {"curr_P": 1013.0, "prev_P": 1013.5, "T": 10.0},
        {"curr_P": 1018.0, "prev_P": 1016.0, "T": 12.0},
        {"curr_P": 950.0,  "prev_P": 952.0,  "T": 8.0}
    ]

    for e in examples:
        res = zambretti_forecast(e["curr_P"], e["prev_P"], e["T"])
        print("--------------------------------------------------")
        print(f"Measured Pressure: {e['curr_P']} hPa (prev: {e['prev_P']} hPa)")
        print(f"Temperature: {e['T']} °C")
        print(f"Sea-level Pressure (current): {res['curr_P0']:.2f} hPa")
        print(f"Sea-level Pressure (previous): {res['prev_P0']:.2f} hPa")
        print(f"Tendency: {res['tendency']}")
        if res["Z"] is not None:
            print(f"Z = {res['Z']:.2f}")
        print(f"Forecast: {res['forecast']}")
    print("==================================================")
