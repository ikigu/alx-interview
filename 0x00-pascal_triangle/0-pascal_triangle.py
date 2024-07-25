def pascal_triangle(n):
    """
    Returns a list of integers representing Pascal's triangle of n

    Args:
        n (int): Number of rows for Pascal's triangle

    Returns:
        list of integers representing pascal's triangle of n
    """
    triangle = []

    for row_num in range(n):
        row = [1]

        if row_num > 0:
            prev_row = triangle[row_num - 1]
            for i in range(1, row_num):
                row.append(prev_row[i - 1] + prev_row[i])

        if row_num != 0:
            row.append(1)
        triangle.append(row)

    return triangle
