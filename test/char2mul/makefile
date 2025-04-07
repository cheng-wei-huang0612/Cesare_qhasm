# 適度根據環境修正 C 編譯器、qhasm 等路徑
CC      := gcc
CFLAGS  := -O2 -Wall
LDLIBS  :=
QHASM   := qhasm-ARMv8       # 或其他對應你想要使用的 qhasm 指令
# QHASM   := ./qhasm-armv8    # 如果是本地一個腳本

TARGET  := test-char2mul-program
OBJ     := test-char2mul.o
ASMOBJ  := char2mul.o

.PHONY: all clean

all: $(TARGET)

# 如果已經有手刻的 char2mul.S，不需再由 .q 產生。
# 若你是想從 .q 自動生成 .S 檔（或其他中間檔案），可加上以下規則：
# char2mul.S: char2mul.q
# 	$(QHASM) < char2mul.q > char2mul.S

# 組譯 char2mul.S 變成 .o
char2mul.o: char2mul.S
	$(CC) $(CFLAGS) -c char2mul.S -o char2mul.o

# 編譯 test-char2mu.c
test-char2mu.o: test-char2mu.c
	$(CC) $(CFLAGS) -c test-char2mul.c -o test-char2mul.o

# 連結產生可執行檔
$(TARGET): $(OBJ) $(ASMOBJ)
	$(CC) $(CFLAGS) $(OBJ) $(ASMOBJ) -o $(TARGET) $(LDLIBS)

clean:
	rm -f $(TARGET) *.o 
