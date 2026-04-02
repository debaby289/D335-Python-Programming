bird_data = [
    ("Anna's Hummingbird", 14),
    ("Ruby-throated Hummingbird", 22),
    ("Blue-throated Hummingbird", 12),
    ("Violet-crowned Hummingbird", 3),
    ("Broad-billed Hummingbird", 0), 
    ("Magnificent Hummingbird", 6),
]

def filter_birds_by_sightings(bird_data, min_count):
    filtered_birds = []
    for bird in bird_data:
        name, count = bird
        if count > min_count:
            filtered_birds.append((name, count))
    return filtered_birds

result = filter_birds_by_sightings(bird_data, 21)
print(result) # { Ruby-throated Hummingbird": 22 }