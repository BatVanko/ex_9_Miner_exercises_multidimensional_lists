def moving_directions(com, ro, co):
    directions = {'up': [ro - 1, co],
                  'down': [ro + 1, co],
                  'left': [ro, co - 1],
                  'right': [ro, co + 1]}
    return directions[com]


size = int(input())
commands_move = input().split(' ')

matrix = []
start_row = None
start_col = None
last_row = None
last_col = None
sum_of_all_coals = 0
for _ in range(size):
    matrix.append(input().split(' '))

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 's':
            start_row = i
            start_col = j
        elif matrix[i][j] == 'c':
            sum_of_all_coals += 1

current_sum_of_coals = 0
game_over = False
for command in commands_move:
    current_row, current_col = moving_directions(command, start_row, start_col)
    if not (0 <= current_row < size and 0 <= current_col < size):
        continue
    start_row = current_row
    start_col = current_col
    last_row = current_row
    last_col = current_col
    if matrix[current_row][current_col] == 'c':
        current_sum_of_coals += 1
        matrix[current_row][current_col] = '*'
        if current_sum_of_coals == sum_of_all_coals:
            print(f"You collected all coal! ({current_row}, {current_col})")
            game_over = True
            break
    elif matrix[current_row][current_col] == 'e':
        print(f"Game over! ({current_row}, {current_col})")
        game_over = True
        break
if not game_over:
    print(f"{sum_of_all_coals - current_sum_of_coals} pieces of coal left. ({last_row}, {last_col})")
