# Boogle 문제 풀이 및 설명

https://www.acmicpc.net/problem/9202

## 문제 이해

### 문제 설명
상근이는 Boggle 게임을 매우 좋아합니다. Boggle은 4x4 크기의 그리드에서 주어진 글자들로 가능한 많은 단어를 찾는 게임입니다. 단어는 상하좌우 및 대각선으로 연결된 인접한 글자들을 사용하여 만들 수 있으며, 동일한 글자를 여러 번 사용할 수 없습니다. 또한, 단어 사전에 있는 단어만 유효한 단어로 인정됩니다.

### 문제 해결 관점
문제를 해결하려면 다음과 같은 관점에서 접근해야 합니다:
1. **단어 찾기**: Boggle 보드에서 사전에 있는 단어를 찾아내기 위한 탐색 방법.
2. **최적화**: 최대 점수, 가장 긴 단어, 찾은 단어의 개수를 계산하기 위한 효율적인 방법.
3. **DFS 탐색**: 각 위치에서 시작하여 모든 가능한 단어를 찾기 위한 깊이 우선 탐색(DFS) 방법.

## 입력 조건
1. 첫 번째 줄에 단어 사전에 들어있는 단어의 수 \( w \)가 주어진다. \( 1 \leq w \leq 300,000 \)
2. 다음 \( w \)개의 줄에 단어가 주어진다. 단어는 최대 8글자이고, 알파벳 대문자로 이루어져 있다.
3. 다음 줄에 Boggle 보드의 개수 \( b \)가 주어진다. \( 1 \leq b \leq 30 \)
4. 각 Boggle 보드는 알파벳 대문자로 이루어진 4줄의 글자들이 주어진다. 각 Boggle 보드 사이에는 빈 줄이 하나 있다.

## 출력 조건
각각의 Boggle 보드에 대해, 얻을 수 있는 최대 점수, 가장 긴 단어, 찾은 단어의 개수를 출력한다. 만약 여러 단어가 가장 긴 단어일 경우, 사전순으로 앞서는 단어를 출력한다.

## 접근 방법
1. **DFS 탐색**: 각 위치에서 시작하여 인접한 글자들을 따라가며 단어를 형성하는 DFS 알고리즘을 사용합니다.
2. **사전 검색**: 단어 사전을 해시 셋으로 저장하여 빠르게 검색할 수 있도록 합니다.
3. **점수 계산**: 단어의 길이에 따라 점수를 계산합니다.
4. **결과 저장 및 출력**: 각 Boggle 보드에 대해 최대 점수, 가장 긴 단어, 찾은 단어의 개수를 계산하여 결과를 저장하고 출력합니다.

## 문제 해결 과정
1. **입력 데이터 읽기**: 표준 입력에서 데이터를 읽어와 단어 사전과 Boggle 보드를 파싱합니다.
2. **DFS 탐색 구현**: 각 Boggle 보드에서 모든 가능한 단어를 찾기 위해 DFS 알고리즘을 구현합니다.
3. **단어 유효성 검사**: 형성된 단어가 단어 사전에 있는지 검사하여 유효한 단어를 찾습니다.
4. **점수 계산**: 찾은 단어의 길이에 따라 점수를 계산합니다.
5. **최종 결과 계산**: 각 Boggle 보드에 대해 최대 점수, 가장 긴 단어, 찾은 단어의 개수를 계산하여 결과를 저장합니다.
6. **결과 출력**: 계산된 결과를 포맷에 맞추어 출력합니다.

## 코드 구현
```python
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
