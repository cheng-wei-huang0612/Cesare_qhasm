
NAME    := ntt_1_layer_ct


CC      := gcc
CFLAGS  := -O2 -Wall
LDLIBS  :=
QHASM   := qhasm-ARMv8  # or ./qhasm-armv8, depending on your environment

# 產生可執行檔名稱
TARGET  := test-$(NAME)-program

# C 測試程式 (e.g. test-char2mul.c → test-$(NAME).c)
TESTC   := test-$(NAME).c
TESTOBJ := test-$(NAME).o

# 組合語言檔 (e.g. char2mul.S → $(NAME).S)
ASMSRC  := $(NAME).S
ASMOBJ  := $(NAME).o

.PHONY: all clean

all: $(TARGET)

# 若需要先由 .q 生成 .S 檔：
# $(NAME).S: $(NAME).q
#   $(QHASM) < $(NAME).q > $(NAME).S

# 組譯 $(NAME).S → $(NAME).o
$(ASMOBJ): $(ASMSRC)
	$(CC) $(CFLAGS) -c $< -o $@

# 編譯 test-$(NAME).c → test-$(NAME).o
$(TESTOBJ): $(TESTC)
	$(CC) $(CFLAGS) -c $< -o $@

# 連結成最終可執行檔
$(TARGET): $(TESTOBJ) $(ASMOBJ)
	$(CC) $(CFLAGS) $^ -o $@ $(LDLIBS)

clean:
	rm -f $(TARGET) *.o 