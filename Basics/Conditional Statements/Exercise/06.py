from math import floor

world_record = float(input())
distance_meters = float(input())
time_seconds_for_one_meter_swimming = float(input())

distance_for_Ivan_to_swim = distance_meters * time_seconds_for_one_meter_swimming
forces_water = floor(distance_meters // 15) * 12.5 #int(distance_meters / 15) * 12.5
total_time = distance_for_Ivan_to_swim + forces_water

if total_time < world_record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {abs(world_record - total_time):.2f} seconds slower.') #(total_time - world_record):.2f
