class JamoUtils:
    CHOSUNG = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
                    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    JUNGSUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
                    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    JONGSUNG = ['', 'ㄱ', 'ㄲ', 'ᆪ', 'ᆫ', 'ᆬ', 'ᆭ', 'ㄷ',
                    'ㄹ', 'ᆰ', 'ᆱ', 'ᆲ', 'ᆳ', 'ᆴ', 'ᆵ', 'ᆶ', 'ㅁ', 'ㅂ', 'ᆹ', 'ᆺ', 'ᆻ', 'ᆼ',
                    'ᆽ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def splitOne(target):
        codePoint = ord(target)
        if codePoint >= 0xAC00 and codePoint <= 0xD79D:
            startValue = ord(target[0]) - 0xAC00
            jong = startValue % 28
            jung = int(((startValue - jong) / 28) % 21)
            cho = int((((startValue - jong) / 28) - jung) / 21)

            return JamoUtils.CHOSUNG[cho], JamoUtils.JUNGSUNG[jung], JamoUtils.JONGSUNG[jong]

        return target, '', ''

    @staticmethod
    def split(target):
        result = []
        for c in target:
            result.append(JamoUtils.splitOne(c))

        return result
