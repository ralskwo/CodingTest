def read_input():
    import sys
    input = sys.stdin.read  # 표준 입력에서 모든 데이터를 읽어온다.
    data = input().split()  # 입력 데이터를 공백 기준으로 나누어 리스트로 저장한다.
    index = 0  # 현재 읽고 있는 데이터의 인덱스를 초기화한다.

    # 첫째 줄에서 단어 사전의 단어 수 w를 읽어온다.
    w = int(data[index])
    index += 1  # 다음 데이터로 인덱스를 이동시킨다.
    dictionary = set()  # 단어들을 저장할 집합을 생성한다.

    # 다음 w개의 줄에서 단어를 읽어와 사전에 추가한다.
    for _ in range(w):
        dictionary.add(data[index])  # 단어를 집합에 추가한다.
        index += 1  # 다음 단어로 인덱스를 이동시킨다.

    # 그 다음 줄에서 Boggle 보드의 개수 b를 읽어온다.
    b = int(data[index])
    index += 1  # 다음 데이터로 인덱스를 이동시킨다.
    boards = []  # Boggle 보드들을 저장할 리스트를 생성한다.

    # 각 Boggle 보드에 대해 4줄을 읽어와 보드 리스트에 추가한다.
    for _ in range(b):
        board = []  # 현재 Boggle 보드를 저장할 리스트를 생성한다.
        for _ in range(4):
            board.append(data[index])  # 보드의 한 줄을 추가한다.
            index += 1  # 다음 줄로 인덱스를 이동시킨다.
        boards.append(board)  # 완성된 보드를 보드 리스트에 추가한다.

    return dictionary, boards  # 단어 사전과 보드 리스트를 반환한다.

def find_words(board, dictionary):
    rows, cols = len(board), len(board[0])  # 보드의 행과 열의 개수를 구한다.
    valid_words = set()  # 유효한 단어들을 저장할 집합을 생성한다.
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 이동 가능한 8방향을 정의한다.

    # DFS를 이용하여 보드에서 단어를 찾는다.
    def dfs(x, y, word, visited):
        if word in dictionary:  # 현재 단어가 사전에 있는 단어인지 확인한다.
            valid_words.add(word)  # 유효한 단어 집합에 추가한다.
        if len(word) > 8:  # 이 문제에서는 8글자 이상의 단어를 찾을 필요가 없다.
            return  # 길이가 8을 넘으면 더 이상 진행하지 않는다.
        for dx, dy in directions:  # 8방향을 탐색한다.
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:  # 보드 범위를 벗어나지 않고 방문하지 않은 경우
                visited[nx][ny] = True  # 현재 위치를 방문 처리한다.
                dfs(nx, ny, word + board[nx][ny], visited)  # 새로운 위치로 이동하여 DFS를 진행한다.
                visited[nx][ny] = False  # 방문 처리를 해제한다.

    # 보드의 각 위치에서 DFS를 시작한다.
    for i in range(rows):
        for j in range(cols):
            visited = [[False] * cols for _ in range(rows)]  # 방문 여부를 저장할 2차원 리스트를 생성한다.
            visited[i][j] = True  # 시작 위치를 방문 처리한다.
            dfs(i, j, board[i][j], visited)  # 현재 위치에서 DFS를 시작한다.

    return valid_words  # 유효한 단어 집합을 반환한다.

def calculate_score(word):
    length = len(word)  # 단어의 길이를 구한다.
    if length <= 2:
        return 0  # 길이가 2 이하인 단어는 점수가 0점이다.
    elif length <= 4:
        return 1  # 길이가 3 또는 4인 단어는 1점이다.
    elif length == 5:
        return 2  # 길이가 5인 단어는 2점이다.
    elif length == 6:
        return 3  # 길이가 6인 단어는 3점이다.
    elif length == 7:
        return 5  # 길이가 7인 단어는 5점이다.
    else:
        return 11  # 길이가 8 이상인 단어는 11점이다.

def solve_boggle(dictionary, boards):
    results = []  # 각 보드의 결과를 저장할 리스트를 생성한다.
    for board in boards:
        valid_words = find_words(board, dictionary)  # 보드에서 유효한 단어들을 찾는다.
        max_score = 0  # 최대 점수를 초기화한다.
        longest_word = ""  # 가장 긴 단어를 초기화한다.
        total_words = len(valid_words)  # 유효한 단어의 총 개수를 구한다.
        for word in valid_words:
            score = calculate_score(word)  # 단어의 점수를 계산한다.
            max_score += score  # 총 점수에 단어의 점수를 더한다.
            if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                longest_word = word  # 더 긴 단어이거나 같은 길이의 단어 중 사전 순으로 앞서는 단어를 선택한다.
        results.append((max_score, longest_word, total_words))  # 결과 리스트에 현재 보드의 결과를 추가한다.
    return results  # 모든 보드의 결과를 반환한다.

def main():
    dictionary, boards = read_input()  # 입력을 읽어와서 단어 사전과 보드 리스트를 얻는다.
    results = solve_boggle(dictionary, boards)  # 각 보드에 대해 유효한 단어들을 찾고 점수를 계산한다.
    for result in results:
        print(result[0], result[1], result[2])  # 각 보드의 결과를 출력한다.

if __name__ == "__main__":
    main()  # 메인 함수를 실행한다.
