
## [rev 108] babyroid

Mở file apk bằng jadx. Trong file MainActivity có đoạn check flag dùng hàm `FlagValidator.checkFlag()`:

```java
public class FlagValidator {
    public static boolean checkFlag(Context ctx, String flag) {
        String result = Helper.retriever();
        if (flag.startsWith("HCMUS-CTF{") && flag.charAt(19) == '_' && flag.length() == 37 && flag.toLowerCase().substring(10).startsWith("this_is_") && flag.charAt(((int) (MagicNum.obtainY() * Math.pow(MagicNum.obtainX(), MagicNum.obtainY()))) + 2) == flag.charAt(((int) Math.pow(Math.pow(2.0d, 2.0d), 2.0d)) + 3) && new StringBuilder(flag).reverse().toString().toLowerCase().substring(1).startsWith(ctx.getString(R.string.last_part)) && new StringBuilder(flag).reverse().toString().charAt(0) == '}' && Helper.ran(flag.toUpperCase().substring((MagicNum.obtainY() * MagicNum.obtainX() * MagicNum.obtainY()) + 2, (int) (Math.pow(MagicNum.obtainZ(), MagicNum.obtainX()) + 1.0d))).equals("ERNYYL") && flag.toLowerCase().charAt(18) == 'a' && flag.charAt(18) == flag.charAt(28) && flag.toUpperCase().charAt(27) == flag.toUpperCase().charAt(28) + 1) {
            return flag.substring(10, flag.length() - 1).matches(result);
        }
        return false;
    }
}
```

Giải các điều kiện cho ta chuỗi flag (chưa biết viết hoa viết thường), trong các điều kiện đáng chú ý có `Helper.ran()` là một hàm thay đổi chuỗi theo quy tắc:

```java
public class Helper {
    public static String ran(String s) {
        String out = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= 'a' && c <= 'm') {
                c = (char) (c + '\r');
            } else if (c >= 'A' && c <= 'M') {
                c = (char) (c + '\r');
            } else if (c >= 'n' && c <= 'z') {
                c = (char) (c - '\r');
            } else if (c >= 'N' && c <= 'Z') {
                c = (char) (c - '\r');
            }
            out = out + c;
        }
        return out;
    }
```

Đây là rot13 encrypt, giải ra được cụm "REALLY".

Sau khi qua điều kiện, chuỗi flag được check regex (lưu trong `result`) được generate từ hàm `Helper.retriever()` 

```java
return flag.substring(10, flag.length() - 1).matches(result);
```

```java
    public static String retriever() {
        String str;
        StringBuilder sb;
        String r = "";
        boolean upper = true;
        for (int i = 0; i < 26; i++) {
            if (upper) {
                sb = new StringBuilder();
                sb.append(r);
                str = "[A-Z_]";
            } else {
                sb = new StringBuilder();
                sb.append(r);
                str = "[a-z_]";
            }
            sb.append(str);
            r = sb.toString();
            upper = !upper;
        }
        return r;
    }
}
```

Regex này nghĩa là chẵn-lẻ đan xen

Flag:`HCMUS-CTF{ThIs_iS_A_ReAlLy_bAsIc_rEv}`