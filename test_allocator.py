from allocator import ResourceAllocator

resources = {
    "food": 100,
    "water": 200,
    "shelter": 20
}

allocator = ResourceAllocator(resources)

result = allocator.allocate("food", 30, vulnerable=True)

print(result)