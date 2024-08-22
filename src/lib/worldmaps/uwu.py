import json

# Mapping of 3-letter country codes to 2-letter country codes
country_code_map = {
    "CPV": "CV", "BES": "BQ", "LIE": "LI", "IMN": "IM", "PNG": "PG",
    "MAR": "MA", "CMR": "CM", "GAB": "GA", "SGS": "GS", "SOM": "SO",
    "PRY": "PY", "TLS": "TL", "SYR": "SY", "ALB": "AL", "PHL": "PH",
    "GLP": "GP", "BRA": "BR", "MOZ": "MZ", "BGR": "BG", "ATG": "AG",
    "QAT": "QA", "TCA": "TC", "GUM": "GU", "SRB": "RS", "JAM": "JM",
    "GTM": "GT", "PRT": "PT", "TUR": "TR", "MYT": "YT", "COD": "CD",
    "HKG": "HK", "MLT": "MT", "BDI": "BI", "CZE": "CZ", "PSE": "PS",
    "BRB": "BB", "COG": "CG", "HRV": "HR", "KOR": "KR", "DNK": "DK",
    "SVK": "SK", "ATF": "TF", "MYS": "MY", "SLE": "SL", "EGY": "EG",
    "MNG": "MN", "TON": "TO", "FSM": "FM", "IRQ": "IQ", "SUR": "SR",
    "WSM": "WS", "RWA": "RW", "CAN": "CA", "LVA": "LV", "PLW": "PW",
    "SXM": "SX", "ESP": "ES", "LBN": "LB", "DMA": "DM", "COM": "KM",
    "RUS": "RU", "PRI": "PR", "GEO": "GE", "PRK": "KP", "ISL": "IS",
    "USA": "US", "NZL": "NZ", "KEN": "KE", "GRC": "GR", "DZA": "DZ",
    "CIV": "CI", "BHR": "BH", "VEN": "VE", "UGA": "UG", "MTQ": "MQ",
    "GUY": "GY", "BEL": "BE", "COL": "CO", "ERI": "ER", "ARG": "AR",
    "MNP": "MP", "DOM": "DO", "MWI": "MW", "HTI": "HT", "DJI": "DJ",
    "SJM": "SJ", "MKD": "MK", "PAN": "PA", "AFG": "AF", "BLR": "BY",
    "AGO": "AO", "TTO": "TT", "AZE": "AZ", "CUW": "CW", "ROU": "RO",
    "UZB": "UZ", "AUT": "AT", "TKM": "TM", "ALA": "AX", "SYC": "SC",
    "BTN": "BT", "VCT": "VC", "MUS": "MU", "HMD": "HM", "BGD": "BD",
    "ARE": "AE", "SWZ": "SZ", "ZWE": "ZW", "LUX": "LU", "PER": "PE",
    "OMN": "OM", "MDA": "MD", "KWT": "KW", "KHM": "KH", "SLV": "SV",
    "PYF": "PF", "URY": "UY", "TUN": "TN", "ISR": "IL", "STP": "ST",
    "MAF": "MF", "MDG": "MG", "TCD": "TD", "GHA": "GH", "NCL": "NC",
    "VUT": "VU", "JPN": "JP", "GNQ": "GQ", "NER": "NE", "AND": "AD",
    "ARM": "AM", "MEX": "MX", "SGP": "SG", "CXR": "CX", "CHN": "CN",
    "BIH": "BA", "SLB": "SB", "FLK": "FK", "BFA": "BF", "YEM": "YE",
    "XKX": "XK", "IRL": "IE", "MNE": "ME", "SEN": "SN", "SVN": "SI",
    "GMB": "GM", "IND": "IN", "GIN": "GN", "TWN": "TW", "CYP": "CY",
    "SDN": "SD", "AUS": "AU", "IDN": "ID", "ECU": "EC", "GRD": "GD",
    "REU": "RE", "MRT": "MR", "NIC": "NI", "HUN": "HU", "KGZ": "KG",
    "JOR": "JO", "DEU": "DE", "FRA": "FR", "THA": "TH", "CAF": "CF",
    "BHS": "BS", "CHL": "CL", "CUB": "CU", "KAZ": "KZ", "GNB": "GW",
    "NLD": "NL", "LTU": "LT", "UKR": "UA", "BOL": "BO", "VNM": "VN",
    "GRL": "GL", "BEN": "BJ", "NIU": "NU", "LAO": "LA", "SAU": "SA",
    "ESH": "EH", "FRO": "FO", "NGA": "NG", "MLI": "ML", "LBY": "LY",
    "CHE": "CH", "ASM": "AS", "ATA": "AQ", "LBR": "LR", "GUF": "GF",
    "HND": "HN", "BRN": "BN", "SWE": "SE", "BWA": "BW", "FJI": "FJ",
    "NOR": "NO", "LKA": "LK", "ETH": "ET", "ITA": "IT", "LCA": "LC",
    "BLZ": "BZ", "EST": "EE", "KIR": "KI", "CRI": "CR", "LSO": "LS",
    "TGO": "TG", "TZA": "TZ", "SSD": "SS", "NPL": "NP", "TJK": "TJ",
    "PAK": "PK", "NAM": "NA", "IRN": "IR", "MMR": "MM", "GBR": "GB",
    "ZMB": "ZM", "MHL": "MH", "FIN": "FI", "POL": "PL", "ZAF": "ZA"
}

def replace_country_codes(json_file_path, output_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Check if 'features' key is in the root object
    if 'features' in data:
        for feature in data['features']:
            # Check if 'properties' and 'A3' key are in the feature
            if 'properties' in feature and 'A3' in feature['properties']:
                a3_code = feature['properties']['A3']
                if a3_code in country_code_map:
                    feature['properties']['A3'] = country_code_map[a3_code]
                else:
                    print(f'Warning: {a3_code} not found in the country code map.')

    # Write the updated JSON to a new file
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
json_file_path = 'countries-land-10km.geo.json'
output_file_path = 'countries-land-10km.geo.json'
replace_country_codes(json_file_path, output_file_path)
