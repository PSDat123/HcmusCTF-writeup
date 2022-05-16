## [No Backend] - Web Security (200 points)

Đường dẫn: http://103.245.250.31:32323/#/auth/login

Vào đường dẫn sẽ cho ta thấy được hình ảnh này:
![image](https://user-images.githubusercontent.com/87664370/168623421-5f7b025f-41bd-494e-8e78-8d7e438c709e.png)

Sau đó ta sẽ Ctrl + U để check source.
Vì source .html không được làm đẹp nên mình đã làm đẹp lại và đưa vào folder src với tên là source.html

Biết rằng vì trang Web này không có Backend nên việc lưu tài khoản mật khẩu gần như bất khả thi, tuy nhiên ta cũng nên tạo 1 cái thử xem sao.
![image](https://user-images.githubusercontent.com/87664370/168624567-69e389a1-56e8-4759-ad13-1ed429cfe635.png)

Phần đăng nhập:
![image](https://user-images.githubusercontent.com/87664370/168624644-affa4aef-3702-46bb-bec5-5c178594350e.png)

Vì trang web không có Backend nên mình đoán rằng trang web sẽ giấu Flag ở những file đính kèm trong source.
Và không nghi ngờ gì nữa, Flag được nằm ở file `chunk-851c22b0.e53301b2.js` và mình sẽ để file đó trong folder src với tên là flag.js.
![image](https://user-images.githubusercontent.com/87664370/168626175-3d7a53ed-eba3-4c9e-a3b9-5119196b1375.png)

Cuối cùng là mẫu của flag là HCMUS-CTF{} nên chỉ cần bọc phần flag lại thôi.

Flag: `HCMUS-CTF{w0w_4uth3ntication_bYP4ss_s000_h4rd}`
