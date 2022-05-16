## [crypto 460] SignMe

Tham số k được generate trong Elgamal Signing Scheme ở thử thách này theo pt: 
<img src="https://render.githubusercontent.com/render/math?math={k = \sum_{n=1} ^{\infty} a_i b_i}#gh-light-mode-only">
<img src="https://render.githubusercontent.com/render/math?math={\color{white}k = \sum_{n=1} ^{\infty} a_i b_i, k%2b=1,   \text{if phi | k }}#gh-dark-mode-only">
.Trong đó a là só random do server generate và b là user base64 decoded input. 

Từ đây ta có thể exploit bằng cách cho `msg1 = b'01'*32` và `msg2 = b'03'*32`, từ pt k trên ta thấy k<sub>2</sub>=3*k<sub>1</sub> (nếu k<sub>1</sub> coprime với phi, do đó có 50% khả năng pt đúng và 50% sai, và phải chọn k<sub>2</sub> = (số lẻ) * k<sub>1</sub> để bypass điều kiện k+=1), đồng thời có được signature của `msg1` và `msg2` nhờ vào signing oracle.

Thu được pt1 trong ring `p-1`: 

s<sub>1</sub> * k<sub>1</sub> = H(msg1) - x * r<sub>1</sub>

pt2 trong ring `p-1`:
  
s<sub>2</sub> * 3k<sub>1</sub> = H(msg2) - x * r<sub>2</sub>

Ta giải hệ pt để tìm được secret key (x) theo cách lập ma trân bằng sage:

```sage
Z = Zmod(p-1)
A = matrix(Z, 2, [[s1, r1],[3*s2,r2]]) 
y = vector(Z, 2, [h1,h2])
k,x = A.solve_right(y)
k = ZZ(k)
if k % 2 ==0:
  #check
  print("fail")
x = ZZ(x)
#check lại
print(pow(g,h1,p)==(pow(pow(g,x,p),r1,p)*pow(r1,s1,p))%p)
```

Có được x ta tạo được chữ ký cho msg được server gửi về bằng cách cho `r=g`-> `k=1` rồi tính `s`:
```sage
h3 = bytes_to_long(sha256(m3).digest())
r2 = g
s3 = (h3 - x*r2) % (p-1)
print(b64encode(long_to_bytes(r1)))
print(b64encode(long_to_bytes(s3)))
```


FLAG: `HCMUS-CTF{B4se64_15_1nt3r3stin9}`
