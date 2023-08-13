object JamoUtils {
    val CHOSUNG = listOf(
        "ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ",
        "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ",
    )
    val JUNGSUNG = listOf(
        "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
        "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ",
    )
    val JONGSUNG = listOf(
        "", "ㄱ", "ㄲ", "ᆪ", "ᆫ", "ᆬ", "ᆭ", "ㄷ",
        "ㄹ", "ᆰ", "ᆱ", "ᆲ", "ᆳ", "ᆴ", "ᆵ", "ᆶ", "ㅁ", "ㅂ", "ᆹ", "ᆺ", "ᆻ", "ᆼ",
        "ᆽ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ",
    )

    fun split(target: String): List<List<String>> {
        return target.split("")
            .filter(String::isNotEmpty)
            .map(JamoUtils::splitOne)
            .toList()
    }

    fun splitOne(target: String): List<String> {
        val codePoint = Character.codePointAt(target, 0)
        return if (codePoint in 0xAC00..0xD79D) {
            val startValue = codePoint - 0xAC00
            val jong = startValue % 28
            val jung = (startValue - jong) / 28 % 21
            val cho = ((startValue - jong) / 28 - jung) / 21

            listOf(
                CHOSUNG[cho],
                JUNGSUNG[jung],
                JONGSUNG[jong],
            )
        } else {
            listOf(target, "", "")
        }
    }
}