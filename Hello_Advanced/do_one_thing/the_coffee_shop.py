# Your code here
def receipt(numEsp, numCap, numLat):
    cost_of_espresso = 1.5
    cost_of_cappuccino = 2.75
    cost_of_latte = 3.25
    line_break = "---------------"
    space = ("---")
    esp_purchased = numEsp * cost_of_espresso
    cap_purchased = numCap * cost_of_cappuccino
    lat_purchased = numLat * cost_of_latte
    total = esp_purchased + cap_purchased + lat_purchased

    print("Developers Cafe")
    print(line_break)
    print(f"{numEsp}x Espresso ($1.5) {space} ${esp_purchased}")
    print(f"{numCap}x Cappuccino ($2.75) {space} ${cap_purchased}")
    print(f"{numLat}x Latte ($3.25) {space} ${lat_purchased}")
    print(line_break)
    print(f"Total {space} ${total}")


receipt(2, 1, 3)


