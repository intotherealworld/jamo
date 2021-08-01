import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class JamoUtils {
    private JamoUtils() {
    }

    public static final String [] CHOSUNG = {"ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ",
                    "ㅅ","ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"};
    public static final String [] JUNGSUNG = {"ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ",
                    "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"};
    public static final String [] JONGSUNG = {"", "ㄱ", "ㄲ", "ᆪ", "ᆫ", "ᆬ", "ᆭ", "ㄷ",
                    "ㄹ", "ᆰ", "ᆱ", "ᆲ", "ᆳ", "ᆴ", "ᆵ", "ᆶ", "ㅁ", "ㅂ", "ᆹ", "ᆺ", "ᆻ", "ᆼ",
                    "ᆽ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"};

    public static List<List<String>> split(String target) {
        return Arrays.asList(target.split(""))
            .stream()
            .map(JamoUtils::splitOne)
            .collect(Collectors.toList());
    }

    public static List<String> splitOne(String target) {
        int codePoint = Character.codePointAt(target, 0);
        if (codePoint >= 0xAC00 && codePoint <= 0xD79D) {
            int startValue = codePoint - 0xAC00;
            int jong = startValue % 28;
            int jung = ((startValue - jong) / 28) % 21;
            int cho = (((startValue - jong) / 28) - jung) / 21;
            return List.of(CHOSUNG[cho], JUNGSUNG[jung], JONGSUNG[jong]);
        }

        return List.of(target, "", "");
    }
}