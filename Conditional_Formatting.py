SEASON_BASE = {
    "peak": 9000,
    "shoulder": 7000,
    "off": 5000
}

# 2. Function Read-Only Access
def get_base(season):
    print ("inside get_base" ,SEASON_BASE.get(season, SEASON_BASE["off"]))
    return SEASON_BASE.get(season, SEASON_BASE["off"])
# 3. Local Scope & Shadowing
season = "off"
print("Global season:", season)

def test_scope():
    season = "peak"
    print("Local season:", season)

test_scope()
print("Global still:", season)

# 4. `global` Keyword
def force_global():
    global season
    season = "shoulder"

force_global()
print("After forcing:", season)

# 5–6. Branching Logic: Seasonal & Weekend Surcharge
def price_with_flow(season, is_weekend):
    base = get_base(season)
    if season == "peak":
        surcharge = 1500
    elif season == "shoulder":
        surcharge = 1000
    else:
        surcharge = 0

    if is_weekend:
        surcharge += 500

    return base + surcharge

# 7. Testing Multiple Paths
print(price_with_flow("peak", False))      # 9000
print(price_with_flow("shoulder", True))   # 8500
print(price_with_flow("off", True))        # 5500