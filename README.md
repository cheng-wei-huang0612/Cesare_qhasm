This repo is still developing...

# Usage
1. in the Cesare_qhasm, run 
```
./qhasm-aarch64-align < my_test/char2mul.q > my_test/char2mul.S   
```
2. cd to my_test, run
```
make
```
3. run
```
 ./test-char2mul-program 
```

It is expected that
```
Result = 0x5
```