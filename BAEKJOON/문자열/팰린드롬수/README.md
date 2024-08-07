# 팰린드롬수 문제 풀이 및 설명

https://www.acmicpc.net/problem/1259

## 문제 이해

이 문제는 주어진 정수가 팰린드롬인지 확인하는 문제입니다. 팰린드롬이란 어떤 수나 단어를 앞에서부터 읽든 뒤에서부터 읽든 동일한 경우를 의미합니다. 예를 들어, "121"과 같은 숫자는 앞뒤로 읽어도 동일하기 때문에 팰린드롬이지만, "1231"은 뒤집었을 때 "1321"이 되어 팰린드롬이 아닙니다.

따라서, 이 문제에서는 입력된 숫자가 팰린드롬인지 아닌지를 판단하는 것이 핵심입니다. 입력은 여러 개의 숫자들로 이루어져 있으며, 각각의 숫자에 대해 팰린드롬 여부를 판단해 결과를 출력해야 합니다. 

마지막 입력 값은 "0"이며, 이 값은 문제 해결의 끝을 의미합니다. 이 "0"은 검사 대상이 아니므로, 이를 처리하지 않고 입력을 종료해야 합니다.

## 입출력 조건

### 입력
- 여러 줄에 걸쳐 1 이상 99999 이하의 정수가 입력으로 주어집니다.
- 입력의 마지막 줄에는 "0"이 주어지며, 이 "0"은 문제 해결의 끝을 나타냅니다. "0"은 검사 대상에 포함되지 않습니다.

### 출력
- 각 줄마다 주어진 숫자가 팰린드롬이면 "yes"를 출력합니다.
- 만약 팰린드롬이 아니면 "no"를 출력합니다.

## 접근 방식

이 문제를 해결하기 위해서는 주어진 숫자가 팰린드롬인지 확인하는 간단한 문자열 처리 방법을 사용할 수 있습니다. 숫자를 문자열로 변환한 후, 이를 뒤집어서 원래의 문자열과 비교하는 방법이 가장 직관적이고 효율적입니다.

구체적으로, 다음과 같은 접근 방식을 사용할 수 있습니다:

1. **문자열 변환 및 비교**: 입력된 숫자를 문자열로 변환한 후, 이를 뒤집어서 원래의 문자열과 비교합니다.
2. **입력 종료 처리**: 입력의 마지막에 등장하는 "0"은 문제 해결을 종료하는 신호로 간주하므로, 이를 따로 처리하여 루프를 종료합니다.
3. **무한 루프**: 여러 줄에 걸쳐 입력이 주어지므로, 무한 루프를 사용하여 각 숫자를 처리합니다. 이때 "0"이 입력되면 루프를 종료하도록 설정합니다.

## 풀이 과정

1. **무한 루프 시작**: 각 숫자를 하나씩 처리하기 위해 무한 루프를 시작합니다. 이는 여러 개의 입력 줄을 처리하기 위해 필요합니다.

2. **입력 받기**: 루프 내에서 숫자를 입력받습니다. 입력된 숫자는 문자열로 처리하여 양 끝의 공백을 제거합니다.

3. **종료 조건 확인**: 입력된 숫자가 "0"인지 확인합니다. 만약 "0"이라면 이는 입력의 끝을 의미하므로, 루프를 종료합니다.

4. **팰린드롬 확인**: 입력된 숫자를 뒤집어서 원래의 숫자와 비교합니다. 이때 문자열의 슬라이싱 기법을 사용하여 뒤집은 문자열을 쉽게 얻을 수 있습니다.

5. **결과 출력**: 비교 결과가 동일하면 "yes"를 출력하고, 그렇지 않으면 "no"를 출력합니다.

6. **루프 반복**: 이 과정을 반복하여 모든 입력된 숫자에 대해 팰린드롬 여부를 확인합니다. "0"이 입력되면 루프가 종료됩니다.

이 과정을 통해 모든 숫자에 대해 팰린드롬인지 여부를 정확히 판단할 수 있습니다. 팰린드롬 확인 자체는 O(n) 시간 복잡도로 처리되며, 입력의 길이가 크지 않기 때문에 매우 효율적으로 문제를 해결할 수 있습니다.

## 코드 구현
```python
while True:  # 무한 루프를 시작합니다. 각 테스트 케이스를 하나씩 처리하기 위해 반복합니다.
    num = input().strip()  # 사용자로부터 입력을 받아 양 끝의 공백을 제거합니다.
    
    if num == "0":  # 입력된 값이 "0"이면,
        break  # 루프를 종료합니다. "0"은 입력의 끝을 의미합니다.
    
    if num == num[::-1]:  # 입력된 문자열이 뒤집었을 때 동일한지 확인합니다.
        print("yes")  # 팰린드롬이라면 "yes"를 출력합니다.
    else:
        print("no")  # 팰린드롬이 아니라면 "no"를 출력합니다.
