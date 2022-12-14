/**
 * zhihancn
 */

function int_to_anybase(decNum, base) {
    rtList = [];
    while (true) {
        remainder = decNum % BigInt(base);
        rtList.push(Number(remainder));
        decNum = decNum / BigInt(base);
        if (decNum == 0) {
            break;
        }
    }
    rtList.reverse();
    return rtList;
}

function anybase_to_int(anybaseList, base) {
    anybaseList.reverse();

    let decNum = BigInt(0);
    let b = BigInt(1);

    for (let i = 0; i < anybaseList.length; i++) {
        decNum = decNum + BigInt(anybaseList[i]) * b;
        b = b * BigInt(base);
    }
    return decNum;
}

class ALTranslater {
    constructor(words) {
        this.words = words;
        this.__pre_treat()
        console.log(this.words)
    }

    __pre_treat() {
        this.words = [...new Set(this.words)];   // 去重
        this.words.sort((a, b) => a.length - b.length); // 按长度排序
    }

    encode(oriStr) {
        // byte to hex
        let encoder = new TextEncoder();
        let byteList = encoder.encode(oriStr);
        let byteStrList = new Array(byteList.length);
        byteList.forEach(toHex);

        function toHex(value, index) {
            byteStrList[index] = value.toString(16).padStart(2, '0');
        }

        let byteStr = byteStrList.join('');
        // hex to int
        let intStr = BigInt('0x' + byteStr);
        // int to anybase
        let anybaseList = int_to_anybase(intStr, this.words.length);
        // anybase to encoded str
        let encodedList = new Array(anybaseList.length);
        for (let i = 0; i < anybaseList.length; i++) {
            encodedList[i] = this.words[anybaseList[i]];
        }

        return encodedList.join('');
    }

    decode(encodedStr) {
        // encoded str to anybase list
        let anybaseStrList = [encodedStr];

        for (let i = this.words.length - 1; i >= 0; i--) {
            for (let j = 0; j < anybaseStrList.length; j++) {
                if (typeof anybaseStrList[j] == 'number') {
                    anybaseStrList[j] = [anybaseStrList[j]];
                } else {
                    let word = this.words[i]
                    let regex = new RegExp('(' + word + ')', 'g');

                    anybaseStrList[j] = anybaseStrList[j].split(regex).filter(i => i != '');

                    anybaseStrList[j].forEach(toNum);

                    function toNum(value, index) {
                        if (value == word) {
                            anybaseStrList[j][index] = i;
                        }
                    }
                }
            }
            anybaseStrList = anybaseStrList.flat();
        }

        // anybase list to int
        let intStr = anybase_to_int(anybaseStrList, this.words.length)

        // int to hex
        let byteStr = intStr.toString(16);

        // hex to oriStr
        return decodeURIComponent('%' + byteStr.match(/.{1,2}/g).join('%'));
    }
}
