def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    moves = 0

    r_q_s = r_q - 1
    r_q_n = r_q + 1

    c_q_e = c_q + 1
    c_q_w = c_q - 1

    for i in range(r_q - 1, 0, -1):
        # print("for 1 ====================")
        if [i, c_q] in obstacles:
            # print("blocked")
            # print([i, c_q])
            break
        else:
            moves += 1
            # print("not blocked")
            # print([i, c_q])

    for i in range(r_q + 1, n + 1):
        # print("for 2 ====================")
        if [i, c_q] in obstacles:
            # print("blocked")
            # print([i, c_q])
            break
        else:
            moves += 1
            # print("not blocked")
            # print([i, c_q])

    for i in range(c_q - 1, 0, -1):
        # print("for 3 ====================")
        if [r_q, i] in obstacles:
            # print("blocked")
            # print([r_q, i])
            break
        else:
            moves += 1
            # print("not blocked")
            # print([r_q, i])

    for i in range(c_q + 1, n + 1):
        # print("for 4 ====================")
        if [r_q, i] in obstacles:
            # print("blocked")
            # print([r_q, i])
            break
        else:
            moves += 1
            # print("not blocked")
            # print([r_q, i])

    # for j in range(cq + 1, n + 1):

    # print(f"moves: {moves}")

    while r_q_s > 0 and c_q_e <= n:
        # print("while 1 ====================")
        # print("=============")
        if [r_q_s, c_q_e] in obstacles:
            # print("not blocked")
            break

            # print([r_q_s, c_q_e])

        else:
            # print("blocked")
            # print([r_q_s, c_q_e])
            moves += 1
        r_q_s -= 1
        c_q_e += 1

    r_q_s = r_q - 1
    r_q_n = r_q + 1

    c_q_e = c_q + 1
    c_q_w = c_q - 1

    while r_q_s > 0 and c_q_w > 0:
        # print("while 2 ====================")
        # print("=============")
        if [r_q_s, c_q_w] in obstacles:
            # print("not blocked")
            break

            # print([r_q_s, c_q_w])

        else:
            # print("blocked")
            # print([r_q_s, c_q_w])
            moves += 1
        r_q_s -= 1
        c_q_w -= 1

    while r_q_n <= n and c_q_e <= n:
        # print("while 3 ====================")
        # print("=============")
        if [r_q_n, c_q_e] in obstacles:
            # print("not blocked")
            break
            # print([r_q_n, c_q_e])

        else:
            # print("blocked")
            # print([r_q_n, c_q_e])
            moves += 1
        r_q_n += 1
        c_q_e += 1

    r_q_s = r_q - 1
    r_q_n = r_q + 1

    c_q_e = c_q + 1
    c_q_w = c_q - 1

    while r_q_n <= n and c_q_w > 0:
        # print("while 4 ====================")
        # print("=============")
        if [r_q_n, c_q_w] in obstacles:
            # print("not blocked")
            break
            # print([r_q_n, c_q_w])

        else:
            # print("blocked")
            # print([r_q_n, c_q_w])
            moves += 1
        r_q_n += 1
        c_q_w -= 1

    return moves

# print(f"moves: {moves}")

