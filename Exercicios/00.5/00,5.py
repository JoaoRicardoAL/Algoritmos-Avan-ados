import heapq
import math

# Funtion thar calculates the distance between two points on Earth based on their latitude and longitude using the Haversine formula.
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Raio da Terra em km

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

# Read the input data
num_players = int(input())
latC, lonC = input().split()
latC = float(latC)
lonC = float(lonC)

# Initialize a priority queue to store players and their distances
players = []
best_try = None
for _ in range(num_players):
    nome, lat, lon = input().split()
    lat = float(lat)
    lon = float(lon)
    distance = haversine(latC, lonC, lat, lon)
    heapq.heappush(players, (distance, nome))
    if best_try is None or distance < best_try:
        best_try = distance
    print(f"> [AVISO] MELHOR PALPITE: {best_try:.3f}km")

# Sort players by distance to ensure the priority order is correct
sorted_players = heapq.nsmallest(len(players), players)

# Print the ranking
print(f"\nRANKING\n-------")
rank = 1
winner_tag = " [FANTASTICO]"
for player in sorted_players:
    if player[0] <= 0.050:
        print(f"{rank:>2}. {player[1]:<20} : {player[0]:>6.3f} km{winner_tag}")
    else:
        print(f"{rank:>2}. {player[1]:<20} : {player[0]:>6.3f} km")
    rank += 1
         