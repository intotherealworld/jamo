class JamoUtils:
    CHOSUNG = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
                    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    JUNGSUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
                    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    JONGSUNG = ['', 'ㄱ', 'ㄲ', 'ᆪ', 'ᆫ', 'ᆬ', 'ᆭ', 'ㄷ',
                    'ㄹ', 'ᆰ', 'ᆱ', 'ᆲ', 'ᆳ', 'ᆴ', 'ᆵ', 'ᆶ', 'ㅁ', 'ㅂ', 'ᆹ', 'ᆺ', 'ᆻ', 'ᆼ',
                    'ᆽ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def split_one(target):
        code_point = ord(target)
        if 0xAC00 <= code_point <= 0xD79D:
            start_value = ord(target[0]) - 0xAC00
            jong = start_value % 28
            jung = int(((start_value - jong) / 28) % 21)
            cho = int((((start_value - jong) / 28) - jung) / 21)

            return JamoUtils.CHOSUNG[cho], JamoUtils.JUNGSUNG[jung], JamoUtils.JONGSUNG[jong]

        return target, '', ''

    @staticmethod
    def split(target):
        result = []
        for c in target:
            result.append(JamoUtils.split_one(c))

        return result
