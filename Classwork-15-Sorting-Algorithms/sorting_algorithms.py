# Classwork 15 - Bubble Sort, Sorting Algorithms
# Armando Karin Molina Marrufo

import random
import stddraw
from color import Color

# ============================================================
# PROCESS - Sorting algorithm functions (no animation)
# ============================================================

def bubble_sort(numbers):
    # PROCESS - Compare adjacent pairs and swap if out of order
    n = len(numbers)
    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]

def insertion_sort(numbers):
    # PROCESS - Pick each element and insert it into its correct position
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key

def selection_sort(numbers):
    # PROCESS - Find the minimum element and place it at the front each pass
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# ============================================================
# PROCESS - Draw bars helper
# ============================================================

def draw_bars(numbers, selected=()):
    # PROCESS - Clear canvas and draw each number as a colored bar
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n
    for i, number in enumerate(numbers):
        x = i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    # OUTPUT - Show current frame
    stddraw.show(500)

# ============================================================
# PROCESS - Animated sorting functions
# ============================================================

def bubble_sort_animated(numbers):
    # PROCESS - Set up canvas scale
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    for sweep in range(n):
        for pair in range(0, n - 1 - sweep):
            # OUTPUT - Draw before swap
            draw_bars(numbers, selected=(pair, pair + 1))
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers[pair + 1], numbers[pair]
                # OUTPUT - Draw after swap
                draw_bars(numbers, selected=(pair, pair + 1))
    # OUTPUT - Draw final sorted result
    draw_bars(numbers)
    stddraw.show()

def insertion_sort_animated(numbers):
    # PROCESS - Set up canvas scale
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        # OUTPUT - Highlight the element being inserted
        draw_bars(numbers, selected=(i,))
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            # OUTPUT - Draw shift step
            draw_bars(numbers, selected=(j, j + 1))
            j -= 1
        numbers[j + 1] = key
        # OUTPUT - Draw after insertion
        draw_bars(numbers, selected=(j + 1,))
    # OUTPUT - Draw final sorted result
    draw_bars(numbers)
    stddraw.show()

def selection_sort_animated(numbers):
    # PROCESS - Set up canvas scale
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            # OUTPUT - Highlight current comparison
            draw_bars(numbers, selected=(j, min_index))
            if numbers[j] < numbers[min_index]:
                min_index = j
        # PROCESS - Swap minimum into position
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        # OUTPUT - Draw after swap
        draw_bars(numbers, selected=(i, min_index))
    # OUTPUT - Draw final sorted result
    draw_bars(numbers)
    stddraw.show()

# ============================================================
# INPUT - Generate random list and run animated sort
# ============================================================

numbers = [random.randint(0, 100) for x in range(10)]
print(f"Before sort: {numbers}")
bubble_sort_animated(numbers)
# To try other algorithms, comment the line above and uncomment one below:
# insertion_sort_animated(numbers)
# selection_sort_animated(numbers)
