const JamoUtil = {
    chosung: ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
                    'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'],
    jungsung: ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
                    'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'],
    jongsung: ['', 'ㄱ', 'ㄲ', 'ᆪ', 'ᆫ', 'ᆬ', 'ᆭ', 'ㄷ',
                    'ㄹ', 'ᆰ', 'ᆱ', 'ᆲ', 'ᆳ', 'ᆴ', 'ᆵ', 'ᆶ', 'ㅁ', 'ㅂ', 'ᆹ', 'ᆺ', 'ᆻ', 'ᆼ',
                    'ᆽ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'],

    splitOne(target) {
        const startValue = target.charCodeAt(0) - 0xAC00;
        const jong = startValue % 28;
        const jung = ((startValue - jong) / 28) % 21;
        const cho = (((startValue - jong) / 28) - jung) / 21;

        return [this.chosung[cho], this.jungsung[jung], this.jongsung[jong]];
    },

    split(target) {
        const result = [];
        target.split('').forEach(element => {
            result.push(this.splitOne(element));
        });

        return result;
    }
}
