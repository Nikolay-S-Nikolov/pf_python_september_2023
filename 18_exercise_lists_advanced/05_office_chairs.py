def free_chairs_check(rooms: int) -> int:
    total_needed_chairs = 0
    extra_chairs = 0
    for number_of_room in range(1, rooms + 1):
        chairs, visitors = input().split()
        if len(chairs) < int(visitors):
            needed_chairs = int(visitors) - len(chairs)
            total_needed_chairs += needed_chairs
            print(f"{needed_chairs} more chairs needed in room {number_of_room}")
        else:
            extra_chairs += len(chairs) - int(visitors)
    total_free_chairs = extra_chairs - total_needed_chairs
    return total_free_chairs


rooms_in_the_business_center = int(input())
free_chairs = free_chairs_check(rooms_in_the_business_center)
if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
