
## [Super secret] Misc (100 points)

## Yêu cầu: Tìm Flag được giấu trong discord.

Thông thường các Flag được giấu ở các tin nhắn đính kèm (pin) hoặc là thông tin cá nhân của các admin hoặc là các bot. Vì vậy ta sẽ tìm kiếm ở những chỗ đấy.

Sau 1 hồi tìm kiếm thì ta thấy được 2 kết quả khá là khả quan.
Đó là một đường dẫn trong phần giới thiệu về tôi của admin Fluoxetine và tin nhắn đính kèm của admin nGth trong phần General:

![image](https://user-images.githubusercontent.com/87664370/168832639-64c525db-9789-4cb1-89d5-644f24e0c824.png)
![image](https://user-images.githubusercontent.com/87664370/168832675-f84149a7-55a4-4682-86c8-86a4fcb759dc.png)

Đầu tiên ta sẽ check xem đường dẫn của admin Fluoxetine là gì, và đây là kết quả.
![image](https://user-images.githubusercontent.com/87664370/168833593-2486f1a7-68fc-44c9-b5cd-ee713a8e674c.png)

Ta nghĩ là ta đã tìm được rồi nhưng đó không phải là Flag cần tìm và đã bị admin-rolled rồi. Đường dẫn trong Flag ra kết quả là bài của Rick Astley => rick-rolled lần 2

Tiếp theo ta sẽ xem tin nhắn của admin nGth và trong đó chỉ có vài dòng thông báo và 1 cái hình và từ đó ta được Flag cần tìm
![image](https://user-images.githubusercontent.com/87664370/168834785-e2f91992-b4fd-4867-9967-5518d5cb9a9f.png)

Cuối cùng là bọc lại trong HCMUS-CTF{} thôi 

Flag: `HCMUS-CTF{c291872ada763ed9a480eca240552890}`
