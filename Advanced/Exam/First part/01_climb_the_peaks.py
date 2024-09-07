# from collections import deque
#
#
# def climbing(peaks, sum_p):
#     for k, v in peaks.items():
#         try:
#             if sum_p >= v:
#                 peaks[k] = "Yes"
#                 return peaks
#             return peaks
#
#         except TypeError:
#             continue
#
#
# def check_all_peaks():
#     climbed_peaks = {k for k, v in mountain_peaks.items() if v == "Yes"}
#     return True if len(climbed_peaks) == 5 else False
#
#
# def output():
#     result = ""
#     for k, v in mountain_peaks.items():
#         if v == "Yes":
#             result += f"{k}\n"
#     return result.strip()
#
#
# first_numbers = [int(x) for x in input().split(", ")]
# second_numbers = deque(int(x) for x in input().split(", "))
# mountain_peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
#
# while first_numbers and second_numbers:
#     mountain_peaks = climbing(mountain_peaks, first_numbers.pop() + second_numbers.popleft())
#
#     if check_all_peaks():
#         print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
#         break
#
# else:
#     print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
#
# if output():
#     print("Conquered peaks:")
#     print(output())




# def climb_peaks(sum_num, peaks, conquered):
#     if not sum_num or not peaks:
#         return conquered
#
#     current_peak = peaks[0]
#     curr_sum = sum_num.pop()
#     if curr_sum >= current_peak[1]:
#         conquered.append(current_peak[0])
#         return climb_peaks(sum_num, peaks[1:], conquered)
#     else:
#         return climb_peaks(sum_num, peaks, conquered)
#
#
# def main():
#     food = [int(x) for x in input().split(", ")]
#     stamina = [int(x) for x in input().split(", ")]
#     summing_numbers = [x + y for x, y in zip(food, reversed(stamina))]
#     peaks = [
#         ("Vihren", 80),
#         ("Kutelo", 90),
#         ("Banski Suhodol", 100),
#         ("Polezhan", 60),
#         ("Kamenitza", 70)
#     ]
#
#     conquered_peaks = climb_peaks(summing_numbers, peaks, [])
#
#     if len(conquered_peaks) == 5:
#         print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
#     else:
#         print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
#
#     if conquered_peaks:
#         print("Conquered peaks:")
#         for peak in conquered_peaks:
#             print(peak)
#
#
# if __name__ == "__main__":
#     main()


from collections import deque


def output():
    result = ""
    for k, v in mountain_peaks.items():
        if v == "Yes":
            result += f"{k}\n"
    return result.strip()


first_numbers = [int(x) for x in input().split(", ")]
second_numbers = deque(int(x) for x in input().split(", "))
summing_numbers = [x + y for x, y in zip(first_numbers, reversed(second_numbers))]
mountain_peaks = {"Vihren": 80, "Kutelo": 90, "Banski Suhodol": 100, "Polezhan": 60, "Kamenitza": 70}
for key, value in mountain_peaks.items():
    try:
        curr_sum = summing_numbers.pop()
        if curr_sum >= value:
            mountain_peaks[key] = "Yes"
            break
    except IndexError:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break
else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

if output():
    print("Conquered peaks:")
    print(output())