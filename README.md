한글 유니코드 자소 분리하는 방법을 설명해 보겠습니다.

유니코드에서 한글은 코드값 0xAC00부터 시작하며,
- 초성 19
- 중성 21
- 종성 28

개의 조합순으로 코드가 배열돼 있습니다. 초성, 중성, 종성의 자모 순서는 [http://www.unicode.org/chart](http://www.unicode.org/chart)에서 오른쪽 끝, 중간 쯤에 있는 **Hangul Jamo** 부분의 링크인 [https://www.unicode.org/charts/PDF/U1100.pdf](https://www.unicode.org/charts/PDF/U1100.pdf) 파일에서 확인할 수 있는데, 다음과 같습니다.

초성
> 'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'

중성
> 'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'

종성
> '', 'ㄱ', 'ㄲ', 'ᆪ', 'ᆫ', 'ᆬ', 'ᆭ', 'ㄷ', 'ㄹ', 'ᆰ', 'ᆱ', 'ᆲ', 'ᆳ', 'ᆴ', 'ᆵ', 'ᆶ', 'ㅁ', 'ㅂ', 'ᆹ', 'ᆺ', 'ᆻ', 'ᆼ', 'ᆽ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'

특정 한글 유니코드에서 초성, 중성, 종성을 분리하는 것을 생각해 보겠습니다. 유니코드에서 특정 글자의 코드 값은 다음과 같은 식으로 생각해 볼 수 있습니다. 이 식에서 초성, 중성, 종성의 의미는 위의 초/중/종성 중에서 각각 몇 번째 초성이다, 중성이다, 종성이다의 의미이며 순서는 0부터 시작합니다.
```
(초성 * 21 * 28) + (중성 * 28) + 종성
```
이를 줄여서 보통 다음과 같이 보통 표기합니다.
```
((초성 * 21) + 중성) * 28 + 종성
```
첫번째 식처럼 표기한 이유는 이해를 쉽게 하기 위해서입니다. 유니코드에서 0xAC00의 한글은 '가'입니다. 이 '가'는 초성 첫번째, 중성 첫번째, 종성 첫번째의 조합입니다. 그러면, 0xAC01은 어떤 글자일까요? 예, 그렇습니다. '각'(초성 첫번째 + 중성 첫번째 + 종성 두번째)입니다. 한글 유니코드는 이런식으로 코드값이 매겨져 있습니다. 그렇다면 이제 특정 글자의 코드 값은 어떻게 구할지를 첫번째 식을 보면서 설명해 보겠습니다.

'꺔'을 가지고 생각해 보겠습니다. 우선 초성인 'ㄲ'까지 오려면 한글 코드의 시작인 0xAC00에서 시작해서 얼마나 많은 글자를 지나와야 할까요. 'ㄲ' 바로 앞에 있는 초성인 'ㄱ'으로 시작하는 모든 글자를 센다고 보면 됩니다. 이 모든 글자를 세려면, 첫번째 식의 첫번째 괄호처럼 **초성 x 21 x 28**의 조합을 거쳐야 'ㄲ'까지 올 수 있습니다. 여기서 기억할 점은 바로 앞 글자라고 해서 현재 초성 순서에서 하나를 빼고 곱하는 것이 아니라 현재 초성 순서를 곱한다는 것입니다. 그 이유는 앞에서 언급한 것처럼 순서가 0부터 시작하기 때문입니다.

이제 중성 차례입니다. 'ㄲ'과 조합돼 'ㅑ'라는 중성 순서까지 오려면 중성과 종성 조합 수를 더해줘야 하므로 **중성 x 28**을 계산해서 더해줘야 합니다. 그리고 나서 종성의 순번으로 글자가 이루어지므로 종성 순서를 더해주면 유니코드 값을 알 수 있습니다.

이제 이 공식을 바탕으로 초/중/종성을 분리하는 코드를 작성해 보겠습니다. 일단, 초성, 중성, 종성을 구하는 공식을 만들어야 합니다. 위의 두 번째 식을 기준으로 만들어 보겠습니다. 다시 정확히 한글 유니코드 값을 정의해 보면 다음과 같습니다.
```
0xAC00 + ((초성순서 * 21) + 중성순서) * 28 + 종성순서 = 한글 유니코드 값
```
여기에서 우리가 필요한 것은 초/중/종성의 순서이므로, 일단 코드 값에서 0xAC00을 빼고 계산을 합니다. 이제 식을 다시 정리해서 0xAC00을 뺀 식의 값을 '순수한글코드'라고 해 보겠습니다. 그러면, 다음과 같이 초/중/종성의 순서를 알아낼 수 있습니다.
```
((초성순서 * 21) + 중성순서) * 28 + 종성순서 = 순수한글코드
```
#### 1. 종성
종성은 순수한글코드를 28로 나눈 나머지를 구하면 됩니다. 식으로 쓰면 다음과 같습니다.
> 순수한글코드 % 28

#### 2. 중성
중성은 종성값을 이용하여 구합니다. 먼저 종성을 순수 한글 코드에서 뺀 후, 이를 28로 나눈 몫을 21로 나눈 나머지가 중성이 됩니다. 말이 좀 복잡할 수 있으나 위에 있는 식을 보면 알 수 있습니다.
> ((순수한글코드 - 종성) / 28) % 21 = 중성

#### 3. 초성
초성은 위의 식에 중성, 종성을 대입하면 구할 수 있습니다. 식으로 정리하면 다음과 같습니다.
> (((순수한글코드 - 종성) / 28) - 중성) / 21 = 초성

다음과 같은 언어별 구현 파일이 있습니다. 각각의 파일을 통해 실제 구현 코드를 확인하실 수 있습니다.
- JavaScript: [jamo.js](https://github.com/intotherealworld/jamo/blob/main/jamo.js)
- Java: [JamoUtils.java](https://github.com/intotherealworld/jamo/blob/main/JamoUtils.java)
- Kotlin: [JamoUtils.kt](https://github.com/intotherealworld/jamo/blob/main/JamoUtils.kt)
- Python: [jamo_utils.py](https://github.com/intotherealworld/jamo/blob/main/jamo_utils.py)