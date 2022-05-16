## [crypto 460] SignMe

Tham số k được generate trong Elgamal Signing Scheme ở thử thách này theo pt: 
<img src="https://render.githubusercontent.com/render/math?math={k = \sum_{n=1} ^{\infty} a_i b_i}#gh-light-mode-only">
<img src="https://render.githubusercontent.com/render/math?math={\color{white}k = \sum_{n=1} ^{\infty} a_i b_i, k+=1 nếu k|phi}#gh-dark-mode-only">
.Trong đó a là só random do server generate và b là user base64 decoded input. 

Từ đây ta có thể exploit bằng cách giải hệ pt khi cho `msg1 = b'01'` 

FLAG: `HCMUS-CTF{B4se64_15_1nt3r3stin9}`
